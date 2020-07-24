# SOCKET COMMUNICATION

from setting import *
from datastructure import plcDataList, visDataList
from datahandling import read_data

# Communication Setting
'''
To communicate with clients as SERVER, 
you are asked to set up 'IP address' and 'Port Number'.
'''
PLC_PORT = 20002
VISION_PORT = 20003
plcSocket = server_socket_open(PLC_PORT)
visSocket = server_socket_open(VISION_PORT)

commThID = thread_run(read_data, loop=True)


server_socket_close(socket)
