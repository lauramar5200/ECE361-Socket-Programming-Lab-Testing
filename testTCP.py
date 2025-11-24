"""
Python test script for lab 3 assignment 1 to auto create number of clients to connect to the tcp server.
 
---SETUP---
1) Place this script along with your server.py and client.py implmentations in the same directory.
2) Replace the file "assignment1_client.py" with whatever your client.py file name is.
3) You can change the number of clients to create by changing the NUM_CLIENTS variable.

---RUNNING---
1) Depnding on how you implement your lab, ensure the server is running.
    I've been running everything in a terminal, so run something like: python3 server.py
2) Once it's running, then you can run this script.
    In another terminal, run: python3 testTCP.py

NOTE: This uses python subprocesses, not threads. So there will be NUM_CLIENTS # of python processes created. Just be aware of this for system performance, probably don't go creating a million processes...
"""
import subprocess
import time

NUM_CLIENTS = 5

for i in range(NUM_CLIENTS):
    print(f"Creating client process {i}...")
    subprocess.Popen(["python3", "assignment1_client.py"])
    time.sleep(0.1)
print(f"All clients created.")
