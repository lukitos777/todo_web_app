import sqlite3
from typing import Any, Union

# don't touch it !
# ===============================================================|
# conn = sqlite3.connect('storehouse.db')                        |
# cursor = conn.cursor()                                         |
# cursor.execute('''                                             |
#	CREATE TABLE Tasks                                           |
#    (id INTEGER PRIMARY KEY, task_name TEXT, is_done BOOLEAN)   |
# ''')                                                           |
# conn.close()                                                   |
# ===============================================================|

def checker(value: Any, type_) -> bool:
	return isinstance(value, type_)
	

def validator(value: str) -> bool:
	expression = value.lower().__contains__('drop') or\
				value.lower().__contains__('create') or\
				value.lower().__contains__('delite') or\
				value == ''
	return False if expression else True


def add_task(name: str) -> None:
	coon = sqlite3.connect('storehouse.db')
	cursor = conn.cursor()

	if checker(name, str) and validator(name):
		cursor.execute(
			'INSERT INTO users (task_name, is_done) VALUES (?, ?)',
			(name, False))
	else:
		pass
	cursor.close()


def remove_task(name: str) -> None:
	conn = sqlite3.connect('storehouse.db')
	cursor = conn.cursor()

	if checker(name, str) and validator(name):
		cursor.execute(
			'DELETE FROM tasks WHERE task_name = ?',
			(name))
	else:
		pass
	cursor.close()


def clear_table() -> None:
	conn = sqlite3.connect('storehouse.db')
	cursor = conn.cursor()
	cursor.execute('DELETE FROM tasks')
	cursor.close()


def fix_task(name: str) -> None:
	conn = sqlite3.connect('storehouse.db')
	cursor = conn.cursor()

	if checker(name, str) and validator(name):
		cursor.execute(
			'UPDATE tasks SET is_done = ? WHERE task_name = ?',
			(True, name))
	else:
		pass
	cursor.close()


def get_creatures() -> list:
	conn = sqlite3.connect('storehouse.db')
	cursor = conn.cursor()
	cursor.execute('SELECT task_name FROM tasks')
	items = cursor.fetchall()
	cursor.close()
	return items