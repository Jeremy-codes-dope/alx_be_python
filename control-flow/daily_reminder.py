task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority :
    case "high":
        if time_bound == "yes":
            print("This task is urgent and should be done immediately.")
        elif time_bound == "no":
            print("This matters, do it as soon as you get time.")
    case "medium":
        print("This task should be done soon, but it's not urgent.")
    case "low":
        print("This task is not urgent and can be done at your convenience.")
    case _:
        print("Invalid input. Please check the priority level and time-bound status.")
