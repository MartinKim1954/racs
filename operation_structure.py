from communication_structure import Communication
from doosan_library import *
from setting import *

class Operation(Communication):
    def go_to_home_position(self):
        if self.RTOP_data[1] | self.RTOP_dic['go_to_home_position_confirmed']:
            stop(DR_HOLD)
            movel(posx(self.home_position), time=3)

    def go_to_wait_position(self):
        if self.RTOP_data[1] | self.RTOP_dic['go_to_wait_position_confirmed']:
            movel(posx(self.wait_position), time=3)

    def do_wait(self):
        pass

    def do_start_charging(self):
        