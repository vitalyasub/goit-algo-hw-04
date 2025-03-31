def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []
            
            for line in file:
                try:
                    developer, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()}")
            
            if not salaries:
                return 0, 0
            
            total = sum(salaries)
            average = total / len(salaries)
            
            return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0


# Приклад використання:
total, average = total_salary("task1/developer_salaries.txt")
print(f"Загальна сума заробітної плати: {int(total)}, Середня заробітна плата: {int(average)}")