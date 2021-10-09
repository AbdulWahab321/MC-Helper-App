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

if "win" in sys.platform:
    try:
        import colorama
    except:
        print("Installing a component which is necessary for windows OS to run...")
        os.system("pip install colorama")
        import colorama
    colorama.init()
commands = ["save-place", "delete-place","get-coords","export-all", "show", "delete-data", "exit"]
def _save_place(name,coords=()):
    already_exists = os.path.exists("data.dt")
    with open("data.dt","w" if not already_exists else "a") as f:
        f.write(f"name:{name};coords:{coords}") if not already_exists else f.write(f"\nname:{name};coords:{coords}")
    cprint(f"Successfully saved place {name} with coordinates {coords}",GREEN)
def _get_place(name):
    dt = ""
    with open("data.dt","r") as f:
        dt = f.readlines()
    for i in dt:
        if name in i:
            if i.split("name:")[1].split(";")[0] == name:
                inname = i.split("name:")[1].split(";")[0]
                coords = i.split(f"name:{inname}")[1].split(";")[1].split("coords:")[1]
                cprint(f"coordinates: {coords}",GREEN)
        else:
            word_exists = False
            for i in dt: 
                inname = i.split("name:")[1].split(";")[0]
                if inname.strip() == name.strip():word_exists = True
            if not word_exists:    
                cprint("Sorry Name does not exists!",FAIL)
def _start():
    cprint(
"""         _        _______  _______  ______            _____ _______  
|\\    /| | |\\   | |        |        |    |     /\\    |         |
| \\  / | | | \\  | |______  |        |____|    /  \\   |_____    | 
|  \\/  | | |  \\ | |        |        |    \\   /====\\  |         |
|      | _ |   \\/ |______  |______  |     \\ /      \\ |         |    

                    _     _  ______ _       _______  ______ _____
                    |     | |       |       |     | |       |    |
                    |_____| |______ |       |_____| |______ |____|
                    |     | |       |       |       |       |    \\
                    |     | |______ |______ |       |______ |     \\                  
""",GREEN)
    cprint(
"""
                                      COMMANDS
                                    ============

    1) save-place    --->  To save your favourite place and its coordinates
    2) get-coords    --->  To get a saved place's coordinates
    3) delete-place  --->  To delete one of your place and coordinates that you don't want anymore
    4) export-all    --->  To export all saved places to given file Path
    5) show          --->  To show all saved places on the console
    6) delete-data   --->  To delete all saved places  
    7) exit          --->  To exit the program    
""",BLUE)            
def _delete_place(name):
    dt = ""
    full_data = ""
    
    with open("data.dt","r") as f:
        dt = f.readlines()
    with open("data.dt","r") as f:
        full_data = f.read()        
    for i in dt:
        if name in i:
            if i.split("name:")[1].split(";")[0] == name:
                inname = i.split("name:")[1].split(";")[0]
                coords = i.split(f"name:{inname}")[1].split(";")[1].split("coords:")[1]
                _new = full_data.replace(f"name:{inname};coords:{coords}","")
                with open("data.dt", "w") as f:
                    f.write(_new)
                cprint(f"Successfully Deleted Place: {inname}",GREEN)
        else:
            word_exists = False
            for i in dt: 
                inname = i.split("name:")[1].split(";")[0]
                if inname.strip() == name.strip():word_exists = True
            if not word_exists:    
                cprint("Sorry Name does not exists!",FAIL)   
def cprint(text,color):
    print(color+text+'\033[0m')   
def colored(text,color):
    return color+text+'\033[0m'              
def _export(filename):
    fl = None
    if os.path.exists("data.dt"):
        dtfl = open("data.dt", "r")
        data = dtfl.readlines()
        dtfl.close()
        if not os.path.exists(os.path.dirname(filename)) or not os.path.isdir(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))
            os.makedirs(filename)
        for i in data:
            inname = i.split("name:")[1].split(";")[0]
            coords = i.split(f"name:{inname}")[1].split(";")[1].split("coords:")[1]
            if os.path.exists(filename):
                fl = open(filename, "a").write(f"Coordinates of {inname} is {coords}")
            else:
                fl = open(filename, "w").write(f"Coordinates of {inname} is {coords}")    
        fl.close()
              
        cprint(f"Successfully exported All Places and Coordinates to file {filename}",GREEN)  
    else:
        cprint(f"Datas are deleted!",FAIL)         
def print_similar(command):
    for i in commands:
        if command in i:
            mean = f'Did you mean: {i}'
            print(f"{colored('Unknown command!',FAIL)}\n{colored(mean,WARNING)}")
            break
        else:
            if command in "get-coords":
                print(f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: get-coords',WARNING)}")
                break
            else:
                if command in "export-all":
                    print(f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: export-all',WARNING)}")
                    break
                else:
                    if command in "delete-":
                        print(f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: delete-place or delete-data',WARNING)}")
                        break   
                    else:
                        if command in "show":
                            print(f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: show',WARNING)}")
                            break
                        else:        
                            if command in "ex":
                                print(f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: exit or export-all',WARNING)}")    
                            else:
                                if command in "exit":
                                    print(f"{colored('Unknown command!',FAIL)}\n{colored('Did you mean: exit',WARNING)}")
                                else:    
                                    return False
                 
def _show():
    dtfl = open("data.dt", "r")
    data = dtfl.readlines()
    dtfl.close()
    if os.path.exists("data.dt"):
        for i in data:
            inname = i.split("name:")[1].split(";")[0]
            coords = i.split(f"name:{inname}")[1].split(";")[1].split("coords:")[1]
            cprint(f"{inname} : {coords}",GREEN)
    else:
        cprint("Datas are deleted!",FAIL)                    
_start()   
print(f"\n{colored('NOTE:',FAIL)} {colored('Everything you save is automatically stored in a file You wont loose any data even when this window is closed except you deleted all the data',WARNING)}\n")                                       
while True:
    inp = input(">> ")
    if inp == "save-place":
        name = input("Name of place to save>> ")
        coords = input("Coords of place to save>> ")
        _save_place(name, coords)
    elif inp == "get-coords":
        name = input("Name of place to get coordinates>> ")
        _get_place(name)
    elif inp == "delete-place":
        name = input("Name of place to delete>> ")    
        _delete_place(name)
    elif inp == "export-all":
        filename = input("Path to export>> ")
        _export(filename)
    elif inp == "show":
        _show()
    elif inp == "delete-data":
        if os.path.exists("data.dt"):
            os.remove("data.dt")
            cprint("Successfully deleted Data",GREEN)
        else:
            cprint("Data already deleted...",FAIL)  
    elif inp == "exit":
        cprint("Exiting Program....",GREEN)
        break
        exit(0)           
    else:
        if inp.strip() == "-":
            cprint("Incomplete Command!",FAIL)
        else:
            if print_similar(inp) == False:
                cprint("Unknown command!",FAIL)
