grade = int(input("Enter your score for grade: "))
user_input = grade
if 70 <= grade <= 100:
    print("Your grade is 'A'")
elif 60 <= grade < 70:
    print("Your grade is 'B'")
elif 50 <= grade < 60:
    print("Your grade is 'C'")
elif 45 <= grade < 50:
    print("Your grade is 'D'")
elif 40 <= grade < 45:
    print("Your grade is 'E'")
elif grade < 40:
    print("Your grade is 'F'")
