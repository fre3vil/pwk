#!/bin/bash
# Performs a ping sweep of range.

nmap -sn 10.11.1.1-254 -oG nmapSweepPing.txt

# Use line below to grep for easy-to-read output of results.
# grep "Up" nmapSweepPing.txt | cut -d " " -f2
