# Personal Daily Planner

## Video Demo
[Watch the project demo on YouTube](https://youtu.be/rx6XRBgKA2M)

## Description

**Personal Daily Planner** is a Python application developed as my final project for Harvard University's CS50's Introduction to Programming with Python (CS50P).

The main purpose of this project is to help users organize their daily tasks and create a more structured schedule. Sometimes, people have several tasks to complete but do not know how to organize them throughout the day. This application provides a simple way to manage tasks and generate a daily plan based on different factors.

Users can add tasks by entering their name, difficulty level, estimated duration, and preferred time of day. The application uses this information to organize tasks and assign time slots to them.

One of the features of this project is that it considers the user's energy level when calculating task durations. Depending on the selected energy level, the application adjusts the time allocated to tasks. This helps create a schedule that better reflects the user's available energy.

## Features

- **Add Tasks:** Users can add tasks with a name, difficulty, estimated duration, and preferred time of day.
- **Create Daily Plans:** The application organizes saved tasks and generates a schedule for the following day.
- **Energy-Based Scheduling:** Task durations are adjusted according to the user's energy level.
- **View Plans:** Users can view previously generated daily plans.
- **Task Management:** Users can delete tasks and manage their saved tasks.
- **Track Progress:** Users can mark completed tasks as done.

## Project Structure

The project is organized into several Python files and directories:

- `project.py`: The main file of the application. It contains the main menu, the Task class, and the scheduling logic.
- `data_base/`: Contains the database-related functions used to create the database and manage task information.
- `file_creator/`: Contains functions for creating, reading, and updating daily plan CSV files.
- `test_project.py`: Contains unit tests for important functions in the project.
- `requirements.txt`: Lists the external Python packages required to run the application.

## Technologies and Libraries

This project was developed using Python and several tools and libraries:

- **Python:** The main programming language used to build the application.
- **SQLite:** Used to store task information in a database.
- **CSV:** Used to save and manage daily schedules.
- **Tabulate:** Used to display information in formatted tables in the terminal.
- **Pytest:** Used to test important functions and check that they work as expected.

## Installation and Usage

To run this project, you need to have Python installed.

First, clone or download this repository.

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python project.py
```

To run the tests:

```bash
python -m pytest test_project.py
```

## Design Choices

I chose SQLite because it provides a simple and reliable way to store task information without requiring a separate database server.

I used CSV files to store generated daily plans because they are easy to create, read, and manage with Python.

I also used object-oriented programming to represent tasks through a `Task` class. This helped organize task-related information and made the code easier to manage.

Finally, I separated database operations and CSV file operations into different modules to keep the project more organized and readable.

## What I Learned

Working on this project helped me practice several concepts from CS50P, including object-oriented programming, functions, exception handling, file handling, database operations, and testing with pytest.

It also gave me the opportunity to combine these concepts into a practical application that solves a real-life problem.

This project is my first complete Python application, and I hope to improve it further in the future.