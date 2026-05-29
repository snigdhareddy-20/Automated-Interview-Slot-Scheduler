def csp_scheduler(students, slots):
    schedule = {}

    domains = {
        student.name: slots[:] for student in students
    }

    def is_valid(student, slot):
        for s in schedule:
            if schedule[s]["slot"] == slot and \
               schedule[s]["interviewer"] == student.interviewer:
                return False
        return True

    # MRV Heuristic
    def select_unassigned():
        unassigned = [
            s for s in students if s.name not in schedule
        ]

        unassigned.sort(key=lambda s: len(domains[s.name]))
        return unassigned[0]

    # Forward Checking
    def forward_check(student, slot):
        removed = []

        for s in students:
            if s.name not in schedule and s.interviewer == student.interviewer:
                if slot in domains[s.name]:
                    domains[s.name].remove(slot)
                    removed.append((s.name, slot))

        return removed

    def restore(removed):
        for name, slot in removed:
            domains[name].append(slot)

    def backtrack():
        if len(schedule) == len(students):
            return True

        student = select_unassigned()

        preferred_first = [student.preferred_slot] + \
                          [s for s in domains[student.name]
                           if s != student.preferred_slot]

        for slot in preferred_first:

            if slot not in domains[student.name]:
                continue

            if is_valid(student, slot):

                schedule[student.name] = {
                    "slot": slot,
                    "interviewer": student.interviewer
                }

                removed = forward_check(student, slot)

                if backtrack():
                    return True

                restore(removed)

                del schedule[student.name]

        return False

    backtrack()
    return schedule