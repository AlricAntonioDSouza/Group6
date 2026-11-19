#Project - Python program to check the grades of 30 students based on their mark.

def grade(mark):
    if mark >= 85:
        return "Passed with Distinction"
    elif mark >= 40:
        return "Passed"
    else:
        return "Failed"

for i in range(1,31):
    mark = int(input("Enter the student's mark: "))
    verdict = grade(mark)
    print("Student", i, "has", verdict)