from src.models.city import City

class Employee:
    def __init__(self, employee_id: int, first_name: str, middle_initial: str, last_name: str,
                 birth_date, gender: str, hire_date, city: City):
        self._id = employee_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._birth_date = birth_date
        self._gender = gender
        self._hire_date = hire_date
        self._city = city

    def full_name(self):
        return f"{self._first_name} {self._middle_initial}. {self._last_name}"

    def __str__(self):
        return f"Employee({self._id}, {self.full_name()})"

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_initial(self):
        return self._middle_initial

    @property
    def last_name(self):
        return self._last_name

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def gender(self):
        return self._gender

    @property
    def hire_date(self):
        return self._hire_date

    @property
    def city(self):
        return self._city
