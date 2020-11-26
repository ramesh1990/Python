"""
Password validation
In this program, we will be taking a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
"""
import re

def passwordValidation(str):
    flag = 1
    if ( len(str) < 8 ):
        flag = -1
        print ("Password is smaller")
    elif not ( re.search('[A-Z]',str) ):
        flag = -1
        print ("Password doesn't contain Capital")
    elif not ( re.search('[a-z]',str) ):
        flag = -1
        print ("Password doesn't contain samll")
    elif not ( re.search('[0-9]',str) ):
        flag = -1 
        print ("Password doesn't contain number")
    elif not( re.search('[@,#,$,%,&,*]',str) ):
        print (" Password doesn't contain special character")
    else :
        print ("Valid password ")
        
passwordValidation("Ramesh1991@jkpm")