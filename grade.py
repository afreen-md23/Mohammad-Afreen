no_of_students = int(input())
count = 1


while count <= no_of_students:

   project_score = int(input("Enter project score: "))
   internal_score = int(input("Enter internal score: "))
   external_score = int(input("Enter external score: "))


   project_score_per = (project_score * 70) / 100
   internal_score_per = (internal_score * 10) / 100
   external_score_per = (external_score * 20) / 100


   if project_score >= 50 and internal_score >= 50 and external_score >= 50:

       total_marks = project_score_per + internal_score_per + external_score_per


       if total_marks >= 90:
           print("The student scored A grade")
       elif total_marks >= 80:
           print("The student scored B grade")
       else:
           print("The student scored C grade")


       print(f"Total Marks: {total_marks:.2f}")
   else:

       if project_score < 50:
           print(f"The student failed in project: {project_score}")
       if internal_score < 50:
           print(f"The student failed in internal: {internal_score}")
       if external_score < 50:
           print(f"The student failed in external: {external_score}")

       if project_score < 50 and internal_score < 50 and external_score < 50:
           print("The student has failed in all subjects")


   count =count+ 1