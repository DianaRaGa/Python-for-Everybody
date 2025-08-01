#Exercise 2: Change your socket program so that it counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire
# document and count the total number of characters and display the count of the number of characters at the
# end of the document.

# Code: https://www.py4e.com/code3/socket1.py
import socket
import re
import sys

#Prompting the user to a URL and finding the host and port to connect to
user_URL=input("Please enter a URL to access to:\n")
match = re.match(r"^http://([^/]+)(/.*)", user_URL)#Getting the host and path with regular expressions
if match:
    host=match.group(1)#This is to extract the match in the get_host 
    path = match.group(2)
        
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

    recived_data = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
            
        recived_data += data
        if len(recived_data.decode())>=3000:
            break
        print(data.decode(),end='')
    print(f"The number of characters is: {len(recived_data.decode())}")
        
    
    mysock.close()
    
except:
    print("It was not possible to connect to the given URL")
    
finally:
    mysock.close()