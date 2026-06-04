def greedy_scheduler(students, slots):
    schedule = {}

    for student in students:

        for slot in slots:

            conflict = False

            for s in schedule:
                if (schedule[s]["slot"] == slot and
                        schedule[s]["interviewer"] == student.interviewer):
                    conflict = True
                    break

            if not conflict:
                schedule[student.name] = {
                    "slot": slot,
                    "interviewer": student.interviewer
                }
                break

    return schedule