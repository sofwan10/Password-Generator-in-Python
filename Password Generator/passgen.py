import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"      # put all alphabet characters to ensure user can obtain any random password with all characters
p = "".join(random.sample(s,passlen ))
print(p)