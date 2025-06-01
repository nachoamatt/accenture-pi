class Country:
    def __init__(self, country_id: int, name: str, code: str):
        self._id = country_id
        self._name = name
        self._code = code

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code
