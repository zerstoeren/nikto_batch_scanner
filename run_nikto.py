#!/usr/bin/python

import os
import sys
import time
import argparse
import threading
import subprocess
import subprocess, signal

def write_log(command_output):

    sys.stdout.write("Logging results to " + proj_name + " for " + proto + "\n\n")

    log_file = open('nikto_results/' + proj_name + "-" + port + '.log', 'a')
    log_file.write('\n')
    log_file.write(command_output)
    log_file.write('\n')
    log_file.close()

    sys.stdout.write("Log results written to " + proj_name + ".\n\n")

    time.sleep(1)

def https_nikto_job(line):
    
    command = subprocess.Popen(["nikto/program/nikto.pl", "-host", proto + "://" + line + ":" + port, "-ssl", "timeout", "3", "-output", "nikto_results/" + line + "-" + port + ".csv"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    command_output = command.communicate()[0]

    write_log(command_output)

def http_nikto_job(line):

    command = subprocess.Popen(["nikto/program/nikto.pl", "-host", proto + "://" + line + ":" + port, "timeout", "3", "-output", "nikto_results/" + line + "-" + port + ".csv"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    command_output = command.communicate()[0]

    write_log(command_output)

if __name__ == "__main__":
    niktoscan = argparse.ArgumentParser(description="Nikto Batch Scanner")
    niktoscan.add_argument("-proto", type=str, required=True, help="http or https")
    niktoscan.add_argument("-port", type=str, required=True, help="port number to scan")
    niktoscan.add_argument("-target_file", type=str, required=True, help="file list of IPs and/or Domains to scan")
    niktoscan.add_argument("-project_name", type=str, required=True, help="Project name for nikto log file")
    niktoscan.add_argument("-packet_rate", type=int, required=False, default=1, help="parallelizing nikto processes")

    niktobatch = niktoscan.parse_args()

    proto = niktobatch.proto
    port = niktobatch.port
    target_file = niktobatch.target_file
    proj_name = niktobatch.project_name
    packet_rate = niktobatch.packet_rate

    sys.stdout.write("Please be patient... This may take some time. \n\n")

    f = open(target_file)
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")

        if proto == "https":
            sys.stdout.write("Now scanning " + line + " with " + proto + "\n\n")

            threads = [packet_rate]
            niktothread = threading.Thread(target=https_nikto_job, args=(line,))
            threads.append(niktothread)
            niktothread.start()

        elif proto == "http":
            sys.stdout.write("Now scanning " + line + " with " + proto + "\n\n")

            threads = [packet_rate]
            niktothread = threading.Thread(target=http_nikto_job, args=(line,))
            threads.append(niktothread)
            niktothread.start()

        else:
            sys.stdout.write("Something went wrong.  Please try run_nikto.py -h for help.\n\n")
            exit       

