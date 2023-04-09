#!/bin/bash

# This script runs the serial_plotter.py script with the specified options

# Set the default values for the options
port="/dev/ttyUSB0"
baudrate=9600
timeout=1
sleep_time=0.1

# Parse the command line options
while getopts ":p:b:t:s:" opt; do
  case ${opt} in
    p )
      port="$OPTARG"
      ;;
    b )
      baudrate="$OPTARG"
      ;;
    t )
      timeout="$OPTARG"
      ;;
    s )
      sleep_time="$OPTARG"
      ;;
    \? )
      echo "Invalid option: -$OPTARG" 1>&2
      exit 1
      ;;
    : )
      echo "Option -$OPTARG requires an argument." 1>&2
      exit 1
      ;;
  esac
done

# Run the script
python serial_plotter.py -p "$port" -b "$baudrate" -t "$timeout" -s "$sleep_time"
