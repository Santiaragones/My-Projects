import re

password=input('Introduce your password: ')

flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        print('You need more characters.')
        break
    elif not re.search("[a-z]", password):
        flag = -1
        print('You need at least one minúscula.')
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        print('You need at least one capital letter.')
        break
    elif not re.search("[0-9]", password):
        flag = -1
        print('You need at least one number.')
        break
    elif not re.search("[_@$]", password):
        flag = -1
        print('You need at least one symbol.')
        break
    #elif re.search("\s", password):
     #   flag = -1
      #  break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag ==-1:
    print("Not a Valid Password")


