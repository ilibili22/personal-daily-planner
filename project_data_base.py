import sqlite3 as sql


def data_base_creator():
    conn = sql.connect("daily_personal_planner_data_base.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            duration REAL NOT NULL,
            prefer_time TEXT NOT NULL
        )
    """)
    # print(type(conn))
    return conn


def data_base_inserter(task_name, task_difficulty, task_duration, task_prefer_time):

    _connection = data_base_creator()

    cursor = _connection.cursor()
    cursor.execute("INSERT INTO tasks (name, difficulty, duration, prefer_time) VALUES (?, ?, ?, ?)", (task_name, task_difficulty, task_duration, task_prefer_time))

    _connection.commit()
    _connection.close()

def data_base_reader():
    connection = data_base_creator()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, difficulty, duration, prefer_time FROM tasks")
    rows = cursor.fetchall()

    connection.close()
    return rows

def data_base_deleter(task_id):
    connection = data_base_creator()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    was_deleted = cursor.rowcount > 0

    connection.close()
    return was_deleted

