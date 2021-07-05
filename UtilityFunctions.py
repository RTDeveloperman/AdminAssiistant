#!/usr/bin/env python

import psutil
import os
import re
import socket    
import subprocess
import threading, time
import platform
from termcolor import colored
import ctypes
from string import ascii_uppercase
import datetime
from persiantools.jdatetime import JalaliDate
from ldap3 import Server, Connection, SAFE_SYNC

####################################################################################################################################################################
def cpu_usage():
    """ Show CPU Usage"""
    # gives a single float value
    print('The CPU usage is: ', psutil.cpu_percent(interval=4))
####################################################################################################################################################################
def memory_usage():
    # you can have the percentage of used RAM
    print('The MEMORY(RAM) usage is: ',psutil.virtual_memory().percent)

####################################################################################################################################################################
# you can calculate percentage of available memory
def  available_memory():
    print("Your available memory(RAM) is :",psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
####################################################################################################################################################################

def hostname_IP():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("Your Computer Name is:" + hostname)    
    print("Your Computer IP Address is:" + IPAddr) 
####################################################################################################################################################################
def wlan_ip():
    
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i: scan=1
        if scan:
            if 'ipv4' in i: print( "Your WIFI IP Address is: "+i.split(':')[1].strip())
####################################################################################################################################################################
# wlan_ip()
# hostname_IP()
# available_memory()
# memory_usage()
# cpu_usage()

####################################################################################################################################################################
def getAppRun(Process_name="firefox.exe"):
    processes = list(p.name() for p in psutil.process_iter())
    count = processes.count(Process_name)
    if count == 0:
        print('Process Not Run')
    else:
        print('Process is already running!')

def getAppRun_contractor():
    getAppRun(input("Enter Your Process Name (Like 'firefox.exe') : "))
####################################################################################################################################################################
def getAppRun_PID(mPID):
    try:
        process = psutil.Process(mPID)
        process_name = process.name()
        getAppRun(process_name)
    except Exception as e:
         print('Process Not Run')
def getAppRun_PID_contractor():
    getAppRun_PID(input("Enter PID process : "))
####################################################################################################################################################################
def ProcessPID(proccess_name):
        for pid in (process.pid for process in psutil.process_iter() if proccess_name in process.name()):
            print(proccess_name+" : "+str(pid))
def ProcessPID_contractor():
    ProcessPID(input("Enter Process Name: "))
####################################################################################################################################################################
def SerchProccessPID(proccess_name):
    processes=(list(p.name() for p in psutil.process_iter()))
    list_app_same_name=[]
    #any(proccess_name in process for process in processes)
    #process= any(proccess_name in process for process in processes)
    for process in processes:
        if proccess_name in process:
            if process not in list_app_same_name:
                ProcessPID(process)
                list_app_same_name.append(process)
def SerchProccessPID_contractor():
    SerchProccessPID(input("Enter Process Name : "))
####################################################################################################################################################################

def CloseApp(name):
    for pid in (process.pid for process in psutil.process_iter() if name in process.name()):
          #for pid in (process.pid for process in psutil.process_iter() if  process.name()==name):
       # os.kill(pid,9)
        subprocess.call(['taskkill', '/F', '/T', '/PID',  str(pid)])
def CloseApp_contractor():
    CloseApp(input("Enter Process Name for Close: "))
####################################################################################################################################################################

def OpenApp(dir,exe_name):
    os.chdir(dir)
    subprocess.Popen(exe_name)
####################################################################################################################################################################

def OpenClose_CloseOpen(exe_name,address="C:\\Program Files\\Mozilla Firefox"):
    processes = list(p.name() for p in psutil.process_iter())
    count = processes.count(exe_name)
    if count == 0:
        OpenApp(address,exe_name)
    else:
        CloseApp(exe_name)
#def OpenClose_CloseOpen_contractor():
   # OpenClose_CloseOpen(input("Enter EXE Address for open app"))
####################################################################################################################################################################



def AlwaysCheck_AppIsRUN(AppName):
#thread = threading.Thread(target=AlwaysCheck("firefox.exe"), daemon=True)
#thread.start()

    while 2>1:
        processes = list(p.name() for p in psutil.process_iter())
        #print(processes)
        count = processes.count(AppName)
        #print(count)
        if count == 0:
            #logging.info('Application started')
            print('Process Not Run')
        else:
            #logging.info('Process is already running!')
            print('Process is already running!')
        print(time.ctime())
        time.sleep(5)
        #sys.exit(0) 
####################################################################################################################################################################
def OS_Name():
    os_details=platform.uname()
    os_name=os_details[0]
    os_Version=os_details[2]
    os_BuildNumber=os_details[3]
    print(colored(f"{os_name} {os_Version} ({os_BuildNumber}) \n","green"))
####################################################################################################################################################################
def User_Folder_Details():
    user_path=r"C:\Users"
    details_list=[]
    dir_list=os.listdir(user_path)
    for folder in dir_list:
        try:
            folder_path=os.path.join(user_path,folder)
            #date_mod=time.ctime(os.path.getmtime(folder_path))
            date_mod=os.path.getmtime(folder_path)
            details_list.append((folder,date_mod))
            
        
        except Exception:
            date_mod=0
            print("ERROR")
        #print(colored(f"{folder} :","blue"),colored(f" {date_mod}","red"))
    sorted_details_list=sorted(details_list,key= lambda x:x[1])
    for name,date in sorted_details_list[::-1]:
        print(colored(f"{name} :","yellow"),colored(f" {time.ctime(date)}","red"))
####################################################################################################################################################################
def CheckUSBDriveIsExist():
    kernel32 = ctypes.WinDLL('kernel32')
    SEM_FAILCRITICALERRORS = 1
    SEM_NOOPENFILEERRORBOX = 0x8000
    SEM_FAIL = SEM_NOOPENFILEERRORBOX | SEM_FAILCRITICALERRORS

    def FETCH_USBPATH():
        usb_List=[]
        oldmode = ctypes.c_uint()
        kernel32.SetThreadErrorMode(SEM_FAIL, ctypes.byref(oldmode))
        try:
            for USBPATH in ascii_uppercase:
                if os.path.exists('%s:\\File.ID' % USBPATH):
                    USBPATH = '%s:\\' % USBPATH
                    print('USB is mounted to:', USBPATH)
                    usb_List.append(USBPATH) 
            return usb_List
        finally:
            kernel32.SetThreadErrorMode(oldmode, ctypes.byref(oldmode))

    USBdrive = FETCH_USBPATH()
    while USBdrive == "":
        print('Please plug in our USB drive and '
            'press any key to continue...', end="")
        input()
        USBdrive = FETCH_USBPATH()
####################################################################################################################################################################
#whichFileChange(f"H:\program files\",5)
def whichFileChange(dir,day):
    ONE_DAY=86400
    today=datetime.datetime.today()
    today_timestamp=datetime.datetime.timestamp(today)
    MuchDay=float(day)*ONE_DAY
    dayForCheck=today_timestamp-MuchDay
    folders=os.listdir(dir)
    try:
        for folder in folders:
            folderpth=os.path.join(dir,folder)
            datemodify=time.ctime(os.path.getmtime(folderpth))
           # print(datemodify)
            datemodify_formater=datetime.datetime.strptime(datemodify, '%a %b %d %H:%M:%S %Y')
            datemodify_time=datemodify_formater.strftime('%H:%M:%S')
            datemodify_timestamp=datemodify_formater.timestamp()
            if datemodify_timestamp >=dayForCheck:
            # print(datemodify_timestamp)
                datemodify_jalali=JalaliDate.fromtimestamp(datemodify_timestamp)
                print(str(folder)+" : "+str(datemodify_jalali)+"  "+str(datemodify_time)+" ENG_Date : "+str(datemodify_formater))
            # print(folderpth+" : "+str(datemodify_formater))
                
            
    except Exception:
        print("ERROR : "+Exception )
def whichFileChange_contractor():
    dir= input("Please Enter Directory Address : ")
    day=input("Please Enter Day for Check File modifed after them or NOT : ")
    whichFileChange(dir,day)
####################################################################################################################################################################
def LDAP_search(paswd,user="guest@internet.com",serv="192.168.0.4",msearch_base='dc=internet,dc=com',msearch_filter='(&(objectCategory=user))'):
    os.system('cls')
    server = Server(serv)
    conn = Connection(server, user, paswd, client_strategy=SAFE_SYNC, auto_bind=True)
    #status, result, response, _ = conn.search('o=test', '(objectclass=*)')  # usually you don't need the original request (4th element of the returned tuple)
    if not conn.bind():
        print('error')
    else:
        print(conn)
        print('##############################################################################')
    entries = conn.search(msearch_base, msearch_filter)
    # for entry in entries:
    #  tet=entry.get('raw_attributes')
    with open('export.txt','w', encoding="utf-8") as export_txt: 
        for entry in entries[2]:
            try:
             just_name=re.findall('CN=(.*?),',str((entry).get('raw_dn')))[0]
             just_OU=re.findall('OU=(.*?),',str((entry).get('raw_dn')))
            #  print(just_name+' ==> '+",".join(just_OU))
            #  print("\n")
             #print(len(just_OU))
             export_txt.write(just_name.encode('latin-1').decode('unicode-escape').encode('latin-1').decode('utf-8')+" ==> "+",".join(just_OU)+'\n')
        
            except Exception:
                 pass
           
####################################################################################################################################################################

def Select(num)  :
   func={
       1:cpu_usage,
       2:memory_usage,
       3:hostname_IP,
       4:wlan_ip,
       5:User_Folder_Details,
       6:getAppRun_contractor,
       7:ProcessPID_contractor,
       8:CloseApp_contractor,
       9:SerchProccessPID_contractor,
       10:CheckUSBDriveIsExist,
       11:whichFileChange_contractor,
      
   }
  
   return func[num]() if num<= len(func) else print("Wront Command")
####################################################################################################################################################################

#OpenClose_CloseOpen("firefox.exe")
#thread = threading.Thread(target=AlwaysCheck("firefox.exe"), daemon=True)
#thread.start()
#SerchProccessPID("Tele")
#getAppRun_PID(101908)
#Select(5)