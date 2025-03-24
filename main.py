import subprocess
import shorter
import scraper
import tldextract
import ssl_script  
import soup  
import domain_info_collecter  
import browser
import mitmcert
import append_proxy  
import os
import time
import shutil

# Type URL to Analyze
url = "https://www.ciphervanguard.com/"

# Extract domain name and use to name file
domain = tldextract.extract(url).domain
filename = f"{domain}.txt"

# Installing Fake-Cert
mitmcert.setup_mitmproxy()

# Open file for Appending
with open(filename, "a") as file:
    
    file.write(f"\n\n==== Analysis of {url} ====\n")
    
    file.write("[DESTINATION URL]")
    shorter.expand_url(url, file)
      
    file.write("\n[WEBSITE CODE]\n")
    scraper.extract_html(url, file)   
    
    file.write("\n[CERTIFICATE INFO]\n")
    ssl_script.fetch_ssl_certificate(url, file)   
    
    file.write("[\nWHOIS INFO]\n")
    domain_info_collecter.extract_and_append_domain_info(url, file)

    file.write("\n[SOUP SCAN]\n")
    soup.analyze_and_append(url, file)

    file.write("\n[BROWSER]\n")
    browser.run_browser(url, file)

append_proxy.append_proxy_output(filename)

print(f"Information has been saved in {filename}")

destination_path = f"/home/vagrant/PhisherMan/outputs/{filename}"

try:
    shutil.move(filename, destination_path)
    print(f"File has successfully been moved to outputs {destination_path}")
except Exception as e:
    print(f"File has failed to move {e}")
