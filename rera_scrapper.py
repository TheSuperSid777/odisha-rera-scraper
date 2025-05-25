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

# Open the main project list page
url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(url)
time.sleep(5)  # wait for JS to load

# Find first 6 'View Details' links
links = driver.find_elements(By.LINK_TEXT, "View Details")[:6]

project_data = []

for i in range(len(links)):
    # Since page reloads after back(), re-find links each iteration
    links = driver.find_elements(By.LINK_TEXT, "View Details")[:6]
    
    print(f"Opening project {i+1} details page...")
    links[i].click()
    time.sleep(4)  # wait for detail page to load
    
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

    driver.back()
    time.sleep(3)  # wait to return to list page

# Print the scraped data
for idx, proj in enumerate(project_data, 1):
    print(f"\nProject {idx}:")
    for key, val in proj.items():
        print(f"{key}: {val}")

driver.quit()