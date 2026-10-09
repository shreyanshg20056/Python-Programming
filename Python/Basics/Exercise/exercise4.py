import time

time1 = time.strftime('%H,%M,%S')
if time1 > ('06,00,00') and time1 < ('12,00,00'):
  print("Good Morning")
elif time1>("12,00,00") and time1< ('18,00,00'):
  print("Good Afternoon")
elif time1>("18,00,00") and time1< ('21,00,00'):
  print("Good Evening")
else:
  print("Good Night")
