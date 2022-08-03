"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""

import socket
import pickle
import sys

def client_fun(temp):

    #collect main_dict from crypto_machine
    fun_dict = temp

    #make pickle file
    msg = pickle.dumps(fun_dict)

    #Create a socket and connect it to the server at the designated IP and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("168.62.194.224", 8080))
    
    #Send dictionary to the server using TCP socket
    s.sendall(msg)
    
    # TODO: Receive a response from the server and close the TCP connection
    print(s.recv(1024).decode())
    s.close()