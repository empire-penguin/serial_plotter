# Pretty Serial Plotter

## Description

This is a CLI to read data from a user defined serial port and plot it using matlibplot

## Installation

### Requirements

- Python 3.7

### Steps

1. Clone the repo
2. Install the requirements

```bash
pip install -r requirements.txt
```
3. Run the script

```bash
python serial_plotter.py
```

## Usage

```bash
usage: serial_plotter.py [-h] [-p PORT] [-b BAUDRATE] [-t TIMEOUT] [-s SLEEP]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial port to read from
  -b BAUDRATE, --baudrate BAUDRATE
                        Baudrate of the serial port
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout of the serial port
  -s SLEEP, --sleep SLEEP
                        Sleep time between each read
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[Gavin Roberts](https://linkedin.com/in/empire-penguin)

## Acknowledgments

- [PySerial](https://pypi.org/project/pyserial/)
- [Matplotlib](https://pypi.org/project/matplotlib/)


## TODO

- [ ] Add tests
- [ ] Add more options to the CLI