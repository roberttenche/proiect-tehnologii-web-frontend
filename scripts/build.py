import subprocess

from sys import argv, exit
from colorama import Fore, Back, Style


###
### UTILITIES
###
def hello   (message: str): print(Fore.MAGENTA + '[HELLO] '   + Style.RESET_ALL + message)
def info    (message: str): print(Fore.BLUE    + '[INFO] '    + Style.RESET_ALL + message)
def success (message: str): print(Fore.GREEN   + '[SUCCESS] ' + Style.RESET_ALL + message)
def warning (message: str): print(Fore.YELLOW  + '[WARNING] ' + Style.RESET_ALL + message); exit(1)
def error   (message: str): print(Fore.RED     + '[ERROR] '   + Style.RESET_ALL + message); exit(2)

args = argv
args_len = len(argv)
# Arguments shall be executed in this order if provided
arg_struct = {
    'help': False,                 # -h --help
    'build': False,                # -b --build
    'test': False,                 # -t --test
    'deploy': False,               # -d --deploy
    'run_local': False,            # -r --run_local # FOR LOCAL USE ONLY
}

def parse_args():
    info('Parsing arguments...\n')
    for arg in args[1:]:
        if arg == '--help' or (arg.count('-') == 1 and 'h' in arg): arg_struct['help'] = True; continue
        if arg == '--build' or (arg.count('-') == 1 and 'b' in arg): arg_struct['build'] = True; continue
        if arg == '--test' or (arg.count('-') == 1 and 't' in arg): arg_struct['test'] = True; continue
        if arg == '--deploy' or (arg.count('-') == 1 and 'd' in arg): arg_struct['deploy'] = True; continue
        if arg == '--run_local' or (arg.count('-') == 1 and 'r' in arg): arg_struct['run_local'] = True; continue
        error('Unrecognized arg: ' + arg)

###
### BUILD SCRIPT FUNCTIONS
###
def arg_help():
    hello('Welcome to the help page')
    print('''Available arguments:
    --help   -h == Brings up this page
    --build  -b == Starts the build
    --test   -t == Runs tests
    --deploy -d == Starts deployment to server\n''')
    exit(0)

def build():
    info('Nothing to build currently\n')

def test():
    info('Tests not implemented!\n')

def kill_last_deploy():
    info('Killing last deployment process\n')

    try:
        out = str(subprocess.check_output([
            "screen", "-list"
        ]))
    except:
        info("No previous deployment found\n")
        return

    pid = out.replace("\\t","") \
        .split("\\n")[1] \
        .split(".")[0]

    subprocess.run(["screen", "kill", pid])

    info("Killed last deployment process\n")

def deploy():
    info('Starting deployment...\n')
    kill_last_deploy()

    subprocess.run(["sleep", "5"])

    subprocess.call([
        "screen",
        "-S", "frontend", # session name
        "-t", "Frontend", # screen 
        "-d", "-m",       # run in detached mode
        "npx", "parcel", "build", "-p", "5000", "src/index.html"
    ])
    success("Sucessfully deployed to server!")

def run_local():
    subprocess.run(["npx", "parcel", "src/index.html"], shell=True)

def main():
    hello('Have a nice day!\n')

    parse_args()

    if arg_struct['help'] == True: arg_help()
    if arg_struct['build'] == True: build()
    elif arg_struct['test'] == True: test()
    elif arg_struct['deploy'] == True: deploy()
    elif arg_struct['run_local'] == True: run_local()
    else: error("No arguments provided. Use --help for more information.")
if __name__ == '__main__':
    main()
