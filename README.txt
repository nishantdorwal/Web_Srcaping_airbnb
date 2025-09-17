

# Airbnb Image Scraper 🏠📸

This project is a **web scraping script** that collects property listing images from [Airbnb](https://www.airbnb.co.in/) using **Selenium**, **Requests**, and **Pillow (PIL)**.
The script scrolls through the Airbnb listings, extracts all available image URLs, and saves them locally in JPG or WebP format.

---

## ✨ Features

* Automated scrolling to load more Airbnb listings
* Extracts images from each listing (`src` and `srcset`)
* Downloads images in high resolution
* Converts images to **JPG** (or WebP if conversion fails)
* Organizes saved images inside `airbnb_images/` folder
* Easily scalable — replace Airbnb city/page links to collect 1500+ images in one run
---

## 🛠 Requirements

Make sure you have Python 3.7+ installed. Install the required libraries with:

```bash
pip install selenium pillow requests webdriver-manager
```

You’ll also need **Google Chrome** installed on your system since the script uses ChromeDriver.

---

## 🚀 Usage

1. Clone or download this project.
2. Run the script:

```bash
python airbnb_scraper.py
```

3. The script will:

   * Open Airbnb (New Delhi, India page by default)
   * Scroll until all listings are loaded
   * Extract image URLs
   * Download and save them in `airbnb_images/` folder

---

## 📂 Project Structure

```
📁 Airbnb-Image-Scraper
│── airbnb_scraper.py   # Main script
│── README.md           # Documentation
│── airbnb_images/      # Folder where images will be saved
```

---

## ⚠️ Notes

* Scraping Airbnb might be against their **Terms of Service**. Use this script **only for educational purposes**.
* Frequent scraping may result in your IP being temporarily blocked. Consider adding delays or proxies.
* The script is currently set for **New Delhi, India**, but you can change the URL to scrape other cities.

---

## 📸 Example Output

Saved images will look like:

```
airbnb_images/
├── image_0.jpg
├── image_1.jpg
├── image_2.webp
...
```

---

## 🙌 Author

Developed by **\[Nishant Dorwal]** – just for learning and experimentation with **Selenium + Web Scraping**.

---
