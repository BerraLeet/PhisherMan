import requests

def expand_url(url, file):
    print("\n \n ", file=file)
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        final_url = response.url  # End destination
        file.write(f"Final Destination or redirected to: {final_url}\n")
    except Exception as e:
        file.write(f"Error: {e}\n")
