from sys import argv, exit
from colorama import Fore, Back, Style



###
### UTILITIES
###
def hello   (message: str): print(Fore.MAGENTA + "[HELLO] "   + Style.RESET_ALL + message)
def info    (message: str): print(Fore.BLUE    + "[INFO] "    + Style.RESET_ALL + message)
def success (message: str): print(Fore.GREEN   + "[SUCCESS] " + Style.RESET_ALL + message)
def warning (message: str): print(Fore.YELLOW  + "[WARNING] " + Style.RESET_ALL + message)
def error   (message: str): print(Fore.RED     + "[ERROR] "   + Style.RESET_ALL + message); exit(1)

args = argv
args_len = len(argv)
# Arguments shall be executed in this order if provided
arg_struct = {
    "build": False,                # -b --build
    "test": False,                 # -t --test
    "deploy": False,               # -d --deploy
}

def parse_args():
    info("Parsing arguments...")
    for arg in args[1:]:
        if arg == "--build" or (arg.count('-') == 1 and "b" in arg): arg_struct["build"] = True; continue
        if arg == "--test" or (arg.count('-') == 1 and "t" in arg): arg_struct["test"] = True; continue
        if arg == "--deploy" or (arg.count('-') == 1 and "d" in arg): arg_struct["deploy"] = True; continue
        error("Unrecognized arg: " + arg)

###
### BUILD SCRIPT FUNCTIONS
###
def build():
    info("Nothing to build currently")

def test():
    warning("Tests not implemented!")

def deploy():
    warning("Deploy not implemented!")

def main():
    hello("Have a nice day!")
    parse_args()

    if arg_struct["build"] == True: build()
    if arg_struct["test"] == True: test()
    if arg_struct["deploy"] == True: deploy()

if __name__ == "__main__":
    main()
