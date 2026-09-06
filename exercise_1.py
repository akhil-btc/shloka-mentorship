import csv

#read the marks.csv file and return as a list
def read_file():
    marks = []
    with open("marks.csv", "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            marks.append(row)
    return marks

#calculate the avg score for each student
def calculate_average(marks):
    students = {}

    for row in marks:
        name = row["Name"].strip()
        score = int(row["Score"].strip())
        if name not in students:
            students[name] = []
        students[name].append(score)

    for name in students:
        students[name] = sum(students[name]) / len(students[name])
    return students

#calculate the avg score for each subject
def get_average(marks):
    subjects = {}

    for row in marks:
        subject = row["Subject"]
        score = int(row["Score"])
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(score)

    for subject in subjects:
        subjects[subject] = sum(subjects[subject]) / len(subjects[subject])
    return subjects

#calculate the avg score across all marks
def get_overall_avg(marks):
    scores = []

    for row in marks:
        scores.append(int(row["Score"]))
    return sum(scores) / len(scores)

#this just prints the summary of the marks
def print_summary(marks):
    student_averages = calculate_average(marks)
    subject_averages = get_average(marks)
    overall_average = get_overall_avg(marks)

    print("Marks Summary:")
    print("__________________________")

    print("Overall average:", overall_average)

    print("\nStudent averages:")
    for name in student_averages:
        print(name, ":", student_averages[name])

    print("\nSubject averages:")
    for subject in subject_averages:
        print(subject, ":", subject_averages[subject])

#reads the file and prints the summary
def main():
    marks = read_file()
    print_summary(marks)

main()
