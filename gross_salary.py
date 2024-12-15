basic_salary=int(input("Enter the basic salary:"))

if(basic_salary<10000):
      HRA=(basic_salary*67)/100
      DA=(basic_salary*73)/100

elif ( basic_salary< 20000):
      HRA = (basic_salary * 69) / 100
      DA = (basic_salary * 76) / 100
else:
      HRA = (basic_salary * 73) / 100
      DA = (basic_salary * 89) / 100
GS=HRA+DA+basic_salary
print(f"the gross salary is :{GS}")