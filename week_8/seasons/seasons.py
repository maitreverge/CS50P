from datetime import date
import sys
import re

import inflect

p = inflect.engine()


class DOB:
    def __init__(self, input_date):
        # pattern to extract the days when subtracting dates
        pattern_days = r"^([\d]+) days?, "

        self._dob = input_date
        difference = str(date.today() - self._dob)
        matches = re.search(pattern_days, difference)
        
        self._days_since = 0 if matches == None else int(matches.group(1))

        self._minutes = self._days_since * 24 * 60

    def __str__(self):
        return f"{p.number_to_words(self._minutes, andword="").capitalize()} minutes"

    @classmethod
    def get_date(cls):
        prompt = input("Date of Birth ? ")
        try:
            d = date.fromisoformat(prompt)
            if d > date.today():
                raise ValueError("DOB > Today")
        except Exception as e:
            sys.exit(1)
        return cls(d)


def main():
    dob = DOB.get_date()
    print(dob)


if __name__ == "__main__":
    main()
