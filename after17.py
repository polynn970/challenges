import re

l = "Beautiful is beetter than ugly"

matches = re.findall("Beautiful", l)

print(matches)


match = re.findall("beautiful", l, re.IGNORECASE)
print(match)




zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

m= re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too."
ma = re.findall("t[ow]o", string, re.IGNORECASE)
print(ma)

line = "123 hi 34 hello."
man = re.findall("\d", line, re.IGNORECASE)
print(man)


