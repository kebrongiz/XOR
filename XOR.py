#29) Python program that prompts the user to enter number of students name and score, and finally displays the name of student with the highest scores

def student_max_score():
    student_no = int(input("Enter the number of students: "))

    scores = {}

    for _ in range(student_no):
        print()
        name = input("Enter student name: ")
        score = int(input("Enter student score: "))

        if scores.get(score) is None:
            scores[score] = []

        scores[score].append(name)
    sorted_scores = sorted(scores)
    sorted_scores.reverse()
    max_score = sorted_scores[0]
    max_socre_students = ", ".join(scores.get(max_score))

    print("The student(s) with the highest score is/are {} with a score of {}".format(
        max_socre_students, max_score))


student_max_score()
