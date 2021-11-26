#This is the client pinger program that connects to the server
#and reports messages, and time it took to connect to ping, and 
#reports time outs, and displays average, max, min, and percentage
#loss for packet loss 

import socket
from socket import AF_INET, SOCK_DGRAM
import time

#open client socket, set timeout time to 1 second
cSocket = socket.socket(AF_INET, SOCK_DGRAM)
cSocket.settimeout(1)
#counter for number of pings
x = 1
#for max, minimum, average return time, and packet loss percentage
return_vals = []

#pings to server 10 times, get start time of each ping, displays start time
#sends message to server, tries to get response from server, if got response
#gets time took to get response, displays time took and message from server to
#screen, if no response from server displays time out and just when ping
#started
while x <= 10:
    start = time.time()
    message = ('PING ' + str(x) + ' STARTS AT TIME ' + str(start)) 
    cSocket.sendto(message.encode(),('localhost', 12000))
    try:
        message, address = cSocket.recvfrom(1024)
        timeTook = (time.time()-start)
        return_vals.append(timeTook)
        print('Response from server is: ' + str(message))
        print('Time took was: ' + str(timeTook) + ' secs')
    except socket.timeout:
        print(message)
        print('Request timed out')
    x += 1

#finds the min, max, and average return time, and percent package loss 
if x > 10:
    avgRTT = sum(return_vals) / len(return_vals)
    print('Maximum return time is: ' + str(max(return_vals)) + ' seconds')
    print('Minimum return time is: ' + str(min(return_vals)) + ' seconds')
    print('Average return time is: ' + str(avgRTT) + ' seconds')
    print('Percentage packet loss rate is: ' + str(((10 - len(return_vals))/10) * 100) + '%') 
    cSocket.close()
    
