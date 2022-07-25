import os

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(f"List of scores you entered: {student_scores}")

highscore = 0
for score in student_scores:
    if score > highscore:
        highscore = score
    else:
        continue

print(f"The highest score in the class is: {highscore}")
os.system('pause')

