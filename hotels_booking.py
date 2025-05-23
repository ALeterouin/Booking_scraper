import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
from geopy.distance import geodesic

# Path to your ChromeDriver
CHROMEDRIVER_PATH = "/Users/mac/booking_scraper/chromedriver-mac-arm64/chromedriver"

def create_driver():
    # Create and configure Chrome WebDriver
    options = webdriver.ChromeOptions()
    # Uncomment below line to run in headless mode
    # options.add_argument("--headless=new")
    prefs = {
        "profile.managed_default_content_settings.images": 2  # disable images for faster loading
    }
    options.add_experimental_option("prefs", prefs)
    service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    return webdriver.Chrome(service=service, options=options)

def scroll_until_all_hotels_loaded(driver, max_wait_time=60):
    # Slowly scroll down until all hotels are loaded or timeout is reached
    SCROLL_PAUSE_TIME = 2.5
    last_count = 0
    start_time = time.time()

    while True:
        driver.execute_script("window.scrollBy(0, 2000);")
        time.sleep(SCROLL_PAUSE_TIME)

        hotels = driver.find_elements(By.XPATH, '//div[@data-testid="property-card"]')
        current_count = len(hotels)
        print(f"Visible hotels: {current_count}")

        if current_count > last_count:
            last_count = current_count
            start_time = time.time()  # reset timer
        else:
            if time.time() - start_time > max_wait_time:
                print("⏹️ Stop scrolling: no new hotels after 60 seconds.")
                break

    return hotels

def extract_hotels(driver):
    # Extract main hotel info from listing page
    hotels = scroll_until_all_hotels_loaded(driver)
    hotel_list = []

    for hotel in hotels:
        data = {}

        try:
            data['Hotel Name'] = hotel.find_element(By.XPATH, './/div[@data-testid="title"]').text
        except:
            data['Hotel Name'] = 'N/A'

        try:
            stars = len(hotel.find_elements(By.XPATH, './/div[@data-testid="rating-stars"]/span'))
            data['Stars'] = stars
        except:
            data['Stars'] = 'N/A'

        try:
            price = hotel.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]').text
            price_clean = re.sub(r'[^\d,]', '', price).replace(',', '.')
            data['Price'] = float(price_clean) if price_clean else 'N/A'
        except:
            data['Price'] = 'N/A'

        try:
            note_elem = hotel.find_element(By.XPATH, './/div[contains(@class, "f63b14ab7a")]')
            note = note_elem.text.strip()
            data['Review Score (/10)'] = float(note.replace(',', '.'))
        except:
            data['Review Score (/10)'] = 'N/A'

        try:
            link = hotel.find_element(By.XPATH, './/a[@data-testid="title-link"]').get_attribute("href")
            data['Hotel URL'] = link
        except:
            data['Hotel URL'] = 'N/A'

        hotel_list.append(data)

    return hotel_list

def fetch_details(driver, url):
    # Visit individual hotel page to fetch coordinates
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "map_trigger_header_pin"))
        )
        latlng_element = driver.find_element(By.ID, "map_trigger_header_pin")
        latlng = latlng_element.get_attribute("data-atlas-latlng")
        latitude, longitude = map(float, latlng.split(',')) if latlng else (None, None)
    except:
        latitude, longitude = None, None

    return latitude, longitude, 'Address not available'

def calculate_distance(hotel_coords, event_coords):
    # Compute distance to event coordinates (in kilometers)
    try:
        return round(geodesic(hotel_coords, event_coords).kilometers, 2)
    except:
        return 'Error'

def run_scraping(destination, checkin, checkout):
    # Main scraping logic
    driver = create_driver()
    event_coords = (36.74196135173365, 15.11610252956532)  # Replace with your own event coordinates

    url = f'https://www.booking.com/searchresults.fr.html?ss={destination}&checkin={checkin}&checkout={checkout}&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204'
    driver.get(url)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-testid="property-card"]'))
    )

    hotels = extract_hotels(driver)
    print(f"\n{len(hotels)} hotels found in {destination}.\n")

    for idx, hotel in enumerate(hotels):
        print(f"Processing {idx+1}/{len(hotels)}: {hotel['Hotel Name']}")
        if hotel['Hotel URL'] != 'N/A':
            lat, lon, address = fetch_details(driver, hotel['Hotel URL'])
            hotel['Latitude'] = lat if lat else 'N/A'
            hotel['Longitude'] = lon if lon else 'N/A'
            hotel['Address'] = address
            if lat and lon:
                hotel['Distance to Event (Km)'] = calculate_distance((lat, lon), event_coords)
            else:
                hotel['Distance to Event (Km)'] = 'Coordinates not available'
        else:
            hotel['Latitude'] = hotel['Longitude'] = hotel['Address'] = hotel['Distance to Event (Km)'] = 'N/A'

    df = pd.DataFrame(hotels)
    filename = f'Hotels - {destination} - {checkin} - {checkout}.xlsx'
    df.to_excel(filename, index=False)
    driver.quit()

    return len(hotels), filename

# Tkinter GUI interface
def on_submit():
    destination = entry_destination.get()
    checkin = entry_checkin.get()
    checkout = entry_checkout.get()

    if not all([destination, checkin, checkout]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        count, file = run_scraping(destination, checkin, checkout)
        messagebox.showinfo("Done", f"{count} hotels retrieved.\nSaved file: {file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI layout
root = tk.Tk()
root.title("Booking Hotel Scraper")

tk.Label(root, text="Destination:").pack()
entry_destination = tk.Entry(root)
entry_destination.pack()

tk.Label(root, text="Check-in (YYYY-MM-DD):").pack()
entry_checkin = tk.Entry(root)
entry_checkin.pack()

tk.Label(root, text="Check-out (YYYY-MM-DD):").pack()
entry_checkout = tk.Entry(root)
entry_checkout.pack()

tk.Button(root, text="Start Scraping", command=on_submit).pack(pady=10)

root.mainloop()
