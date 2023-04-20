import secrets
print('Printing integer numbers using secrets module')
byte_value =secrets.token_bytes(2)
print(byte_value,type(byte_value))#bytes
#ထည့်လိုက်တဲ့ byteပေါ်မှာမူတည်ပြီးတော့ format မကျတဲ့string တွေထွက်လာတယ်။
hex_value = secrets.token_hex(16)
#1 bytes change to two hex digits
#2 bytes ထည့်ပေးလိုက် ရင် ၄လုံးထွက်လာရမယ်။ 
print(hex_value,type(hex_value))#str
