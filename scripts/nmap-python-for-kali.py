#!/usr/bin/env python3
#Just in case you don't have Python installed on Kali use the commands below 
# sudo apt install python3-pip 
# pip install python-nmap 

import nmap 
#create regular expressions to ensure that the input is correctly formatted. 
import re 

# Regular Expression Pattern to recognize IPv4 addresses 
id_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern to extract the number of ports you want to scan
# You have to specify <lowest_port_number>--<highest_port_number> (ex 10-100) 
port_range_pattern = re.compile("([0-9]+)-([0-9]+)") 
# Initializing the port numbers, will be using the variables later on. 
port_min = 0 
port_max = 65535

open_prots = []
# Asks the user to input the Ip addresses they want to scan. 
while True:
  ip_add_entered = input("\nPlease enter the ip address that you want to scan: ") 
  if ip_add_pattern.search(ip_add_entered): 
    print(f"{ip_add_entered} is a valid ip address")
    break

while True: 
  # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning all the ports will take a very long time and is not advised 
  print("Please enter the range of ports you want to scan in format: <int>--<int> (ex would be 60-120)
  port_range = input("Enter port range: ") 
  port_range_valid = port_range_pattern.search(port_range.replace(" "," "))
  if port_range_valid: 
      port_min = int(port_range_valid.group(1))
      prot_max = int(port_range_valid.group(2))
      break 

nm = nmap.PortScanner()
# We're looping over all of the ports in the specified range.
for port in range(port_min, port_max + 1): 
    try:
        # The result is interesting to see. You might want to inspect the dictionary it returns. 
        # It contains what was sent to the command line in addition to the port status we're after. 
        # For in nmap for port 80 and ip 10.0.0.2 you'd run: nmap -oX - -p 89 -sV 10.0.0.2
        result = nm.scan(ip_add_entered, str(port))
        # Uncomment following line to look at dictionary 
        # print(result) 
        # We extract the port status from the returned object 
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
      except: 
          # We cannot scan some ports this ensures the program dosen't crash when we try to scan them 
          print(f"Cannot scan port {port}.")
