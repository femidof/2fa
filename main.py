import time
import pyotp
import qrcode

key=pyotp.random_base32() # Key for generating the OTP
# key="MyRANDOMkey12333"

#To generate a qr

uri = pyotp.totp.TOTP(key).provisioning_uri(name="User123", issuer_name="My App")
print(uri)

qrcode.make(uri).save("totp.png")

totp=pyotp.TOTP(key)

# time.sleep(30)

print(totp.now())

# for vverifying 

input_code=input("ENter 2FA code:")

verify=totp.verify(input_code)

print(verify)

# For HOTP


hotp=pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))

for _ in range(2):
	print(hotp.verify(input("Enter Code:"), counter))
	counter+=1



