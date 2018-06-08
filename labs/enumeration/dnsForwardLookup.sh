#!/bin/bash
# Performs a DNS lokup using a list of commonly used names.

for name in $(cat dnsForwardLookupList.txt);do
  host $name.megacorpone.com | grep "has address" | cut -d " " -f1,4
done
