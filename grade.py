print("STUDENT GRADE MANAGEMENT SYSTEM")
name = input("Enter student name: ")
math_score = int(input("Enter Mathematics score: "))
english_score = int(input("Enter English score: "))
python_score = int(input("Enter Python score: "))

total_score = math_score + english_score + python_score
print("Total Score:", total_score)

average_score = total_score / 3
print("Average Score:", average_score)

if average_score >= 70:
    grade = "A"
elif average_score >= 60:
    grade = "B"
elif average_score >= 50:
    grade = "C"
elif average_score >= 45:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average_score >= 45:
    result = "Pass"
else:
    result = "Fail"

print("Result:", result)

math_score = int(input("Enter Mathematics score: "))

while math_score < 0 or math_score > 100:
    print("Invalid score! Enter a score between 0 and 100.")
    math_score = int(input("Enter Mathematics score again: "))



english_score = int(input("Enter English score: "))

while english_score < 0 or english_score > 100:
    print("Invalid score! Enter a score between 0 and 100.")
    english_score = int(input("Enter English score again: "))

python_score = int(input("Enter Python score: "))

while python_score < 0 or python_score > 100:
    print("Invalid score! Enter a score between 0 and 100.")
    python_score = int(input("Enter Python score again: "))


