#!/usr/bin/python3
import subprocess
import telnetlib
import argparse
from getpass import getpass


def title(text):
    print('')
    print("---- " + text + " ----")
    print('')


def icmp_check(ip):
    ping = ['ping', ip, '-c', '1']
    print("\nICMP/level 3 testing...", end=' ')
    p = subprocess.Popen(ping, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    if p.wait() == 0:
        return "-->" + '\33[92m' + " OK" + '\033[0m' + "\n"
    else:
        print("-->" + '\33[91m' + " FAILED" + '\033[0m' + "\n")
        return p.stdout.read()


def port22_check(ip):
    port = 22
    try:
        print("\nPORT 22 testing...", end=' ')
        if telnetlib.Telnet(ip, port):
            return "-->" + '\33[92m' + " OK" + '\033[0m'
    except (ConnectionRefusedError, OSError) as e:
        print("-->" + '\33[91m' + " FAILED" + '\033[0m' + "\n")
        return e


def ssh_check_password(ip, password):
    global val  # boolean variable for ssh connection
    l1 = ['sshpass', '-p', password, 'ssh', '-o', 'StrictHostKeyChecking=no', ip, 'exit']
    print("\nSSH password connection test...", end=' ')
    p1 = subprocess.Popen(l1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    if p1.wait() == 0:
        print("-->" + '\33[92m' + " OK" + '\033[0m')
        val = True
    else:
        print("-->" + '\33[91m' + " FAILED" + '\033[0m' + "\n")
        print(p1.stdout.read())
        val = False


def ssh_check_key(ip, key):
    global val
    l2 = ['ssh', '-i', key, '-o', 'StrictHostKeyChecking=no', ip, 'exit']
    print("\nSSH key connection test...", end=' ')
    p2 = subprocess.Popen(l2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    if p2.wait() == 0:
        print("-->" + '\33[92m' + " OK" + '\033[0m')
        val = True
    else:
        print("-->" + '\33[91m' + " FAILED" + '\033[0m' + "\n")
        print(p2.stdout.read())
        val = False


# function will perform connections whether password or key option is chosen
def ssh_extract(ip):
    print("\n\n###Extracting data...###\n")
    if args.password:
        ssh_list = ['sshpass', '-p', pass_input, 'ssh', '-o', 'StrictHostKeyChecking=no', ip, 'hostname;', 'echo "";',
                    'df -h;', 'echo "";', 'free -h;', 'echo "";', 'cat /etc/*release;', 'echo "";', 'ip a;', 'echo "";',
                    'uptime;', 'echo "";', 'ss -tuln', '|', ' grep LISTEN']
    else:
        ssh_list = ['ssh', '-i', args.key, '-o', 'StrictHostKeyChecking=no', ip, 'hostname;', 'echo "";', 'df -h;',
                    'echo "";', 'free -h;', 'echo "";', 'cat /etc/*release;', 'echo "";', 'ip a;', 'echo "";',
                    'uptime;', 'echo "";', 'ss -tuln', '|', ' grep LISTEN']

    p3 = subprocess.Popen(ssh_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output_list = p3.stdout.read().split('\n\n')
    header_list = ["HOSTNAME", "DISK SPACE", "MEMORY", "DISTRIBUTION DETAILS", "INTERFACES", "UPTIME", "OPEN PORTS"]

    for header, output in zip(header_list, output_list):
        title(header)
        print(output)


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-p', '--password', action='store_true', help="use ssh with password")
group.add_argument('-k', '--key', help="use ssh with private key")
parser.add_argument('-l', '--limit', help="use only one specific host")
args = parser.parse_args()

with open('hosts.txt') as f:
    host_list = f.read().splitlines()
if args.password:
    pass_input = getpass()
print("")

if args.limit:
    host_list = ["[hosts]", args.limit]
for host in host_list[1:]:
    print('\33[93m' + "==== " + " HOST - " + host + " ====" + '\033[0m')
    print(icmp_check(host), end=' ')
    print(port22_check(host))
    if args.password:
        ssh_check_password(host, pass_input)
    else:
        ssh_check_key(host, args.key)
    if val: # if ssh connection was ok
        ssh_extract(host)
