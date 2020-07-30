
from doosan_library import *
from setting import *

class Operation(Setting):
    def get_current_position(self):
        self.currentPos, _ = get_current_posx(ref=DR_BASE)
        if self.currentPos == posx(self.home_position):
            self.outData = 1

        elif self.currentPos == posx(self.wait_position):
            self.outData = 1

    def to_home_position(self):
        print("Moving to 'Home Position..'")
        # 나중에 home position 위치 지정해서 저장하고 움직이기
        # home position 도달 '전'엔 01을 보내고
        # home position 도달 '후'엔 00을 보내기

    def to_wait_position(self):
        print("Moving to 'Wait Position..'")
        # 나중에 wait position 위치 지정해서 저장하고 움직이기
        # wait position 도달 '전'엔 09을 보내고
        # wait position 도달 '후'엔 10을 보내기

    def do_wait(self):
        print("Waiting..")
        

    def start_charging(self):
        pass

    def finish_charging(self):
        pass
    
    def do_recover(self):
        pass

