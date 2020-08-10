from doosan_library import *

class Setting:
    # Position setting
    home_position = [0, 0, 0, 0, 0, 0]
    wait_position = [0, 0, 0, 0, 0, 0]
    # Data setting
    PTOR_data = [0 for _ in range(8)]
    RTOP_data = [0 for _ in range(8)]
    ''' Basic Assigments '''
    PTOR_dic = {
        'comm_connected': 0x01, 'connect_vision': 0x02, 'clamp': 0x04, 'push': 0x08, 'emergency_pushed': 0x80,
        'go_to_home_position': 0x01, 'go_to_wait_position': 0x02,
        'wait': 0x01, 'start_charging': 0x02, 'finish_charging': 0x04, 'recover': 0x08,
        'grasp_combo': 0x01, 'grasp_chademo': 0x02, 'release_combo': 0x10, 'release_chademo': 0x20,
    }
    RTOP_dic = {
        'comm_connected': 0x01, 'vision_connected': 0x02, 'clamped': 0x04, 'pushed': 0x08, 'emergency_pushed': 0x80,
        'go_to_home_position_confirmed': 0x01, 'go_to_wait_position_confirmed': 0x02,
        'home_positioned': 0x10, 'wait_positioned': 0x20,
        'wait_confirmed': 0x01, 'start_charging_confirmed': 0x02, 'finish_charging_confirmed': 0x04, 'recover_confirmed': 0x08, 
        'waiting': 0x10, 'charging': 0x20, 'finished_charging': 0x40, 'recovered': 0x80,
        'grasp_combo_confirmed': 0x01, 'grasp_chademo_confirmed': 0x02, 'combo_grasped': 0x04, 'chademo_grasped': 0x08,
        'release_combo_confiremd': 0x10, 'release_chademo_confirmed': 0x20,
    }
    # Communication setting
    PLC_PORT = 50000
    VISION_PORT = 60000
    # Open Ports
    plc_socket = server_socket_open(PLC_PORT)

    
    # Open it later.....
    # vission_socket = server_socket_open(VISION_PORT)
