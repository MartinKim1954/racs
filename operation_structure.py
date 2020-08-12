from communication_structure import Communication
from doosan_library import *
from setting import *

class Operation(Communication):
    def do_go_to_home_position(self):
        if self.home_positioned == True:
            stop(DR_HOLD)   # is needed?
            movel(posx(self.HOME_POSITION), time=3)
            self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['wait_positioned']
            self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['home_positioned']

    def do_go_to_wait_position(self):
        if self.wait_positioned == True:
            movel(posx(self.WAIT_POSITION), time=3)
            self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['home_positioned']
            self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['wait_positioned']

    def do_wait(self):
        if self.PTOR_data[3] & self.PTOR_dic['wait']:
            pass
        if self.wait == True:
            self.RTOP_data[3] & self.RTOP_dic['waiting']

    def do_start_charging(self):
        if self.start == True:
            self.do_grasp_combo()
            self.do_grasp_chademo()

    def do_finish_charging(self):
        pass

    def do_recover(self):
        pass

    def do_grasp_combo(self):
        if self.combo_state == True:
            # 영민 will teach the robot and its position will be passed by Global_variables.
            # With passed data, movel(~~~) / set(~~~) will be written and run.
            self.RTOP_data[5] = self.RTOP_data[5] & ~self.RTOP_dic['chademo_grasped']
            self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['combo_grasped']
            # Gun connection test will be done with vision data calculated by me.
        
    def do_grasp_chademo(self):
        if self.chademo_state == True:
            # 영민 will teach the robot and its position will be passed by Global_variables.
            # With passed data, movel(~~~) / set(~~~) will be written and run.            
            self.RTOP_data[5] = self.RTOP_data[5] & ~self.RTOP_dic['combo_grasped']
            self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['chademo_grasped']
            # Gun connection test will be done with vision data calculated by me.

    def do_release_combo(self):
        pass

    def do_release_chademo(self):
        pass


    