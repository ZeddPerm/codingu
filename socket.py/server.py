###server.py
from socket import *
##host=''
##port=12345
##s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.bind((host, port))
##print('socket binded to', port)
##backlog = 5
##s.listen(backlog)
##conn,addr = s.accept()
##print ('socket is listening')
##print ("Got connection from",addr)
##while 1:
##    name=input('Hello, say something to the client')
##    print("waiting for client's response")
##    conn.send(name.encode())
##    data=conn.recv(1024).decode('utf-8')
##    print('Received from client address: ', addr)
##    print("Message received: ",data)
##conn.close()
####################===================== RESTART: chat message above /home/pi/Desktop/socket.py/server.py ===========================
##host=''
##port=12345
##s=socket(AF_INET,SOCK_STREAM)
##server_ip_address=gethostbyname("google.com")
##server_port=80
##s.connect((server_ip_address,server_port))
##s.sendall(b"GET / HTTP/1.1\r\n\r\n")
##while True:
##     received_letter=s.recv(1).decode("utf-8")
##     if received_letter=='':
##          break
##     print(received_letter,end='')
##s.close()
s=socket(AF_INET,SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
##browser,browser_address=s.accept()
##print("Browser connected at address: {}".format(browser_address))
##while True:
##     ch=None
##     message=""
##     while message[len(message)-2:]!='\r\n':
##          ch=browser.recv(1).decode('utf-8')
##          message=message+ch
##     print("Message from browser: "+message)
##     browser.sendall(b"""HTTP/1.1 200 OK\r\n
##        <!DOCTYPE html>
##        <html>
##         <head>
##          <title>
##           Python Web Server
##          </title>
##          <h1>
##           Python Web Server
##          </h1>
##         </head>
##         <body>
##          <p>A Python web server is serving this webpage.</p>
##         </body>
##        </html>
##             """)
##browser.close()
