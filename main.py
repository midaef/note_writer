
from ezprint import *
import os
import hashlib
import sys

#key: 1.8093 2.8904
def main():
	cls()
	key = 8904
	hsh = '7818354194c4feae57304abadc2c437c'
	if hsh == hashlib.md5(input('Введите пароль:').encode("utf")).hexdigest():
		print('hash-ключь совпал!')
	else:
		print('Введите пароль правильно!')
		exit()
	key1 = int(input('Введите дополнительный пароль:'))
	if key == key1:
		print('Вы успешно вошли в блокнот!')
		print()
	else:
		print('Введите пароль правильно!')
		exit()
	while True:
		print('1.Посмотреть предыдущие записи')
		print('2.Записать новую запись в блокнот')
		print('3.Очистить блокнот')
		vibor = input('Введите:')
		if vibor == '3':
			f = open('mes.txt', 'w')
			f.close()
			print('Блокнот отчищен!')
		elif vibor == '1':
			f = open('mes.txt', 'r')
			for g in f:
				print(g)
			f.close()
			if os.stat('mes.txt').st_size == 0:
				print('Нету записей!')
		elif vibor == '2':
			mes = str(input('Введите запись на сегодня:'))
			if len(mes)>0:
				l = []
				f = open('mes.txt', 'r')
				for j in f:
					l.append(j)
				f.close()
				l.append('\n' + mes)
				f = open('mes.txt', 'w')
				for i in l:
					f.write(i)
				print('Успешное сохранение')
				f.close()
	else:
		print('Введите правильное значение!')


if __name__ == '__main__':
	main()