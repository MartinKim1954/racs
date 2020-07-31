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
    ''' Basic Assigments '''
    # Status
    COMMUNICATION_CONNECTED = 0x01
    EMERGENCY_PUSHED = 0x02
    CLAMP = 0x04
    CLAMPED = 0x04
    # Command
    WAIT = 0x01
    START_CHARGING = 0x02
    FINISH_CHARGING = 0x04
    RECOVER = 0X08
    WAIT_CONFIRMED = 0x01
    START_CHARGING_CONFIRMED = 0x02
    FINISH_CHARGING_CONFIRMED = 0x04
    RECOVER_CONFIRMED = 0x08
    WAITING = 0x10
    CHARGING = 0x20
    FINISHED_CHARGING = 0x40
    RECOVERED = 0x80
    # Position
    GO_TO_HOME_POSITION = 0x01
    GO_TO_WAIT_POSITION = 0x02
    GO_TO_HOME_POSITION_CONFIRMED = 0x01
    GO_TO_WAIT_POSITION_CONFIRMED = 0x02
    HOME_POSITIONED = 0x10
    WAIT_POSITIONED = 0x20
    # Charging Type
    COONECT_COMBO = 0x01
    CONNECT_CHADEMO = 0x02
    NOT_CONNECTED = 0x01
    CONNECTING_WITH_VISION_DATA_COMING_IN = 0x02
    COMBO_CONNECTED = 0x04
    CHADEMO_CONNECTED = 0x08
    COMBO_DISCONNECTED = 0x10
    CHADEMO_DISCONNECTED = 0x20