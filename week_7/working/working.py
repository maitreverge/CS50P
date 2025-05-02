import re


def main():
    print(convert(input("Hours: ").strip()))


def append_result(pattern, hour):
    if matches := re.search(pattern, hour):
        hours = int(matches.group(1))
        # Transform missing minutes into "00"
        ext_minutes = matches.group(2)
        minutes = "00" if ext_minutes == None else ext_minutes

        # Check if need to shift +12 hours if the specified time is PM
        is_pm = matches.group(3) == "PM"
        # Edge case for 12PM
        if is_pm and hours != 12:
            hours += 12
        # Edge case for 12AM
        elif not is_pm and hours == 12:
            hours -= 12

        return f"{hours:02}:{minutes}"
    else:
        raise ValueError


def convert(s):
    # Split the hours in two blocks, and strip both results
    hours = [hour.strip() for hour in s.split("to")]
    pattern = r"^([1-9]|0[1-9]|1[0-2])(?::([0-5][0-9]))? +(AM|PM)$"

    result = ""
    result += append_result(pattern, hours[0])
    result += " to "
    result += append_result(pattern, hours[1])

    return result


if __name__ == "__main__":
    main()
