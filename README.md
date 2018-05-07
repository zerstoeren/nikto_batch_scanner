# nikto_batch_scanner - beta
----------------------------------
script to scan batch of domains and IPs with nikto

This is script is written to be able to batch nikto scans so that you can run and leave them.  It is currently only written with basic scan parameters, but plan to fix that at a later date.  This was all that I needed at the time.  This will also become part of Lex-Talionis in the long run, but who knows how far along it will be by that time.

This script will accept a file of IP addresses, FQDNs, or a mix in a file together, but not CIDRs.  Please do not use CIDRs and not sure that I plan on supporting CIDRS, but create an issue if you think it should accept CIDRs and I will consider it.

Also, nikto_batch_scanner now has assumptions for project names so that multiple batches can be run on the same server at once.  All projects will have verbose nikto results stored to a centralized project file inside the nikto_results folder for all scans that were run along with a csv file for each individual target.  Multithreading has also been included now.

How do I use it?
-----------------------------------

```
python run_nikto.py -target_file path/filename -proto https -port 443 -project_name test
```

Assumptions
------------------------------------

run_nikto.py assumes that it resides in the same path as the top level nikto directory.  run_nikto.py now allows flexible path storage of results with the "-results_path" flag, but if a path is not set it will default to "nikto_results" as is did before.  This is to better support multiple projects running at one time.  You will need to ensure that the desired file paths exist.

```
os:> ls
nikto   nikto_results   run_nikto.py
```

To Do
--------------------------------------

- Make run_nikto.py more flexible by allowing changes in scan parameters

- other suggestions.  create an issue and i'll add it to the backlog to add/fix when i can get to it.

kthxbye.  ~zerstoeren
