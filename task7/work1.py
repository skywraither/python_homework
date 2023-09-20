
#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

#*Пример:*

#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#    **Вывод:** Парам пам-пам





def count_vowels(word):
    vowels = "AEIOUYaeiouy"  # Гласные буквы
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


def check_rhythm(pooh_poem):
    lines = pooh_poem.split()
    rhythm = None

    for line in lines:
        words = line.split('-')
        syllable_count = count_vowels(words[0])

        for word in words[1:]:
            syllable_count += count_vowels(word)

        if rhythm is None:
            rhythm = syllable_count
        elif rhythm != syllable_count:
            return "Пам парам"

    return "Парам пам-пам"


# Ввод стихотворения
pooh_poem = input("Введите стихотворение Винни-Пуха: ")

# Проверка ритма и вывод результата
result = check_rhythm(pooh_poem)
print(result)
