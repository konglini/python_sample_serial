import serial
from threading import Thread


class serial_test:
    def __init__(self, port, baudrate):
        self._serial = None
        self.port = port
        self.baudrate = baudrate

    def connect(self):
        if self._serial is None:
            self._serial = serial.Serial(self.port, self.baudrate, timeout=2)

    def disconnect(self):
        if self._serial is None:
            return
        self._serial.close()
        self._serial = None

    def _serial_get_data(self):
        try:
            data = self._serial.readline()
            result_data = data.decode()
            return result_data
        except Exception as err:
            print(err)

    def read_data(self):
        while True:
            self.driver_data_list = self._serial_get_data()
            yield self.driver_data_list

    def serial_write(self, command):
        send = command.encode("utf-8")  # 바이트 객체 형변환
        self._serial.write(send)  # 데이터 전송


if "__main__" == __name__:
    serial_obj = serial_test('/dev/ttyUSB0', 115200)
    # serial_obj = serial_test("COM10", 115200)

    serial_obj.connect()

    serial_obj.serial_write("123")

    for data in serial_obj.read_data():
        print(f"---{data}")
        # global serial_data
        # serial_data = data
