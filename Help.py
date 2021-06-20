import art
import os
from UtilityFunctions import Select
from UtilityFunctions import OS_Name
os.system('CLS')
Title_big="ADMIN"
Title_small="Assistant"
print(art.text2art(Title_big,font='block',chr_ignore=True))
print(art.text2art(Title_small))
OS_Name()
with open ("Guide.txt","r") as guide:
    print(guide.read())
    while 1==1:
        user_select=int(input("Enter Your Choose: "))
        Select(user_select)

