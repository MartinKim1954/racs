from doosan_library import *

class Setting:
    # Position setting
    home_position = [0, 0, 0, 0, 0, 0]
    wait_position = [0, 0, 0, 0, 0, 0]
    # Data setting
    PTOR_data = ['00' for _ in range(10)]
    RTOP_data = ['00' for _ in range(10)]
    command_list = [['A0', 'B0', 'C0', 'Z0'], 
                    ['AC', 'BC', 'CC', 'ZC'], 
                    ['0A', '0B', '0C', '0Z']]
    position_list = [['H0', 'W0'],
                     ['HC', 'WC'],
                     ['0H', '0C']]
    # Communication setting
    PLC_PORT = 50000
    VISION_PORT = 60000
    # Open Ports
    plc_socket = server_socket_open(PLC_PORT)
    vission_socket = server_socket_open(VISION_PORT)
    # git test