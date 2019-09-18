# Class for writing/reading and parsing data with the Nextech DFS force gauge 


class nextechReading():
    def serial_read_write(serial, command):
        serial.write((command + '\n').encode('utf-8'))
        return serial.readline()

    def clean_reading(self, reading):
        reading = str(reading)
        if "b'\\r" not in reading and "b'" not in reading:
            return "Error: Value format different than expected in beginning"
        elif "b'\\r" in reading:
            reading_split = (reading.partition("b'\\r"))[2]
        elif "b'" in reading:
            reading_split = (reading.partition("b'"))[2]

        if "\\tN" not in reading_split:
            return "Error: Value format different than expected in end"
        elif "\\tN" in reading_split:
            reading_cleaned = reading_split[:reading_split.find("\\tN")]

        return reading_cleaned

    def get_clean_reading(serial, command):
        reading = serial_read_write(serial, command)
        return clean_reading(reading)
