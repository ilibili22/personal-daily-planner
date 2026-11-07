# this project will make the tomorrow plan:
from sys import exit
from data_base import project_data_base as db
from tabulate import tabulate
from file_creator import project_creator 

class Task:
    def __init__(self,task_name, difficulty, duration, prefer_time):
        self.task_name = task_name
        self.difficulty = difficulty
        self.duration = duration
        self.prefer_time = prefer_time
        
    def __repr__(self):
        return f"task_name = {self.task_name}, difficulty = {self.difficulty}, duration = {self.duration}, day time = {self.prefer_time}"



def main():
    
    

    while True:

        user_decision = input("what do you want to do: adding a task, making tomorrow plan, seeing exist tasks, finishing a task, deleting a task or you want to leave?(A/M/S/D/F/L): ").lower()

        if user_decision == "a":
            task_adder()

        elif user_decision == "f":
            user_date = input("Enter the date of the day you want to change in this format(YYYY-MM-DD): ")
            task_terminator(user_date)    

        elif user_decision == "s":
            tasks_table_printer(db.data_base_reader())

        elif user_decision == "m":
            if not db.data_base_reader():
                print("\nno tasks yet.\n")
                print("please add new task...")
                continue
            

            user_tomorrow_tasks = [name.strip() for name in input("Enter the tasks that you plan to do(task name,task name...): ").split(",")]

            flag = False
            for tomorrow_task in user_tomorrow_tasks:
                if not tomorrow_task in all_tasks():
                    print(f"\nERROR: there is no task known as '{tomorrow_task}', please add it...\n")
                    flag = True
                    break
            if flag:
                continue

            sorted_tasks = sorted_tasks_prefer_and_hardness(tasks_from_database(user_tomorrow_tasks))
            # print("sorted: ",sorted_tasks)
            while True:
                
                user_energy = input("Enter your energy level between (low/medium/high): ").lower()
                if user_energy == "low" or user_energy == "medium" or user_energy == "high":
                    tomorrow_plan_maker(user_energy,sorted_tasks)
                    break
                else:
                    print("please Enter the right options.")
                    continue

        elif user_decision == "d":
            task_remover()

        elif user_decision == "l":
            break
        
        else:
            print("Enter A / M /S /D /F /L: ")
            continue
        

def all_tasks():
    rows = db.data_base_reader()

    tasks = []

    for _, name, difficulty, duration, prefer_time in rows:
        tasks.append(name)   

    # print(tasks)
    return tasks


def tasks_from_database(task_names):
    rows = db.data_base_reader()

    tasks = []

    for _, name, difficulty, duration, prefer_time in rows:
        if name in task_names:
            tasks.append(Task(name, difficulty, duration, prefer_time))

    return tasks


def tomorrow_plan_maker(user_energy,sorted_tasks):
    # print(user_energy)
    # latter , after i made the data base this function will check that the tasks exist or not , if not it will call task_adder function.

    part_of_day_start = {"morning": 8 * 60,"afternoon":12 * 60 ,"evening":18 * 60 ,"night":21 * 60  ,}
    part_of_day_end = {"morning": 12 * 60,"afternoon":18 * 60 ,"evening":21 * 60 ,"night":23 * 60  ,}

    weird_list = []
    
    for key in sorted_tasks.keys():
        for task in sorted_tasks[key]:
            adjusted = task_duration_based_on_energy(task.duration, user_energy)
            # print(adjusted)
            assign_time(part_of_day_start[task.prefer_time], adjusted, task.task_name, part_of_day_start, task.prefer_time, part_of_day_end,task.difficulty,user_energy,weird_list,task.prefer_time)
    # print(weird_list)
    tasks_table_printer_for_tomorrow_plan(weird_list)
    project_creator.file_creator(project_creator.file_getter(weird_list))


def task_terminator(date):
    project_creator.file_reader(date)
        

def assign_time(start_time, duration, task_name, part_of_day_start, part_of_day_key, part_of_day_end,task_difficulty,user_energy,weird_list,prefer_time, is_continued=False):

    next_slot_map = {
        "morning": "afternoon",
        "afternoon": "evening",
        "evening": "night",
        "night": None
    }

    if start_time >= part_of_day_end[part_of_day_key]: 
        next_slot = next_slot_map[part_of_day_key]
        if next_slot is None:
            exit("\ntasks time cant be more than 15 hours\n")
        assign_time(
            part_of_day_start[next_slot],
            duration,
            task_name,
            part_of_day_start,
            next_slot,
            part_of_day_end,
            task_difficulty,
            user_energy,
            weird_list,
            prefer_time,
            is_continued
        )
        return
                # 480 + 4 * 60
    total_end = int(start_time + (duration * 60))
        # 720           # 720
    if total_end > part_of_day_end[part_of_day_key]:
        overflow_minutes = total_end - part_of_day_end[part_of_day_key]
        end_time = part_of_day_end[part_of_day_key]

        part_of_day_start[part_of_day_key] = end_time

        label = " continue" if is_continued else ""
        output = (task_name,prefer_time,task_difficulty,start_time,end_time,label)
        weird_list.append(output)
        
        # print(part_of_day_start)

        next_slot = next_slot_map[part_of_day_key]
        if next_slot is None:
            exit("\ntasks time cant be more than 15 hours\n")

        remaining_duration = overflow_minutes / 60


        assign_time(
            part_of_day_start[next_slot],
            remaining_duration,
            task_name,
            part_of_day_start,
            next_slot,
            part_of_day_end,
            task_difficulty,
            user_energy,
            weird_list,
            prefer_time,
            True
        )

    else:
        end_time = total_end
        part_of_day_start[part_of_day_key] = end_time

        label = " continue" if is_continued else ""
        output = (task_name,prefer_time,task_difficulty,start_time,end_time,label)
        weird_list.append(output)

        # print(part_of_day_start)

def HH_MM(time):
    return f"{time // 60:02d}:{time % 60:02d}"
    

def task_duration_based_on_energy(duration, energy):
    if energy == "low":
        return duration / 3
    elif energy == "medium":
        return duration / 2
    else:
        return duration


def tasks_table_printer_for_tomorrow_plan(rows):
    sorted_rows = sorted(rows, key=lambda row: row[3])

    display_rows = []
    for name, prefer, difficulty, start, end, label in sorted_rows:
        display_rows.append((name, prefer, difficulty, HH_MM(start), HH_MM(end), label.strip()))

    headers = ["Task Name", "Prefer Time", "Difficulty", "Start", "End", "Note"]
    print(tabulate(display_rows, headers=headers, tablefmt="rounded_grid"))

def tasks_table_printer(rows):   
    if not rows:
        print("\nno tasks yet.\n")
        return
    # print("rows: ",rows)
    headers = ["ID", "Task Name", "Difficulty", "Duration (H)", "Prefer Time"]
    print(tabulate(rows, headers=headers, tablefmt="rounded_grid"))


def task_remover():
    rows = db.data_base_reader()
    tasks_table_printer(rows)

    if not rows:
        return

    try:
        task_id = input("Enter the ID of the task you want to delete you can delete multi IDs(ID,next ID): ").split(",")
        new_task_id = []

        for item in task_id:
            item = int(item)
            new_task_id.append(item)

        new_task_id = set(new_task_id)

        
    except ValueError:
        print("ID must be a number.")
        return

    for item in new_task_id:
        if db.data_base_deleter(item):
            print(f"this task id:({item}) deleted.")
        else:
            print("no task with that ID.")



def task_adder():

    tasks = []
    counter = 0
    while True:

        print(f"\nuser: {counter+1} \n")

        user_task_name = input("Enter your task name: ").strip()
        if user_task_name.isdigit() or not user_task_name:
            print("task name must be a sentence.")
            continue

        try:    
            user_task_duration = float(input("Enter your task duration: "))
            if user_task_duration <= 0 :
                raise ValueError

        except ValueError:
            print("task duration must be a number.")
            continue

        user_task_difficulty = input("Enter your task hardness level, (easy/medium/hard): ").lower()
        if not(user_task_difficulty == "easy" or user_task_difficulty == "medium" or user_task_difficulty == "hard"):
            print("you can only choose between, (easy/medium/hard).")
            continue

        user_task_prefer_time = input("Enter the time you want to start the task (morning/afternoon/evening/night): ").lower()
        if not (user_task_prefer_time == "morning" or user_task_prefer_time == "afternoon" or user_task_prefer_time == "evening" or user_task_prefer_time == "night"):
            print("you can only choose between, (morning/afternoon/evening/night).")
            continue


        task_a = Task(user_task_name,user_task_difficulty,user_task_duration,user_task_prefer_time)

        counter += 1
        tasks.append(task_a)
        flag = False
        while True:
            adding_task_finisher = input("Enter Done if you added all your tasks or Enter More if you want to continue adding(D/M): ").lower()
            if not (adding_task_finisher == "d" or adding_task_finisher == "m"):
                print("you can only use M or D. try again...")
                continue
            elif adding_task_finisher == "d":
                flag = True
                break
            elif adding_task_finisher == "m":
                break
        if flag:
            break

    tasks_adder_to_database(tasks)

    tasks_table_printer(db.data_base_reader())

    return tasks


def tasks_adder_to_database(tasks):

    for task in tasks:
        db.data_base_inserter(task.task_name, task.difficulty, task.duration, task.prefer_time)

        



def sorted_tasks_prefer_and_hardness(all_tasks):
    """this function will sort tasks based on prefer time and difficulty."""

    grouped_tasks = {
        "morning": [],
        "afternoon": [],
        "evening": [],
        "night": [],

    }

    for task in all_tasks:
        grouped_tasks[task.prefer_time].append(task)

    for slot in grouped_tasks:
        grouped_tasks[slot] = lis_sorter(grouped_tasks[slot])

    # print(grouped_tasks)
    return grouped_tasks


    
def lis_sorter(unsorted_lis):    

    value_of_hard_parts = {"medium":2,"hard":3,"easy":1}
    return sorted(unsorted_lis, key=lambda task: value_of_hard_parts[task.difficulty], reverse = True)





if __name__ == "__main__":
    main()


