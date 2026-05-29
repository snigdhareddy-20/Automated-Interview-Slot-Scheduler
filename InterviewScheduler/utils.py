def print_schedule(schedule):
    print("\nFINAL SCHEDULE")
    print("-" * 30)

    for student, details in schedule.items():
        print(f"{student} -> {details['slot']} -> {details['interviewer']}")

    print("-" * 30)