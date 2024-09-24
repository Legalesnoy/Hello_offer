from typing import Optional


class Replica:
    def __init__(self, replica: str = '', expected_responses: Optional[dict] = None, wrong_answer='', sep='/'):
        self._expected_responses = {}
        self.replica = replica
        self.expected_responses = expected_responses if expected_responses else {}
        self.wrong_answer = wrong_answer
        self.sep = sep
        if expected_responses:
            for k, v in expected_responses.items():
                self._expected_responses[k.lower()] = v

    def __call__(self, *args, **kwargs):
        if not self._expected_responses:
            print(self.__str__())
            return ''

        response = input(self.__str__())
        if self._expected_responses:
            while True:
                result = self._expected_responses.get(response.lower(), None)
                if result is not None:
                    if callable(result):
                        return result()
                    return result

                if self.wrong_answer != '':
                    if callable(self.wrong_answer):
                        return self.wrong_answer()
                    return self.wrong_answer
                else:
                    response = input(self.__str__())

    def __str__(self):
        if not self.expected_responses:
            return f'{self.replica}'

        else:
            return f'{self.replica} ({self.sep.join([resp for resp in self.expected_responses])})'

class Dialogue:

    ...


class Scenario():
    ...

if __name__ == '__main__':
    rep1 = Replica('А пиво будешь?', {"да": "!", "Нет": "?!"})
    rep1 = Replica('А пиво будешь?', {"да": "!", "Нет": "?!"}, rep1)
    rep2 = Replica('Чай, кофе?', {'чай': 'ок, чай', 'кофе': 'ок, кофе', 'нет': rep1}, rep1)
    rep3 = Replica('1111111')
    print(rep3())
