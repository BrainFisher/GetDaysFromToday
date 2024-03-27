from datetime import datetime


def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримуємо поточну дату
        current_date = datetime.today().date()
        # Розраховуємо різницю у днях
        difference = current_date - input_date
        # Повертаємо різницю у днях як ціле число
        return difference.days
    except ValueError:
        # Обробляємо помилку неправильного формату вхідних даних
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."


# Приклад використання
print(get_days_from_today("2021-10-09"))
