import serial
from serial.tools import list_ports

class connectHardware():
    def __init__(self):
        self.ports = {}

    def connect_DFS50(self):
        # Need to add safety for multiple of the same gauge
        port = list(list_ports.grep("0403:6001"))[0].device
        self.ports['dfs50'] = serial.Serial(port, 38400)
        if self.ports['dfs50'].is_open:
            print("DFS50 connected")

    def connect_dial_switch(self):
        port = list(list_ports.grep("2341:0043"))[0].device
        self.ports['dialswitch'] = serial.Serial(port, 115200)
        if self.ports['dialswitch'].is_open:
            print("Dial Switch connected")
    
    def connect_actuator_controller(self):        
        port = list(list_ports.grep("RAMBo"))[0].device
        self.ports['actuator'] = serial.Serial(port, 120000)
        if self.ports['actuator'].is_open:
            print("Actuator controller connected")

    def connect_printer(self):
        if 'RAMBo' not in self.ports:
            print("Establish the connection with the actuator controller first")
        else:
            port = list(list_ports.grep("RAMBo"))[0].device
            self.ports['printer'] = serial.Serial(port, 120000)
            if self.ports['printer'].is_open:
                print("Printer controller connected")



