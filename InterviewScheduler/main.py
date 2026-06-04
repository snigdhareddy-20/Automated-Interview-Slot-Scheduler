from models import Student
from greedy_scheduler import greedy_scheduler
from search_scheduler import dfs_scheduler
from csp_scheduler import csp_scheduler
from utils import print_schedule
import time

# Dynamic Input

students = []

num = int(input("Enter number of students: "))

print("\nEnter student details:\n")

for i in range(num):
    name = input(f"Student {i+1} Name: ")
    preferred_slot = input("Preferred Slot (Example: 9AM): ")
    interviewer = input("Interviewer Name: ")

    students.append(
        Student(name, preferred_slot, interviewer)
    )

# Automatic Slot Generation

slots = []

for student in students:
    if student.preferred_slot not in slots:
        slots.append(student.preferred_slot)

# Extra backup slots automatically added

extra_slots = ["9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM"]

for slot in extra_slots:
    if slot not in slots:
        slots.append(slot)

print("\nAvailable Slots:", slots)

# GREEDY SCHEDULER

print("\n===== GREEDY SCHEDULER =====")

start = time.time()

greedy_result = greedy_scheduler(students, slots)

end = time.time()

print_schedule(greedy_result)

print(f"Time Taken: {end - start:.6f} seconds")

# SEARCH BASED SCHEDULER

print("\n===== SEARCH BASED SCHEDULER =====")

start = time.time()

search_result = dfs_scheduler(students, slots)

end = time.time()

print_schedule(search_result)

print(f"Time Taken: {end - start:.6f} seconds")

# CSP BASED SCHEDULER

print("\n===== CSP BASED SCHEDULER =====")

start = time.time()

csp_result = csp_scheduler(students, slots)

end = time.time()

print_schedule(csp_result)

print(f"Time Taken: {end - start:.6f} seconds")
