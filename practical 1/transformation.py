from datetime import date
#write your code here...
date_str1 = input().strip()
date_str2 = input().strip()
d1 = date(*map(int,date_str1.split("-")))
d2 = date(*map(int,date_str2.split("-")))
delta = d2-d1
print(delta.days)