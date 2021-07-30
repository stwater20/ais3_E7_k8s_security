import json
from os import readlink
import sys
import argparse
from datetime import datetime
import logging
import urllib3
import re
import yaml
import os
import shutil
def yaml2json(file):
    with open(file,'r') as yaml_in:
        json_data = yaml.load(yaml_in,Loader=yaml.FullLoader)
        return json_data


def readfile(filename):
    f = open(filename,'r')
    data = json.load(f)
    f.close()

    return data

def getRemark(num):
    data = readfile("remark.json")
    return data[num-1]["dec"]


def getFile(num):
    num_s=str(num)
    while(len(num_s)<2):
        num_s = "0"+str(num)
    tempfile = "./Manifest/"+num_s+".yaml"
    print(getRemark(num))
    return yaml2json(tempfile)

def diff_compare(num):
    num_s=str(num)
    while(len(num_s)<2):
        num_s = "0"+str(num)
    temp = "pytest -rP ./test/test_pod_"+num_s+".py"
    os.system("pytest -rP ./test/test_pod_00.py")
    os.system(temp)
    pass

def handle(args):
    if args.list:
        print()
        print("01. DENY all traffic to an application")
        print("02. LIMIT traffic to an application")
        print("03. DENY all non-whitelisted traffic to a namespace (Zero Trust Policy)")
    elif args.reqfile and args.tempNum:
        shutil.copyfile(args.reqfile,"./test/test.yaml") #複製檔案到test裏面給pytest
        num_s = args.tempNum
        while(len(num_s)<2):
            num_s = "0"+str(num_s)
        diff_compare(num_s)
    elif args.reqfile:
        print("")
        print("")
        print("Choose the template you want to compare... ")
        print("-------------------")
        print("01. DENY all traffic to an application")
        print("02. LIMIT traffic to an application")
        print("03. DENY all non-whitelisted traffic to a namespace (Zero Trust Policy)")
        # print("04. DENY all traffic from other namespaces")
        # print("05. ALLOW traffic to an application from all namespaces")
        # print("06. ALLOW all traffic from a namespace")
        # print("07. ALLOW traffic from some pods in another namespace")
        # print("08. ALLOW traffic from external clients")
        # print("09. ALLOW traffic only to a port of an application")
        # print("10. ALLOW traffic from apps using multiple selectors")
        # print("11. DENY egress traffic from an application")
        # print("12. DENY all non-whitelisted traffic from a namespace")
        print()
        x = int(input("Choose Number : "))
        print()
        shutil.copyfile(args.reqfile,"./test/test.yaml") #複製檔案到test裏面給pytest
        diff_compare((x))
    if args.tempNum and args.outfile:
        num_s = args.tempNum
        while(len(num_s)<2):
            num_s = "0"+str(num_s)
        temp = "./Manifest/"+num_s+".yaml"
        shutil.copyfile(temp,args.outfile)
        print("=======================================")
        print("File Export Success!")
            



def display_banner():
    print(" _   ___                    _            _                  _               _ _           _            _    ")
    print("| |_( _ )___  _ __  ___  __| |  _ _  ___| |___ __ _____ _ _| |__  _ __  ___| (_)__ _  _  | |_ ___  ___| |___") 
    print("| / / _ (_-< | '_ \/ _ \/ _` | | ' \/ -_)  _\ V  V / _ \ '_| / / | '_ \/ _ \ | / _| || | |  _/ _ \/ _ \ (_-<")
    print("|_\_\___/__/ | .__/\___/\__,_| |_||_\___|\__|\_/\_/\___/_| |_\_\ | .__/\___/_|_\__|\_, |  \__\___/\___/_/__/")
    print("             |_|                                                 |_|               |__/                     ")
 


def parse_args():
    example_text = '''Examples:
    python k8spod.py -i test.yaml       # compare defult template
    pythno k8spod.py -i test.yaml -c 1  # comapre test.yaml with your choose template of network policy
    python k8spod.py -c 1 -o output.yaml # choose template of network policy then output dest yaml
    '''
    parser = argparse.ArgumentParser(epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', action ='store', dest='reqfile', help="Pod Network Policy Request file")
    parser.add_argument('-c', action ='store', dest='tempNum', help="Choose The Template Num to compare yaml file")
    parser.add_argument('-l', '--list', action='store_true', help='Lists Network Policies')
    parser.add_argument('-o', action ='store', dest='outfile', help="Export YAML Template File")
    results = parser.parse_args()
    parser.print_help()
    # if results.reqfile == None:
    #     parser.print_help()
    #     exit()

    return results





if __name__ == "__main__":
    # disable ssl warning for self signed certificate
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # enable custom logging
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s]:%(message)s')
    logging.addLevelName( logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
    display_banner()
    args = parse_args()
    # readfile(args.reqfile)
    handle(args)
    # print(yaml2json(args.reqfile))