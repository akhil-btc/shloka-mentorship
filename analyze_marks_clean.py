import csv
# from math import math


SUBJECTS = ["math", "science", "english", "history", "art"]


def load_marks(file_path):
    """Load the CSV as a list of dict rows."""
    with open(file_path, "r", newline="") as f:
        return list(csv.DictReader(f))


def subject_averages(rows):
    """Compute the average per subject across all students.

    Returns a dict of {subject: average}.
    """
    averages = {}
    for subject in SUBJECTS:
        total = sum(int(row[subject]) for row in rows)
        averages[subject] = round(total / len(rows), 2)
    return averages


def total_marks(row):
    """Sum all subject marks for one student row."""
    return sum(int(row[s]) for s in SUBJECTS)


def top_student(rows):
    """Find the student with the highest total marks.

    Returns a (name, total) tuple.
    """
    best = max(rows, key=total_marks)
    return best["name"], total_marks(best)


def print_summary(rows):
    """Print a clean summary of the marks."""
    print(f"Total students: {len(rows)}")
    print()

    print("Subject averages:")
    for subject, avg in subject_averages(rows).items():
        print(f"  {subject.capitalize():<10} {avg}")
    print()

    name, total = top_student(rows)
    print(f"Top student: {name} with {total} marks")


def main():
    """Entry point. Load marks.csv and print the summary."""
    rows = load_marks("marks_missing.csv")
    print_summary(rows)


if __name__ == "__main__":
    main()
