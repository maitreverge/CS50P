# Goal here is to extract the username from an URL:
# Example : https://twitter.com/davidmalan
import re 

# username = url.replace("https://twitter.com/", "")
url = input("URL : ").strip()

"""
sub stands 

re.sub(pattern, repl, string, count=0, flags=0)
Pattern : Regex pattern we're looking for
repl : What do you want to replace the string with
string : Target string where to do the remplacement

"""

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(username)

"""
This regex is then sensitive to other domain names such as google.com
"""

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)

if matches :
    print(f"Username: {matches.group(1)}")

