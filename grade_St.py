import streamlit as st
st.title("Grade of students")
project_score=st.number_input("Enter the project score: " ,min_value=0,step=1)
external_score=st.number_input("Enter the external score:",min_value=0,step=1)
internal_score=st.number_input("Enter the internal score:",min_value=0,step=1)

if st.button("score "):
   project_score_per = (project_score * 70) / 100
   internal_score_per = (internal_score * 10) / 100
   external_score_per = (external_score * 20) / 100
   if project_score >= 50 and internal_score >= 50 and external_score >= 50:

       total_marks = project_score_per + internal_score_per + external_score_per


       if total_marks >= 90:
           st.write("The student scored A grade")
       elif total_marks >= 80:
           st.write("The student scored B grade")
       else:
           st.write("The student scored C grade")


       st.write(f"Total Marks: {total_marks:.2f}")
   else:

       if project_score < 50:
           st.write(f"The student failed in project: {project_score}")
       if internal_score < 50:
           st.write(f"The student failed in internal: {internal_score}")
       if external_score < 50:
           st.write(f"The student failed in external: {external_score}")

       if project_score < 50 and internal_score < 50 and external_score < 50:
            st.write("The student has failed in all subjects")
else:
   st.write("Click the button to know the score")