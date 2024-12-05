import argparse
import json


# Store inputs to a JSON file
def save_inputs_to_JSON(tasks):
    with open("tasktrackerJSON.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Load tasks from JSON file
def load_tasks_from_JSON():
    try:
        with open("tasktrackerJSON.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        print("No existing file found. Starting fresh!")
        return {
            "add_task": [],
            "delete_task": [],
            "completed": [],
            "in_progress": [],
            "todo": []
        }
    except json.JSONDecodeError:
        print("Error reading the JSON file. It may be corrupted. Starting fresh!")
        return {
            "add_task": [],
            "delete_task": [],
            "completed": [],
            "in_progress": [],
            "todo": []
        }

def print_tasks(tasks):
    print("\nCurrent Tasks:")
    print("-" * 40)
    for category, task_list in tasks.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        if task_list:
            for task in task_list:
                print(f" - {task}")
        else:
            print(" No tasks.")
    print("-" * 40)


def main():
    print("Welcome to Task Tracker")

    # Define arguments
    parser = argparse.ArgumentParser(description="A task tracker")
    parser.add_argument("-a", "--add_task", type=str, nargs="*",
                        metavar="task_name", help="Adds task to be completed")
    parser.add_argument("-d", "--delete_task", type=str, nargs="*",
                        metavar="task_name", help="Deletes a specific task")
    parser.add_argument("-c", "--completed", type=str, nargs="*",
                        metavar="task_name", help="Marks specific task as completed")
    parser.add_argument("-p", "--in_progress", type=str, nargs="*",
                        metavar="task_name", help="Marks a specific task as in progress")
    parser.add_argument("-t", "--todo", type=str, nargs="*",
                        metavar="task_name", help="Marks a specific task as to do")

    args = parser.parse_args()

    # Load existing tasks
    existing_tasks = load_tasks_from_JSON()

    print("\nTasks before update:")
    print_tasks(existing_tasks)

    # Add tasks to the appropriate categories
    if args.add_task:
        existing_tasks["add_task"].extend(args.add_task)

    if args.completed:
        existing_tasks["completed"].extend(args.completed)

    if args.in_progress:
        existing_tasks["in_progress"].extend(args.in_progress)

    if args.todo:
        existing_tasks["todo"].extend(args.todo)

    # Delete tasks
    if args.delete_task:
        for task in args.delete_task:
            for key in ["add_task", "completed", "in_progress", "todo"]:
                if task in existing_tasks[key]:
                    existing_tasks[key].remove(task)
                found = True
            if not found:
                print(f"Task '{task}' not found in any category.")

    # Remove from add if completed
    if args.completed:
        for task in args.completed:
            for key in ["add_task", "in_progress", "todo"]:
                if task in existing_tasks[key]:
                    existing_tasks[key].remove(task)

        existing_tasks["completed"] = list(set(existing_tasks["completed"]))


    # Save the updated tasks back to the JSON file
    save_inputs_to_JSON(existing_tasks)

    print("\--- Tasks after updates ---")
    print_tasks(existing_tasks)


if __name__ == "__main__":
    main()
