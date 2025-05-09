# PhisherMan
![Phisheranlogo](https://github.com/user-attachments/assets/51669f17-f6b3-4780-ae5b-2a2732021af8)
PhisherMan is a simple phishing analysis toolkit that performs both static and dynamic analysis of a given URL. It collects key information about web pages, certificates, domains, redirects, and browser-level behavior, while also logging detailed network activity and save data in a clean format for futher analysis, example with LLMs or manually.

**Should be used in a secure environment!**
that is segmented from prod environments, example docker or dedicated VM, i found vagrant useful to automate the building

---

## Features

### Static Analysis Components

PhisherMan performs static inspection of a target URL and extracts:

- Full HTML scraping of the target webpage  
- Redirection and final destination checks  
- TLS/SSL certificate information  
- WHOIS domain registration data  
- DNS resolution data  
- HTML content analysis using BeautifulSoup:
  - Page title  
  - Meta description and keywords  
  - JavaScript tags  
  - Links and iframes  
- Proxy output with full HTTP request and response logging

### Dynamic Analysis

The tool also runs the target webpage inside a real browser (via `browser.py`), allowing for:

- Visual rendering of the page  
- Collection of live network activity (HTML requests and responses)  
- Observation of runtime behavior and client-side interactions
- Also possibility for editing to be automating processes

---

## Output

All extracted data is saved in a clearly formatted `.txt` file for easy review and further analysis. The txt file will inherit extracted name of domain example: `domainname.com.txt`

---


---

## prequisities

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/BerraLeet/PhisherMan.git
cd PhisherMan
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run main:
```bash
python3 main.py
```
## Project Structure

| File/Folder                | Description                                                |
|----------------------------|------------------------------------------------------------|
| `mitmcert.py`              | Sets up local MITM proxy and certificate handling          |
| `shorter.py`               | Expands and resolves shortened URLs                        |
| `scraper.py`               | Extracts and saves full HTML code of the page             |
| `ssl_script.py`            | Fetches TLS/SSL certificate information                    |
| `domain_info_collecter.py` | Retrieves WHOIS and DNS information                        |
| `soup.py`                  | Parses HTML using BeautifulSoup (title, meta, tags, etc.)  |
| `browser.py`               | Launches browser for dynamic page behavior analysis        |
| `regex.py`                 | Cleans up and processes proxy response logs                |
| `append_proxy.py`          | Appends the final proxy traffic log to the report file     |
| `outputs/`                 | Stores the final `.txt` analysis reports                   |

## Use Cases

PhisherMan can be used for:

- Phishing detection and research  
- Cyber threat intelligence 
- Training data generation for machine learning models  
- Educational demonstrations and cybersecurity training

---

## License

This project is licensed under the MIT License.  


