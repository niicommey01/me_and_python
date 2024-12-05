import argparse
import json
from textwrap import indent

#define arguments
parser = argparse.ArgumentParser (description= "A task tracker")
parser.add_argument("-a", "--add_task", type = str, nargs = "*",
                    metavar = "task_name",
                    help = "Adds task to be completed")

parser.add_argument("-r", "--delete_task", type = str, nargs = "*",
                    metavar = "task_name",
                    help = "Deletes a specific task")

parser.add_argument("-d", "--completed", type = str, nargs = "*",
                    metavar = "task_name",
                    help = "Marks specific task as completed")

parser.add_argument("-p", "--in_progress", type = str, nargs = "*",
                    metavar = "task_name",
                    help = 'Marks a specific task as in progress')

parser.add_argument("-t", "--todo", type = str, nargs = "*",
                    metavar = "task_name",
                    help = "Marks a specific task as to do")

args = parser.parse_args()

#create a dictionary for tasks
tasks ={
    "add_task": args.add_task or [],
    "delete_task": args.delete_task or [],
    "completed": args.completed or [],
    "in_progress": args.in_progress or [],
    "todo": args.todo or []
}

#store inputs to a JSON file
def save_inputs_to_JSON(tasks):
    with open("tasktrackerJSON.json", "w") as file:
        json.dump(tasks, file, indent=4)

#load tasks from JSON file
def load_tasks_from_JSON():
    try:
        with open("tasktrackerJSON.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        print("No existing file found. Starting fresh!")
        return{}
    except json.JSONDecodeError:
        print("Error reading the JSON file. It may be corrupted. Starting fresh!")
        return {}

#load existing tasks
existing_tasks = load_tasks_from_JSON()
#print existing tasks
print("loaded tasks: ", existing_tasks)

existing_tasks["add_task"].extend(tasks["add_task"])
existing_tasks["delete_task"].extend(tasks["delete_task"])
existing_tasks["completed"].extend(tasks["completed"])
existing_tasks["in_progress"].extend(tasks["in_progress"])
existing_tasks["todo"].extend(tasks["todo"])

for task in existing_tasks["delete_task"]:
    for key in ["add_task", "completed", "in_progress","todo"]:
        if task in existing_tasks[key]:
            existing_tasks[key].remove(task)

# CLear the delete_task to avoid redundant processing
existing_tasks["delete_task"].clear()

save_inputs_to_JSON(existing_tasks)