import datetime

def sort_by_age (List1):
    return sorted(alist, key=lambda x:x['age'],reverse=True)

year = input(" Please enter the year: ")
month = input(" Please enter the month : ")
day = input("Please enter the date : ")
#targerDay=datetime.date(year,month,day)
#daycount=targerDay - datetime.date (targerDay.year -.1 , 12, 31 )

#print( "%s was %s of in %s day . " %(targerDay,year,daycount.days))

alist = [ { 'name' : 'a' , 'age' : 20 },{ 'name' : 'b' , 'age' : 30 },{ 'name' : 'c' , 'age' : 25 } ]

print(sort_by_age(alist))

List1 = [1,2,3,4,5]
List2 = [5,6,3,4,7]
set1=set(List1)
set2=set(List2)
print(set1 & set2)
print(set1 ^ set2)

print ([x * 11  for x in  range ( 10 )])

l1=['a','b','c','a','c','d']
l2=list(set(l1))
print(sorted(l2))
