from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import pandas as pd

MESSAGES = [
    "Hi {name}, I came across your profile and was impressed by your experience in {industry}. As a student exploring opportunities, I'd love to connect and learn from your journey.",
    "Hello {name}, I noticed we share an interest in {industry}. I'm currently expanding my network and would appreciate connecting with someone with your experience.",
    "Hi {name}, I'm building my professional network in {industry} and would be honored to connect with someone with your background. Looking forward to learning from your insights!"
]

def run_linkedin_bot(email, password, search_term, max_pages):
    logs = []
    options = Options()
    # Uncomment below line for headless mode
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        print("[INFO] Navigating to LinkedIn login...")
        driver.get("https://www.linkedin.com/login")
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)
        time.sleep(5)

        print(f"[INFO] Searching for: {search_term}")
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Search")]')))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "People")]'))).click()
            time.sleep(2)
        except:
            print("[WARNING] Could not filter by people.")

        def connect_all_on_page():
            profiles = driver.find_elements(By.XPATH, '//div[contains(@class, "reusable-search__result-container")]')
            print(f"[INFO] Found {len(profiles)} profiles on current page.")

            for card in profiles:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", card)
                    time.sleep(1.5)

                    name_elem = card.find_element(By.XPATH, './/span[contains(@class, "entity-result__title-text")]/a/span[1]')
                    industry_elem = card.find_element(By.XPATH, './/div[contains(@class, "entity-result__primary-subtitle")]')
                    
                    name = name_elem.text.split()[0] if name_elem.text else "Unknown"
                    industry = industry_elem.text.split(',')[0] if industry_elem.text else "General"

                    connect_button = card.find_element(By.XPATH, './/button//span[text()="Connect"]/..')
                    connect_button.click()
                    time.sleep(2)

                    message = ""
                    try:
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Add a note")]'))).click()
                        message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@name="message"]')))
                        template = random.choice(MESSAGES)
                        message = template.format(name=name, industry=industry)
                        message_box.send_keys(message)
                    except Exception as e:
                        print(f"[WARNING] Could not add a message: {str(e)}")

                    try:
                        send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
                        send_btn.click()
                        logs.append({"Name": name, "Industry": industry, "Message Sent": message, "Status": "Connected"})
                    except:
                        logs.append({"Name": name, "Industry": industry, "Message Sent": message, "Status": "Failed to Send"})

                except Exception as e:
                    logs.append({"Name": "Unknown", "Industry": "Unknown", "Message Sent": "", "Status": f"Error: {str(e)}"})

        for page in range(1, max_pages + 1):
            print(f"[INFO] Processing page {page}/{max_pages}...")
            connect_all_on_page()

            try:
                next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
                if "disabled" in next_button.get_attribute("class"):
                    break
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                time.sleep(random.uniform(3, 5))
            except Exception as e:
                print(f"[WARNING] Could not click Next: {str(e)}")
                break

        df = pd.DataFrame(logs)
        df.to_excel("output.xlsx", index=False)
        print(f"[INFO] Logs saved. Total profiles processed: {len(logs)}")
        return f"\ud83c\udf89 Automation complete! {len(logs)} profiles processed."

    except Exception as e:
        return f"\u274c Error during automation: {str(e)}"

    finally:
        print("[INFO] Closing browser session.")
        driver.quit()

