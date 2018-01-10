# nikto_batch_scanner - beta
----------------------------------
script to scan batch of domains and IPs with nikto

This is script is written to be able to batch nikto scans so that you can run and leave them.  It is currently only written with basic scan parameters, but plan to fix that at a later date.  This was all that I needed at the time.  This will also become part of Lex-Talionis in the long run, but who knows how far along it will be by that time.

This script will accept a file of IP addresses, FQDNs, or a mix in a file together, but not CIDRs.  Please do not use CIDRs and not sure that I plan on supporting CIDRS, but create an issue if you think it should accept CIDRs and I will consider it.

How do I use it?
-----------------------------------

```python run_nikto.py -target_file nikto/niktonames.txt -proto https -port 443
```

Assumptions
------------------------------------

run_nikto.py assumes that it resides in the same path as the top level nikto directory and a directory called nikto_results which is where the results will be stored.

```ubuntu:> ls
nikto   nikto_results   run_nikto.py
```

To Do
--------------------------------------

- Make run_nikto.py more flexible by allowing changes in scan parameters

- other suggestions.  create an issue and i'll add it to the backlog to add/fix when i can get to it.

kthxbye.  ~zerstoeren
