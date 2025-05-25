import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")  # Use new headless mode if your Chrome supports it
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(url)
wait = WebDriverWait(driver, 15)

time.sleep(5)  # Let the page load

project_data = []

for i in range(6):
    # Re-find the links every iteration because DOM reloads after back()
    links = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "View Details")))
    link = links[i]

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    
    # Wait until clickable, then try clicking with retries
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Details")))
            link.click()
            break
        except ElementClickInterceptedException:
            print(f"Click intercepted on attempt {attempt + 1}, retrying...")
            time.sleep(1)
    else:
        print("Failed to click after retries, skipping this project.")
        continue

    time.sleep(4)  # Wait for detail page to load

    soup = BeautifulSoup(driver.page_source, "html.parser")

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
    time.sleep(3)  # Wait for the list page to reload

print("\nScraped Projects:\n")
for idx, proj in enumerate(project_data, 1):
    print(f"Project {idx}:")
    for k, v in proj.items():
        print(f"  {k}: {v}")
    print()

driver.quit()