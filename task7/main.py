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
