from doosan_library import *

class Setting:
    # Position setting
    HOME_POSITION = [0, 0, 0, 0, 0, 0]
    WAIT_POSITION = [0, 0, 0, 0, 0, 0]
    # Data setting
    PTOR_data = [0 for _ in range(8)]
    RTOP_data = [0 for _ in range(8)]
    DEFAULT = 0x00          # Default Value
    unclamp_combo = 0       # SIGNAL: ROBOT -> PLC
    unclamp_chademo = 0     # SIGNAL: ROBOT -> PLC
    # Combo Grasping
    combo_grasping_pos1 = Global_g_combo1
    combo_grasping_pos2 = Global_g_combo2
    combo_grasping_pos3 = Global_g_combo3
    combo_grasping_pos4 = Global_g_combo4
    combo_grasping_pos5 = Global_g_combo5
    combo_grasping_pos6 = Global_g_combo6
    combo_grasped = 0       # Value to confirm whether grasping Combo is carried out successfully
    # CHAdeMO Grasping
    chademo_grasping_pos1 = Global_g_chademo1
    chademo_grasping_pos2 = Global_g_chademo2
    chademo_grasping_pos3 = Global_g_chademo3
    chademo_grasping_pos4 = Global_g_chademo4
    chademo_grasping_pos5 = Global_g_chademo5
    chademo_grasping_pos6 = Global_g_chademo6
    chademo_grasped = 0     # Value to confirm whether grasping CHAdeMO is carried out successfully
    # Combo Test
    combo_test_pos1 = Global_t_combo1
    combo_test_pos2 = Global_t_combo2
    combo_test_pos3 = Global_t_combo3
    combo_test_pos4 = Global_t_combo4
    combo_test_pos5 = Global_t_combo5
    combo_test_pos6 = Global_t_combo6
    combo_test_completed = 0
    # CHAdeMO Test
    chademo_test_pos1 = Global_t_chademo1
    chademo_test_pos2 = Global_t_chademo2
    chademo_test_pos3 = Global_t_chademo3
    chademo_test_pos4 = Global_t_chademo4
    chademo_test_pos5 = Global_t_chademo5
    chademo_test_pos6 = Global_t_chademo6
    chademo_test_completed = 0
    
    ''' Basic Assigments '''
    PTOR_dic = {
        'comm_connected': 0x01, 'connect_vision': 0x02, 'clamp': 0x04, 'push': 0x08, 
        'combo_holder_unclamped': 0x10, 'chademo_holder_unclamped': 0x20, 'emergency_pushed': 0x80,
        'go_to_home_position': 0x01, 'go_to_wait_position': 0x02,
        'wait': 0x01, 'start_charging': 0x02, 'finish_charging': 0x04, 'recover': 0x08,
        'grasp_combo': 0x01, 'grasp_chademo': 0x02,
    }
    RTOP_dic = {
        'comm_connected': 0x01, 'vision_connected': 0x02, 'clamped': 0x04, 'pushed': 0x08, 
        'unclamp_combo_holder': 0x10, 'unclamp_chademo_holder': 0x20, 'emergency_pushed': 0x80,
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
