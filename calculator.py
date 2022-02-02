
class Calculator:
   def multiply(self, x, y):
       return x * y

   def division(self, x, y):
       return x / y

   def subtraction(self, x, y):
       return x - y

   def adding(self, x, y):
       return x + y

import requests

latitude = '55'
longitude = '37'
res = requests.get( "http://api.open-notify.org/iss-pass.json?lat="+latitude+"&lon="+longitude)
print(res.text)