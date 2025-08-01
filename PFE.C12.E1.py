#Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read
# any web page. You can use split('/') to break the URL into its component parts so you can extract
# the host name for the socket connect call. Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

# Code: https://www.py4e.com/code3/socket1.py
import socket
import re
import sys

#Prompting the user to a URL and finding the host and port to connect to
user_URL=input("Please enter a URL to access to:\n")
match = re.match(r"^http://([^/]+)(/.*)", user_URL)#Getting the host and path with regular expressions
if match:
    host=match.group(1)#This is to extract the match in the get_host 
    path = match.group(2) if match.group(2) else "/"
        
else:
    print("No valid host found")
    exit()

#Try and except to make the port number a integer
while True:
    user_Port=input("Please enter a number to connect to a port, or put 'done' to exit:\n")
    
    if user_Port.lower() == 'done':
        print("Exiting the program")
        sys.exit()
    try:
        user_Port=int(user_Port)
        break
    
    except ValueError:
        print("Error, the port number must be a numeric whole number value")
    
#Making the connection with the socket and connects to the host
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, user_Port))

#Try and except block to try and making the connection to the URL the user put
try:
    cmd = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n".encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    
    mysock.close()
    
except:
    print("It was not possible to connect to the given URL")