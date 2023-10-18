import eel
from db import *


@eel.expose
def add(name: str) -> None:
	add_task(name)


@eel.expose
def clear() -> None:
	clear_table()


@eel.expose
def fix(name: str) -> None:
	fix_task(name)


@eel.expose
def delite(name: str) -> None:
	remove_task(name)


@eel.expose
def get() -> list:
	return get_creatures()


def main() -> None:
	eel.init('web')
	eel.start('index.html', mode='chrome', size=(700, 900))


if __name__ == '__main__':
	main()