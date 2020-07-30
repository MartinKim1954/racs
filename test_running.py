from communication_structure import Communication
from operation_structure import Operation
from doosan_library import *
from setting import *

robot_communication = Communication()
robot_operation = Operation()

first_thread = thread_run(updating, loop=True)

def updating():
    robot_communication.get_PTOR_data()
    robot_communication.decode_and_split()
    robot_communication.communication_check()
    robot_communication.command_check()   # Done without udpates from 'Operation'
    robot_communication.position_check()  # Done without udpates from 'Operation'
    robot_communication.IO_status_check()
    # robot_communication.charging_type() # 이건 어떡할건지.... 로봇이 무슨 타입인지 그 전 프로세스가 없으면 확인할 수가 없음. 근데 어떤 플로우로 확인할건지?
    robot_communication.emergency_pushed_check()
    robot_communication.merge_and_encode()
    robot_communication.send_RTOP_data()

# 로봇 동작 관련
while True:
    pass
