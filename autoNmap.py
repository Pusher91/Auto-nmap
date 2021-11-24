#!/usr/bin/python3

import argparse
import subprocess
import re

parser = argparse.ArgumentParser(description='Automated nmap scanning utility')
parser.add_argument('Target', metavar='<ip address>', type=str, help='Target to scan')
args = parser.parse_args()
target = args.Target

def tcp_ping_scan():
    
    tcp_ping_scan_check = subprocess.call("test -e '{}'".format('tcp_ping_scan'), shell=True)

    if tcp_ping_scan_check != 0:

        print("******************************************************")
        print("Scanning for open tcp ports...")
        print("------------------------------------------------------")
        
        subprocess.run(["nmap", "-p-","{}".format(target), "-oN", "tcp_ping_scan"])

        print("\n")
        print("******************************************************")
        print("+ Finished scanning for open ports. 'tcp_ping_scan' created.")
        print("******************************************************")

    elif tcp_ping_scan_check == 0:
        
        print("\n")
        print("******************************************************")
        print("- Skipping tcp ping scan.  'tcp_ping_scan' already exists.")
        print("******************************************************")

def tcp_script_scan():

    tcp_script_scan_check = subprocess.call("test -e '{}'".format('tcp_script_scan'), shell=True)

    if tcp_script_scan_check != 0:
        
        print("\n")
        print("******************************************************")
        print("Running nmap scripts against open tcp ports...")
        print("------------------------------------------------------")

        textfile = open("tcp_ping_scan", "r")
        filetext = textfile.read()
        textfile.close()
        matches = re.findall("[0-9].*/tcp", filetext)
        matches2 = re.findall("\d{1,5}[0-9]", str(matches))
        open_tcp_ports = ",".join(matches2)
        
        subprocess.run(["nmap", "-p","{}".format(open_tcp_ports), "{}".format(target), "-sV", "-sC", "-oN", "tcp_script_scan"])
        
        print("\n")
        print("******************************************************")
        print("+ Finished tcp script scan. 'tcp_script_scan' created.")
        print("******************************************************")
    
    elif tcp_script_scan_check == 0:
       
        
        print("\n")
        print("******************************************************")
        print("- Skipping tcp script scan.  'tcp_script_scan' already exists.")
        print("******************************************************")

def udp_ping_scan():
    
    udp_ping_scan_check = subprocess.call("test -e '{}'".format('udp_ping_scan'), shell=True)
    
    if udp_ping_scan_check != 0:
        
        print("\n")
        print("******************************************************")
        print("Scanning for open udp ports...")
        print("------------------------------------------------------")
        
        subprocess.run(["nmap", "-sU", "-sV","{}".format(target), "-oN", "udp_ping_scan"])
        
        print("\n")
        print("******************************************************")
        print("+ Finished udp ping scan. 'udp_ping_scan' created.")
        print("******************************************************")
    
    elif udp_ping_scan_check == 0:

        print("\n")
        print("******************************************************")
        print("- Skipping udp ping scan.  'udp_ping_scan' already exists.")
        print("******************************************************")

def udp_script_scan():

    udp_script_scan_check = subprocess.call("test -e '{}'".format('udp_script_scan'), shell=True)
    
    if udp_script_scan_check != 0:
        
        print("\n")
        print("******************************************************")
        print("Running nmap scripts against open udp ports...")
        print("------------------------------------------------------")

        textfile = open("udp_ping_scan", "r")
        filetext = textfile.read()
        textfile.close()
        matches = re.findall("[0-9].*/udp", filetext)
        matches2 = re.findall("\d{1,5}[0-9]", str(matches))
        open_udp_ports = ",".join(matches2)

        subprocess.run(["nmap", "-p","{}".format(open_udp_ports), "{}".format(target), "-sU", "-sV", "-sC", "-oN", "udp_script_scan"])
        
        print("\n")
        print("******************************************************")
        print("+ Finished udp script scan. 'udp_script_scan' created.")
        print("******************************************************")
    
    elif udp_script_scan_check == 0:
        
        print("\n")
        print("******************************************************")
        print("- Skipping udp script scan.  'udp_script_scan' already exists.")
        print("******************************************************")

tcp_ping_scan()
tcp_script_scan()
udp_ping_scan()
udp_script_scan()
