import pandas as pd

df = pd.read_csv("students.csv")


def check_eligibility(row):
    name = row["Name"]

    try:
        marks = float(row["Marks (%)"])
        income = float(row["Income (per year)"])
        attendance = float(row["Attendance (%)"])
    except (ValueError, TypeError):
        print(f"Invalid data for {name}: row skipped.")
        return "Invalid", 0

    if pd.isna(marks) or pd.isna(income) or pd.isna(attendance):
        print(f"Missing data for {name}: row skipped.")
        return "Invalid", 0

    if not (0 <= marks <= 100 and 0 <= attendance <= 100 and income >= 0):
        print(f"Invalid values for {name}: row skipped.")
        return "Invalid", 0

    if attendance >= 75 and marks >= 75 and income <= 500000:
        if marks >= 90 and income <= 300000:
            return "Full", 50000
        else:
            return "Partial", 25000

    return "Not Eligible", 0


def show_results():
    for _, row in df.iterrows():
        status, amount = check_eligibility(row)

        if status == "Invalid":
            continue

        if status == "Not Eligible":
            print(f'{row["Name"]} | Not Eligible')
        else:
            print(f'{row["Name"]} | {status} | Rs. {amount}')


def show_summary():
    results = []

    for _, row in df.iterrows():
        status, amount = check_eligibility(row)

        if status != "Invalid":
            results.append((row, status, amount))

    full = sum(1 for _, status, _ in results if status == "Full")
    partial = sum(1 for _, status, _ in results if status == "Partial")
    not_eligible = sum(
        1 for _, status, _ in results if status == "Not Eligible"
    )

    eligible_marks = [
        float(row["Marks (%)"])
        for row, status, _ in results
        if status in ("Full", "Partial")
    ]

    total = sum(amount for _, _, amount in results)
    average = (
        sum(eligible_marks) / len(eligible_marks)
        if eligible_marks else 0
    )

    print(
        f"Eligible: {full + partial} | "
        f"Not Eligible: {not_eligible} | "
        f"Full: {full} | Partial: {partial}"
    )
    print(
        f"Total scholarship: Rs. {total} | "
        f"Average marks (eligible): {average:.2f}"
    )


def filter_by_marks():
    try:
        minimum = float(input("Enter minimum marks: "))
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return

    if not 0 <= minimum <= 100:
        print("Marks must be between 0 and 100.")
        return

    found = False

    for _, row in df.iterrows():
        status, _ = check_eligibility(row)

        if status == "Invalid":
            continue

        marks = float(row["Marks (%)"])

        if marks >= minimum:
            print(f'{row["Name"]} | {marks:g}')
            found = True

    if not found:
        print("No students match the minimum marks.")


while True:
    print("\n--- Student Scholarship Eligibility Analyzer ---")
    print("1. Eligibility results")
    print("2. Scholarship summary")
    print("3. Filter by minimum marks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_results()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        filter_by_marks()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")