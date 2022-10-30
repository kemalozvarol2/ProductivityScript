# ProductivityScript     &nbsp;&nbsp; `README.md`
ProductivityScript is a script I wrote, to keep myself from being distracted during the day and focus on working on my project.

## How it works?

Running **`main.py`** starts an infinite loop that runs every 5 seconds until you kill the script or shut down your computer. In every run, It checks the current time and if it is between the time constraints you set, the script will replace your default hosts file with hosts2 file that's in the same directory as the script. Therefore blocking the websites you'll choose within the time period of your choosing.

### Files : 
**hosts** : The script will delete your hosts file to re-allow your blocked sites. So if you would want the original `hosts` file back for some reason, I included the original hosts file that comes with a fresh Windows installation.
**hosts2** : This is the hosts file you are supposed to edit if you want to add or remove a blocked website. If you don't, by default this file blocks : **Facebook**, **YouTube** and **Instagram**. 
**`main.py`** : Where the magic happens.

# How to use ProductivityScript?

## 1. Open & Edit `main.py` on a Python IDE or any notepad app.

And edit `block_from` and `block_until` variables in the script according to your schedule. By default it is set to 00:00 AM to 20:00 PM.

## 2. Open & Edit `hosts2` file.

In `hosts2`, you will see how each website has been blocked. There's 4 lines to block various subdomains for a single website. You can edit or remove sites from this file however you like. Just duplicate one of the 4-line-blocks, and replace website URL with the URL of the website you want to block.
**<sub>Do NOT edit the website prefix, if you want to block website.net, just replace youtube.com part with website.net and leave the rest as is.</sub>**


## 3. Use pyInstaller to convert the script into an executable file

After you made your selections, run CMD in the directory of the script and run this command.

    pip install pyinstaller
    pyinstaller .\main.py --onefile --noconsole

Wait until the process is complete and then move your **`hosts2`** file, to newly created **`/dist`** directory. Then navigate to `dist` folder, copy **`main.exe`** AND **`hosts2`** files.

<sub>Warning : You can't change blocking time after this step. If you want to change it after creating the exe file, you'll need to return back to step 1.</sub>

<sub>Tip : You can rename the exe file to something you can remember by, like `ProductivityScript.exe`, while the script is running, it will show up on your task manager by that name.</sub>


## 4. Go to your startup folder and paste the `.exe` and `hosts2` files

Startup folder location is;

On Windows 11 : 

    C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
    
On Windows 7 :

    C:\Users\[user name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

<sub>**( Remember to change the [user name] to the username on your PC )**</sub>

After doing that, you can delete the main folder that `main.py` file was in.

## 5. Run the script as administrator
Because this script edits a file that's inside System32 folder, it needs to be run as an Administrator. To allow the script to run as administrator;
* Right click to the exe file and click properties
* Navigate to **Compatibility** tab and check the box next to **Run this Program as Administrator**.
* Click **OK**.


## You're all set!

To run the script, you can now double click the exe file, or restart your computer. (You may see a terminal screen, don't close that, it will disappear in a few seconds.)

Next time you turn your PC on, ProductivityScript will run at the startup and block the selected websites within selected time period.

**Make something awesome with your now social-media-free time!**
