task = input("Enter your task: ")
priority_level = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match (priority_level.lower(), time_bound.lower()):
    case ("high", "yes"):
        print("This task is urgent and should be done immediately.")
    case ("high", "no"):
        print("This task is important but can be scheduled later.")
    case ("medium", "yes"):
        print("This task should be done soon, but it's not urgent.")
    case ("medium", "no"):
        print("This task can be planned for a later time.")
    case ("low", "yes"):
        print("This task is not urgent and can be done at your convenience.")
    case ("low", "no"):
        print("This task can be postponed indefinitely.")
    case _:
        print("Invalid input. Please check the priority level and time-bound status.")
