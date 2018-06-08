#!/bin/bash
# Scans the top 20 ports (according to nmap).
# Best used first to get a general idea, then perform a wider sweep of an interesting machine.

nmap -sT --top-ports 20 10.11.1.1-254 -oG nmapSweepTopPorts.txt
