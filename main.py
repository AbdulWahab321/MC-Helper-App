import os
import sys

BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
GREYBG = '\033[100m'
REDBG = '\033[101m'
GREENBG = '\033[102m'
YELLOWBG = '\033[103m'
BLUEBG = '\033[104m'
PINKBG = '\033[105m'
CYANBG = '\033[106m'

commands = ["save-place", "delete-place", "get-coords", "export-all", "list-all", "list-sections", "help",
            "list-names", "list-coords", "delete-data", "enter-section", "create-section", "delete-section", "delete-all" "exit"]
currentSection = None
if "win" in sys.platform:
    try:
        import colorama
    except:
        print("Installing a component which is necessary for windows OS to run...")
        os.system("pip install colorama")
        import colorama
    colorama.init()


def cprint(text, color):
    print(color+text+'\033[0m')


def colored(text, color):
    return color+text+'\033[0m'


def word_exists_in_array(string, array):
    exists = False
    for i in array:
        if string in i:
            exists = True
    return exists


def get_index(string, array):
    if word_exists_in_array(string, array):
        index = 0
        for i in array:
            index = index + 1
            if string in i:
                return index
                break
    else:
        return False


def unpacked(data=()):
    x, y, z = data
    return f"{x}, {y}, {z}"


def _save_place(name, coords=()):
    already_exists = os.path.exists(f"sections/{currentSection}.dt")
    with open(f"sections/{currentSection}.dt", "w" if not already_exists else "a") as f:
        f.write(f"name:{name};coords:{unpacked(coords)}") if not already_exists else f.write(
            f"\nname:{name};coords:{unpacked(coords)}")
    cprint(
        f"Successfully saved place {name} with coordinates {unpacked(coords)}", GREEN)


def _update_coords(name, coords):
    _delete_place(name)
    _save_place(name, coords)


def _get_place(name):
    dt = ""
    with open(f"sections/{currentSection}.dt", "r") as f:
        dt = f.readlines()
    for i in dt:
        if i.strip()!="":
            if name in i:
                if i.split("name:")[1].split(";")[0] == name:
                    inname = i.split("name:")[1].split(";")[0]
                    coords = i.split(f"name:{inname}")[1].split(";")[
                        1].split("coords:")[1]
                    cprint(f"coordinates: {coords}", GREEN)
        else:
            word_exists = False
            for i in dt:
                if i.strip()!="":
                    inname = i.split("name:")[1].split(";")[0]
                    if inname.strip() == name.strip():
                        word_exists = True
            if not word_exists:
                cprint("Sorry Name does not exists!", FAIL)


def _help():
    cprint(
        """
                                      COMMANDS
                                    ============

    1) save-place     --->  To save your favourite place and its coordinates
    2) get-coords     --->  To get a saved place's coordinates
    3) update-coords  --->  To update the place's coordinates 
    4) delete-place   --->  To delete one of your place and coordinates that you don't want anymore
    5) export-all     --->  To export all saved places to given file Path
    6) list-all       --->  To list all saved places on the console
    7) delete-data    --->  To delete all saved places in a specific section  
    8) list-names     --->  To list all saved places
    9) list-coords    --->  To list all saved coordinates
   10) create-section --->  To create a new section and create places there (IMPORTANT)
   11) enter-section  --->  To enter a created section
   12) delete-section --->  To delete a created section
   13) delete-all     --->  To delete all sections  
   14) list-sections  --->  To list all created sections
   15) exit           --->  To exit the program    
   16) help           --->  prints this message again         
""", BLUE)


def _start():
    cprint(
        """
 /$$      /$$ /$$                                                   /$$$$$$   /$$    
| $$$    /$$$|__/                                                  /$$__  $$ | $$    
| $$$$  /$$$$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$ | $$  \__//$$$$$$  
| $$ $$/$$ $$| $$| $$__  $$ /$$__  $$ /$$_____/ /$$__  $$|____  $$| $$$$   |_  $$_/  
| $$  $$$| $$| $$| $$  \ $$| $$$$$$$$| $$      | $$  \__/ /$$$$$$$| $$_/     | $$    
| $$\  $ | $$| $$| $$  | $$| $$_____/| $$      | $$      /$$__  $$| $$       | $$ /$$
| $$ \/  | $$| $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$     |  $$$$$$$| $$       |  $$$$/
|__/     |__/|__/|__/  |__/ \_______/ \_______/|__/      \_______/|__/        \___/  
                                                                                     
                                                                                     
                                                                                     
 /$$   /$$           /$$                                                             
| $$  | $$          | $$                                                             
| $$  | $$  /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$                                
| $$$$$$$$ /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$                               
| $$__  $$| $$$$$$$$| $$| $$  \ $$| $$$$$$$$| $$  \__/                               
| $$  | $$| $$_____/| $$| $$  | $$| $$_____/| $$                                     
| $$  | $$|  $$$$$$$| $$| $$$$$$$/|  $$$$$$$| $$                                     
|__/  |__/ \_______/|__/| $$____/  \_______/|__/                                     
                        | $$                                                         
                        | $$                                                         
                        |__/                                                                        
""", GREEN)
    _help()


def _delete_place(name):
    dt = ""
    full_data = ""

    with open(f"sections/{currentSection}.dt", "r") as f:
        dt = f.readlines()
    with open(f"sections/{currentSection}.dt", "r") as f:
        full_data = f.read()
    for i in dt:
        if i.strip()!="":
            if name in i:
                if i.split("name:")[1].split(";")[0] == name:
                    inname = i.split("name:")[1].split(";")[0]
                    coords = i.split(f"name:{inname}")[1].split(";")[
                        1].split("coords:")[1]
                    _new = full_data.replace(f"name:{inname};coords:{coords}", "")
                    with open("data.dt", "w") as f:
                        f.write(_new)
                    cprint(f"Successfully Deleted Place: {inname}", GREEN)
        else:
            word_exists = False
            for i in dt:
                if i.strip()!="":
                    inname = i.split("name:")[1].split(";")[0]
                    if inname.strip() == name.strip():
                        word_exists = True
            if not word_exists:
                cprint("Sorry Name does not exists!", FAIL)


def _export(filename):
    fl = None
    if os.path.exists(f"sections/{currentSection}.dt"):
        dtfl = open(f"sections/{currentSection}.dt", "r")
        data = dtfl.readlines()
        dtfl.close()
        if not os.path.exists(os.path.dirname(filename)) or not os.path.isdir(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))
            os.makedirs(filename)
        for i in data:
            if i.strip()!="":
                inname = i.split("name:")[1].split(";")[0]
                coords = i.split(f"name:{inname}")[1].split(";")[
                    1].split("coords:")[1]
                if os.path.exists(filename):
                    if open(filename).read().split() != "":
                        fl = open(filename, "a")
                        fl.write(f"\nCoordinates of {inname} : {coords}")
                    else:
                        fl = open(filename, "w")
                        fl.write(f"Coordinates of {inname} : {coords}")
                else:
                    fl = open(filename, "w")
                    fl.write(f"Coordinates of {inname} : {coords}")
        fl.close()

        cprint(
            f"Successfully exported All Places and Coordinates to file {filename}", GREEN)
    else:
        cprint(f"Datas are deleted!", FAIL)


def print_similar(command):
    for i in commands:
        if command in i:
            mean = f'Did you mean: {i}'
            print(f"{colored('Unknown command!',FAIL)}\n{colored(mean,WARNING)}")
            break
        else:
            if command in "get-coords":
                print(
                    f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: get-coords',WARNING)}")
                break
            else:
                if command in "export-all":
                    print(
                        f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: export-all',WARNING)}")
                    break
                else:
                    if command in "delete-":
                        print(
                            f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: delete-place or delete-all',WARNING)}")
                        break
                    else:
                        if command in "show":
                            print(
                                f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: show',WARNING)}")
                            break
                        else:
                            if command in "ex" or command.strip() == "ex":
                                print(
                                    f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: exit or export-all',WARNING)}")
                                break
                            else:
                                if command in "exit":
                                    print(
                                        f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: exit',WARNING)}")
                                    break
                                else:
                                    if command in "list-":
                                        if currentSection:
                                            print(
                                                f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: list-all or list-names or list-coords or list-section',WARNING)}")
                                        else:
                                            print(
                                                f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: list-sections',WARNING)}")
                                        break
                                    else:
                                        if command in "list-all":
                                            print(
                                                f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: list-all',WARNING)}")
                                            break
                                        else:
                                            if command in "list-names":
                                                print(
                                                    f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: list-names',WARNING)}")
                                                break
                                            else:
                                                if command in "list-coords":
                                                    print(
                                                        f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: list-coords',WARNING)}")
                                                    break
                                                else:
                                                    if command in "help":
                                                        print(
                                                            f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: help',WARNING)}")
                                                        break
                                                    else:
                                                        if command in "create-section":
                                                            print(
                                                                f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: create-section',WARNING)}")
                                                            break
                                                        else:
                                                            if command in "enter-section":
                                                                print(
                                                                    f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: enter-section',WARNING)}")
                                                                break
                                                            else:
                                                                if command in "list-sections":
                                                                    print(
                                                                        f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: list-sections',WARNING)}")
                                                                    break
                                                                else:
                                                                    cprint(
                                                                        "Unknown command!", FAIL)
                                                                    break


def _show():
    if os.path.exists(f"sections/{currentSection}.dt"):
        dtfl = open(f"sections/{currentSection}.dt", "r")
        data = dtfl.readlines()
        dtfl.close()
        for i in data:
            if i.strip()!="":
                inname = i.split("name:")[1].split(";")[0]
                coords = i.split(f"name:{inname}")[1].split(";")[
                    1].split("coords:")[1]
                cprint(f"{inname} : {coords}", GREEN)
    else:
        cprint("Current section does not exists!", FAIL)


def _list_names():

    if os.path.exists(f"sections/{currentSection}.dt"):
        dtfl = open(f"sections/{currentSection}.dt", "r")
        data = dtfl.readlines()
        dtfl.close()
        cprint("Listing All Saved Places...", BLUE)
        for i in data:
            if i.strip()!="":
                inname = i.split("name:")[1].split(";")[0]
                cprint(f"{inname}", GREEN)
    else:
        cprint("Current section does not exists!", FAIL)


def _list_coords():
    if os.path.exists(f"sections/{currentSection}.dt"):
        dtfl = open(f"sections/{currentSection}.dt", "r")
        data = dtfl.readlines()
        dtfl.close()
        cprint("Listing All Saved Coordinates...", BLUE)
        for i in data:
            if i.strip()!="":
                inname = i.split("name:")[1].split(";")[0]
                coords = i.split(f"name:{inname}")[1].split(";")[
                    1].split("coords:")[1]
                cprint(f"{coords}", GREEN)
    else:
        cprint("Current section does not exists!", FAIL)


def _list_sections():
    cprint("Listing sections...", BLUE)
    num = 1
    for i in os.listdir("sections"):
        cprint("section "+str(num)+": "+i.replace(".dt", ""), GREEN)
        num += 1


_start()
print(f"\n{colored('NOTE:',FAIL)} {colored('Everything you save is automatically stored in a file You wont loose any data even when this window is closed except you deleted all the data',WARNING)}\n")
while True:
    if not os.path.exists("sections"):
        os.mkdir("sections")
    if not currentSection:
        inp = input(">> ")
    else:
        inp = input(f"section: {currentSection}>> ")

    if inp == "save-place":
        if currentSection != None:
            name = input("Name of place to save>> ")
            if name.strip() != "":
                cprint("Type 'none' to save it as ~", BLUE)
                x = input("X coordinate of place to save>> ")
                y = input("Y coordinate of place to save>> ")
                z = input("Z coordinate of place to save>> ")
                if x.strip() and y.strip() and z.strip() != "":
                    _save_place(name, coords=(x if x != "none" else "~",
                                y if y != "none" else "~", z if z != "none" else "~"))
                else:
                    print(
                        f"{colored('Found empty input!',FAIL)}\n{colored('Skipped Saving Place...',WARNING)}")
            else:
                print(
                    f"{colored('Found empty input!',FAIL)}\n{colored('Skipped Saving Place...',WARNING)}")
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "get-coords":
        if currentSection != None:
            name = input("Name of place to get coordinates>> ")
            if name.strip() != "":
                _get_place(name)
            else:
                print(
                    f"{colored('Found empty input!',FAIL)}\n{colored('Skipped Get Place...',WARNING)}")
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "delete-place":
        if currentSection != None:
            name = input("Name of place to delete>> ")
            _delete_place(name)
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "export-all":
        if currentSection != None:
            filename = input("Path to export>> ")
            _export(filename)
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "list-all":
        if currentSection != None:
            _show()
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "create-section":
        if not os.path.exists("sections"):
            os.mkdir("sections")
        name = input("Name of section>> ")
        with open(f"sections/{name}.dt", "w") as f:
            f.write("")

        if os.path.exists(f"sections/{name}.dt"):
            cprint(f"Sucessfully created section: {name}", GREEN)
            currentSection = name
        else:
            cprint(f"Some error occurred while creating section {name}!", FAIL)
    elif inp == "enter-section":
        if not os.path.exists("sections"):
            os.mkdir("sections")        
        name = input("Name of section>>")
        if os.path.exists(f"sections/{name}.dt"):
            currentSection = name
            cprint(f"Successfully changed section to {name}", GREEN)
        else:
            cprint(
                "No section found!\nPlease create a new section using create-section", FAIL)
    elif inp == "delete-all":
        os.system("del /Q sections")
    elif inp == "delete-section":
        if not os.path.exists("sections"):
            os.mkdir("sections")        
        name = input("Name of section>> ")
        if os.path.exists(f"sections/{name}.dt"):
            os.remove(f"sections/{name}.dt")
            cprint(f"Successfully deleted section {name}",GREEN)
            if name == currentSection:
                currentSection = None
        else:
            cprint("Section not found!", FAIL)
    elif inp == "list-names":
        if currentSection != None:
            _list_names()
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "list-coords":
        if currentSection != None:
            _list_coords()
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "list-sections":
        if not os.path.exists("sections"):
            os.mkdir("sections")        
        _list_sections()
    elif inp == "help":
        _help()
    elif inp == "delete-data":
        if not os.path.exists("sections"):
            os.mkdir("sections")        
        name = input("Name of section to clear data>> ")
        if os.path.exists(f"section/{name}.dt"):
            os.remove(f"section/{name}.dt")
            cprint("Successfully deleted Data", GREEN)
            currentSection = None
        else:
            cprint("Data already deleted or does not exists...", FAIL)
    elif inp == "update-coords":
        if currentSection != None:
            name = input("Name of place to update>> ")
            cprint("Type 'none' to save it as ~", BLUE)
            x = input("X coordinate of place to save>> ")
            y = input("Y coordinate of place to save>> ")
            z = input("Z coordinate of place to save>> ")
            if x.strip() and y.strip() and z.strip() != "":
                _update_coords(name, coords=(x if x != "none" else "~",
                               y if y != "none" else "~", z if z != "none" else "~"))
        else:
            cprint(
                "No section currently selected Use create-section or enter-section commands first", FAIL)
    elif inp == "exit":
        cprint("Exiting Program....", GREEN)
        break
        exit(0)
    else:
        if inp.strip() == "-":
            cprint("Incomplete Command!", FAIL)
        else:
            if print_similar(inp) == False:
                cprint("Unknown command!", FAIL)
