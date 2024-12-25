import os
from distutils.command.clean import clean

import modrinth_downloader.api
import requests
import pprint
import modrinth_downloader
import platform

from tqdm import tqdm

files_to_delete = ['oceanclient.jar', 'fabricAPI.jar']
url = "https://github.com/AxiomLab/OceanClient/releases/download/v1.1D/oceanclient-1.1-SNAPSHOT.jar"

def getting_ready():
    os = platform.system()
    startmenu(os=os)

def uninstall():
    print("Select the location to uninstall OceanClient(mods folder)")
    choice = input("Put it here(full path): ")
    os.remove(choice + 'oceanclient.jar')
    choice2 = input("Do you want to close this app(y/n): ")
    if choice2 == "y" or "yes".lower():
        exit()
    else:
        pass

def uninstall_with_deps():
    print("Select the location to uninstall OceanClient with Dependencies(mods folder)")
    choice = input("Put it here(full path): ")
    for file in files_to_delete:
        os.remove(file)
    choice2 = input("Do you want to close this app(y/n): ")
    if choice2 == "y" or "yes".lower():
        exit()
    else:
        pass

def update():
    print("!!!WARNING!!!")
    print("This client supports 1.21.4 FABRICMC only")
    print("Select the location to update OceanClient(mods folder)")
    choice = input("Put it here(full path): ")

    print("Downloading Fabric API...")
    modrinth_downloader.api.download_project_file(project_id="P7dR8mSH", game_version="1.21.4", loader="fabric",
                                                  download_path=choice, output_file="fabricAPI.jar")
    print('Fabric API downloaded')
    print("Downloading OceanClient...")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024
    with open(choice + 'oceanclient.jar', "wb") as f:
        with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
            for chunk in response.iter_content(block_size):
                f.write(chunk)
                pbar.update(len(chunk))
    print('OceanClient downloaded')
    choice2 = input("Do you want to close this app(y/n): ")
    if choice2 == "y" or "yes".lower():
        exit()
    else:
        pass


def InstallOceanClient():
    print("!!!WARNING!!!")
    print("This client supports 1.21.4 FABRICMC only")
    print("Select the location to install OceanClient(mods folder)")
    choice = input("Put it here(full path): ")

    print("Downloading Fabric API...")
    modrinth_downloader.api.download_project_file(project_id="P7dR8mSH", game_version="1.21.4", loader="fabric",
                                                  download_path=choice, output_file="fabricAPI.jar")
    print('Fabric API downloaded')
    print("Downloading OceanClient...")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024
    with open(choice + 'oceanclient.jar', "wb") as f:
        with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
            for chunk in response.iter_content(block_size):
                f.write(chunk)
                pbar.update(len(chunk))
    print('OceanClient downloaded')
    choice2 = input("Do you want to close this app(y/n): ")
    if choice2 == "y" or "yes".lower():
        exit()
    else:
        pass

def startmenu(os):
    if os == "Windows":
        mainMenu(os=os)
    elif os == "Linux":
        mainMenu(os=os)
    elif os == "Darwin":
        mainMenu(os=os)
    else:
        exit("Unsupported OS" + os)
def mainMenu(os):
    print('Running on: ' + os + '(' + platform.platform() + ')')
    print(''' ██████   ██████ ███████  █████  ███    ██  ██████ ██      ██ ███████ ███    ██ ████████     ██ ███    ██ ███████ ████████  █████  ██      ██      ███████ ██████  
██    ██ ██      ██      ██   ██ ████   ██ ██      ██      ██ ██      ████   ██    ██        ██ ████   ██ ██         ██    ██   ██ ██      ██      ██      ██   ██ 
██    ██ ██      █████   ███████ ██ ██  ██ ██      ██      ██ █████   ██ ██  ██    ██        ██ ██ ██  ██ ███████    ██    ███████ ██      ██      █████   ██████  
██    ██ ██      ██      ██   ██ ██  ██ ██ ██      ██      ██ ██      ██  ██ ██    ██        ██ ██  ██ ██      ██    ██    ██   ██ ██      ██      ██      ██   ██ 
 ██████   ██████ ███████ ██   ██ ██   ████  ██████ ███████ ██ ███████ ██   ████    ██        ██ ██   ████ ███████    ██    ██   ██ ███████ ███████ ███████ ██   ██ 
                                                                                                                                                                   
                                                                                                                                                                   ''')
    print('By AxiomLab and contributors')
    print('--->')
    print('AxiomLab LIMITED & GmbH')
    print('Wassergasse 1')
    print('04552 Borna')
    print('Germany')
    print('--->')
    print('Select an option:')
    print('1. Install OceanClient')
    print('2. Uninstall OceanClient')
    print('3. Uninstall OceanClient with Dependencies')
    print('4. Update OceanClient')
    print('5. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        InstallOceanClient()

    elif choice == '2':
        print('Uninstall OceanClient')
    elif choice == '3':
        print('Uninstall OceanClient with Dependencies')
    elif choice == '4':
        print('Update OceanClient')
    elif choice == '5':
        exit(0)
getting_ready()

