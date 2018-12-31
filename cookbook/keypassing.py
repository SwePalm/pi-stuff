#!/usr/bin/python3
#keypassing.py
import encryptdecrypt as ENC

KEY1 = 20
KEY2 = 50

print ("Please enter text to scramble:")
user_input = input()
encodedKEY1 = ENC.encryptText(user_input,KEY1)
print ("USER1: Send message encrypted with KEY1 (KEY1): " + encodedKEY1)
encodedKEY1KEY2 = ENC.encryptText(encodedKEY1,KEY2)
print ("USER2: Encrypt with KEY2 & returns it (KEY1+KEY2): " + encodedKEY1KEY2)
encodedKEY2 = ENC.encryptText(encodedKEY1KEY2,-KEY1)
print ("USER1: Removes KEY1 & returns with just KEY2 (KEY2): " + encodedKEY2)
message_result = ENC.encryptText(encodedKEY2,-KEY2)
print ("USER2: Removes KEY2 & Message received: " + message_result)

