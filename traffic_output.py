import time
from mitmproxy import ctx

def request(flow):
    # preparing stamps
    request_info = f"Request at {time.time()}:\n"
    request_info += f"URL: {flow.request.url}\n"
    request_info += f"Headers: {flow.request.headers}\n"

    # Ignore Binary text
    try:
        text_content = flow.request.content.decode('utf-8', 'ignore')
    except UnicodeDecodeError:
        text_content = None
    if text_content:
        request_info += f"Content: {text_content}\n"
    
    # write request-information 
    with open("traffic_data.txt", "a") as f:
        f.write(request_info)

def response(flow):
    # Förbered information om response
    response_info = f"Response at {time.time()}:\n"
    response_info += f"Status Code: {flow.response.status_code}\n"
    response_info += f"Headers: {flow.response.headers}\n"

    # Ignore Binary text
    try:
        text_content = flow.response.content.decode('utf-8', 'ignore')
    except UnicodeDecodeError:
        text_content = None
    if text_content:
        response_info += f"Content: {text_content}\n"
    
    # write response-information
    with open("traffic_data.txt", "a") as f:
        f.write(response_info)
    f.write("\n" + "-"*40 + "\n")  # separator between request and responses
