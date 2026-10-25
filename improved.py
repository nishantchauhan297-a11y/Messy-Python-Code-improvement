"""Student marks report: average, best mark and grade for each student."""

STUDENT_MARKS = {
    "amit": [88, 92, 79],
    "riya": [45, 60, 52],
    "sam": [70, 81, 77],
}


def calculate_average(marks):
    """Return the average of a list of marks."""
    if not marks:
        raise ValueError("marks list cannot be empty")
    return sum(marks) / len(marks)


def find_highest(marks):
    """Return the highest mark in the list."""
    return max(marks)


def get_grade(average):
    """Convert an average mark into a letter grade."""
    if average >= 90:
        return "A"
    if average >= 75:
        return "B"
    if average >= 50:
        return "C"
    return "F"


def print_report(student_marks):
    """Print one summary line per student."""
    for name, marks in student_marks.items():
        average = calculate_average(marks)
        best = find_highest(marks)
        grade = get_grade(average)
        print(f"{name} avg:{round(average, 2)} best:{best} grade:{grade}")


if __name__ == "__main__":
    print_report(STUDENT_MARKS)
