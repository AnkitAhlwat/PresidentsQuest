import json
import describe_current_location
from colorama import Fore, Style

def check_inventory_for_key():
    with open("character.json", "r") as file_object:
        character_dictionary = json.load(file_object)
        if "key" in character_dictionary["Items"]:
            print("I told you that you can not- Oh wait is that the key...\n you may enter...")
        else:
            print(Fore.RED + "You must find the key to open this door!\n" + Style.RESET_ALL)
            describe_current_location.setup_current_location()
def main():
    check_inventory_for_key()


if __name__ == "__main__":
    main()
