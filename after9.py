import os
"""
print(os.path.join("User","bob","st.txt"))
"""

"""
ファイルパスを組み立てるときはosモジュールを使う

モードは、open関数がファイルを開く時にどのように動作するべきかを決定するための引数です。

r 読み込み専用
w 書き出し専用 ファイルの上書き・新規ファイルの作成
w+ 読み書き両方　ファイルの上書き・新規ファイルの作成

open関数は、ファイルオブジェクトと言われるオブジェクトを返します。
ファイルオブジェクトを介して、ファイルを読み書きできます。
モードが"w"の場合、プログラムを実行したディレクトリに、open関数によって新しいファイルが作られます。

ファイル内に日本語などの非アスキー文字を含む可能性を考えると、
常にencoding引数を指定したほうが良い

[メソッド]
write 書き込み
close 閉じる

[with文]
処理がwithブロックを抜けたときに自動的に指定した処理を実行します。
with open(ファイルパス,モード) as 変数名:
    コード
"""
"""
st = open("st.txt","w", encoding="utf-8")
st.write("こんにちは from japan!")
st.close
"""
"""
with open("st.txt","w") as f:
    f.write("(hi form python!")

with open("st.txt","r") as f:
    print(f.read())

my_list = []

with open("st.txt","r") as f:
    my_list.append(f.read())

print(my_list)
"""

"""
import csv

with open("st.csv","w", newline='') as f:
          w = csv.writer(f, delimiter=",")
          w.writerow(["one","two","three"])
          w.writerow(["four","five","six"])

with open("st.csv","r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

"""

import csv

with open("st.txt","r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

ans = input("What's your name?")

st = open("st.txt","w",encoding="utf-8")
st.write(ans)
st.close

chal = ["top gun","risky business","minority report"]
chal2 = ["titanic","the revenant","Inception"]
chal3 = ["肉体強化日","炎の中の男","飛行"]

with open("st.csv","w",encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(chal)
    w.writerow(chal2)
    w.writerow(chal3)


