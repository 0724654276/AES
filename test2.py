from email import message
from Crypto.Cipher import AES
import hashlib

password = "mypassword".encode()
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = "This is an IV456"


def pad_message(message):
    while len(message)%16 != 0:
        message = message + "}"
    return message



cipher = AES.new(key,mode,IV)

#decrypted_text = cipher.decrypt(encrypted_message)

message = "this is my super secret"
padded_message = pad_message(message)

encrypted_message = cipher.encrypt(padded_message)


print(padded_message)

print(encrypted_message)



decrypted_text = cipher.decrypt(encrypted_message)
print(decrypted_text.rstrip().decode())