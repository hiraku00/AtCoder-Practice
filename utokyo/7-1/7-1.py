import pandas as pd
import numpy as np

# リストからシリーズの作成
s1 = pd.Series([0,1,2])
print(s1)

# 配列からシリーズの作成
s2 = pd.Series(np.random.rand(3))
print(s2)

# 辞書からシリーズの作成
s3 = pd.Series({0:'boo',1:'foo',2:'woo'})
print(s3)

print(f'========================================================================================= ')

# 多次元リストからデータフレームの作成
d1 = pd.DataFrame([[0,1,2],[3,4,5],[6,7,8],[9,10,11]], index=[10,11,12,13], columns=['c1','c2','c3'])
print(d1)

# 多次元配列からデータフレームの作成
d2 = pd.DataFrame(np.random.rand(12).reshape(4,3), columns=['c1','c2','c3'])
print(d2)

# 辞書からデータフレームの作成
d3 = pd.DataFrame({'Initial':['B','F','W'], 'Name':['boo', 'foo', 'woo']}, columns=['Name','Initial'])
print(d3)

print(f'================================================================================ iris 1')

# CSVファイルの読み込み
iris_d = pd.read_csv('iris.csv')

# 先頭10行のデータを表示
print(iris_d.head(10))

print(f'================================================================================ iris 2')

print(iris_d.index) #インデックスの情報
print(len(iris_d.index)) #インデックスの長さ

print(f'================================================================================ iris 3')

# データフレームの先頭5行のデータ
print(iris_d[:5])

print(f'================================================================================ iris 4')

# データフレームの終端5行のデータ
print(iris_d[-5:])

print(f'================================================================================ iris 5')

# データフレームの'species'の列の先頭10行のデータ
print(iris_d['species'].head(10))

print(f'================================================================================ iris 6')

# データフレームの'sepal_length'とspecies'の列の先頭10行のデータ
print(iris_d[['sepal_length','species']].head(10))

print(f'================================================================================ iris 7')

# データフレームの2行のデータ
print(iris_d.iloc[1])

print(f'================================================================================ iris 8')

# データフレームの2行,2列目のデータ
print(iris_d.iloc[1, 1])

# データフレームの1から5行目と1から2列目のデータ
print(iris_d.iloc[0:5, 0:2])

print(f'================================================================================ iris 9')

# データフレームの行インデックス5のデータ
print(iris_d.loc[5])

print(f'================================================================================ iris 10')

# データフレームの行インデックス5と'sepal_length'と列のデータ
print(iris_d.loc[5, 'sepal_length'])

print(f'================================================================================ iris 11')

# データフレームの行インデックス1から5と'sepal_length'とspecies'の列のデータ
print(iris_d.loc[1:5, ['sepal_length','species']])

print(f'================================================================================ iris 12')

# データフレームの'sepal_length'列の値が7より大きく、'species'列の値が3より小さいデータ
print(iris_d[(iris_d['sepal_length'] > 7.0) & (iris_d['sepal_width'] < 3.0)])

print(f'================================================================================ iris 13')

# データフレームに'mycolumn'という列を追加
iris_d['mycolumn']=np.random.rand(len(iris_d.index))
print(iris_d.head(10))

# データフレームから'mycolumn'という列を削除
del iris_d['mycolumn']
print(iris_d.head(10))

print(f'================================================================================ iris 14')

# データフレームに'mycolumn'という列を追加し新しいデータフレームを作成
myiris1 = iris_d.assign(mycolumn=np.random.rand(len(iris_d.index)))
print(myiris1.head(5))

# データフレームから'mycolumn'という列を削除し、新しいデータフレームを作成
myiris2 = myiris1.drop('mycolumn',axis=1)
print(myiris2.head(5))

print(f'================================================================================ iris 15')

# 追加する行のデータフレーム
row = pd.DataFrame([[1,1,1,1, 'setosa']], columns=iris_d.columns)

# データフレームに行を追加し新しいデータフレームを作成
myiris4 = pd.concat([iris_d, row], ignore_index=True)
print(myiris4[-2:])

# データフレームから行インデックス150の行を削除し、新しいデータフレームを作成
myiris4 = myiris4.drop(150)
print(myiris4[-2:])

print(f'================================================================================ iris 16')

# iris_dデータフレームの4つ列の値に基づいて昇順にソート
sorted_iris = iris_d.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(sorted_iris.head(10))

# iris_dデータフレームの4つ列の値に基づいて降順にソート
sorted_iris = iris_d.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],ascending=False)
print(sorted_iris.head(10))

print(f'================================================================================ iris 17')

# iris_dデータフレームの各数値列の要約統計量を表示
print(iris_d.describe())

print(f'================================================================================ iris 18')

# iris_dデータフレームの先頭5行と最終5行を連結
concat_iris = pd.concat([iris_d[:5],iris_d[-5:]])
print(concat_iris)

# iris_dデータフレームの'sepal_length'列と'species'列を連結
sepal_len = pd.concat([iris_d.loc[:, ['sepal_length']],iris_d.loc[:, ['species']]], axis=1)
print(sepal_len.head(10))

print(f'================================================================================ iris 19')

# 'sepal_length'と'species'列からなる3行のデータ
sepal_len = pd.concat([iris_d.loc[[0,51,101],['sepal_length']],iris_d.loc[[0,51,101], ['species']]], axis=1)
# 'sepal_width'と'species'列からなる3行のデータ
sepal_wid = pd.concat([iris_d.loc[[0,51,101],['sepal_width']],iris_d.loc[[0,51,101], ['species']]], axis=1)

# sepal_lenとsepal_widを'species'をキーにして結合
sepal = pd.merge(sepal_len, sepal_wid, on='species')
print(sepal)

print(f'================================================================================ iris 20')

# iris_dデータフレームの'species'の値で行をグループ化
iris_d.groupby('species')

# グループごとの先頭5行を表示
print(iris_d.groupby('species').head(5))

print(f'================================================================================ iris 21')

# グループごとの'sepal_length'列,'sepal_width'列の値の平均を表示
print(iris_d.groupby('species')[['sepal_length','sepal_width']].mean())

