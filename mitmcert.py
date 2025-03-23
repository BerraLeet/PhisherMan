import subprocess
import time

def setup_mitmproxy():
    print("Starting mitmproxy...")
    mitmproxy_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'mitmproxy && exit'])

    time.sleep(5)

    print("Getting mitmproxy certificate...")
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c',
                      'wget -e use_proxy=yes -e http_proxy=http://localhost:8080 -e https_proxy=http://localhost:8080 http://mitm.it/cert/pem -O ~/mitmproxy-ca-cert.pem && exit'])

    print("Waiting until download finishes...")
    time.sleep(5)

    print("Moving certificate and updating certificates...")
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c',
                      'sudo mv ~/mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy.crt && sudo update-ca-certificates && exit'])


    print("Terminating mitmproxy process...")
    subprocess.Popen(['pkill', 'mitmproxy'])

    time.sleep(5)

    print("Starting mitmproxy with mitm_output.py script...")
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'mitmproxy -s mitm_output.py && exit'])

    print("Completed, Proxy is setup")

    

