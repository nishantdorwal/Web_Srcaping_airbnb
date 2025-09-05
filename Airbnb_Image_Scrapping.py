
import time
import os
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver and Navigate ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.airbnb.co.in/s/New-Delhi--India/homes")
 
# Set a longer wait time for page elements
driver.implicitly_wait(10)


# Scroll to load all images ---
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) # Wait for new content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height




# Get all image URLs ---
try:
# by the use a more stable CSS selector to find all listing images
    #images = driver.find_elements(By.CSS_SELECTOR, "div.cy5jw6o.dir.dir-ltr img")
    #src_list = [img.get_attribute("src") for img in images if img.get_attribute("src")]
    
# by using the shorter xpath     
    
    images = driver.find_elements(By.XPATH, "//picture/img")
    print(f"Found: {len(images)} images")
    src_list = []
    for img in images:
        src = img.get_attribute("src")
        if not src:             # if no src, try srcset
            srcset = img.get_attribute("srcset")
            if srcset:
                src = srcset.split(" ")[0] 
# for best image resolution you can use below code 
#best_img = srcset.split(",")[-1].split(" ")[0]

        if src:
            src_list.append(src)

    print(f"Collected {len(src_list)} image URLs")
    
except Exception as e:
    print(f"Error finding images: {e}")
    src_list = []

finally:
# Always quit the driver    
    driver.quit() 

# Download and Save Images ---
os.makedirs("airbnb_images", exist_ok=True)

for i, src in enumerate(src_list):
    try:
# Clean the URL (remove tracking parameters)
        clean_src = src.split("?")[0]
        r = requests.get(clean_src, stream=True, timeout=10)
        
        if r.status_code == 200:
            try:
# Try to open and convert to JPG
                image = Image.open(BytesIO(r.content)).convert("RGB")
                filename = f"airbnb_images/image_{i}.jpg"
                image.save(filename, "JPEG")
                print(f"Saved {filename}")
            except UnidentifiedImageError:
# If conversion fails (e.g., it's a WebP file), save as raw bytes
                filename = f"airbnb_images/image_{i}.webp"
                with open(filename, "wb") as f:
                    f.write(r.content)
                print(f"Saved raw WebP {filename}")
        else:
            print(f"Failed to download {src}, status: {r.status_code}")

    except Exception as e:
        print(f"Error with {src}: {e}")

