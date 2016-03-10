#!/usr/bin/python
import struct
import datetime
import sys

infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

#long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)
    print("%s.%d: Event type %u, code %u, value: %u" % \
        (datetime.datetime.fromtimestamp(int(tv_sec)).strftime('%Y-%m-%d %H:%M:%S'), tv_usec, type, code, value))
    event = in_file.read(EVENT_SIZE)

in_file.close()
