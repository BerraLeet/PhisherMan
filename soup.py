import requests
from bs4 import BeautifulSoup

# get HTML code
def fetch_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Get site title
def get_title(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.text if soup.title else "No title"
    return title

# Getting keywords and meta description
def get_meta_info(html):
    soup = BeautifulSoup(html, "html.parser")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_keywords = soup.find("meta", attrs={"name": "keywords"})
    meta_content = meta_desc["content"] if meta_desc else "No description"
    keywords = meta_keywords["content"] if meta_keywords else "No keywords"
    return meta_content, keywords

# Getting all Redirecting links
def get_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = [a.get("href") for a in soup.find_all("a", href=True)]
    return links

# get JavaScript-redirects
def get_js_redirects(html):
    soup = BeautifulSoup(html, "html.parser")
    js_redirects = []
    for script in soup.find_all("script"):
        if script.string and ("window.location" in script.string or "document.location" in script.string):
            js_redirects.append(script.string.strip())
    return js_redirects

# extract iframe-src
def get_iframes(html):
    soup = BeautifulSoup(html, "html.parser")
    iframes = [iframe.get("src") for iframe in soup.find_all("iframe", src=True)]
    return iframes

# collecting outputs and formatting then append to file
def analyze_and_append(url, file):
    html_content = fetch_html(url)
    
    # appends titeln
    title = get_title(html_content)
    file.write(f"Page Title: {title}\n")

    # appends meta-information
    meta_desc, meta_keywords = get_meta_info(html_content)
    file.write(f"Meta Description: {meta_desc}\n")
    file.write(f"Meta Keywords: {meta_keywords}\n")

    # appends all links
    links = get_links(html_content)
    file.write(f"Found {len(links)} links:\n")
    for link in links[:5]:  # Print the first 5 links
        file.write(f"{link}\n")

    # appends JavaScript-redirections
    js_redirects = get_js_redirects(html_content)
    if js_redirects:
        file.write(f"Found {len(js_redirects)} JavaScript redirects:\n")
        for redirect in js_redirects:
            file.write(f"{redirect}\n")
    else:
        file.write("No JavaScript redirects found.\n")

    # appends iframe-src info
    iframes = get_iframes(html_content)
    if iframes:
        file.write(f"Found {len(iframes)} iframes:\n")
        for iframe in iframes:
            file.write(f"{iframe}\n")
    else:
        file.write("No iframes found.\n")
