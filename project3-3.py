# Imports necessary libraries
from cryptography.fernet import Fernet
from faker import Faker

# Generates key and cipher suite for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Prints out intro and allows user to choose one of 2 modes with if statement
print("Welcome to the Dolos Security Suite! Please select a mode of operation.")
print("1. Encryption\n2. Identity Falsifier")
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