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
sys_cmd_application_code_dict={'install':0,'update':1,'uninstall':2,'play':3,'find':4,'run':5,'exit':6,'clear':7,'time':8,'send bytes':9,'calculator':10,'recoder':11,'open':12,'download':13}
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
            if sys_cmd_run_code == 13:
                try:
                    import urllib
                except ModuleNotFoundError:
                    print('Sorry,We can not find the software.Plaese install urllib')
                else:
                    try:
                        from urllib import request
                    except ModuleNotFoundError:
                        print('Sorry,We can not find the software. Please install urllib and request')
                    else:
                        time_4=0
                        file_name_list=[1,2,3,4,5,6,7,8,9]
                        while 1:
                            url_list=[]
                            file_name_list=[]
                            input_0=int(input('Number of files download at a time：'))
                            if input_0 == 0:
                                print('Please enter again')
                            else:    
                                if time_4 == 0:
                                    at_a=0
                                else:
                                    at_a=at_a
                                for i in range(input_0):
                                    if time_4 == 0:
                                        at_a += 1
                                        file_name_list.append(at_a)
                                    else:
                                        file_name_list.append(at_a)
                                        at_a += 1
                                at_x=0
                                str_1=file_name_list[at_x]
                                input_1=input('Please enter download file name：')
                                input_2=input('Please enter download path：')
                                def download(a):
                                    url=str(a)
                                    downPath=('{first}/{second}.{third}'.format(first=input_2,second=input_1,third=str_1))
                                    urllib.request.urlretrieve(url,downPath)   
                                a=input('Please enter the download url：')
                                input_url_0=a
                                len_0=len(file_name_list)
                                print('Please wait...')
                                if len_0 == 1:
                                    download(input_url_0)
                                    finished_fuc_0=1
                                else:    
                                    for i in range(len_0):
                                        download(input_url_0)
                                        at_x += 1
                                        str_1=file_name_list[at_x]
                                baifenbi_1=0
                                time_1=1
                                fuhao_baifenbi='%'
                                time_2=19
                                for i in range(10):
                                    baifenbi_1 += 10
                                    str_baifenbi='{first}{second}'.format(first=str(baifenbi_1),second=fuhao_baifenbi)
                                    print('{first} [[ {third}{second} ]]'.format(third='\r'+'█' *time_1,end='',first=str_baifenbi,second='\r'+' '*time_2))
                                    time_1 += 1
                                    time_2 -= 1
                                print('Success download.')
                                contiue_ask=input('Continue?：')
                                if contiue_ask != 'yes':
                                    break
                                else:
                                    input_3=input('Is this download file same the last download file：')
                                    input_4=input('Whether the file extention is the same as one：')
                                    if input_4 == 'yes':
                                        time_4 += 1
                                        at_a=0
                                        for i in range(time_4+1):
                                            at_a += 1
                                             
    else:
        os.system(sys_cmd_run_code)
