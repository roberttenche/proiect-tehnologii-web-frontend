from os import path, getcwd, system as system_run


from sys import argv, platform as system_type, exit
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
    'cleanup': False,              # -c --cleanup
    'run_local': False,            # -r --run_local # FOR LOCAL USE ONLY
}

def parse_args():
    info('Parsing arguments...\n')
    for arg in args[1:]:
        if arg.count('-') == 1:
            if 'h' in arg: arg_struct['help'] = True
            if 'b' in arg: arg_struct['build'] = True
            if 't' in arg: arg_struct['test'] = True
            if 'd' in arg: arg_struct['deploy'] = True
            if 'c' in arg: arg_struct['cleanup'] = True
            if 'r' in arg: arg_struct['run_local'] = True
        elif arg.count('-') == 2:
            if arg == '--help': arg_struct['help'] = True; continue
            if arg == '--build': arg_struct['build'] = True; continue
            if arg == '--test': arg_struct['test'] = True; continue
            if arg == '--deploy': arg_struct['deploy'] = True; continue
            if arg == '--cleanup': arg_struct['cleanup'] = True; continue
            if arg == '--run_local': arg_struct['run_local'] = True; continue
        else:
            error('Unrecognized arg: ' + arg)

    true_cout = 0
    for arg in arg_struct:
        if arg_struct[arg]: true_cout+=1; break
    if true_cout == 0:
        error("Something went wrong with argument parsing.")

###
### BUILD SCRIPT FUNCTIONS
###
def arg_help():
    hello('Welcome to the help page')
    print('''Available arguments:
    --help      -h    == Brings up this page
    --build     -b    == Starts the build
    --test      -t    == Runs tests
    --deploy    -d    == Starts deployment to server  (Linux only)
    --cleanup   -c    == Clean build generated f iles (Linux only)
    --run_local -r == Starts local development server
    \n''')
    exit(0)

def build():
    info('Starting build...\n')
    system_run("ng build")
    success('Build sucessfully finished!\n')

def test():
    info('Tests not implemented!\n')

def deploy():
    info('Starting deployment...\n')

    if not (system_type == "linux" or system_type == "linux2"): error("Deploy is an Linux only feature")

    if not path.exists("dist/"): error("Build project first!")

    system_run("sudo rm -r /var/www/html/assets")
    system_run("sudo rm /var/www/html/*")

    system_run("cp -a dist/proiect-tehnologii-web-frontend/* /var/www/html")

    success("Sucessfuly deployed!\n")

def run_local():
    system_run("ng serve --open")

def cleanup():
    if not (system_type == "linux" or system_type == "linux2"): error("Cleanup is an Linux only feature")
    system_run("sudo rm -r ~/mynvm")


###
### MAIN ENTRY POINT
###
def main():
    hello('Have a nice day!\n')

    parse_args()

    if args_len == 1: error("No arguments provided. Use --help for more information.")

    if arg_struct['help']       == True: arg_help()

    if arg_struct['build']      == True: build()
    if arg_struct['test']       == True: test()
    if arg_struct['deploy']     == True: deploy()
    if arg_struct['cleanup']    == True: cleanup()
    if arg_struct['run_local']  == True: run_local()

if __name__ == '__main__':
    main()
