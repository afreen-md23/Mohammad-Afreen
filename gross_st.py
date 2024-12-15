import streamlit as st


st.title("Gross Salary Calculator")


basic_salary = st.number_input("Enter your basic salary:", min_value=0, step=1)


if st.button("Calculate gross salary"):
   HRA = 0
   DA = 0

   if basic_salary < 10000:
       HRA = (basic_salary * 67) / 100
       DA = (basic_salary * 73) / 100
   elif basic_salary < 20000:
       HRA = (basic_salary * 69) / 100
       DA = (basic_salary * 76) / 100
   else:
       HRA = (basic_salary * 73) / 100
       DA = (basic_salary * 89) / 100


   GS = HRA + DA + basic_salary


   st.write(f"Your Gross Salary is: ₹{GS}")
else:
   st.write("Click the button to calculate your gross salary.")
