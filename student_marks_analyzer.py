import numpy as np
marks = np.array([
    [85, 78, 92, 88],
    [72, 69, 75, 80],
    [90, 88, 94, 86],
    [60, 65, 70, 68],
    [88, 92, 85, 91]
])

student = ["Alice", "Bob","Charlie", "David","Eva"]
subject = ["Math", "Physics", "Chemistry", "English"]

# Basic Analysis

# Average marks of  each student
avg_per_student = np.mean(marks, axis=1)
print("Average marks per student:")
for name, avg in zip(student, avg_per_student):
    print(f"{name}:{avg:.2f}")

# Average marks in each subject  
avg_per_subject = np.mean(marks, axis=0)
print("\n Average marks per subject")
for sub, avg in zip(subject, avg_per_subject):
    print(f"{sub}: {avg: 2f}")  

# Total marks per student
total_marks = np.sum(marks, axis=1)
print("\n Total marks per student:")
for name,total in zip(student,total_marks):
    print(f"{name}:{total}")    

# Highest scorer
topper_index = np.argmax(total_marks)
print(f"\n Highest Scorer: {student[topper_index]} ({total_marks[topper_index]} marks)")

# Subject with best class performance
best_subject_index = np.argmax(avg_per_subject)
print(f" Best SubjectOverall: {subject[best_subject_index]}")