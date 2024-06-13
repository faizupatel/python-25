#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Faizan
#
# Created:     12/06/2024
# Copyright:   (c) Faizan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
