import re

email = input("What's your email ? ").strip()

# if re.search("@", email): # ! Same  that if "@" in email
#     print("valid")
# else:
#     print("invalid")

# if re.search(".*@.*", email): # ! The combinaison .* means any chars, any number
# if re.search(".+@.+", email): # ! .+ => Any chars, at least 1
# if re.search(".+@.+.edu", email): #! Problem : The .edu will be interpreted as regex syntax
# if re.search(".+@.+\.edu", email): # ? To solve this =>  \.edu

#! GOOD HABIT TO PUT r""
"""
By Doing ".+@.+\.edu", the litteral string might interpret the trailing \.edu
As a special sequence, and that can lead to misinterpretation in a regular string
To solve this, we must indicate that the regex pattern is a RAW string by doing this :
r".+@.+\.edu"
"""
if re.search(r".+@.+\.edu", email):
# if re.search(".+@.+.edu", email):
    print("valid")
else:
    print("invalid")

"""
.           Any character expect a new line
*           0 or more repetitions
+           1 or more repetitions
?           0 or 1 repetitions
{m}         m repetitions
{m, n}      m to n repetitions
"""

"""
^           Matches the start of a string
$           Matches the end of the string
"""

# How to avoid typing multiples @ signs, there is more symtax

"""
[]          Set of characters
[^]         Complementing the set
Example
[^@]+  => Everything excluding @ at least once
"""

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")




if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

"""
\d          Decial digit [0-9]
\D          Not Decial digit [^0-9]
\s          Whitespace [ \t\n\r\f\v]
\S          Not whitespace [^ \t\n\r\f\v]
\w          Words [a-zA-Z0-9_]
\W          Not words [^a-zA-Z0-9_]

"""

"""
This version will ignore such email : MALAN@HARVARD.EDU

Regex re.search comes with a third optional argument flags witch comes
re.IGNORECASE       Treat cases insensitively
re.MULTILINE        The ^ and $ treats lines in fact, this flags bypass this
re.DOTALL           The . match everything except a new line. This flags bypass this

This allows to treat the regex differently without changing the user input
"""


if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")





if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")





if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")





