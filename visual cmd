import os

#Initialize exit_dict
exit_dict={'exit':1,'clear':2,'pause':3}
#Main program
while 1:
    temial_input=input(">>> ")
    try:
        a=exit_dict[temial_input]
    except KeyError:
        os.system(temial_input)
    else:
        if a == 1:
            exit(0)
        else:
            if a == 2:
                os.system('cls')
            else:
                if a == 3:
                    os.system('pause') 
