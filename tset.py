
# def test(grade):
#     return {
#         1: 'This is A',
#         2: 'This is B',
#         3: 'This is C',
#         4: 'This is D',
#         5: 'This is F',
#     }.get(grade, f'{grade} is not a grade!') 

# print(test(3))
##########################################################################################################################################################################
##########################################################################################################################################################################
# from string import ascii_uppercase
# from os import path

# def get_usb_drive():
#     for drive in ascii_uppercase:
#         pth=drive + f":\File.ID"
#         if path.exists(pth):
#             return drive + ":\\"
#     return ("")
# drive = get_usb_drive()
# while drive == "":
#     print('Please plug in our USB drive and press any key to continue...',end="")
#     input()
#     drive = get_usb_drive()
# print(get_usb_drive())
##########################################################################################################################################################################
##########################################################################################################################################################################
import os
import pathlib
import time
import datetime
from persiantools.jdatetime import JalaliDate
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


whichFileChange(f"H:\program files\Warcraft III",150000)
# mydate=datetime.datetime.strptime('Mon Jun 21 07:58:26 2021', '%a %b %d %H:%M:%S %Y')
# print(mydate.timestamp())
# dt = datetime.datetime.fromtimestamp(mydate.timestamp())
# dt.strftime('%d-%B-%Y')
# print(dt)

