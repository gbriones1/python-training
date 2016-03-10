#!/usr/bin/python3

import sys
import time
import subprocess
import threading
import logging

LOG = logging.getLogger(__name__)

_ch = logging.StreamHandler()
_ch.setLevel(logging.DEBUG)
_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_ch.setFormatter(_formatter)
LOG.addHandler(_ch)
LOG.setLevel(logging.DEBUG)

class WatchableProcess(threading.Thread):
    def __init__(self, cmd):
        self.poll = lambda *x: None
        self.cmd = cmd
        self.process = None
        self.output = []
        self.done = False
        threading.Thread.__init__(self)

    def run(self):
        self.process = subprocess.Popen(self.cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             bufsize=1)
        self.poll = self.process.poll
        lines = self.process.stdout
        # LOG.debug("Reading output")
        for line in lines:
            # LOG.debug("Output: {0}".format(line.decode()))
            self.output.append(line.decode())
        # LOG.debug("Done reading output")
        self.done = True

def main():
    outputlog = 'lorem.log'
    open(outputlog, 'w').close()
    cmd = ['./lorem.py', '&> {0}'.format(outputlog)]
    cmd = ['./lorem.py']
    # cmd = ['swupd', 'verify', '--fix']
    LOG.info("Executing command " + ' '.join(cmd))
    watch_list = [
        {"name":"Started", "find":"Line: 3/703 Word: Lorem"},
        {"name":"Second startover", "find":"Line: 1/703"},
        {"name":"Third startover", "find":"Line: 1/703"},
        {"name":"Fourth startover", "find":"Line: 1/703"},
        {"name":"Fifth startover", "find":"Line: 1/703"},
        {"name":"End", "find":"Line: 703/703"},
    ]
    # watch_list = [
    #     {"name":"Swupd started", "find":"swupd-client software verify"},
    #     {"name":"Swupd finished", "find":"Fix successful"}
    # ]
    watch = WatchableProcess(cmd)
    watch.start()
    current = 0
    new_current = 0
    index = 0
    while not watch.done:
        # LOG.debug("Process not finished yet")
        if len(watch.output) > current:
            LOG.debug("Process has {0} lines of output".format(len(watch.output)))
            new_current = len(watch.output)
            if index < len(watch_list):
                buff = watch.output[current:new_current]
                found = False
                for line in buff:
                    if not found and watch_list[index]["find"] in line:
                        LOG.info(watch_list[index]["name"])
                        index += 1
                        found = True
                    with open(outputlog, 'a') as f:
                        f.write(line)
            current = new_current


if __name__ == "__main__":
    main()
