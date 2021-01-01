print ("""
██████╗  █████╗ ███████╗███████╗██╗    ██╗██████╗                                            
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔══██╗                                           
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║  ██║                                           
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║  ██║                                           
██║     ██║  ██║███████║███████║╚███╔███╔╝██████╔╝                                           
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═════╝                                            
                                                                                             
                 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
                ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
                ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
                ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
                 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                              By: Luca"zz Dev
""")

key = input("Enter the base of your password: ")

passwd = ""
for letter in key:
    if letter in "Aa":
        passwd = passwd + "#"

    elif letter in "Bb":
        passwd = passwd + "("

    elif letter in "Cc":
        passwd = passwd + "z&"

    elif letter in "Dd":
        passwd = passwd + "z/"

    elif letter in "Ee":
        passwd = passwd + "%"

    elif letter in "Ff":
        passwd = passwd + ")"

    elif letter in "Gg":
        passwd = passwd + "z6"

    elif letter in "Hh":
        passwd = passwd + "z7"

    elif letter in "Ii":
        passwd = passwd + "$"

    elif letter in "Jj":
        passwd = passwd + "z9"

    elif letter in "Kk":
        passwd = passwd + "*"

    elif letter in "Ll":
        passwd = passwd + "&/"

    elif letter in "Mm":
        passwd = passwd + "&&"

    elif letter in "Nn":
        passwd = passwd + "&/"

    elif letter in "Oo":
        passwd = passwd + "&4"

    elif letter in "Pp":
        passwd = passwd + "&5"

    elif letter in "Qq":
        passwd = passwd + "&6"

    elif letter in "Rr":
        passwd = passwd + "&7"

    elif letter in "Ss":
        passwd = passwd + "&z"

    elif letter in "Tt":
        passwd = passwd + "&9"

    elif letter in "Uu":
        passwd = passwd + "/0"

    elif letter in "Vv":
        passwd = passwd + "/z"

    elif letter in "Ww":
        passwd = passwd + "/&"

    elif letter in "Xx":
        passwd = passwd + "//"

    elif letter in "Yy":
        passwd = passwd + "/4"

    elif letter in "Zz":
        passwd = passwd + "8"

    elif letter in "1":
        passwd = passwd + "q"

    elif letter in "2":
        passwd = passwd + "a"

    elif letter in "3":
        passwd = passwd + "z"

    elif letter in "4":
        passwd = passwd + "w"

    elif letter in "5":
        passwd = passwd + "s"

    elif letter in "6":
        passwd = passwd + "x"

    elif letter in "7":
        passwd = passwd + "e"

    elif letter in "8":
        passwd = passwd + "d"

    elif letter in "9":
        passwd = passwd + "c"

    elif letter in "0":
        passwd = passwd + "r"

    else:
        passwd + passwd + letter
print(passwd)