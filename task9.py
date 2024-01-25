# task9.py
#Если вы введите "Привет, мир!", то программа выведет 3 7, так как в этой строке 3 гласных (и, е, о) и 7 согласных (п, р, в, т, м, р, м).
vowels = 'аеёиоуыэюя' # Список гласных букв
consonants = 'бвгджзйклмнпрстфхцчшщ' # Список согласных букв

text = input().lower() # Считываем строку и приводим ее к нижнему регистру
vowel_count = sum(1 for char in text if char in vowels) # Подсчитываем количество гласных
consonant_count = sum(1 for char in text if char in consonants) # Подсчитываем количество согласных

print(vowel_count, consonant_count) # Выводим количество гласных и согласных
