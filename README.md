# k8s pod network policy tools

This tools can scan your network policy of pod config . 

```
 _   ___                    _            _                  _               _ _           _            _    
| |_( _ )___  _ __  ___  __| |  _ _  ___| |___ __ _____ _ _| |__  _ __  ___| (_)__ _  _  | |_ ___  ___| |___
| / / _ (_-< | '_ \/ _ \/ _` | | ' \/ -_)  _\ V  V / _ \ '_| / / | '_ \/ _ \ | / _| || | |  _/ _ \/ _ \ (_-<
|_\_\___/__/ | .__/\___/\__,_| |_||_\___|\__|\_/\_/\___/_| |_\_\ | .__/\___/_|_\__|\_, |  \__\___/\___/_/__/
             |_|                                                 |_|               |__/                     
usage: k8spod.py [-h] [-i REQFILE] [-c TEMPNUM] [-l] [-o OUTFILE] [-f DEPLOY]

optional arguments:
  -h, --help  show this help message and exit
  -i REQFILE  Pod Network Policy Request file
  -c TEMPNUM  Choose The Template Num to compare yaml file
  -l, --list  Lists Network Policies
  -o OUTFILE  Export YAML Template File
  -f DEPLOY   Depoly YAML to k8s network policy.

Examples:
    python k8spod.py -i test.yaml       # compare defult template
    pythno k8spod.py -i test.yaml -c 1  # comapre test.yaml with your choose template of network policy
    python k8spod.py -c 1 -o output.yaml # choose template of network policy then output dest yaml
    python k8spod.py -f test.yaml # apply test.yaml to k8s pod network policy

```