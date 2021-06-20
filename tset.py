
# def test(grade):
#     return {
#         1: 'This is A',
#         2: 'This is B',
#         3: 'This is C',
#         4: 'This is D',
#         5: 'This is F',
#     }.get(grade, f'{grade} is not a grade!') 

# print(test(3))

import os
import time
from termcolor import colored


# style1 = colored.fg("red") + colored.attr("bold")
# style2= colored.fg("green") + colored.attr("underlined")
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
    print(colored(f"{name} :","blue"),colored(f" {time.ctime(date)}","red"))