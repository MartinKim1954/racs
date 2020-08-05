# Socket Communication Setting - as SERVER


PORT = 20002
socket = server_socket_open(PORT)
txData = b"33b0a"


try:
    server_socket_state(socket)
    tp_popup("TCP/IP has opened.")
except DR_Error(DR_ERROR_TYPE):
    tp_popup("Data type is wrong in opening a socket.")
except DR_Error(DR_ERROR_RUNTIME):
    tp_popup("An error occured while terminating.")

try:
    writeStatus = server_socket_write(socket, txData)
    if writeStatus == 0:
        tp_popup("Transmitted successfully!")
    elif writeStatus == -1:
        tp_popup("Not connected to the client while transmitting.")
    elif writeStatus == -2:
        tp_popup("An error occured while transmitting.")
except DR_Error(DR_ERROR_TYPE):
    tp_popup("Data type is wrong in transmitting data")

try:
    rxLength, rxData = server_socket_read(socket, length=-1, timeout=3)
    if rxLength == 0:
        tp_popup("Data length: {}\n Data received: {}" .format(rxLength, rxData))
    elif rxLength == -1:
        tp_popup("Not connected to the client while receiving.")
    elif rxLength == -2:
        tp_popup("An error occured while receiving.")
    elif rxLength == -3:
        tp_popup("Timeout(more than 3 seconds)")


if server_socket_close(socket) == False:
    tp_popup("TCP/IP has closed.")