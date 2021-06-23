# Imports necessary libraries
from cryptography.fernet import Fernet
from faker import Faker
import requests
import nmap
import subprocess, sys

# Generates key and cipher suite for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Prints out intro and allows user to choose one of 2 modes with if statement
print("Welcome to the Dolos Security Suite! Please select a mode of operation.")
print("1. Encryption\n2. Identity Falsifier\n3. HTTP Requester\n4. Nmap Scanner\n5. Port-closer")
mode = input("Type the corresponding number to select a mode of operation.\n")
# Using the input variable, user can select one of two modes
if mode == ("1"):
    print("Encryption allows you to enter any string of text for the application to encrypt and give back to you.")
    # Text is taken, and then encoded into utf-8, before being encrypted and decrypted from utf-8 bytes into a string
    encryptInput = input("Please enter the string you wish to encrypt.\n")
    cipher_text = cipher_suite.encrypt(bytes(encryptInput, 'utf-8'))
    cipher_text = cipher_text.decode("utf-8")
    print("Your encrypted text is:" + cipher_text)
    print("Your key is: ")
    # Generates key for user for later decryption
    print(key)

elif mode == ("2"):
    print("The Identity Falsifier allows you to quickly create a fake identity from a variety of English-speaking countries.")
    print("A false name, address, and phone number will be generated.")
    identityTrigger = True
    while identityTrigger == True:
        print("Which country do you wish to create a fake identity for?")
        # Input and if statement allows for the user to select one of 5 countries, using faker's localization feature
        mode2 = input("1. United States\n2. United Kingdom\n3. Australia\n4. Canada\n5. New Zealand\n")
        if mode2 == ("1"):
            fake = Faker('en_US')
        elif mode2 == ("2"):
            fake = Faker('en_GB')
        elif mode2 == ("3"):
            fake = Faker('en_AU')
        elif mode2 == ("4"):
            fake = Faker('en_CA')
        elif mode2 == ("5"):
            fake = Faker('en_NZ')
        # Faker then generates a typical name, address, and phone number according to the localization. It is then printed
        fake.name()
        fake.address()
        fake.phone_number()
        print(fake.name())
        print(fake.address())
        print(fake.phone_number())
        identityEnd = input("Would you like to: \n1. Generate another identity\n2. Exit\n")
        if identityEnd == ("1"):
            print("Returning to menu...")
        elif identityEnd == ("2"):
            print("Exiting...")
            identityTrigger = False
elif mode == ("3"):
    # Setups later loop
    requestTrigger = True
    requestInput = input("First, input a website.")
    # Turns user-input into website for later requests
    r = requests.get(requestInput)
    # Creates a loop that allows user to continue acting after selecting one function
    while requestTrigger == True:
        print("Select a function!")
        print("1. Help")
        print("2. Grab site's header")
        print("3. Grab a site's content")
        print("4. Grab a site's text (content in unicode)")
        print("5. Add parameter to request")
        print("6. Remove parameters")
        print("7. Exit")
        modeSelection = input("")
        if modeSelection == ("1"):
            # Requests the site with the help option
            print(help(r))
        elif modeSelection == ("2"):
            # Requests the site with the header option
            print(r.headers)
        elif modeSelection == ("3"):
            # Requests the site with the content option
            print(r.content)
        elif modeSelection == ("4"):
            # Requests the site with the text option
            print(r.text)
        elif modeSelection == ("5"):
            # Allows the user to enter their own custom parameter to a request
            payload = input("Enter your parameter! An example would be \"firstName\": \"John\"")
            # Adds user-entered parameter to string
            r = requests.get(requestInput, params=payload)
            print("Parameter added!")
        elif modeSelection == ("6"):
            # Allows the user to remove a previously-entered parameter and return it to normal
            r = requests.get(requestInput)
            print("Parameter removed")
        elif modeSelection == ("7"):
            # Ends loop and exits
            print("Exiting HTTP requester...")
            requestTrigger = False
elif mode == ("4"):
    print("First, input a target for your scan!")
    print("DISCLAIMER: Please make sure to only scan targets that have agreed to port scans, as per their scope for public vulnerability testing. This tool is not responsible for the actions you take with this scanner.")
    print("Make sure that nmap and python-nmap have been installed using pip before hand, elsewise you will receive an error.")
    # Loop to allow user to repeat
    nmapTrigger = True
    while nmapTrigger == True:
        # Entering target and ports and strings
        target = input("Type in target:")
        portBegin = input("Select a port number to begin with:")
        portEnd = input("Select a port number to end with:")
        # Using portscanner to scan strings
        scanner = nmap.PortScanner()
        # Small loop to go port-by-port and test if each is closed
        for i in range(portBegin, portEnd+1):
            # Scans port
            res = scanner.scan(target, str(i))
            # Grabs a port's state and prints it
            res= res['scan'][target]['tcp'][i]['state']
            print(f'Port {i} is {res}')
            nmapAnswer = input("\nScan finished! Would you like to scan again?\n1. Scan again\n2. Exit\n")
            # Allows for user to restart menu or exit
            if nmapAnswer == ("1"):
                print("Restarting scan...")
            elif nmapAnswer == ("2"):
                print("Exiting Nmap Scanner...")
                nmapTrigger = False

elif mode == ("5"):
    print("Welcome to the Port-closer! This tool will generate firewall rules for Windows 10 systems to block traffic on a specified port.")
    print("Choose one of two ports to close! Having either of these ports open could possibly open you to unwanted intrusion later.")
    print("NOTE: If this application is not run as an administrator, you will receive an error! To run it as an admin, open command prompt as an admin and run it from there.")
    print("NOTE: Please place the Dolos folder included in the zip file onto your desktop. After that, input your Windows 10 User Name")
    # Input user's name so filepath works correctly
    userName = input("Enter your username:")
    # Loop to allow user to restart
    portTrigger = True
    while portTrigger == True:
        print("Which port would you like to close?")
        print("1. Close port 5938 (Teamviewer)")
        print("2. Close port 3389 (Microsoft Remote Desktop")
        print("3. Re-open port 3989 (can only be done if it's already closed)")
        print("4. Re-open port 5938 (can only be done if it's already closed)")

        portInput = input("Choose an option:")
        if portInput == ("1"):
            # Just grabs and runs port1.ps1 in powershell.exe
            p = subprocess.Popen(["powershell.exe",
                                  "C:\\Users\\"+userName+"\\Desktop\\Dolos\\port1.ps1"],
                                 stdout=sys.stdout)
        if portInput == ("2"):
            # Just grabs and runs port2.ps1 in powershell.exe
            p = subprocess.Popen(["powershell.exe",
                                  "C:\\Users\\"+userName+"\\Desktop\\Dolos\\port2.ps1"],
                                 stdout=sys.stdout)
        if portInput == ("3"):
            # Just grabs and runs port3.ps1 in powershell.exe
            p = subprocess.Popen(["powershell.exe",
                                  "C:\\Users\\"+userName+"\\Desktop\\Dolos\\port3.ps1"],
                                 stdout=sys.stdout)
        if portInput == ("4"):
            # Just grabs and runs port4.ps1 in powershell.exe
            p = subprocess.Popen(["powershell.exe",
                                  "C:\\Users\\"+userName+"\\Desktop\\Dolos\\port4.ps1"],
                                 stdout=sys.stdout)
        # Prints out results!
        p.communicate()
        print("Action completed!")
        portEnd = input("Would you like to: \n1. Do another action\n2. Exit\n")
        # User is given option to restart or exit
        if portEnd == ("1"):
            print("Returning to menu...")
        elif portEnd == ("2"):
            print("Exiting...")
            portTrigger = False