def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subjects):
    return total / subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_results(students):
    print("\n--- STUDENT RESULTS ---")

    for name in students:
        total = calculate_total(students[name])
        percentage = calculate_percentage(total, len(students[name]))
        grade = calculate_grade(percentage)

        print("\nName:", name)
        print("Total:", total)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)


def find_topper(students):
    topper = ""
    highest = -1

    for name in students:
        total = calculate_total(students[name])

        if total > highest:
            highest = total
            topper = name

    print("\nTopper:", topper)
    print("Total Marks:", highest)


def display_rank_list(students):
    names = list(students.keys())

    # Sort students based on total marks
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if calculate_total(students[names[j]]) > calculate_total(students[names[i]]):
                names[i], names[j] = names[j], names[i]

    print("\n--- RANK LIST ---")

    rank = 1
    for name in names:
        print(rank, name, "-", calculate_total(students[name]))
        rank += 1


# Main Program

students = {}

try:
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be positive.")

    for i in range(n):
        name = input("\nEnter student name: ").strip()

        if name == "" or name in students:
            raise ValueError("Missing or duplicate student name.")

        subjects = int(input("Enter number of subjects: "))

        if subjects <= 0:
            raise ValueError("Number of subjects must be positive.")

        marks = []

        for j in range(subjects):
            mark = float(input("Enter mark: "))

            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            marks.append(mark)

        students[name] = marks

    if len(students) == 0:
        print("No student data available.")
    else:
        display_results(students)
        find_topper(students)
        display_rank_list(students)

except ValueError as e:
    print("Error:", e)

except KeyboardInterrupt:
    print("\nProgram stopped.")
