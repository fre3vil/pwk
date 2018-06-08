#!/bin/bash
# Performs a reverse DNS lookup on the whole range of the target, 10.11.1.1-10.11.1.254.

for ip in $(seq 1 254); do
  host 10.11.1.$ip | grep "megacorp" | cut -d " " -f1,5
done
