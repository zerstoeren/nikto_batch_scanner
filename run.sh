#!/bin/bash

./run_nikto.py -proto https -port 443 -target_file 443_sites.txt -project_name 443_site -results_path /home/443sites/
./run_nikto.py -proto http -port 80 -target_file 80_sites.txt -project_name 80_sites -results_path /home/80sites/
./run_nikto.py -proto http -port 8080 -target_file 8080_sites.txt -project_name 8080_sites #will write results in nikto_results/
