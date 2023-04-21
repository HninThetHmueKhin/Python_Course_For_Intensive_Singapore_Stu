import secrets
import string

OTP = ""
digit = string.digits
for i in range(8):
    OTP += ("".join(secrets.choice(digit) ))
print(OTP)