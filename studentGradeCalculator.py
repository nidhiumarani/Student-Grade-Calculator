# STUDENT GRADE CALCULATOR
# Create an empty dictonary
student_data = {}

def add_students():
    active = True
    while active:
        name = input("Enter student name: ")
        marks = float(input(f"Enter student marks for {name}: "))
        student_data[name] = marks
        add_more = input("Would you like to add more student data (Yes/No): ")
        if(add_more.lower() == "no"):
            active = False

def get_grades(marks):
    if(marks >= 90):
        return "A"
    elif(marks >= 80):
        return "B"
    elif(marks >= 70):
        return "C"
    elif(marks >= 60):
        return "D"
    else:
        return "F"
    
def view_all_students():
    for name, marks in student_data.items():
        grade = get_grades(marks)
        print(f"name - {name}, Marks - {marks}, Grade - {grade}")

def save_to_file():
    with open("Student.txt", "w") as file:
        for name, marks in student_data.items():
            grade = get_grades(marks)
            file.write(f"{name} | {marks} | {grade}\n")
    
# Add a menu
print("------STUDENT GRADE CALCULATION SYSTEM------")
while True:
    print("1. Add Students\n 2. View all students\n 3. Exit")
    choice = input("Please choose an option: ")
    if choice == '1':
        add_students()
    elif choice == '2': 
        view_all_students()
    elif choice == '3':
        save_to_file()
        print("Data has been stored to file.. ")
        print("Goodbye")
        break
    else: 
        print("Invalid choice.. Please choose correct options")