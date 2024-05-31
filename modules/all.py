from modules.fast_sql import fast_sql
from colorama import Fore, init, Style
from platform import uname
from os import system
from time import sleep
from requests import get

init()

WHITE = Fore.WHITE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
RED = Fore.RED
CYAN = Fore.CYAN
plat = uname()[0].lower()
first_time = True
commands = ["add_new_column", "all_rows", "all_table_data", "clear_table", "close", "custome_command", "insert_in", "remove_column", "select_from"]
exit_commands = ["exit", "quit", "exit()", "quit()"]
help_commands = ["help()", "help", "help_me", "helpme", "i_dont_know", "idontknow", "sos"]

def clear():
    global plat
    if "win" in plat: system("cls")
    else: system("clear")
def start():
    clear()
    global WHITE, GREEN, YELLOW, BLUE, RESET, RED, CYAN
    db_name = input(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Write your database name{WHITE}({BLUE}ex{YELLOW}: {BLUE}database.db{WHITE}){YELLOW}: ")
    tb_name = input(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Write your table name{WHITE}({BLUE}ex{YELLOW}: {BLUE}users{WHITE}){YELLOW}: ")
    columns_name = input(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Write your columns name{WHITE}({BLUE}ex{YELLOW}: {BLUE}name,email,password{WHITE}){YELLOW}: ")
    if db_name == "": db_name = "database.db"
    if tb_name == "": tb_name = "users"
    if columns_name == "": columns_name = "name,email,password"
    columns = columns_name.split(",")
    fsql = fast_sql(db_name, tb_name, columns)
    print(f"{YELLOW}   Connecting...")
    fsql.connect()
    print(f"{GREEN}   Connected")
    sleep(0.5)
    return fsql
def help():
    global GREEN, YELLOW
    text = f"""{GREEN}These are the commands:\n"""
    num = len(commands)-1 
    commands.sort()
    for i in range(len(commands)):
        text += f"{YELLOW}{commands[i]}"
        if i >= num: pass
        else: text += f"{GREEN}, "
        if (i % 5) == 0 and i != 0: text += "\n"
    return text
def send_out(out):
    global GREEN, RED
    if out == True: print(f"{GREEN}Completed!")
    else: print(f"{RED}Error!")
def go_out(text=f"{RED} IF YOU CLOSE THIS PROCESS JUST YOUR DATABASE WILL SAVE!!! {YELLOW} ARE YOU SURE(Y/N)?{RED} "):
    global RED, BLUE, YELLOW
    ex = input(text).lower()
    if "y" in ex: exit()
    else: 
        clear()
        print(f"{BLUE}    YOUR SAFE NOW!  :)")
        sleep(3)
def banner():
    global BLUE, CYAN, WHITE, YELLOW, RED
    print(f"""{BLUE}
 ________________                              ___________________              ___
|_______________/    ________________        /                     \           |   |
|   |                \___________    \      /    {YELLOW}github.com/{BLUE}        \          |   |
|   |___________                /    /     /     {YELLOW}Unknow-per/{BLUE}         \         |   |
| {RED}({BLUE} |__________/   ____________/    /     /      {YELLOW}Fast_sql{BLUE}    ____     \        |   |  {CYAN} Sqlite is for {BLUE}
| {RED}F{BLUE} |             /  ______________/     |                  \    \     |       |   |  {YELLOW} Everyone{WHITE}.{BLUE}
| {RED}){BLUE} |            /  /                     \        {RED}(Q){BLUE}       \    \   /        |   |
|   |            \  \    {RED}(S){BLUE}               \                  \    \ /         |   |___________   
|   |             \  \_______________       \                  \    \          |    {RED}(L){BLUE}        |
|___|              \________________/        \__________________\____\         |_______________|
""")
def cli(fsql):
    global WHITE, GREEN, YELLOW, BLUE, RESET, RED, CYAN, plat, first_time, commands, exit_commands, help_commands
    while True:
        try:
            clear()
            if first_time == True:
                print(f"{YELLOW}***{GREEN}write {CYAN}i_dont_know{YELLOW}({BLUE}or something like help, SOS, help_me, ...{YELLOW}){GREEN} to show all commands.{YELLOW}***{RESET}")
                first_time = False
            banner()
            command = input(f"{YELLOW}>>>{BLUE} ").lower()
            if command in help_commands: print(help())
            if command in exit_commands: 
                go_out()
                continue
            if command in commands: 
                if command == "add_new_column":
                    cn = input(f"{YELLOW}<<<{GREEN} Write your column name: ")
                    out = fsql.add_new_column(cn)
                    send_out(out)
                if command == "all_rows":
                    out = fsql.all_rows()
                    print(GREEN + out)
                if command == "all_table_data":
                    out = fsql.all_table_data
                    print(GREEN + out)
                if command == "clear_table":
                    out = fsql.clear_table()
                    send_out(out)
                if command == "close":
                    go_out(f"{YELLOW} ARE YOU SURE(Y/N)?{RED} ")
                    continue
                if command == "custome_command":
                    cm = input(f"{YELLOW}<<<{GREEN} Write your query: ")
                    out = fsql.Custome_command(cm)
                    print(out)
                if command == "insert_in":
                    cm = input(f"{YELLOW}<<<{GREEN} Write your attributes(ex: {columns_name}): ")
                    out = fsql.Insert_in(cm.split(","))
                    send_out(out)
                if command == "remove_column":
                    cn = input(f"{YELLOW}<<<{GREEN} Write column name: ")
                    out = fsql.remove_column(cn)
                if command == "select_from":
                    se = input(f"{YELLOW}<<<{GREEN} Select what(ex: email)? ")
                    wv = input(f"{YELLOW}<<<{GREEN} Where(ex: username)? ")
                    ip = input(f"{YELLOW}<<<{GREEN} Where(ex: Alex)? ")
                    out = fsql.Select_from(se, wv, ip)
                    print(GREEN + out)
            if command not in commands and command not in exit_commands and command not in help_commands:
                input(f"{RED}Invalid Command :/\n")
                continue
            input(f"{Fore.BLACK + Style.DIM}PRESS ENTER TO CONTINUE{RESET}\n")
        except KeyboardInterrupt:
            go_out()
