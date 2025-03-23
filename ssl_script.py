import os
import tldextract

def fetch_ssl_certificate(url, file):
    print("\n\n [Fetching SSL certificate] \n", file=file)
    
    # extract domain name
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    # creates full URL without https://
    full_url = f"https://{domain}"
    
    # temp file to save SSL cert info
    temp_file = "temp_ssl_output.txt"
    
    # command to get cert info
    command = f"echo | openssl s_client -showcerts -servername {domain} -connect {domain}:443 2>/dev/null > {temp_file}"
    
    try:
        # Run command
        os.system(command)
        
        # append to tempfile
        with open(temp_file, "r") as temp:
            content = temp.read()
            file.write(content)
        
        # delete tempfile
        os.remove(temp_file)
    
    except Exception as e:
        file.write(f"Error: {e}\n")
