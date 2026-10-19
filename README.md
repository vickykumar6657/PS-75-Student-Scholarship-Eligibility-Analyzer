# Student Scholarship Eligibility Analyzer

## Project Details
- Project Number: 75
- Language: Python 3
- Library: Pandas

## Problem Statement
This project analyzes student data using marks, family income, and attendance to determine scholarship eligibility.

## Eligibility Rules
- Attendance must be at least 75%.
- Marks must be at least 75%.
- Annual income must not exceed Rs. 500000.
- Full Scholarship: Rs. 50000 if marks are at least 90 and income is at most Rs. 300000.
- Partial Scholarship: Rs. 25000 for other eligible students.

## Features
1. Check scholarship eligibility.
2. Display scholarship summary.
3. Filter students by minimum marks.
4. Skip invalid student records.
5. Calculate total scholarship and average eligible marks.

## Files
- scholarship_analyzer.py: Main Python program.
- students.csv: Student dataset.
- README.md: Project documentation.

## How to Run
1. Install Python 3.
2. Install Pandas using `python -m pip install pandas`.
3. Open the terminal in the project folder.
4. Run `python scholarship_analyzer.py`.

## Test Data
The project includes student names, marks, annual income, and attendance.


## Expected Output

The program displays:

* Each student's scholarship eligibility status.
* Full or partial scholarship amount.
* Total eligible students and scholarship amount.
* Average marks of eligible students.
* Students matching the minimum marks entered by the user.
* A message when invalid student data is skipped.

## Input Validation

The program handles invalid marks or other student data and rejects non-numeric minimum marks input.

## Conclusion

The Student Scholarship Eligibility Analyzer helps identify eligible students and calculate scholarship amounts using marks, annual income, and attendance.
