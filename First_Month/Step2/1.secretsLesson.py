#3.6 မှစတင်ပါဝင်
#Cryptographically strong Pseudo_random number generator
#random
#security နဲ့ပတ်သတ်တဲ့ sensitive ဖြစ်ရမည့် အခြေအနေမျိုးမှာ အသုံးပြုတယ်။
#token တွေ OTP message တွေ gmail ကို reset ချမယ်ဆိုရင် gmail ကိုလွယ်လွယ်ကူကူ နဲ့ဝင်လို့မရအောင် token တွေနဲ့ခံထားတဲ့ နေရာတွေမှာသုံးတယ်။
import secrets
print('Printing integer numbers using secrets module')
secureNumber = secrets.SystemRandom()
numberList = [1,2,3,4,5,6,7,8,9,77]
# randomNumber = secureNumber.sample(numberList,4)
# randomNumber = secureNumber.randint(0,10)
randomNumber = secureNumber.randrange(0,20,4)
print('Secure Random Number: ',randomNumber)
#Flask---> web framework
#Flutter