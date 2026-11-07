from datetime import datetime as dt, timedelta
import csv
from sys import exit
import pathlib


# print(dt.today().strftime("%Y-%m-%d"))



def main():
    test_list = [('programming', 'morning', 'hard', 480, 720, ''), ('English', 'afternoon', 'medium', 720, 840, '')]
    x = file_getter(test_list)

    file_creator(x)
    file_reader(tomorrows_date())



def file_getter(tasks_data):

    list_of_dics = []
    for task in tasks_data:

        task_name, prefer_time, difficulty, start, end, note = task
        data = {
            "Task Name": task_name,
            "Prefer Time": prefer_time,
            "Difficulty": difficulty,
            "Start": start,
            "End": end,
            "Done": "0",
        }
        list_of_dics.append(data)

    return list_of_dics



def file_creator(data):

    if pathlib.Path(f"{tomorrows_date()}.csv").exists():
        while True:
            user_decision = input("you have file with this date, you wanna recreate it?(yes/no): ").lower()
            if user_decision == "yes":

                with open(f"{tomorrows_date()}.csv","w",newline="") as file:
                    headers = ["Task Name", "Prefer Time", "Difficulty", "Start", "End", "Done"]
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(data)
                    return
            elif user_decision == "no":
                return
            else:
                print("you cant only write(yes or no)...")
                continue
    else:
        with open(f"{tomorrows_date()}.csv", "w", newline="") as file:
            headers = ["Task Name", "Prefer Time", "Difficulty", "Start", "End", "Done"]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)


def file_reader(date):
    row_list = []
    try:    
        with open(f"{date}.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(f"Task Name: {row['Task Name']}")
                
                while True:
                    user_decision = input("have you done this task?(yes/no): ").lower()
                    if not (user_decision == "yes" or user_decision == "no"):
                        print("you can only enter yes or no...")
                        continue
                    else:
                        break

                if user_decision == "yes":
                    # line.replace("0","1(done)")
                    row["Done"] = "1"
                    print(f"Task Status: {row['Done']}\n")
                    row_list.append(row)
                
                else:
                    print(f"Task Status: {row['Done']}\n")
                    row_list.append(row)
                    continue

    except FileNotFoundError:
        print(f"There are no tasks in this day {date}")
        return

    with open(f"{date}.csv", "w", newline="") as file:
        headers = ["Task Name", "Prefer Time", "Difficulty", "Start", "End", "Done"]
        writer = csv.DictWriter(file, fieldnames=headers) 
        writer.writeheader()
        writer.writerows(row_list)          



def tomorrows_date():
    return (dt.today() + timedelta(days=1)).strftime("%Y-%m-%d")

if __name__ == "__main__":
    main()




    