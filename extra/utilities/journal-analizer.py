#!/usr/bin/python

import subprocess
import argparse
import datetime
import math
import pdb

def local_cmd(cmd):
    print "executing Command:", cmd.split()
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out, err, p.returncode


def main():
    parser = argparse.ArgumentParser(prog='./journal-analizer.py',
                                     usage='%(prog)s [options]')
    parser.add_argument('-u', '--unit', nargs='*',
                        help="Show messages for the specified systemd unit")
    args = parser.parse_args()

    unit_cmd = "-u {0}".format(args.unit[0]) if args.unit else ""
    cmd = "journalctl {0} -o short-precise -b".format(unit_cmd)
    out, err, retcode = local_cmd(cmd)
    if not retcode:
        logs = []
        max_duration = 0
        min_duration = 0
        toggle_min = True
        total_duration = 0
        entries = 0
        average = 0
        root_mean = 0
        root_mean2 = 0
        durations = []
        lines = out.split("\n")
        for line_no in range(len(lines)):
            line = lines[line_no]
            # print line
            if line and not line.startswith("-") and len(line) > 25:
                entries += 1
                curr_time = datetime.datetime.strptime(line[:22], "%b %d %H:%M:%S.%f")
                hostname = line[23:].split()[0]
                service_full = line[23:].split()[1][:-1]
                service = service_full
                pid = None
                if "[" in service:
                    pid = service.split("[")[1][:-1]
                    service = service_full.split("[")[0]
                text = line[23:].split(service_full)[1][2:]
                logs.append({"real_line_no":line_no, "timestamp":curr_time, "text":text, "service":service, "hostname":hostname, "pid":pid})
        if entries:
            logs.sort(key=lambda x: x["timestamp"])
            for log_index in range(len(logs)):
                log = logs[log_index]
                timestamp_duration = None
                if log_index+1 != len(logs):
                    timestamp_duration = (logs[log_index+1]["timestamp"] - log["timestamp"])
                duration = 0
                if timestamp_duration:
                    duration = timestamp_duration.microseconds + timestamp_duration.seconds*1000*1000
                total_duration += duration
                if duration > max_duration:
                    max_duration = duration
                if duration < min_duration or toggle_min:
                    min_duration = duration
                    toggle_min = False
                durations.append(duration)
                log["duration"] = duration
            average = total_duration/entries
            root_mean = int(math.sqrt(sum(map(lambda x: math.pow(x,2), durations))/entries))
            higher_durations = filter(lambda y: y > root_mean, durations)
            root_mean2 = int(math.sqrt(sum(map(lambda x: math.pow(x,2), higher_durations))/len(higher_durations)))
            for log in logs:
                note_chars = "   "
                if log["duration"] == max_duration:
                    note_chars = "***"
                elif log["duration"] > root_mean2:
                    note_chars = " **"
                elif log["duration"] > root_mean:
                    note_chars="  *"
                print note_chars, "{:010d}".format(log["duration"]), log["timestamp"], log["text"]
            print "Total duration", total_duration
            print "Entries found", entries


if __name__ == "__main__":
    main()
