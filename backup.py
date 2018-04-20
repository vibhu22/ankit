import getpass
import telnetlib

#HOST =("192.168.68.154","192.168.68.155","192.168.68.156")
user = raw_input("Enter your username:")
password = getpass.getpass()
HOST =("192.168.68.156","192.168.68.154","192.168.68.155")
for i in HOST:
    print("\n\nconnecting to "+i)
    tn = telnetlib.Telnet(i, timeout = 15)
    if i is "192.168.68.156":
        tn.read_until("login:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("sh configuration | display set\n")
        tn.write("exit\n")
    
    elif i is "192.168.68.154":
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password +"\n")
        tn.write("terminal length 0\n")
        tn.write("show runni\n")
        tn.write("int lo 0\n")
        tn.write("exit\n")

    elif i is "192.168.68.155":
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("terminal length 0\n")
        tn.write("show runn\n\n")
        tn.write("exit\n\n")

    readall = tn.read_all()
    File = open("File" + str(i), "w")
    File.write(readall)
    File.write("\n")
    File.close()
    print("Backup of "+i+" completed")
 

