#!/bin/bash
# Sweeps for port 80 within range to identify Web servers.

nmap -p 80 10.11.1.1-254 -oG nmapSweepWeb.txt
