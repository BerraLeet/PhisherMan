from mitmproxy.net.http.http1.assemble import assemble_request, assemble_response

f = open('/home/vagrant/PhisherMan/proxy_output.txt', 'w')

def response(flow):
    f.write(assemble_request(flow.request).decode('utf-8')) # Ignoring Binary data
