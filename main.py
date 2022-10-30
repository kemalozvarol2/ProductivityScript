import os
import shutil
import subprocess
from datetime import datetime
from time import sleep

#   WARNING:
#   THIS SCRIPT DELETES YOUR CURRENT HOSTS FILE.
#   DON'T USE IT IF YOU WANT TO BLOCK OTHER SITES
#   OUTSIDE OF THE TIME LIMIT YOU'LL SELECT HERE.

path_to_hosts = "C:\Windows\System32\drivers\etc\hosts"


path_to_edited_hosts_file = "./hosts2"  # CHANGE THIS TO YOUR EDITED HOSTS FILE
block_until = 20  # CHANGE THIS TO THE HOUR YOU WANT TO BLOCK SITES UNTIL

def allow_sites():
    os.remove(path_to_hosts)
    subprocess.Popen('ipconfig -flushdns', shell=False)
    subprocess.Popen('ipconfig -release', shell=False)
    subprocess.Popen('ipconfig -renew', shell=False)
def block_sites():
    shutil.copyfile(path_to_edited_hosts_file, path_to_hosts)
    subprocess.Popen('ipconfig -flushdns', shell=False)
    subprocess.Popen('ipconfig -release', shell=False)
    subprocess.Popen('ipconfig -renew', shell=False)


# MAIN CODE WITH EXPLANATIONS,
# YOU CAN EDIT IF YOU KNOW WHAT YOU'RE DOING.

while True:
    current_hour = int(datetime.now().strftime("%H"))  # GET CURRENT HOUR AS HH
    if current_hour < block_until:  # CHECK IF IT'S BEFORE SELECTED HOUR
        if not os.path.exists(path_to_hosts):  # IF SITES ARE NOT BLOCKED
            block_sites()  # BLOCK THE SITES
    else:  # IF IT'S AFTER SELECTED HOUR
        if os.path.exists(path_to_hosts):  # IF SITES ARE BLOCKED
            allow_sites()  # ALLOW THE SITES
    sleep(5)
