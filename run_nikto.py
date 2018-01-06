#!/usr/bin/python

import os
import sys
import time
import argparse
import subprocess
import subprocess, signal

def https_nikto_job(target_file, proto, port):
    f = open(target_file)
    lines = f.readlines()
    for line in lines:

        line = line[:-1]
        sys.stdout.write("Now scanning " + line + " with " + proto + "\n\n")

        command = subprocess.Popen(["nikto/program/nikto.pl", "-host", proto + "://" + line + ":" + port, "-ssl", "timeout", "3", "-output", "nikto_results/" + line + "-" + port + ".csv"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        command_output = command.communicate()[0]

        log_file = open('nikto_results/' + line + "-" + port + '.log', 'a')
        log_file.write('\n')
        log_file.write(command_output)
        log_file.write('\n')
        log_file.close()

        sys.stdout.write("Nikto scan complete for " + line + " with " + proto + "\n\n")

        time.sleep(2)

def http_nikto_job(target_file, proto, port):
    f = open(target_file)
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        sys.stdout.write("Now scanning " + line + " with " + proto + "\n\n")

        command = subprocess.Popen(["nikto/program/nikto.pl", "-host", proto + "://" + line + ":" + port, "timeout", "3", "-output", "nikto_results/" + line + "-" + port + ".csv"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        command_output = command.communicate()[0]

        log_file = open('nikto_results/' + line + '-' + port + '.log', 'a')
        log_file.write('\n')
        log_file.write(command_output)
        log_file.write('\n')
        log_file.close()

        sys.stdout.write("Nikto scan complete for " + line + " with " + proto + "\n\n")

        time.sleep(2)


#        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
#        out, err = p.communicate()

#        for process in out.splitlines():
#                if 'nikto' in process:
#                        pid = int(process.split(None, 1)[0])
#                        os.kill(pid, signal.SIGKILL)

if __name__ == "__main__":
    niktoscan = argparse.ArgumentParser(description="Nikto Batch Scanner")
    niktoscan.add_argument("-proto", type=str, required=True, help= "http or https")
    niktoscan.add_argument("-port", type=str, required=True, help="port number to scan")
    niktoscan.add_argument("-target_file", type=str, required=True, help="File List of IPs and/or Domain names")
    niktobatch = niktoscan.parse_args()

    if niktobatch.proto == "https":
        sys.stdout.write("Please be patient.  This may take some time. \n\n")
        https_nikto_job(niktobatch.target_file, niktobatch.proto, niktobatch.port)

    elif niktobatch.proto == "http":
        sys.stdout.write("Please be patient.  This may take some time. \n\n")
        http_nikto_job(niktobatch.target_file, niktobatch.proto, niktobatch.port)   

    else:
        sys.stdout.write("Something is wrong. run_nikto.py -h for usage..\n")
        exit
