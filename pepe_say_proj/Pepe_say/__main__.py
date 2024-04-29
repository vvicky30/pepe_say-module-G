#from pepesay_module import pepe_say
   
from Pepe_say import pepesay_module
from sys import argv

def main():
    message_cli = argv[1:]
    pepesay_module.pepe_say(message_cli)

if __name__ == "__main__":
    main()

