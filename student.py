class Student:
    """Store one student's name and subject marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, value):
        """Add a mark, or store None if it is invalid."""
        try:
            mark = int(value)
        except (ValueError, TypeError):
            mark = None

        self.marks[subject] = mark
        return mark

    def total(self):
        """Add up the valid marks."""
        total = 0

        for mark in self.marks.values():
            if mark is not None:
                total = total + mark

        return total

    def average(self):
        """Find the average of valid marks, or return None if there are none."""
        count = 0

        for mark in self.marks.values():
            if mark is not None:
                count = count + 1

        if count == 0:
            return None

        return round(self.total() / count, 2)

    def best_subject(self):
        """Return the subject with the highest valid mark."""
        best = None

        for subject, mark in self.marks.items():
            if mark is not None:
                if best is None or mark > self.marks[best]:
                    best = subject

        return best

    def __str__(self):
        return f"{self.name}: {self.total()} total marks"
