# Создаем пустой справочник
phonebook = []


# Функция для добавления записи
def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = {"Фамилия": last_name, "Имя": first_name, "Отчество": middle_name, "Телефон": phone_number}
    phonebook.append(contact)
    print("Запись добавлена.")


# Функция для вывода всех записей
def display_contacts():
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}, Телефон: {contact['Телефон']}")


# Функция для поиска записей по характеристике
def search_contacts(attribute, value):
    results = [contact for contact in phonebook if contact.get(attribute) == value]
    if results:
        for contact in results:
            print(
                f"Результаты поиска: {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}, Телефон: {contact['Телефон']}")
    else:
        print("Запись не найдена.")


# Функция для изменения записи
def edit_contact():
    last_name = input("Введите фамилию для редактирования: ")
    found_contacts = []
    for contact in phonebook:
        if contact["Фамилия"] == last_name:
            found_contacts.append(contact)

    if not found_contacts:
        print("Запись не найдена.")
    else:
        print("Найдены следующие записи:")
        for index, contact in enumerate(found_contacts, start=1):
            print(
                f"{index}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}, Телефон: {contact['Телефон']}")
        choice = input("Выберите номер записи для редактирования: ")
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(found_contacts):
                edited_contact = found_contacts[choice]
                print(
                    f"Редактирование записи: {edited_contact['Фамилия']} {edited_contact['Имя']} {edited_contact['Отчество']}, Телефон: {edited_contact['Телефон']}")
                attribute = input(
                    "Введите характеристику для редактирования (Фамилия/Имя/Отчество/Телефон): ").capitalize()
                new_value = input("Введите новое значение: ")
                edited_contact[attribute] = new_value
                print("Запись отредактирована.")
            else:
                print("Неправильный выбор.")
        except ValueError:
            print("Неправильный выбор.")


# Функция для удаления записи
def delete_contact():
    last_name = input("Введите фамилию для удаления: ")
    found_contacts = [contact for contact in phonebook if contact["Фамилия"] == last_name]

    if not found_contacts:
        print("Запись не найдена.")
    else:
        print("Найдены следующие записи:")
        for index, contact in enumerate(found_contacts, start=1):
            print(
                f"{index}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}, Телефон: {contact['Телефон']}")
        choice = input("Выберите номер записи для удаления: ")
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(found_contacts):
                deleted_contact = found_contacts[choice]
                phonebook.remove(deleted_contact)
                print(
                    f"Запись удалена: {deleted_contact['Фамилия']} {deleted_contact['Имя']} {deleted_contact['Отчество']}, Телефон: {deleted_contact['Телефон']}")
            else:
                print("Неправильный выбор.")
        except ValueError:
            print("Неправильный выбор.")


# Функция для экспорта данных в файл
def export_to_file():
    file_name = input("Введите имя файла для экспорта (с расширением .txt): ")
    with open(file_name, "w") as file:
        for contact in phonebook:
            file.write(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}, {contact['Телефон']}\n")
        print(f"Данные экспортированы в файл '{file_name}'.")


# Функция для импорта данных из файла
def import_from_file():
    file_name = input("Введите имя файла для импорта (с расширением .txt): ")
    phonebook.clear()
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                last_name, first_name, middle_name = parts[0].split()
                phone_number = parts[1]
                contact = {"Фамилия": last_name, "Имя": first_name, "Отчество": middle_name, "Телефон": phone_number}
                phonebook.append(contact)
        print(f"Данные импортированы из файла '{file_name}'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")


# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить запись")
    print("2. Вывести все записи")
    print("3. Поиск по характеристике")
    print("4. Редактировать запись")
    print("5. Удалить запись")
    print("6. Экспорт данных в файл")
    print("7. Импорт данных из файла")
    print("8. Выход")
    choice = input("Выберите опцию: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        attribute = input("Введите характеристику для поиска (Фамилия/Имя/Отчество/Телефон): ").capitalize()
        value = input("Введите значение: ")
        search_contacts(attribute, value)
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        export_to_file()
    elif choice == '7':
        import_from_file()
    elif choice == '8':
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
