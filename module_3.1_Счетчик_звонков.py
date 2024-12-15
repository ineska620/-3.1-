calls = 0 # в начале вызовов нет
def count_calls (): # создаем функцию "Количество вызовов"
    global calls # используем глобальные данные Вызов
    calls+=1 # после вызова счет стал 1, после следующего вызова станет 2
def string_info(string): # создаем функцию "информация о строке"
    count_calls() # будем работать с этими данными
    return (len(string), string.upper(), string.lower()) # окончание фукнции, подсчет кол-ва смвлов, представление в разных регистрах
def is_contains (string, spisok): # создаем функцию "содержание"
    count_calls() # работаем с этими данными
    return string in spisok #окончание. данные из строки переносим в список
print(string_info('Capybara')) # на вывод 8 (кол-во букв в слове), CAPYBARA(верхний) и Capybara (нижний регистр)
print(string_info('Armageddon'))# на выводе 10, ARMAGEDDON, armageddon
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # false. Нет Urban в списке
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls) # выведит 4 - т.к. перед этим 4 запроса