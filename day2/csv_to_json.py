"""import csv
from pathlib import Path

input_file = Path(__file__).parent / "students.csv"

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
"""

"""import csv
from pathlib import Path

input_file = Path(__file__).parent / "students.csv"

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]

        python_marks = float(row["python"])
        sql_marks = float(row["sql"])
        communication_marks = float(row["communication"])
        marks = [
            python_marks,
            sql_marks,
            communication_marks
        ]
        average = round(sum(marks) / len(marks), 2)

        print(name, "-> Average:", average)
"""

"""import csv
from pathlib import Path

input_file = Path(__file__).parent / "students.csv"

students = []

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]

        python_marks = float(row["python"])
        sql_marks = float(row["sql"])
        communication_marks = float(row["communication"])

        marks = [
            python_marks,
            sql_marks,
            communication_marks
        ]

        average = round(sum(marks) / len(marks), 2)

        student = {
            "name": name,
            "python": python_marks,
            "sql": sql_marks,
            "communication": communication_marks,
            "average": average
        }

        students.append(student)

for student in students:
    print(student)

class_average = round(
    sum(student["average"] for student in students) / len(students),
    2
)

print("Class average:", class_average)
topper = max(students, key=lambda student: student["average"])

print("Topper:", topper["name"])
print("Topper average:", topper["average"])"""


from pathlib import Path
import csv
import json

# Locate the input and output files
folder = Path(__file__).parent
input_file = folder / "students.csv"
output_file = folder / "summary.json"

students = []

# Read student details from the CSV file
with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        python_marks = float(row["python"])
        sql_marks = float(row["sql"])
        communication_marks = float(row["communication"])

        average = round(
            (python_marks + sql_marks + communication_marks) / 3,
            2
        )

        student = {
            "name": row["name"],
            "python": python_marks,
            "sql": sql_marks,
            "communication": communication_marks,
            "average": average
        }

        students.append(student)

# Calculate the class average and find the topper
class_average = round(
    sum(student["average"] for student in students) / len(students),
    2
)

topper = max(students, key=lambda student: student["average"])

# Prepare the summary data
summary = {
    "total_students": len(students),
    "class_average": class_average,
    "topper": {
        "name": topper["name"],
        "average": topper["average"]
    },
    "students": students
}

# Save the summary in JSON format
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(summary, file, indent=4)

print("Student summary generated successfully!")
print(f"Total students: {len(students)}")
print(f"Class average: {class_average}")
print(f"Topper: {topper['name']} ({topper['average']})")
print(f"Output file: {output_file}")
