""" 
問題33
2つのリストで共通の文字列を格納したリストを出力するプログラムを作成してください。
※使用するリスト :

l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']

▼期待する出力
共通する値を格納したリスト : ['Python', 'Ruby'] """

l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']

L=[]

for i in l1:
    if i in l2:
        L.append(i)

print(L)
