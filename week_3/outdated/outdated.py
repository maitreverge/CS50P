import sys


def check_values(year, month, day, result):

    assert 1 <= year <= 9999
    assert 1 <= month <= 12
    assert 1 <= day <= 31

    result.append(year)
    result.append(month)
    result.append(day)


def parse_prompt(list_months) -> list():
    """
    The input is either formated :
    9/8/1636
    or
    September 8, 1636

    and need to return a list
    ["YYYY", "MM", "DD"]
    """

    result = list()
    while True:
        try:
            prompt = input("Date: ").strip()
            # CASE 1 : parse 9/8/1636 which is MM/DD/YYYY
            if (5 <= len(prompt) <= 10) and (prompt.count("/") == 2):
                month, day, year = map(int, prompt.split("/"))

                check_values(year, month, day, result)
                break
            elif prompt.count(",") == 1:
                # Split the first part (September 8) and the second part (1636)
                first_part, second_part = prompt.split(",")

                # Extract the month and days
                m, d = first_part.split(" ")
                # Capitalize the output to match list_months
                m = m.capitalize()

                month = list_months.index(m) + 1
                day = int(d)
                year = int(second_part)

                check_values(year, month, day, result)
                break
        except EOFError:
            sys.exit(1)
        except:
            continue

    return result


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    prompt = parse_prompt(months)

    year = prompt[0]
    month = prompt[1]
    day = prompt[2]

    # YYYY-MM-DD
    print(f"{year:04d}-{month:02d}-{day:02d}")


if __name__ == "__main__":
    main()
