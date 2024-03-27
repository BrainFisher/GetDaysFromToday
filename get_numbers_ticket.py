import random


def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка на відповідність вхідних параметрів
    if not (1 <= minimum <= maximum <= 1000 and 1 <= quantity <= (maximum - minimum + 1)):
        return []  # Повертаємо пустий список, якщо вхідні дані невірні

    # Генеруємо випадкові унікальні числа та сортуємо їх
    numbers = sorted(random.sample(range(minimum, maximum + 1), quantity))
    return numbers


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
