from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == "__main__":
    print(f"Дата вызова функции {calculate_salary()}: {datetime.today()}")
    print(f"Дата вызова функции {get_employees()}: {datetime.today()}")