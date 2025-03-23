def append_proxy_output(filename):
    try:
        with open("proxy_output.txt", "r") as proxy_file:
            proxy_content = proxy_file.read()
            with open(filename, "a") as file:
                file.write("\n\n==== Proxy Output ====\n")
                file.write(proxy_content)
            print("[INFO] Proxy output appended successfully.")
    except FileNotFoundError:
        print("[ERROR] proxy_output.txt not found.")
    except Exception as e:
        print(f"[ERROR] Failed to append proxy output: {str(e)}")


