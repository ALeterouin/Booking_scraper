Voici un README complet et détaillé pour votre projet de scraping d'hôtels sur Booking.com.

---

# Booking Scraper

Ce projet est un script Python qui utilise **Selenium** et **Tkinter** pour extraire des informations d'hôtels depuis **Booking.com**. Il inclut une interface graphique pour faciliter la configuration des paramètres de recherche (destination, dates) et enregistre les résultats dans un fichier Excel. Ce script est utile pour collecter des informations telles que les prix, les étoiles, les avis, et calculer la distance entre chaque hôtel et un lieu spécifique.

## Fonctionnalités

- **Extraction d’informations hôtelières** : Récupère des informations comme le nom de l’hôtel, les étoiles, le prix, la note, l'adresse et le lien vers la page de l’hôtel.
- **Calcul de la distance** : Calcule la distance en kilomètres entre chaque hôtel et un point de référence donné, tel qu’un lieu d’événement.
- **Interface graphique (GUI)** : Interface utilisateur avec Tkinter pour entrer facilement les détails de la recherche.
- **Export des données** : Enregistre les informations extraites dans un fichier Excel pour une utilisation ou une analyse ultérieure.

## Structure du Projet

- **`hotels_booking.py`** : Script principal pour le scraping d’hôtels.
- **`README.md`** : Documentation du projet.
- **`.gitignore`** : Fichier pour ignorer les fichiers inutiles (comme `.DS_Store`).
- **`requirements.txt`** : Liste des bibliothèques Python nécessaires pour exécuter le script.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les éléments suivants :

- **Python** 3.x
- Les bibliothèques Python suivantes :
  - `selenium`
  - `webdriver_manager`
  - `pandas`
  - `geopy`
  - `tkinter` (inclus avec Python)
  
Vous pouvez installer les dépendances en utilisant le fichier `requirements.txt`.

### Installation des dépendances

1. Clonez ce dépôt sur votre machine :

   ```bash
   git clone https://github.com/ALeterouin/Booking_scraper.git
   ```
   
   ```bash
   cd Booking_scraper
   ```

2. Installez les bibliothèques nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le script :

   ```bash
   python hotels_booking.py
   ```

2. **Entrez les informations de recherche** :
   - **Destination** : Le lieu de recherche des hôtels.
   - **Date d'arrivée** et **Date de départ** (format : `YYYY-MM-DD`).

3. **Lancez le scraping** :
   - Cliquez sur le bouton "Lancer le Scraping" pour démarrer l'extraction des données.
   - Une fois le scraping terminé, une boîte de dialogue apparaîtra avec le nombre d’hôtels récupérés et le nom du fichier Excel généré contenant les résultats.

## Détails du Code

### Fonctions principales

- **`extract_hotels(driver)`** : Récupère les informations sur chaque hôtel affiché (nom, étoiles, prix, note, lien) depuis la page de résultats de Booking.com.
- **`fetch_details(driver, hotel_link)`** : Accède à la page d’un hôtel pour récupérer l'adresse, la latitude et la longitude.
- **`calculate_distance(hotel_coords, event_coords)`** : Utilise la bibliothèque `geopy` pour calculer la distance entre l'hôtel et un lieu d'événement donné.
- **`run_scraping(destination, checkin_date, checkout_date)`** : Fonction principale pour configurer le navigateur, exécuter le scraping et enregistrer les résultats dans un fichier Excel.
- **`on_submit()`** : Fonction de rappel pour le bouton "Lancer le Scraping", qui récupère les informations entrées par l'utilisateur et lance le processus de scraping.

### Interface graphique (Tkinter)

L'interface graphique comporte trois champs d'entrée :
- **Destination**
- **Date d'arrivée**
- **Date de départ**

Un bouton "Lancer le Scraping" lance le processus et affiche les résultats dans une boîte de dialogue une fois terminé.

## Exemples de Résultats

Les résultats sont enregistrés dans un fichier Excel nommé selon le modèle suivant :

   ```
   Hotels - <destination> - <checkin_date> - <checkout_date>.xlsx
   ```

Chaque ligne du fichier contient des informations comme :
- Nom de l’hôtel
- Nombre d’étoiles
- Prix par nuit
- Note /10
- Lien vers la page de l’hôtel
- Latitude, Longitude, Adresse
- Distance de l'événement (en km)

## Avertissement

Ce projet est destiné à un **usage éducatif uniquement**. Le scraping de sites web comme Booking.com peut être contraire à leurs conditions d’utilisation. Utilisez ce projet de manière responsable, et respectez les règles d’utilisation du site.

## Auteur

- **ALeterouin** (https://github.com/ALeterouin)

---

Cela devrait fournir toutes les informations nécessaires aux utilisateurs pour comprendre, installer et exécuter votre projet !
