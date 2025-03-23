import socket
import whois
import dns.resolver
from urllib.parse import urlparse
import tldextract

def extract_domain(url):
    parsed_url = urlparse(url)
    extracted = tldextract.extract(parsed_url.netloc)
    return f"{extracted.domain}.{extracted.suffix}"  # extracting domain name

def get_dns_info(domain):
    records = {}
    subdomain = f"www.{domain}"  # creates www-version

    def query_dns(domain_name, record_type):
        # DNS query and error handling 
        try:
            return [str(rdata) for rdata in dns.resolver.resolve(domain_name, record_type)]
        except dns.resolver.NoAnswer:
            return f"No {record_type} records found for {domain_name}"
        except dns.resolver.NXDOMAIN:
            return f"NXDOMAIN: {domain_name} does not exist"
        except Exception as e:
            return f"DNS Error: {e}"

    # tries with subdomain (www.DOMAIN.com)
    records["A"] = query_dns(subdomain, 'A')
    records["AAAA"] = query_dns(subdomain, 'AAAA')
    records["MX"] = query_dns(subdomain, 'MX')
    records["TXT"] = query_dns(subdomain, 'TXT')
    records["NS"] = query_dns(subdomain, 'NS')
    records["CNAME"] = query_dns(subdomain, 'CNAME')

    # if "NXDOMAIN" or no information, try domain
    for record in ["A", "AAAA", "MX", "TXT", "NS", "CNAME"]:
        if "NXDOMAIN" in records[record] or "No" in records[record]:
            records[record] = query_dns(domain, record)

    return records

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w  #returns whois
    except Exception as e:
        return {"error": str(e)}

def extract_and_append_domain_info(url, file):
    domain = extract_domain(url)  # Extract domain name

    dns_info = get_dns_info(domain)  # get DNS-poster
    whois_info = get_whois_info(domain)  # get WHOIS-info

    file.write(f"\n Analysing Domain: {domain}\n")
    
    # Appends DNS-info
    file.write("\n [DNS INFO]\n")
    for record_type, record_values in dns_info.items():
        file.write(f"{record_type}: {record_values}\n")

    # Appends WHOIS-info
    file.write("\n [WHOIS INFO]\n")
    file.write(str(whois_info) + "\n")  
