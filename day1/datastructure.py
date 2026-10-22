# PROGRAM 1: LISTS
print("\n===== PROGRAM 1: LISTS =====")

fruits = ["apple", "banana", "mango", "orange"]

fruits.append("grapes")
fruits.remove("banana")

print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Number of fruits:", len(fruits))


# PROGRAM 2: TUPLES
print("\n===== PROGRAM 2: TUPLES =====")

student = ("Sowndharya", "CSE", 4)

print("Student details:", student)
print("Name:", student[0])
print("Department:", student[1])
print("Study year:", student[2])


# PROGRAM 3: DICTIONARIES
print("\n===== PROGRAM 3: DICTIONARIES =====")

student_marks = {
    "Tamil": 85,
    "English": 90,
    "Computer Science": 95
}

student_marks["Mathematics"] = 88

print("Marks:", student_marks)
print("Computer Science mark:", student_marks["Computer Science"])

for subject, mark in student_marks.items():
    print(f"{subject}: {mark}")


# PROGRAM 4: SETS
print("\n===== PROGRAM 4: SETS =====")

numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = set(numbers)

print("Original numbers:", numbers)
print("Unique numbers:", unique_numbers)

first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}

print("Union:", first_set | second_set)
print("Intersection:", first_set & second_set)


# PROGRAM 5: SLICING
print("\n===== PROGRAM 5: SLICING =====")

numbers = [10, 20, 30, 40, 50, 60]

print("Original list:", numbers)
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Middle items:", numbers[2:5])
print("Reversed list:", numbers[::-1])


# PROGRAM 6: LIST COMPREHENSION
print("\n===== PROGRAM 6: LIST COMPREHENSION =====")

numbers = list(range(1, 11))

squares = [number ** 2 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)


# PROGRAM 7: DICTIONARY AND SET COMPREHENSIONS
print("\n===== PROGRAM 7: COMPREHENSIONS =====")

words = ["python", "java", "python", "sql", "java", "python"]

word_lengths = {word: len(word) for word in set(words)}
unique_words = {word.lower() for word in words}

print("Word lengths:", word_lengths)
print("Unique words:", unique_words)


# PROGRAM 8: WORD-FREQUENCY COUNTER
print("\n===== PROGRAM 8: WORD FREQUENCY COUNTER =====")

import re
from collections import Counter

paragraph = input("Enter a paragraph:\n")
words = re.findall(r"\b[a-zA-Z0-9']+\b", paragraph.lower())

word_frequency = Counter(words)
top_five = word_frequency.most_common(5)

print("\nTotal words:", len(words))
print("Unique words:", len(set(words)))
print("\nTop 5 most frequent words:")

if not top_five:
    print("No words were entered.")
else:
    for rank, (word, count) in enumerate(top_five, start=1):
        print(f"{rank}. {word}: {count} time(s)")

