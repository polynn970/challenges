"""
リスト：["GOT","Narusas","Vice"]
タプル：("A, Development","Friends","Always Sunny")
辞書　：{"G. Bluth II":"A, Development",
          "Barney":"NIMYM",
          "Dennis":"Always Sunny",}
"""
"""
name = "Ted"
for character in name:
    print(character)

    
shows = ["GOT","Narusas","Vice"]
for show in shows:
    print(show)
    
coms = ("A, Development","Friends","Always Sunny")
for show in coms:
    print(show)
    
people = {"G. Bluth II":"A, Development",
          "Barney":"NIMYM",
          "Dennis":"Always Sunny",}
for character in people:
    print(character)

tv = ["GOT","Narocs","vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

tc = ["GOT","nars","vicee"]
for i, new in enumerate(tv):
    new = tc[i]
    new = new.upper()
    tc[i] = new

print(tc)

tv = ["GOT","nars","vicee"]
coms = ["Arrested Development","friends","Always Sunny"]
all_shows = []
for show in tv:
    show = show.upper()
    all_shows.append(show)
for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

for i in range(1,11):
    print(i)

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy new yeah!")

for i in range(0,100):
    print(i)
    break

qs = ["what is your name","what is your fav color?","whats your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n+1) % 3

for i in range(1,6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

"""
"""
for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)
        
list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)

while input('y or n?') !='n':
    for i in range(1,6):
        print(i)
"""
"""chall
i = 0
listing = ["ウォーキンｇウデッド","アントラージュ","ザ・ソプラノズ","ヴァンパイアダイアリーズ"]
for buta in listing:
    print(buta)

for tom in range(25,51):
    print(tom)

"""
"""
list = range(0,99)
while True:
    ans = input("enter a Number(1-99) or press q to end:")
    print(ans)
    new = ans
    if new == 5:
        print("correct")
        break
    elif new != 5:
        print("Not correct")
    elif new == "q":
        print("done")
        break
    else:
        new
"""


        
"""
qs = ["what is your name","what is your fav color?","whats your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n+1) % 3
"""


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
mpy = []
for i in list1:
    for j in list2:
        mpy.append(i*j)
print(mpy)
