def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return total / 3

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

def display_results(students):
    print("\n--- STUDENT RESULTS ---")

    for s in students:
        print("\nName:", s["name"])
        print("Total:", s["total"])
        print("Percentage:", round(s["percentage"], 2), "%")
        print("Grade:", s["grade"])

def display_toppers(students):
    highest = 0

    for s in students:
        if s["percentage"] > highest:
            highest = s["percentage"]

    print("\n--- TOPPER ---")

    for s in students:
        if s["percentage"] == highest:
            print(s["name"], "-", highest, "%")


def display_rank_list(students):
    # Simple sorting using loops
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[j]["percentage"] > students[i]["percentage"]:
                students[i], students[j] = students[j], students[i]

    print("\n--- RANK LIST ---")
    rank = 1
    for s in students:
        print(rank, s["name"], "-", round(s["percentage"], 2), "%")
        rank += 1


# Main Program

students = []

try:
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("\nEnter student name: ")

        marks = []

        for j in range(3):
            mark = float(input("Enter subject mark: "))

            if mark < 0 or mark > 100:
                raise ValueError("Invalid marks! Enter between 0 and 100.")

            marks.append(mark)

        total = calculate_total(marks)
        percentage = calculate_percentage(total)
        grade = calculate_grade(percentage)

        students.append({
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        })

    if students:
        display_results(students)
        display_toppers(students)
        display_rank_list(students)
    else:
        print("No student data available!")

except ValueError as e:
    print("Error:", e)
