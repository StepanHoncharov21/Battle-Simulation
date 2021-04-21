import random

class Player():
	"""Описывает поведение и свойства всех игроков,
	   которые только могут быть созданы. 
	"""
	def __init__(self):
		# hp - здоровье
		self.__hp = 100

	def small_range_demage(self):
		self.__hp = self.__hp - random.randint(18,25)

	def large_range_demage(self):
		self.__hp = self.__hp - random.randint(10,35)

	def helling(self):
		self.__hp = self.__hp + random.randint(18,25)
	#Возвращаем hp в диапазноне от 0 до 100
	def get_hp(self):
		if self.__hp > 100:
			self.__hp = 100
		elif self.__hp < 0:
			self.__hp = 0
		return self.__hp


class Computer(Player):
	"""Описывает поведение и свойства игрока 'Компьютер'.
	   Наследник от класса 'Player'.
	"""
	def action_selection(self,Target):
		"""Выбор следующего из шагов. Функция получает объект в качестве 
		   параметра.
	   	   И может вызывать его методы, таким образом "атакуя его".
	       **************
	       Выбор зависит от количества "hp" у игрока.
	       Например невозможно запустить функцию "helling" если hp = 100.
	       Так же, шанс на излечение увеличивается при hp < 35 на 27%
	       *************
	       Функция возращает "actionName" - название действия (str)
	    """

		"""Определяем значение переменной "lastParameterInRandom".
		   Которая задает диапазон выбора случайного числа
		"""
		if self.get_hp() == 100:
			lastParameterInRandom = 2
		elif self.get_hp() > 35:
			lastParameterInRandom = 3
		else:
			lastParameterInRandom = 5 

		randomNumber = random.randint(1,lastParameterInRandom)
		#Выбор действия на основании случайного числа
		if  randomNumber == 1:
			Target.small_range_demage()
			action_name = "Компьютер: Нанес умеренный урон небольшого диапазона"
		elif randomNumber == 2:
			Target.large_range_demage()
			action_name = "Компьютер: Нанес умеренный урон большого диапазона"
		else:
			self.helling()
			action_name = "Компьютер: Излечился"

		return action_name


class Human(Player):
	"""Описывает поведение и свойства игрока 'Человек'.
	   Наследник от класса 'Player'.
	"""	
	def action_selection(self,Target):
		"""Выбор следующего из шагов. Функция получает объект в качестве 
		   параметра.
	   	   И может вызывать его методы, таким образом "атакуя его".
	       **************
	       Выбор зависит от количества "hp" у игрока.
	       Например невозможно запустить функцию "helling" если hp = 100.
	       *************
	       Шанс на выпадение каждого действия при hp < 100 - 33%
	       Функция возращает "actionName" - название действия (str)
	    """

		"""Определяем значение переменной "lastParameterInRandom".
		   Которая задает диапазон выбора случайного числа
		"""
		if self.get_hp() == 100:
			lastParameterInRandom = 2
		else:
			lastParameterInRandom = 3

		randomNumber = random.randint(1,lastParameterInRandom)
		#Выбор действия на основании случайного числа
		if randomNumber == 1:
			Target.small_range_demage()
			action_name = "Человек: Нанес умеренный урон небольшого диапазона"
		elif randomNumber == 2:
			Target.large_range_demage()
			action_name = "Человек: Нанес умеренный урон большого диапазона"
		else:
			self.helling()
			action_name = "Человек: Излечился"

		return action_name
