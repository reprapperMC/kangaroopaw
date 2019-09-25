import threading
from time import sleep
from connect_hardware import connectHardware
from nextech_gauge import nextechReading

class dragTest():
    def __init__(self):
        self.nextech = nextechReading()
    
    def printer_x_prep(self, devices):
        with open('gcodes/machine_X_drag.gcode', 'r') as gcode:
            gcode_lines = gcode.read().splitlines()
        for line in gcode_lines:
            devices.ports['printer'].write(('\r\n' + line + '\r\n').encode('utf-8'))

    def printer_y_prep(self, devices):
        with open('gcodes/machine_Y_drag.gcode', 'r') as gcode:
            gcode_lines = gcode.read().splitlines()
        for line in gcode_lines:
            devices.ports['printer'].write(('\r\n' + line + '\r\n').encode('utf-8'))

    def printer_z_prep(self, devices):
        with open('gcodes/machine_Z_drag.gcode', 'r') as gcode:
            gcode_lines = gcode.read().splitlines()
        for line in gcode_lines:
            devices.ports['printer'].write(('\r\n' + line + '\r\n').encode('utf-8'))

    def x_drag_actuate(self, devices):
        with open('gcodes/fixture_X_drag_calibration.gcode', 'r') as gcode:
            gcode_lines = gcode.read().splitlines()
        for line in gcode_lines:
            devices.ports['actuator'].write(('\r\n' + line + '\r\n').encode('utf-8'))

    def y_drag_actuate(self, devices):
        with open('gcodes/fixture_Y_drag_calibration.gcode', 'r') as gcode:
            gcode_lines = gcode.read().splitlines()
        for line in gcode_lines:
            devices.ports['actuator'].write(('\r\n' + line + '\r\n').encode('utf-8'))

    def z_drag_actuate(self, devices):
        with open('gcodes/fixture_Z_drag_calibration.gcode', 'r') as gcode:
            gcode_lines = gcode.read().splitlines()
        for line in gcode_lines:
            devices.ports['actuator'].write(('\r\n' + line + '\r\n').encode('utf-8'))

    def x_axis_drag_test(self, devices, command):
        zero_gauge = self.nextech.zero_gauge(devices, 'dfs_xz')
        self.printer_x_prep(devices)
        sleep(12.0)
        reading = []
        t = threading.Timer(4, self.x_drag_actuate, args=(devices,)).start()
        reading_count = 100
        while reading_count != 0:
            reading.append(self.nextech.get_clean_force_reading(devices, 'dfs_xz', 'x'))
            reading_count -= 1
            sleep(0.5)
        return reading

    def y_axis_drag_test(self, devices, command):
        zero_gauge = self.nextech.zero_gauge(devices, 'dfs_y')
        self.printer_y_prep(devices)
        sleep(5.0)
        reading = []
        t = threading.Timer(8, self.y_drag_actuate, args=(devices,)).start()
        reading_count = 100
        while reading_count != 0:
            reading.append(self.nextech.get_clean_force_reading(devices, 'dfs_y', 'x'))
            reading_count -= 1
            sleep(0.5)
        return reading
            
        
