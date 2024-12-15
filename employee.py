employee_salary=int(input())
bills=int(input())
count=1
sum=0
while count <= bills:
   bill=int(input())
   print(bill)
   sum=sum+bill
   count=count+1
print(sum)
perc=((sum/100)*employee_salary)
print(perc)