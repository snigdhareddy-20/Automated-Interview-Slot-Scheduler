def dfs_scheduler(students, slots):
    schedule = {}

    def is_valid(student, slot):
        for s in schedule:
            if schedule[s]["slot"] == slot and \
               schedule[s]["interviewer"] == student.interviewer:
                return False
        return True

    def dfs(index):
        if index == len(students):
            return True

        student = students[index]

        preferred_first = [student.preferred_slot] + \
                          [s for s in slots if s != student.preferred_slot]

        for slot in preferred_first:
            if is_valid(student, slot):
                schedule[student.name] = {
                    "slot": slot,
                    "interviewer": student.interviewer
                }

                if dfs(index + 1):
                    return True

                del schedule[student.name]

        return False

    dfs(0)
    return schedule