import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initialize the webdriver using ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get('https://journeynorth.org/sightings/querylist.html?season=fall&map=monarch-adult-fall&year=2023&submit=View+Data')  # Replace with the actual URL

# Function to extract data from the page using BeautifulSoup
def extract_data_from_page(source):
    soup = BeautifulSoup(source, 'html.parser')
    
    # Find all the table rows on the current screen
    rows = soup.find_all('tr')  # Assuming your rows are <tr> tags

    data = []

    # Loop through each row
    for row in rows:
        # Find all the cells
        cells = row.find_all('td')  # Assuming cells are <td> tags

        # Ensure there are enough cells in the row before accessing data
        if len(cells) > 6:
            date_spotted = cells[1].get_text(strip=True)
            city = cells[2].get_text(strip=True)
            state = cells[3].get_text(strip=True)
            number_spotted = cells[6].get_text(strip=True)
            latitude = cells[4].get_text(strip=True)
            longitude = cells[5].get_text(strip=True)
            # Append the extracted data
            data.append((date_spotted,city, state,latitude,longitude, number_spotted))
    
    return data

# Scroll the page and collect data
all_data = []
scroll_pause_time = 2  # Time to wait after scrolling

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Extract data from the current page
    new_data = extract_data_from_page(driver.page_source)
    all_data.extend(new_data)
    
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for new content to load
    time.sleep(scroll_pause_time)
    
    # Check if more content has loaded by comparing the scroll heights
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # No more content to load
    last_height = new_height

# Close the browser once all the data is collected
driver.quit()

# Create a DataFrame and save the data to Excel
df = pd.DataFrame(all_data, columns=['Date Sighted', 'City', 'State','Latitude','Longitude', 'Number Reported'])
df.to_excel("C:\\Users\\sefra\\Downloads\\New.xlsx", index=False)
