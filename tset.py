
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
<<<<<<< HEAD
# import ctypes
# import os

# kernel32 = ctypes.WinDLL('kernel32')

# SEM_FAILCRITICALERRORS = 1
# SEM_NOOPENFILEERRORBOX = 0x8000
# SEM_FAIL = SEM_NOOPENFILEERRORBOX | SEM_FAILCRITICALERRORS

# def FETCH_USBPATH():
#     usb_List=[]
#     oldmode = ctypes.c_uint()
#     kernel32.SetThreadErrorMode(SEM_FAIL, ctypes.byref(oldmode))
#     try:
#         for USBPATH in ascii_uppercase:
#             if os.path.exists('%s:\\File.ID' % USBPATH):
#                 USBPATH = '%s:\\' % USBPATH
#                 print('USB is mounted to:', USBPATH)
#                 usb_List.append(USBPATH) 
#         return usb_List
#     finally:
#         kernel32.SetThreadErrorMode(oldmode, ctypes.byref(oldmode))

# USBdrive = FETCH_USBPATH()
# while USBdrive == "":
#     print('Please plug in our USB drive and '
#           'press any key to continue...', end="")
#     input()
#     USBdrive = FETCH_USBPATH()



    ##################################################################################################################


    
=======
##########################################################################################################################################################################
##########################################################################################################################################################################

# mydate=datetime.datetime.strptime('Mon Jun 21 07:58:26 2021', '%a %b %d %H:%M:%S %Y')
# print(mydate.timestamp())
# dt = datetime.datetime.fromtimestamp(mydate.timestamp())
# dt.strftime('%d-%B-%Y')
# print(dt)


############################################
# def custom(*args):
#     print(args)
#     print(type(args))

# custom(input())
# def custom__(**args):
#     print(args)
#     print(type(args))

# custom__(a=1,reza=2,sahih=4,d="34434")
###############################################

           
>>>>>>> e8cf66a0655f60c21a805a8cd000407315f5d66f
