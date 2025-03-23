import requests

def extract_html(url, file):
    print("\n \n ", file=file)
    try:
        response = requests.get(url)
        file.write(response.text)  # Write the full HTML code to the file
    except Exception as e:
        file.write(f"Error: {e}\n")
