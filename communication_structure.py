from doosan_library import *
from setting import *

class Communication(Setting):
    def get_PTOR_data(self):
        _, self.raw_data = server_socket_read(self.plc_socket, length=-1, timeout=2)
        self.comm_state = server_socket_state(self.plc_socket)

    def split_and_decode(self):
        for i in range(len(self.PTOR_data)):
            j = i*2
            self.PTOR_data[i] = self.raw_data[j:(j+2)]
            self.PTOR_data[i] = int(self.PTOR_data[i], 16)

    def communication_check(self):
        if self.PTOR_data[0] & self.PTOR_dic['comm_connected']:
            self.comm_state = True
            print("Communication Successful!")
            self.RTOP_data[0] = self.RTOP_data[0] | self.RTOP_dic['comm_connected']
        else:
            self.comm_state = False
            print("Communication Unsuccessful!")
            
    def vision_check(self):
        if self.comm_state:
            if self.PTOR_data[0] & self.PTOR_dic['vision_connected']:
                self.vis_state = True
                print("Vision Connection Successful!")
                self.RTOP_data[0] = self.RTOP_data[0] | self.RTOP_dic['vision_connected']
            else:
                self.vis_state = False
                print("Vision Connection Unsuccessful!")
        else:
            print("Communication Unsuccessful!")

    def IO_check(self):
        if self.comm_state:
            self.clamping_tool_state = get_tool_digital_input(1)
            self.pushing_tool_state = get_tool_digital_input(2)
            if (self.PTOR_data[0] & self.PTOR_dic['clamp']) or (self.clamping_tool_state):
                set_tool_digital_output(1, ON)
                print("Clamped!")
                self.RTOP_data[0] = self.RTOP_data[0] | self.RTOP_dic['clamped']
            else:
                set_tool_digital_output(1, OFF)
                print("Unclamped!")
            if (self.PTOR_data[0] & self.PTOR_dic['pushed']) or (self.pushing_tool_state):
                set_tool_digital_output(2, ON)
                print("Pushed!")
                self.RTOP_data[0] = self.RTOP_data[0] | self.RTOP_dic['pushed']
            else:
                set_tool_digital_output(2, OFF)
                print("Unpushed!")
        else:
            print("Communication Unsuccessful!")

    def emergency_check(self):
        if self.PTOR_data[0] & self.PTOR_dic['emergency_pushed']:
            stop(DR_HOLD)
            print("Emergency Pushed!")
            server_socket_close(self.plc_socket) # Cut the communication

    def position_check(self):
        if self.comm_state:
            self._current_position, _ = get_current_posx(ref=DR_BASE)
            if self._current_position == posx(self.home_position):
                self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['home_positioned']
            elif self._current_position == posx(self.wait_position):
                self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['wait_positioned']
            else:
                if self.PTOR_data[1] & self.PTOR_dic['go_to_home_position']:
                    self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['go_to_home_position_confirmed']
                elif self.PTOR_data[1] & self.PTOR_dic['go_to_wait_position']:
                    self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['go_to_wait_position_confirmed']
        else:
            print("Communication Unsuccessful!")

    def command_check(self):
        if self.comm_state:
            if self.PTOR_data[3] & self.PTOR_dic['wait']:
                self.RTOP_data[3] = self.RTOP_data[3] | self.RTOP_dic['wait_confirmed']
                # send the signal first, then act a little later.
            elif self.PTOR_data[3] & self.PTOR_dic['start_charging']:
                self.RTOP_data[3] = self.RTOP_data[3] | self.RTOP_dic['start_charging_confirmed']
                # send the signal first, then act a little later.
            elif self.PTOR_data[3] & self.PTOR_dic['finish_charging']:
                self.RTOP_data[3] = self.RTOP_data[3] | self.RTOP_dic['finish_charging_confirmed']
                # send the signal first, then act a little later.
            elif self.PTOR_data[3] & self.PTOR_dic['recover']:
                self.RTOP_data[3] = self.RTOP_data[3] | self.RTOP_dic['recover_confirmed']
                # send the signal first, then act a little later.
            else:
                print(f"Error Command: {self.PTOR_data[1]}")
        else:
            print("Communication Unsuccessful!")

    def charging_type_check(self):
        if self.comm_state:
            if self.PTOR_data[5] & self.PTOR_dic['grasp_combo']:
                self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['grasp_combo_confirmed']
                # send the signal first, then act a little later.
            elif self.PTOR_data[5] & self.PTOR_dic['grasp_chademo']:
                self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['grasp_chademo_confirmed']
                # send the signal first, then act a little later.
            elif self.PTOR_data[5] & self.PTOR_dic['release_combo']:
                self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['release_combo_confiremd']
                # send the signal first, then act a little later.
            elif self.PTOR_data[5] & self.PTOR_dic['release_chademo']:
                self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['release_chademo_confirmed']
                # send the signal first, then act a little later.
        else:
            print("Communication Unsuccessful!")

    def encode_and_merge(self):
        self.encodedRTOP_data = b''
        for i in range(len(self.PTOR_data)):
            self.PTOR_data[i] = str(hex(self.PTOR_data[i]))
            self.PTOR_data[i] = self.PTOR_data[i][2:].encode()
            self.encodedRTOP_data += self.PTOR_data[i]

    def send_RTOP_data(self):
        server_socket_write(self.plc_socket, self.encodedRTOP_data)
        if self.RTOP_data[9] == '99':
            stop(DR_HOLD)   # After sending data, it stops

    def reset_data(self):
        self.RTOP_data = [0 for _ in range(8)]
