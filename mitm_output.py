from mitmproxy.net.http.http1.assemble import assemble_request, assemble_response

f = open('/home/vagrant/PhisherMan/proxy_output.txt', 'w')

def response(flow):
    try:
        f.write("=== REQUEST ===\n")
        f.write(assemble_request(flow.request).decode('utf-8'))
        f.write("\n")

        f.write("=== RESPONSE ===\n")
        f.write(assemble_response(flow.response).decode('utf-8'))
        
    except:
        pass  # letting run if having problems
