import json
from os import readlink
import sys
import argparse
from datetime import datetime
import logging
import urllib3
import re
import yaml

def yaml2json(file):
    with open(file,'r') as yaml_in:
        json_data = yaml.load(yaml_in,Loader=yaml.FullLoader)
        return json_data


def readfile(filename):
    f = open(filename,'r')
    data = json.load(f)
    f.close()
    return data


def diff_compare(file):
    pass



def display_banner():
    print(" _   ___                    _            _                  _               _ _           _            _    ")
    print("| |_( _ )___  _ __  ___  __| |  _ _  ___| |___ __ _____ _ _| |__  _ __  ___| (_)__ _  _  | |_ ___  ___| |___") 
    print("| / / _ (_-< | '_ \/ _ \/ _` | | ' \/ -_)  _\ V  V / _ \ '_| / / | '_ \/ _ \ | / _| || | |  _/ _ \/ _ \ (_-<")
    print("|_\_\___/__/ | .__/\___/\__,_| |_||_\___|\__|\_/\_/\___/_| |_\_\ | .__/\___/_|_\__|\_, |  \__\___/\___/_/__/")
    print("             |_|                                                 |_|               |__/                     ")
 


def parse_args():
    example_text = '''Examples:
    python k8spod.py -i test.yaml
    '''
    parser = argparse.ArgumentParser(epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', action ='store', dest='reqfile', help="Pod Network Policy Request file")
    results = parser.parse_args()
    
    if results.reqfile == None:
        parser.print_help()
        exit()

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
    print(yaml2json(args.reqfile))