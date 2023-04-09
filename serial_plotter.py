import argparse
import serial
import time
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description='CLI to read data from a user defined serial port and plot it using matplotlib')
    parser.add_argument('-p', '--port', type=str, help='Serial port to read from')
    parser.add_argument('-b', '--baudrate', type=int, default=9600, help='Baudrate of the serial port')
    parser.add_argument('-t', '--timeout', type=float, default=1, help='Timeout of the serial port')
    parser.add_argument('-s', '--sleep', type=float, default=0.1, help='Sleep time between each read')
    return parser.parse_args()


def main():
    args = parse_args()
    port = args.port
    baudrate = args.baudrate
    timeout = args.timeout
    sleep_time = args.sleep

    print("Opening serial port...")
    ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    print("Serial port opened")

    print("Starting plotter...")
    with plt.ion():
        fig, ax = plt.subplots()
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Value')

        print("Plotter started")
        while True:
            try:
                print(ser.readline())
                line = ser.readline().decode().split('\r\n')
                print(line)
                value = float(line)
                ax.scatter(time.monotonic(), value)
                ax.plot()
                plt.pause(sleep_time)
            except KeyboardInterrupt:
                break

        ser.close()
        plt.ioff()
        plt.show()


if __name__ == '__main__':
    main()