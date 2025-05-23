# 🏨 Booking Scraper

This Python project uses **Selenium** and **Tkinter** to automatically extract hotel data from **Booking.com**. It features a graphical interface to define search parameters (destination, dates), then stores the result in an Excel file. Ideal for comparing hotels around an event location such as a wedding, festival, or conference.

## ✨ Features

- **User-friendly GUI** with `Tkinter`
- **Automated hotel data extraction**:
  - Hotel name
  - Star rating
  - Price
  - Review score
  - Booking.com link
  - Address and GPS coordinates
  - Distance from a fixed location
- **Distance calculation** using `geopy`
- **Excel export** with `pandas` and `openpyxl`


## 🗂 Project Structure

```bash
booking_scraper/
├── hotels_booking.py         # Main script
├── chromedriver/             # Folder containing the ChromeDriver
├── README.md                 # English version
├── README_fr.md              # French version
├── requirements.txt          # Required libraries
````


## ✅ Requirements

* Python 3.12.4
* Google Chrome installed
* ChromeDriver ([https://chromedriver.chromium.org/](https://chromedriver.chromium.org/))
* Python libraries:

  * `selenium`
  * `webdriver_manager`
  * `pandas`
  * `geopy`
  * `openpyxl`


## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ALeterouin/Booking_scraper.git
   ```
   
   ```bash
   cd Booking_scraper
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `chromedriver` is correctly located and executable in the expected folder.


## 🚀 How to Use

1. Run the script:

   ```bash
   python hotels_booking.py
   ```

2. In the GUI window:

   * Enter your **destination**
   * Select your **check-in** and **check-out** dates (`YYYY-MM-DD`)
   * Click **Start Scraping**

3. Once scraping is complete, an Excel file will be generated with the results:

   ```
   Hotels - <Destination> - <Checkin> - <Checkout>.xlsx
   ```

## 🧠 Technical Overview

### Main Functions:

* `extract_hotels(driver)`: Extracts the main hotel information from the Booking results page.
* `fetch_details(driver, hotel_link)`: Gathers additional details such as address, latitude, and longitude.
* `calculate_distance(hotel_coords, event_coords)`: Computes distance in kilometers between each hotel and a fixed reference point.
* `run_scraping(destination, checkin, checkout)`: Orchestrates the scraping process and writes to Excel.
* `on_submit()`: GUI callback triggered when the user clicks the scraping button.

### Distance Calculation Location:

By default, the distance is calculated from this fixed location:

```python
event_coords = (36.74196135173365, 15.11610252956532)
```

You can replace these coordinates with your own event location.


## 📄 Sample Excel Output

| Hotel Name   | Stars | Price (€) | Score (/10) | Address           | Latitude | Longitude | Distance (km) | Booking Link |
| ------------ | ----- | --------- | ----------- | ----------------- | -------- | --------- | ------------- | ------------ |
| Hotel Sample | 4     | 142.00    | 8.2         | Via Roma 12, Rome | 41.9028  | 12.4964   | 2.4           | https\://... |


## ⚠️ Disclaimer

This script is for **educational purposes only**. Scraping Booking.com may violate their terms of service. Use responsibly and respect website rules.


## 👤 Author

Developed by [ALeterouin](https://github.com/ALeterouin)

Free to use and modify

<<<<<<< HEAD:ReadME
=======
Cela devrait fournir toutes les informations nécessaires aux utilisateurs pour comprendre, installer et exécuter votre projet !
>>>>>>> 0983c147ee08a4ed2b219d6fdd7f40e34f660ba9:README.md
