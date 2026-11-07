from project import (
    task_duration_based_on_energy as tdb,
    sorted_tasks_prefer_and_hardness as stp,
    lis_sorter as lsr,
    Task
)


def test_task_duration_based_on_energy():

    assert tdb(3, "low") == 1
    assert tdb(3, "medium") == 1.5
    assert tdb(3, "high") == 3



def test_sorted_tasks_prefer_and_hardness():

    task_1 = Task("programming", "hard", 4, "morning")
    task_2 = Task("English", "medium", 2, "morning")
    task_3 = Task("dinner", "easy", 1, "night")

    tasks = [task_1, task_2, task_3]

    result = stp(tasks)

    assert [task.task_name for task in result["morning"]] == [
        "programming",
        "English"
    ]

    assert [task.task_name for task in result["night"]] == ["dinner"]

    assert result["afternoon"] == []
    assert result["evening"] == []



def test_lis_sorter():

    task_1 = Task("programming", "hard", 4, "morning")
    task_2 = Task("English", "medium", 2, "morning")
    task_3 = Task("dinner", "easy", 1, "night")

    tasks = [task_3, task_1, task_2 ]

    result = lsr(tasks)

    assert result == [task_1, task_2, task_3]
