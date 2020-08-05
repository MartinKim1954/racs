from doosan_library import *
from setting import *

class Communication(Setting):
    def get_PTOR_data(self):
        _, self.raw_data = server_socket_read(self.plc_socket, length=-1, timeout=2)
        self.comm_state = server_socket_state(self.plc_socket)

    def split_data(self):
        for i in range(len(self.PTOR_data)):
            j = i*2
            self.PTOR_data[i] = self.raw_data[j:(j+2)]
            self.PTOR_data[i] = int(self.PTOR_data[i], 16)

    def communication_check(self):
        if self.PTOR_data[0] == self.PTOR_dic['comm_connected']:
            if self.comm_state == False:
                self.RTOP_data[0] = '00'
                print("Communication Unsuccessful!")
        elif self.PTOR_data[0] == '10':
            if self.comm_state == True:
                self.RTOP_data[0] = '10'
                print("Communication Successful!")
        else:
            print(f"Error Communication: {self.PTOR_data[0]}")

    def command_check(self):
        if self.comm_state == True:
            if self.PTOR_data[1] in self.command_list[0]:
                self._idx = self.command_list[0].index(self.PTOR_data[1])
                if self.RTOP_data[1] != self.command_list[2][self._idx]:
                    self.RTOP_data[1] = self.command_list[1][self._idx]
            else:
                print(f"Error Command: {self.PTOR_data[1]}")
        else:
            print("Fail to communicate with PLC!")

    def position_check(self):
        if self.comm_state == True:
            self._current_position, _ = get_current_posx(ref=DR_BASE)
            if self._current_position == posx(self.home_position):
                self.RTOP_data[2] = '0H'
            elif self._current_position == posx(self.wait_position):
                self.RTOP_data[2] = '0W'
            else:
                if self.PTOR_data[2] in self.position_list[0]:
                    self._idx = self.position_list[0].index(self.PTOR_data[2])
                    if self.RTOP_data[2] != self.position_list[2][self._idx]:
                        self.RTOP_data[2] = self.position_list[1][self._idx]
                else:
                    print(f"Error Position: {self.PTOR_data[2]}")
        else:
            print("Fail to communicate with PLC!")
    
    def IO_status_check(self):
        if self.comm_state == True:
            toolStatus = get_tool_digital_input(1)
            if toolStatus == False or self.PTOR_data[3] == '00':
                set_tool_digital_output(1, OFF)
                self.RTOP_data[3] == '00'
                print("Unclamping..")
            elif toolStatus == True or self.PTOR_data[3] == '10':
                set_tool_digital_output(1, ON)
                self.RTOP_data[3] == '10'
                print("Clamping..")
        else:
            print("Fail to communicate with PLC!")

    # def charging_type_check(self):
    #     if self.comm_state == True:
    #         if self.PTOR_data[2] == '00':
    #             print("Not Connected to any..")
    #             self.RTOP_data[2] == '00'
    #         elif self.PTOR_data[2] == 'd':
    #             pass
    #     else:
    #         print("Fail to communicate with PLC!")
    #         # tp_popup("Fail to communicate with PLC!")

    def emergency_pushed_check(self):
        if self.comm_state == True:
            if self.PTOR_data[9] == '00':
                self.RTOP_data[9] = '00'
                print("Emergency not pushed")
            elif self.PTOR_data[9] == '99':
                self.RTOP_data[9] = '99'
                print("Emergency pushed!")
        else:
            print("Fail to communicate with PLC!")

    def merge_and_encode(self):
        self.encodedRTOP_data = ""
        for i in range(len(self.RTOP_data)):
            self.encodedRTOP_data += self.RTOP_data[i]
        self.encodedRTOP_data = self.encodedRTOP_data.encode()

    def send_RTOP_data(self):
        server_socket_write(self.plc_socket, self.encodedRTOP_data)
        if self.RTOP_data[9] == '99':
            stop(DR_HOLD)   # After sending data, it stops