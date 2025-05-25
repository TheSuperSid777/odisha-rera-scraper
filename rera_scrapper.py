import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://rera.odisha.gov.in"

# Open main project list page
driver.get(f"{base_url}/projects/project-list")
time.sleep(5)  # wait for page to load JS content

# Find the first 6 'View Details' links
links = driver.find_elements(By.LINK_TEXT, "View Details")[:6]
project_links = []

for link in links:
    href = link.get_attribute("href")
    # Fix relative URLs by prepending base URL
    if href.startswith("/"):
        href = base_url + href
    project_links.append(href)

project_data = []

for url in project_links:
    print("Opening URL:", url)
    driver.get(url)
    time.sleep(3)  # wait for page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    def get_field(label):
        tag = soup.find('td', string=label)
        if tag and tag.find_next_sibling('td'):
            return tag.find_next_sibling('td').text.strip()
        return "N/A"

    project = {
        "RERA Regd. No": get_field("RERA Regd. No"),
        "Project Name": get_field("Project Name"),
        "Promoter Name": get_field("Company Name"),
        "Promoter Address": get_field("Registered Office Address"),
        "GST No": get_field("GST Number")
    }
    project_data.append(project)

# Print all projects
for i, proj in enumerate(project_data, 1):
    print(f"\nProject {i}:")
    for key, val in proj.items():
        print(f"{key}: {val}")

driver.quit()