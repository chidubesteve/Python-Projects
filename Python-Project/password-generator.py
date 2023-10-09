import string
import secrets

l = string.ascii_letters
d = string.digits
sp = string.punctuation

passwordPossibleDigits = l + d + sp
# print(passwordPossibleDigits) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

password_length = 16
temp = ''

for password in range(password_length):
    temp += secrets.choice(passwordPossibleDigits)
print(temp) # can also use the .join()  method
    

