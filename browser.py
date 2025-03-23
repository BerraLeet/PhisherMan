from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess 

def run_browser(url, file):
    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-dev-shm-usage")  # Handle shared memory problems
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--proxy-server=http://localhost:8080")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(f"--user-agent={my_user_agent}")
    chrome_options.add_argument("--sec-ch-ua-platform=Windows")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")

    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open URL
    driver.get(url)
    
    # Log interaction time and details
    file.write(f"Opened URL: {url}\n")
    
    # Interaction time
    time.sleep(25)
    
    # Close the browser and mitmproxy after
    driver.quit()
    print("Terminating mitmproxy process...")
    subprocess.Popen(['pkill', 'mitmproxy'])

    file.write(f"Browser closed after interaction with {url}\n")
