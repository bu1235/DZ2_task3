subject_dict = {}
while True:
    line = input("Введите предмет Фамилию и оценку: ")
    if len(line) == 0:
        break
    subject, student, grade = line.split()
    if subject not in subject_dict:
        subject_dict[subject] = {student: [grade]}
        print("Subject not in dict, added: ", subject_dict)
    else:
        if student not in subject_dict[subject]:
            subject_dict[subject][student] = [grade]
            print("Student not in dict, added: ", subject_dict)
        else:
            subject_dict[subject][student].append(grade)
            print("Student in dict, added grade: ", subject_dict)

print("Final dict:")
print(subject_dict)

print("Итог:")
for subject in subject_dict:
    print(subject)
    for student,grade in subject_dict[subject].items():
        print (student,":", ''.join(grade))