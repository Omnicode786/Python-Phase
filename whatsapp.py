from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver with updated syntax
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Prompt user to scan QR code
print("Scan the QR code on WhatsApp Web and press Enter to continue...")
input("Press Enter after scanning the QR code...")

# Wait for WhatsApp Web to load completely
print("Waiting for WhatsApp Web to load...")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='3']")))

# Define contacts and message
contacts = ["Abdul Kabeer", "Muhammad Suman", "Mansoor Alam"]  # Replace with your contact names or group names
message = "Happy New Year! 🎉 Wishing you all the best!"

# Send message to each contact
for contact in contacts:
    try:
        print(f"Searching for contact: {contact}...")
        
        # Find and click on the search box
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab='3']")
        search_box.click()
        search_box.clear()  # Clear any previous input
        search_box.send_keys(contact)
        time.sleep(3)  # Wait for results to appear

        # Wait for the contact to appear and click on it
        search_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@title='{contact}']"))
        )
        search_result.click()
        time.sleep(2)  # Wait for the chat to load

        # Wait for the message input box to be available
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='1']"))
        )
        message_box.click()  # Make sure it's active
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(2)

        print(f"Message successfully sent to {contact}.")

        # Clear the search box after sending the message
        search_box.clear()
        time.sleep(1)  # Add some delay before continuing

    except Exception as e:
        print(f"Failed to send message to {contact}. Error: {e}")

# Close the browser after completing all tasks
print("Task completed. Closing the browser...")
driver.quit()
