
import nmap as nm
import os
sc = nm.PortScanner()

print("""        _      _      _  _       
  /\ /\(_)  __| |  __| |(_)  ___ 
 / //_/| | / _` | / _` || | / _ \
/ __ \ | || (_| || (_| || ||  __/
\/  \/ |_| \__,_| \__,_||_| \___|
""")



def main():
    n = input("1 : Network Scanner\n2 : Exploit\n\nPlease enter a number: ")
    if n == "1":
        nmap()
    if n == "2":
        meta()
    else:
        print("Veuillez faire un choix entre 1 et 2.")



def nmap():
    print("""   _____   _____            _   _ 
  / ____| / ____|    /\    | \ | |\n
 | (___  | |        /  \   |  \| |\n
  \___ \ | |       / /\ \  | . ` |\n
  ____) || |____  / ____ \ | |\  |\n
 |_____/  \_____|/_/    \_\|_| \_|\n
                                  
                                  \n""")
    ip = input("\nEnter the IP address : ")
    sc.scan(ip, '1-1024')
    print("Nmap command : ", sc.command_line())
    print("Hosts : ",sc.all_hosts())
    print("Hostname :", sc[ip].hostname())
    print("Open Ports : ",sc[ip]['tcp'].keys())

def meta():
    print("""  __  __  ______  _______          _____  _____   _       ____  _____  _______ 
|  \/  ||  ____||__   __| /\     / ____||  __ \ | |     / __ \|_   _||__   __|
| \  / || |__      | |   /  \   | (___  | |__) || |    | |  | | | |     | |   
| |\/| ||  __|     | |  / /\ \   \___ \ |  ___/ | |    | |  | | | |     | |   
| |  | || |____    | | / ____ \  ____) || |     | |____| |__| |_| |_    | |   
|_|  |_||______|   |_|/_/    \_\|_____/ |_|     |______|\____/|_____|   |_|                                                                                                                                                                          
""")
    print("Metasploit is starting...")        
    os.system('msfconsole')



if __name__ == "__main__":
    main()