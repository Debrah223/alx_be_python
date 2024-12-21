#  Personal Daily Reminder
# Prompt user for a Single Task
task = input(" Enter your task: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes or no): ").lower()
# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Task: {task}\nPriority: high\nThis task requires your urgent attention!"
    case "medium":
        reminder = f"Task: {task}\nPriority: medium\nThis task should be completed soon."
    case "low":
        reminder = f"Task: {task}\nPriority: low\nThis task can be done in the near future."
    case _:
        reminder = f"Task: {task}\nPriority: Unknown\nPlease check the task priority again."
#  Modify the reminder if the task is time-bound.
if time_bound == "yes":
    reminder += f"{task}\nNote: is a high priority task that requires immediate attention today!"
else:
    reminder = f"{task}\nNote: is a low priority task. Consider completing it when you have free time."
# Provide a Customized Reminder    
print("\n---Daily Reminder---")
print(reminder)