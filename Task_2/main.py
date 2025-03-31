def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats_list.append({"id": cat_id, "name": name, "age": age})
                else:
                    print(f"Помилка: Неправильний формат даних '{line.strip()}'")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    
    return cats_list

# Приклад використання
cats_info = get_cats_info("task2/cats_info.txt")
print(cats_info)