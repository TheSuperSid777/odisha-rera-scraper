import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Setup headless Chrome
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

base_url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(base_url)

# Wait for the "View Details" buttons to load
try:
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(),'View Details')]")))
except TimeoutException:
    print("❌ View Details buttons did not load.")
    driver.quit()
    exit()

# Get all "View Details" buttons
view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View Details')]")[:6]

project_data = []

for i in range(len(view_buttons)):
    try:
        # Re-fetch buttons each time because page reloads after .back()
        view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View Details')]")[:6]

        print(f"\n🔍 Opening project {i+1}")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_buttons[i])
        time.sleep(1)
        view_buttons[i].click()
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        def get_field(label):
            tag = soup.find("td", string=label)
            return tag.find_next_sibling("td").text.strip() if tag and tag.find_next_sibling("td") else "N/A"

        project = {
            "RERA Regd. No": get_field("RERA Regd. No"),
            "Project Name": get_field("Project Name"),
            "Promoter Name": get_field("Company Name"),
            "Promoter Address": get_field("Registered Office Address"),
            "GST No": get_field("GST Number")
        }

        print("📦 Extracted:", project)
        project_data.append(project)

        driver.back()
        time.sleep(3)

    except Exception as e:
        print(f"❌ Failed on project {i+1}: {e}")
        driver.back()
        time.sleep(2)
        continue

driver.quit()

# Print final result
print("\n✅ Scraped Projects:")
for idx, proj in enumerate(project_data, 1):
    print(f"\n📌 Project {idx}")
    for k, v in proj.items():
        print(f"{k}: {v}")import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Setup headless Chrome
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

base_url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(base_url)

# Wait for the "View Details" buttons to load
try:
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(),'View Details')]")))
except TimeoutException:
    print("❌ View Details buttons did not load.")
    driver.quit()
    exit()

# Get all "View Details" buttons
view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View Details')]")[:6]

project_data = []

for i in range(len(view_buttons)):
    try:
        # Re-fetch buttons each time because page reloads after .back()
        view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View Details')]")[:6]

        print(f"\n🔍 Opening project {i+1}")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_buttons[i])
        time.sleep(1)
        view_buttons[i].click()
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        def get_field(label):
            tag = soup.find("td", string=label)
            return tag.find_next_sibling("td").text.strip() if tag and tag.find_next_sibling("td") else "N/A"

        project = {
            "RERA Regd. No": get_field("RERA Regd. No"),
            "Project Name": get_field("Project Name"),
            "Promoter Name": get_field("Company Name"),
            "Promoter Address": get_field("Registered Office Address"),
            "GST No": get_field("GST Number")
        }

        print("📦 Extracted:", project)
        project_data.append(project)

        driver.back()
        time.sleep(3)

    except Exception as e:
        print(f"❌ Failed on project {i+1}: {e}")
        driver.back()
        time.sleep(2)
        continue

driver.quit()

# Print final result
print("\n✅ Scraped Projects:")
for idx, proj in enumerate(project_data, 1):
    print(f"\n📌 Project {idx}")
    for k, v in proj.items():
        print(f"{k}: {v}")import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Setup headless Chrome
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

base_url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(base_url)

# Wait for the "View Details" buttons to load
try:
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(),'View Details')]")))
except TimeoutException:
    print("❌ View Details buttons did not load.")
    driver.quit()
    exit()

# Get all "View Details" buttons
view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View Details')]")[:6]

project_data = []

for i in range(len(view_buttons)):
    try:
        # Re-fetch buttons each time because page reloads after .back()
        view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View Details')]")[:6]

        print(f"\n🔍 Opening project {i+1}")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_buttons[i])
        time.sleep(1)
        view_buttons[i].click()
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        def get_field(label):
            tag = soup.find("td", string=label)
            return tag.find_next_sibling("td").text.strip() if tag and tag.find_next_sibling("td") else "N/A"

        project = {
            "RERA Regd. No": get_field("RERA Regd. No"),
            "Project Name": get_field("Project Name"),
            "Promoter Name": get_field("Company Name"),
            "Promoter Address": get_field("Registered Office Address"),
            "GST No": get_field("GST Number")
        }

        print("📦 Extracted:", project)
        project_data.append(project)

        driver.back()
        time.sleep(3)

    except Exception as e:
        print(f"❌ Failed on project {i+1}: {e}")
        driver.back()
        time.sleep(2)
        continue

driver.quit()

# Print final result
print("\n✅ Scraped Projects:")
for idx, proj in enumerate(project_data, 1):
    print(f"\n📌 Project {idx}")
    for k, v in proj.items():
        print(f"{k}: {v}")
