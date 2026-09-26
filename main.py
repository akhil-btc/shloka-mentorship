import csv
from student import Student


SUBJECTS = ["math", "science", "english", "history", "art"]


def load_marks(file_path):
    """Load the CSV as a list of dict rows."""
    with open(file_path, "r", newline="") as f:
        return list(csv.DictReader(f))


def make_students(rows):
    """Turn valid CSV rows into Students and record skipped rows."""
    students = []
    skipped_rows = []

    for row_number, row in enumerate(rows, start=2):
        name = (row.get("name") or "").strip()

        if name == "":
            skipped_rows.append(f"Row {row_number}: missing name")
            continue

        student = Student(name)
        invalid_subjects = []

        for subject in SUBJECTS:
            mark = student.add_mark(subject, row.get(subject))

            if mark is None:
                invalid_subjects.append(subject)

        if len(invalid_subjects) > 0:
            skipped_rows.append(
                f"Row {row_number} ({name}): invalid marks in {', '.join(invalid_subjects)}"
            )
        else:
            students.append(student)

    return students, skipped_rows


def subject_averages(students):
    """Compute the average per subject across valid students."""
    averages = {}

    for subject in SUBJECTS:
        total = 0
        count = 0

        for student in students:
            mark = student.marks.get(subject)

            if mark is not None:
                total = total + mark
                count = count + 1

        if count == 0:
            averages[subject] = None
        else:
            averages[subject] = round(total / count, 2)

    return averages


def top_student(students):
    """Find the Student with the highest total marks."""
    if len(students) == 0:
        return None

    best = students[0]

    for student in students:
        if student.total() > best.total():
            best = student

    return best


def print_summary(students, skipped_rows):
    """Print a clean summary of the marks and skipped rows."""
    print(f"Total students: {len(students)}")
    print(f"Skipped rows: {len(skipped_rows)}")

    for reason in skipped_rows:
        print(f"  {reason}")

    print()
    print("Subject averages:")

    for subject, avg in subject_averages(students).items():
        if avg is None:
            print(f"  {subject.capitalize():<10} no valid marks")
        else:
            print(f"  {subject.capitalize():<10} {avg}")

    print()

    best = top_student(students)

    if best is None:
        print("Top student: none (no valid rows)")
    else:
        print(f"Top student: {best.name} with {best.total()} marks")
        print(f"Best subject: {best.best_subject()}")


def main():
    """Entry point. Load marks_missing.csv and print the summary."""
    rows = load_marks("marks_missing.csv")
    students, skipped_rows = make_students(rows)
    print_summary(students, skipped_rows)


if __name__ == "__main__":
    main()
