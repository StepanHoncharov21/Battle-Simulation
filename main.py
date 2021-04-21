import random
import time
from  src.LogicCharecter  import Computer,Human

Computer = Computer()
Human = Human()


def game_loop():
	"""Игровой цикл.
	   Случайным образом выбирается игрок который будет совершать действие
	"""
	inGame = True
	while inGame:
		randomNumber = random.randint(0,1)
		
		if randomNumber == 0:
			print(Computer.action_selection(Human))
			time.sleep(1)
			print("\nЗдоровье Компьютера: " + str(Computer.get_hp()) + "%")
			print("Здоровье Человека: " + str(Human.get_hp()) + "%\n")
			time.sleep(2)
		else:
			print(Human.action_selection(Computer))
			time.sleep(1)
			print("\nЗдоровье Компьютера: " + str(Computer.get_hp()) + "%")
			print("Здоровье Человека: " + str(Human.get_hp()) + "%\n")
			time.sleep(2)

		if Computer.get_hp() == 0:
			print("\nЧеловек победил!!!!!")
			inGame = False
		elif Human.get_hp() == 0:
			print("\nКомпьютер победил")
			inGame = False
	input()


def main():
	print("Здравствуйте, сегодня будет бой!")
	time.sleep(1)
	print("Его запомнят надолго....")
	time.sleep(2)
	print("Нажмите ENTER что-бы начать ")
	input()
	game_loop()


if __name__ == '__main__':
	main()
