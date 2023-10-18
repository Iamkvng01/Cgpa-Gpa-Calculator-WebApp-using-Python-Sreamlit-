# Streamlit lets you turn data scripts into shareable web apps in minutes,
import streamlit as st
# Remove unused variables
creditUnit = []
weighted_gp = []


# Initialize count
count = 0

def calculateGpa():
    global count  # Define count as global
    gradingSystem = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    courses = st.number_input("Enter total number of courses taken: ", min_value=1, step=1, key=f"courses_{count}")
    
    for i in range(courses):
        count += 1  # Increment count within the loop
        value = st.text_input(f'Enter Grade of course {i+1}:', key=f"value_{count}_{i + 1}").upper()
        sc = gradingSystem.get(value, 1)  # Use get() to handle invalid grades
        
        if sc == -1:
            st.write('Invalid grade given')
        
        
        credit = st.number_input(f'Enter credit unit of course {i+1}:', min_value=1, step=1, key=f"credit_{count}_{i + 1}")
        creditUnit.append(credit)
        weighted_gp.append(sc * credit)
    
    total_weighted_gp = sum(weighted_gp)
    total_credit_units = sum(creditUnit)

   
    return (total_weighted_gp / total_credit_units)
   
    

def calculateCgpa():
    global count  # Define count as global
    sem = st.number_input("How many semesters have you done?: ", min_value=1, step=1, key=f"sem_{count}")
    
    if not isinstance(sem, int):
        st.write('Invalid input for the number of semesters.')
        return
    
    cgpa_calc = []
    
    for j in range(sem):
        st.write("Information for semester {}".format(j + 1))
        cgpa = calculateGpa()
        cgpa_calc.append(cgpa)
    
    return (sum(cgpa_calc) / sem)

st.title('Welcome to our CGPA and GPA calculator\n')    
choice = st.number_input('Enter 1 for GPA and 2 for CGPA calculator: ', min_value=1, step=1,)
if choice == 1:
    count += 1  # Increment count when calculating GPA
    st.write(f'Your current GP is:  {calculateGpa()}')
elif choice == 2:
    count += 1  # Increment count when calculating CGPA
    st.write(f'Your current CGPA is:  {calculateCgpa():.2f}')
else:
    st.write('Invalid Input given')
    