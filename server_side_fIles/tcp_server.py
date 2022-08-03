import socket
import pickle
import sys
import time

from plot_data import plot

import os
import sys
import psutil
import logging

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)

    python = sys.executable
    os.execl(python, python, *sys.argv)

#set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#allow any IP to be commincated with via port 8080 (easier to do all 0's)
s.bind(("0.0.0.0", 8080))
#listen for any tx
s.listen()
#accept tx
conn, addr = s.accept()
try:
    with conn:
        #connection establish message
        print('Connected by', addr)
        while True:
            #take in data
            data = conn.recv(1024)
            if not data:
                continue
                print("test")
            else:
                #unpack pickle
                crypto_data = pickle.loads(data)
                link = plot(crypto_data)
                conn.sendall((link).encode()) #final sendall message should be link
                s.close()
                restart_program()
except KeyboardInterrupt:
    s.close()
