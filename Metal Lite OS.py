#-- metal Lite OS--
#Copyright MetalStudio
import os
import pip
import pipes
import sys
print('hi,administrator.')
print('''Lite OS 1.00
    help,creating,lisence''')
sys_cmd_dict={'update software list':'pip list -o',"clear":'cls',"installed software list":'pip list',"market help":'pip',"shutdown":"shutdown -s -t 60",'restart':'shutdown -r -t 60',"running python":'python','running mysql':'mysql'}
sys_cmd_application_code_dict={'install':0,'update':1,'uninstall':2,'play':3,'find':4,'run':5,'exit':6,'clear':7,'time':8,'send bytes':9,'calculator':10,'recoder':11,'open':12}
while 1:
    sys_termail_input=input("@admin@: >>> ")
    try:
        sys_cmd_run_code=sys_cmd_dict[sys_termail_input]
    except KeyError:
        try:
            sys_cmd_run_code=sys_cmd_application_code_dict[sys_termail_input]       
        except KeyError:
            print('Sorry,I do not know what you entered.Please enter again.Thanks.')
        else:
            if sys_cmd_run_code == 0:
                install_pak=input('install software name: ')
                os.system('pip install {first}'.format(first=install_pak))
                sys_cmd_run_code=' '
            if sys_cmd_run_code == 1:
                update_pak=input('update software name: ')
                os.system("pip install -U {first}".format(first=update_pak))
                sys_cmd_run_code=' '
            if sys_cmd_run_code == 2:
                uninstall_pak=input('uninstall software name: ')
                os.system('pip uninstall {first}'.format(first=uninstall_pak))
                sys_cmd_run_code=' '
            if sys_cmd_run_code == 3:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    play_path_input=input('video or music path: ')
                    os.system(play_path_input)
                    sys_cmd_run_code=' '
            if sys_cmd_run_code == 4:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    find_disk=input('find disk path: ')
                    os.system(find_disk)
                    find_disk_0=input('path: ')
                    os.system('cd {first}'.format(first=find_disk_0))
            if sys_cmd_run_code == 5:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    run_name=input('code name: ')
                    run_exe=input('compiling exe: ')
                    os.system('{first} {second}'.format(first=run_exe,second=run_name))
            if sys_cmd_run_code == 6:
                exit(0)
            if sys_cmd_run_code == 7:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    os.system('cls')
            if sys_cmd_run_code == 8:
                try:
                    import datetime
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install datetime')
                else:
                    now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print('{first}'.format(first=now_time))  
            if sys_cmd_run_code == 9:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    send_computer=input('send computer ip : ')
                    send_bytes=input('bytes : ')
                    send_time=int(input('send times : '))
                    os.system('ping ip {first} -| {second} -n {third}'.format(first=send_computer,second=send_bytes,third=send_time))
            if sys_cmd_run_code == 10:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else: 
                    os.system('calc')
            if sys_cmd_run_code == 11:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    os.system('sndrec32')
            if sys_cmd_run_code == 12:
                try:
                    import os
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Please install os')
                else:
                    open_path=input(' open_path : ')
                    os.system('{first}'.format(first=open_path))                                               
    else:
        os.system(sys_cmd_run_code)
