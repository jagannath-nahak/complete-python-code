import re

pattern="Ages"

text='''Myst V: End of Ages is a 2005 adventure video game, developed by Cyan Worlds, published by Ubisoft, and released for Macintosh and Windows PC platforms. Directed by Rand Miller (pictured) it is the fifth installment in the Myst series. Like in past entries, gameplay consists of navigating worlds known as "Ages" via the use of special books and items which act as portals. End of Ages replaces pre-rendered environments used in past games with worlds rendered in real-time 3D graphics, allowing easy navigation. It also includes an in-game camera.'''

# match=re.search(pattern,text)
# print(match)

matches=re.finditer(pattern,text)

for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])