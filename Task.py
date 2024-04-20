import json

# Функція для виведення вмісту JSON файлу
def display_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

# Функція для додавання нового запису у JSON файл
def add_record(file_name, record):
    with open(file_name, 'r+') as file:
        data = json.load(file)
        data.append(record)
        file.seek(0)
        json.dump(data, file, indent=4)

# Функція для видалення запису з JSON файлу за ім'ям
def delete_record_by_name(file_name, name):
    with open(file_name, 'r+') as file:
        data = json.load(file)
        filtered_data = [record for record in data if record['name'] != name]
        file.seek(0)
        json.dump(filtered_data, file, indent=4)
        file.truncate()
        print("Записи з ім'ям '{}' були успішно видалені.".format(name))

# Функція для пошуку даних у JSON файлі за полем
def search_by_field(file_name, field, value):
    with open(file_name, 'r') as file:
        data = json.load(file)
        results = [record for record in data if record.get(field) == value]
        if results:
            print("Результати пошуку:")
            for result in results:
                print(json.dumps(result, indent=4))
        else:
            print("Нічого не знайдено за вказаними критеріями.")

# Функція для визначення, чи перевищує сумарний зріст дівчат у класі зріст хлопців
def compare_heights(class_data):
    total_girls_height = sum([student['height'] for student in class_data if student['gender'] == 'female'])
    total_boys_height = sum([student['height'] for student in class_data if student['gender'] == 'male'])
    print(f"Сумарний зріст хлопців = {total_boys_height}")
    print(f"Сумарний зріст дівчат = {total_girls_height}")
    return total_girls_height > total_boys_height

# Функція для збереження результату порівняння зросту у файл result_file
def save_comparison_result(result_file, result):
    with open(result_file, 'w', encoding= 'utf-8') as file:
        json.dump({"comparison_result": result}, file, ensure_ascii=False, indent=4)

# Головна функція для виклику інших функцій у діалоговому режимі
def main():
    json_file = "class_data.json"
    result_file = "result.json"

    # Створення прикладу JSON файлу
    class_data = [
        {"name": "David", "gender": "male", "height": 190},
        {"name": "Mike", "gender": "male", "height": 185},
        {"name": "John", "gender": "male", "height": 180},
        {"name": "Bob", "gender": "male", "height": 175},
        {"name": "Emily", "gender": "female", "height": 173},
        {"name": "Tom", "gender": "male", "height": 172},
        {"name": "Eve", "gender": "female", "height": 170},
        {"name": "Alice", "gender": "female", "height": 168},
        {"name": "Sophia", "gender": "female", "height": 162},
        {"name": "Sara", "gender": "female", "height": 160}
    ]

    # Запис прикладу даних у JSON файл
    with open(json_file, 'w') as file:
        json.dump(class_data, file, indent=4)

    while True:
        print("\nМеню:")
        print("1. Виведення вмісту JSON файлу")
        print("2. Додавання нового запису у JSON файл")
        print("3. Видалення запису з JSON файлу за ім'ям")
        print("4. Пошук даних у JSON файлі за полем")
        print("5. Порівняння зросту учнів")
        print("6. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            display_json(json_file)
        elif choice == '2':
            name = input("Введіть ім'я нового учня: ")
            gender = input("Введіть стать нового учня (male/female): ")
            height = int(input("Введіть зріст нового учня: "))
            new_record = {"name": name, "gender": gender, "height": height}
            add_record(json_file, new_record)
        elif choice == '3':
            name_to_delete = input("Введіть ім'я запису для видалення: ")
            delete_record_by_name(json_file, name_to_delete)
        elif choice == '4':
            field = input("Введіть поле для пошуку: ")
            value = input("Введіть значення для поля: ")
            search_by_field(json_file, field, value)
        elif choice == '5':
            # Отримання оновлених даних про клас
            with open(json_file, 'r') as file:
                class_data = json.load(file)
            comparison_result = compare_heights(class_data)
            if comparison_result:
                result_string = "Сумарний зріст дівчат перевищує зріст хлопців."
            else:
                result_string = "Сумарний зріст дівчат не перевищує зріст хлопців."
            save_comparison_result(result_file, result_string)
            print(result_string)
            print("Результат порівняння зросту успішно записано у файл {}.".format(result_file))
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
