import socket, requests, re

# socket.gethostbyname() translates a host name to IPv4 address format.
# socekt.gethostname() returns a string containing the hostname of the machine
# where the interpreter is currently executing.
# in_addr = socket.gethostbyname(socket.gethostname())

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.com", 443))
print("Internal IP addr:", in_addr.getsockname()[0])

# My IPv4 addr is '172.30.1.18', based my own router, from the above print statement, and also can check my ip_add through ifconfig on terminal
# to whether those are same or not. ifconfig shows 'inet 172.30.1.18', thus both show the same results.
assert in_addr.getsockname()[0] == "172.30.1.18"

# Below few lines are to check my ip_addr on the Internet.
req = requests.get("http://ipconfig.kr")
# req.text returns a pure html file converted to the text format from the given url.
# Also we can notice that every time when we execute this file, the external ip_addr is changing.
out_addr = re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1]
print("External IP addr:", out_addr)
