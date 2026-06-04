nodes_expanded = 0

def csp_scheduler(students, slots):
    global nodes_expanded
    nodes_expanded = 0

    schedule = {}

    domains = {
        student.name: slots[:] for student in students
    }

    def is_valid(student, slot):
        for s in schedule:
            if (schedule[s]["slot"] == slot and
                    schedule[s]["interviewer"] == student.interviewer):

                print(
                    f"Conflict: {student.name} cannot be assigned "
                    f"{slot} because interviewer "
                    f"{student.interviewer} is already busy."
                )

                return False

        return True

    # MRV Heuristic
    def select_unassigned():
        unassigned = [
            s for s in students
            if s.name not in schedule
        ]

        unassigned.sort(
            key=lambda s: len(domains[s.name])
        )

        return unassigned[0]

    # Forward Checking
    def forward_check(student, slot):
        removed = []

        for s in students:

            if (s.name not in schedule and
                    s.interviewer == student.interviewer):

                if slot in domains[s.name]:
                    domains[s.name].remove(slot)
                    removed.append(
                        (s.name, slot)
                    )

        return removed

    def restore(removed):
        for name, slot in removed:
            domains[name].append(slot)

    def backtrack():
        global nodes_expanded

        nodes_expanded += 1

        if len(schedule) == len(students):
            return True

        student = select_unassigned()

        preferred_first = (
            [student.preferred_slot] +
            [
                s for s in domains[student.name]
                if s != student.preferred_slot
            ]
        )

        for slot in preferred_first:

            if slot not in domains[student.name]:
                continue

            print(
                f"Trying: {student.name} -> {slot}"
            )

            if is_valid(student, slot):

                schedule[student.name] = {
                    "slot": slot,
                    "interviewer": student.interviewer
                }

                print(
                    f"Assigned: {student.name} -> {slot}"
                )

                removed = forward_check(
                    student,
                    slot
                )

                if backtrack():
                    return True

                print(
                    f"Backtracking: {student.name}"
                )

                restore(removed)

                del schedule[student.name]

        return False

    success = backtrack()

    print(f"\nNodes Expanded: {nodes_expanded}")

    if not success:
        print("No valid schedule found.")

    return schedule
