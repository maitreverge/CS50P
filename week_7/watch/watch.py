import re
import sys

# TEST = "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/xvFZjo5PgG0\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"

def main():
    print(parse(input("HTML: ")))
    # print(TEST)
    # print(parse(str(TEST)))


def parse(s):
    iframe_pattern = r'^<iframe.*src="([\w:/\.]+)"'
    link_pattern = r'^https?://(?:www\.)?youtube.com/embed/([\w]+)$'

    if matches := re.search(iframe_pattern, s):
        url = matches.group(1)
        print(f"EXTRACTED URL = {url}")
        if matches_2 := re.search(link_pattern, url):
            print(f"END URL = {matches_2.group(1)}")
            return f"https://youtu.be/{matches_2.group(1)}"


if __name__ == "__main__":
    main()
