from doosan_library import *

class Setting:
    # Position setting
    HOME_POSITION = [0, 0, 0, 0, 0, 0]
    WAIT_POSITION = [0, 0, 0, 0, 0, 0]
    # Data setting
    PTOR_data = [0 for _ in range(8)]
    RTOP_data = [0 for _ in range(8)]
    DEFAULT = 0x00
    ''' Basic Assigments '''
    PTOR_dic = {
        'comm_connected': 0x01, 'connect_vision': 0x02, 'clamp': 0x04, 'push': 0x08, 'emergency_pushed': 0x80,
        'go_to_home_position': 0x01, 'go_to_wait_position': 0x02,
        'wait': 0x01, 'start_charging': 0x02, 'finish_charging': 0x04, 'recover': 0x08,
        'grasp_combo': 0x01, 'grasp_chademo': 0x02,
    }
    RTOP_dic = {
        'comm_connected': 0x01, 'vision_connected': 0x02, 'clamped': 0x04, 'pushed': 0x08, 'emergency_pushed': 0x80,
        'home_positioned': 0x01, 'wait_positioned': 0x02,
        'waiting': 0x01, 'charging': 0x02, 'finished_charging': 0x04, 'recovered': 0x08,
        'combo_grasped': 0x01, 'chademo_grasped': 0x02,
    }
    # Communication setting
    PLC_PORT = 50000
    VISION_PORT = 60000
    # Open Ports
    plc_socket = server_socket_open(PLC_PORT)

    
    # Open it later.....
    # vission_socket = server_socket_open(VISION_PORT)
