"""
辞書

songs = {"1":"fun",
         "2":"blue",
         "3":"me",
         "4":"floor",
         "5":"live",
        }

n = input("enter a number")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("no here")
"""
"""
コンテナinコンテナ

lists = []
rap = ["kanie","jei","eminamue",'nazu']
rock = ['a','medaka',"hage","PENIS"]
djs = ["sezded"]
lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
print(rap)

rap.append("tai")
print(rap)
print(lists)

rock.append("douuuuubaaaaaaaaaaaa")
print(lists)
"""
"""
タプル・リスト・辞書
locations = []
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

ny = {
    "座標": (40.7128, 74.0059),
    "セレブ": [
        "ウッディ・アレン",
        "ジェイ・Ｚ",
        "kevin-becon",
        ],
    "事実": {
        "州": "NewYork",
        "国": "AFRICA",
        }
    }
"""



"""
mainly zisho

musician = ["aoikoharu","becon","mikael"]
wherei = (10.10,123.985)
zisyo = {"sintyo": "200.10",
         "color": "yellow",
         "miyabe":"bravestory",
         }

thisis = input("enter a something")

if thisis in zisyo:
    print(thisis)
else:
    print("GO AWAY")

zisyo.update({"sawada":["surumeSong"]})

print(zisyo)

#set:シーケンスからの重複除去、積集合、和集合、差集合、対称差 (排他的論理和) のような数学的演算の計算が含まれます。

"""
