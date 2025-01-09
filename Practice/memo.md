# Python 演習38問

[【Python練習問題50問+演習38問+解答】初心者から上級者まで！でPythonを極める演習38問](https://odigo.jp/%E3%80%90python%E7%B7%B4%E7%BF%92%E5%95%8F%E9%A1%8C50%E5%95%8F%E6%BC%94%E7%BF%9238%E5%95%8F%E3%80%91%E5%88%9D%E5%BF%83%E8%80%85%E3%81%8B%E3%82%89%E4%B8%8A%E7%B4%9A%E8%80%85%E3%81%BE%E3%81%A7%EF%BC%81/#toc53)

<br>

---
# 02

辞書型（dictionary）を直接sortすることはできませんが、以下の方法で辞書のキーや値でソートすることができます：

1. キーでソートする場合：
```python:Practice/02.py
# ... existing code ...
sorted_by_keys = dict(sorted(a.items()))
# または特定の順序で結果を見たい場合：
sorted_items = sorted(a.items())  # タプルのリストとして取得
```

2. 値でソートする場合：
```python:Practice/02.py
# ... existing code ...
sorted_by_values = dict(sorted(a.items(), key=lambda x: x[1]))
```

説明：
- `sort()`はリストのメソッドで、辞書には使用できません
- `sorted()`関数を使用して、辞書の`items()`をソートします
- `key=lambda x: x[1]`を使用すると値でソートできます
- 結果を再び辞書に変換するには`dict()`を使用します

例えば、値でソートした結果は以下のようになります：
```python
# 結果
{'banana': 2, 'apple': 5, 'cherry': 8}
```

## [補足] `lambda x: x[1]` の説明

このコードは辞書をその値に基づいてソートしています。`key=lambda x: x[1]`の部分は、ソートの基準を指定するためのものです。以下に詳しく説明します：

1. `lambda x: x[1]`は、各要素の2番目の項目（値）を返す小さな関数です[1][4]。

2. `x`は辞書の各項目（キーと値のペア）を表します。

3. `x[1]`は、そのペアの2番目の要素、つまり値を指します[2]。

   - 例：`("apple", 5)`というペアでは、`x`は"apple"（キー）、`x[1]`は5（値）になります。

4. `sorted()`関数は、この`lambda`関数を使って各項目の値（数字）を比較し、小さい順に並べ替えます[3]。

つまり、このコードは辞書`a`の項目を、値（数字）の小さい順に並べ替えて新しい辞書を作成します。結果は以下のようになります：

```python
{'banana': 2, 'apple': 5, 'cherry': 8}
```

この方法を使うと、辞書の値に基づいて簡単にソートすることができます[5]。

<br>
<br>

---
# 03

このコードは、リスト `a` の数字の出現頻度を辞書で返します。

ここで、コードを説明していきます。

1. `return {num: a.count(num) for num in a}`: ここで、次のことを行います。
 * `for num in a`: ここで、リスト `a` の各数字を `num` という変数に代入します。
 * `a.count(num)`: ここで、リスト `a` に `num` という数字が何回出現したかを調べます。
 * `{num: ...}`: ここで、結果を辞書で返します。`num` というキーに、前のステップで取得した値を設定します。
2. `print(num2freq(a))`: ここで、`num2freq` 関数を呼び出し、リスト `a` の数字の出現頻度を出力します。

例えば、リスト `a = [1, 2, 3, 1, 2, 1, 4, 5, 2]` の場合、次のようになります。

* `num = 1` の場合、`a.count(num)` は `3` を返します。つまり、リスト `a` に `1` という数字が 3 回出現したことになります。
* `num = 2` の場合、`a.count(num)` は `3` を返します。つまり、リスト `a` に `2` という数字が 3 回出現したことになります。
* `num = 3` の場合、`a.count(num)` は `1` を返します。つまり、リスト `a` に `3` という数字が 1 回出現したことになります。
* `num = 4` の場合、`a.count(num)` は `1` を返します。つまり、リスト `a` に `4` という数字が 1 回出現したことになります。
* `num = 5` の場合、`a.count(num)` は `1` を返します。つまり、リスト `a` に `5` という数字が 1 回出現したことになります。

最終的に、`num2freq` 関数は次の値を返します。

```python
{1: 3, 2: 3, 3: 1, 4: 1, 5: 1}
```

これは、リスト `a` の数字の出現頻度を表しています。

<br>
<br>

---
# 05

AとBのJaccard係数を計算するには、次の手順を実行します。

1. AとBの積集合を計算します。積集合は、AとBの両方に含まれる要素の集合です。

- A ∩ B = {“apple”, “cherry”}

2. AとBの和集合を計算します。和集合は、AとBの両方に含まれる要素の集合です。

- A ∪ B = {“apple”, “banana”, “cherry”, “orange”}

3. AとBの積集合の要素数を計算します。

- |A ∩ B| = 2

4. AとBの和集合の要素数を計算します。

- |A ∪ B| = 4

5. Jaccard係数を計算します。

Jaccard係数 = |A ∩ B| / |A ∪ B| = 2 / 4 = 0.5

したがって、AとBのJaccard係数は0.5です。

---

```python:Practice/05.py
def jaccard(a, b):
    return len(a & b) / len(a | b)

A = {"apple", "banana", "cherry"}
B = {"apple", "cherry", "orange"}
print(f"A & B : {len(A & B)}: {A & B}")
print(f"A | B : {len(A | B)}: {A | B}")
print(f"Jaccard係数 = |A ∩ B| / |A ∪ B| = {len(A & B)} / {len(A | B)} = {jaccard(A, B)}")
```

この値は、AとBの両方に含まれる要素の割合を表しています。


`len(a & b)` と `len(a | b)` は、集合 `a` と `b` の積集合と和集合の要素数を表します。

* `a & b` は集合 `a` と `b` の積集合を表します。積集合は、集合 `a` と `b` の両方に含まれる要素の集合です。`len(a & b)` は、積集合の要素数を表します。
* `a | b` は集合 `a` と `b` の和集合を表します。和集合は、集合 `a` と `b` の両方に含まれる要素の集合です。`len(a | b)` は、和集合の要素数を表します。

このコードでは、`len(a & b)` と `len(a | b)` は、次の式を評価するために使用されています。

`Jaccard係数 = |A ∩ B| / |A ∪ B| = len(A & B) / len(A | B)`

この式は、集合 `A` と `B` のJaccard係数を計算します。Jaccard係数は、積集合の要素数を和集合の要素数で割った値です。

`len(a & b)` と `len(a | b)` は、次の値を表します。

* `len(A & B) = 2` (積集合の要素数)
* `len(A | B) = 4` (和集合の要素数)

したがって、Jaccard係数は次のようになります。

`Jaccard係数 = len(A & B) / len(A | B) = 2 / 4 = 0.5`

この結果は、集合 `A` と `B` の積集合が 2 つの要素、和集合が 4 つの要素、Jaccard係数が 0.5 であることを示しています。

<br>
<br>

---
# 11

このコードは、Pythonの公式ブログ（`https://www.python.org/blogs/`）から、最近のブログ記事のタイトルとURLを取得するプログラムです。

**1. ライブラリのインポート**

```python
import requests
from bs4 import BeautifulSoup
from typing import Iterator, Tuple
from urllib.parse import urljoin
```

* `requests`: ウェブサイトにアクセスしてHTMLデータを取得するためのライブラリです。  ブラウザでURLを入力してEnterキーを押す操作を、プログラムで行うようなものです。
* `BeautifulSoup`: 取得したHTMLデータを解析し、必要な情報を取り出すためのライブラリです。  HTMLデータは人間には読みにくいので、BeautifulSoupを使って整理されたデータ構造に変換します。
* `typing`:  型ヒントと呼ばれる機能を使うためのライブラリです。  型ヒントを使うと、変数や関数の値の型を指定することで、コードの可読性や保守性を向上させることができます。  初心者のうちはあまり気にしなくても構いません。
* `urllib.parse`: URLを操作するためのライブラリです。 特に、相対URLを絶対URLに変換するために使用します。 例えば、`/blogs/news/` のような相対URLを `https://www.python.org/blogs/news/` のような絶対URLに変換します。


**2. 関数 `scope_articles` の定義**

```python
def scope_articles(base_url: str = "https://www.python.org/blogs/") -> Iterator[Tuple[str, str]]:
    ...
```

* `def scope_articles(...)`:  `scope_articles` という名前の関数を定義しています。関数は、特定の処理をまとめて再利用可能な形にしたものです。
* `base_url: str = "https://www.python.org/blogs/"`:  関数の引数 `base_url` を定義しています。 `base_url` はスクレイピング対象のURLを指定するための引数で、デフォルト値としてPythonの公式ブログのURLが設定されています。  `: str` は型ヒントで、`base_url` が文字列型(`str`)であることを示しています。
* `-> Iterator[Tuple[str, str]]`: これも型ヒントで、関数が返す値の型を指定しています。 `Iterator` はイテレータと呼ばれるもので、順番に値を返すことができます。 `Tuple[str, str]` は、文字列型の値を2つ持つタプルを意味します。 つまり、この関数は、(タイトル, URL) のタプルを順番に返すイテレータを返します。

**3.  HTTPリクエストの送信とHTMLデータの取得**

```python
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        ...
```

* `headers = {'User-Agent': 'Mozilla/5.0'}`:  `User-Agent` を設定しています。  `User-Agent` は、ウェブサイトにアクセスする際に、自分がどんなブラウザを使っているかを伝える情報です。  一部のウェブサイトでは、`User-Agent` が設定されていないアクセスを拒否することがあります。
* `try...except`: エラー処理を行うための構文です。 `try` ブロック内のコードを実行中にエラーが発生した場合、`except` ブロック内のコードが実行されます。
* `response = requests.get(base_url, headers=headers, timeout=10)`:  `requests.get()` 関数を使って、指定したURLにアクセスし、HTMLデータを取得します。 `timeout=10` は、10秒以内に応答がなければタイムアウトするように設定しています。  取得したHTMLデータは `response` オブジェクトに格納されます。
* `response.raise_for_status()`:  HTTPリクエストが成功したかどうかを確認します。  もしリクエストが失敗した場合（例えば、404エラーなど）、例外を発生させます。

**4. BeautifulSoupによるHTML解析**

```python
        soup = BeautifulSoup(response.text, "html.parser")
        ...
```

* `soup = BeautifulSoup(response.text, "html.parser")`:  `BeautifulSoup` を使って、取得したHTMLデータを解析します。  `response.text` は、`response` オブジェクトからHTMLデータ（文字列）を取り出しています。 `"html.parser"` は、HTMLを解析するためのパーサーを指定しています。  解析結果は `soup` オブジェクトに格納されます。  `soup` オブジェクトを使えば、HTMLの要素に簡単にアクセスできます。


**5. 記事情報の抽出とyield**

```python
        for article in soup.select("ul.list-recent-posts li a"):
            title = article.text.strip()
            url = urljoin(base_url, article.get("href"))
            yield (title, url)
```

* `for article in soup.select("ul.list-recent-posts li a"):`:  `soup.select()` メソッドを使って、CSSセレクタ `"ul.list-recent-posts li a"` に一致するHTML要素を全て取得します。  このセレクタは、ブログ記事のリスト (`<ul class="list-recent-posts">`) 内の各記事 (`<li>`) 内のリンク (`<a>`) を選択します。 取得した要素はリストとして返され、`for` ループで順番に処理されます。  各ループでは、`article` 変数に `<a>` タグの要素が代入されます。
* `title = article.text.strip()`:  `article.text` で `<a>` タグ内のテキスト（記事のタイトル）を取得します。  `strip()` は、テキストの先頭と末尾にある空白文字を取り除きます。
* `url = urljoin(base_url, article.get("href"))`:  `article.get("href")` で `<a>` タグの `href` 属性の値（記事へのリンク）を取得します。 `urljoin(base_url, ...)` は、取得したリンクが相対パスの場合、`base_url` を使って絶対パスに変換します。 例えば、`href` 属性が `/blogs/news/new-feature/` で、`base_url` が `https://www.python.org/blogs/` の場合、`urljoin` は `https://www.python.org/blogs/news/new-feature/` を返します。
* `yield (title, url)`:  `yield` キーワードを使って、`title` と `url` をタプルとして返します。  `yield` を使うと、関数はジェネレータ関数になります。 ジェネレータ関数は、`for` ループで反復処理されるたびに、`yield` で指定された値を1つずつ返します。 全ての値を一度に返すのではなく、順番に値を返すことで、メモリ効率を良くすることができます。

**6. エラー処理**

```python
    except requests.RequestException as e:
        print(f"Request failed: {e}")
```
*  `requests.exceptions.RequestException as e`:  `requests` ライブラリで発生する可能性のある例外（エラー）をキャッチします。 例外が発生した場合、`e` に例外オブジェクトが代入されます。
* `print(f"Request failed: {e}")`: 例外が発生した場合にエラーメッセージを出力します。


**7. メインブロック**

```python
if __name__ == "__main__":
    for title, link in scope_articles():
        print(f"Title: {title}")
        print(f"URL: {link}")
        print("-" * 50)

```

* `if __name__ == "__main__":`:  このブロック内のコードは、スクリプトが直接実行された場合のみ実行されます。  他のスクリプトからインポートされた場合は実行されません。
* `for title, link in scope_articles():`:  `scope_articles()` 関数を呼び出し、返されたジェネレータオブジェクトを `for` ループで反復処理します。 各ループでは、`yield` で返された `(title, url)` のタプルが `title` 変数と `link` 変数に代入されます。
* `print(...)`:  各記事のタイトルとURLを出力します。


このコードを実行すると、Pythonの公式ブログの最近のブログ記事のタイトルとURLが順番に出力されます.

<br>
<br>

## [補足] `yield` の説明

`scrape_python_blogs` 内で `for` ループを使って記事情報を取得し、`main` ブロックでも `for` ループを使って出力しているので、二重ループのように見えます。

しかし、`scrape_python_blogs` は**ジェネレータ関数**であるため、`return` で値を返すのではなく、`yield` で値を生成します。ジェネレータ関数は、呼び出されたときに一度に全ての値を生成するのではなく、`for` ループで反復されるたびに1つずつ値を生成します。

そのため、`scrape_python_blogs()` を呼び出すと、ジェネレータオブジェクトが返されます。このオブジェクトは、`for` ループで反復処理することで、`yield` で生成された値を順番に取得できます。

`main` ブロックの `for` ループは、`scrape_python_blogs()` が生成したジェネレータオブジェクトを反復処理し、`yield` で生成された `(title, link)` のタプルを1つずつ受け取っています。

つまり、`main` ブロックの `for` ループは、`scrape_python_blogs` 内の `for` ループが**全て完了した後に実行されるのではなく**、`scrape_python_blogs` が1つの記事情報を `yield` するたびに実行されます。

例を挙げて説明します。`scrape_python_blogs` が3つの記事情報を `yield` すると仮定します。

1. `scrape_python_blogs` が1つ目の記事情報を `yield` します。
2. `main` ブロックの `for` ループが実行され、1つ目の記事情報が出力されます。
3. `scrape_python_blogs` が2つ目の記事情報を `yield` します。
4. `main` ブロックの `for` ループが実行され、2つ目の記事情報が出力されます。
5. `scrape_python_blogs` が3つ目の記事情報を `yield` します。
6. `main` ブロックの `for` ループが実行され、3つ目の記事情報が出力されます。
7. `scrape_python_blogs` が全ての情報を `yield` し終えると、`main` ブロックの `for` ループも終了します。

このように、ジェネレータ関数を使うことで、全てのデータを一度にメモリに格納する必要がなく、効率的に処理できます。  また、`scrape_python_blogs` と `main` ブロックの処理を分離することで、コードの可読性と保守性も向上します。


ジェネレータを使用しない場合、`scrape_python_blogs` は全てのデータをリストに格納して返し、`main` ブロックでそのリストをループ処理する必要があります。  これでは、大量のデータがある場合にメモリ消費量が増加する可能性があります。 ジェネレータを使用することで、データを逐次的に処理できるため、メモリ効率が向上します。

## [補足] `soup.select("ul.list-recent-posts li a")` の説明

`soup.select("ul.list-recent-posts li a")` がどのようにHTMLから記事のタイトルとリンクを取得しているか、具体的に説明します。

提供いただいたHTMLを例に、`soup.select()` がどのように要素を選択するのか、段階的に見ていきましょう。

1. **`ul.list-recent-posts`**:  まず、`ul.list-recent-posts` は、`class="list-recent-posts"` を持つ `<ul>` タグを探します。提供されたHTMLには、この条件に一致する `<ul>` タグが1つあります。

   ```html
   <ul class="list-recent-posts menu">
       ...
   </ul>
   ```

2. **`ul.list-recent-posts li`**:  次に、`li` が追加されます。これは、先ほど見つかった `<ul class="list-recent-posts menu">` の**直接の子要素**である `<li>` タグを全て探します。 提供されたHTMLでは、この `<ul>` タグの中に5つの `<li>` タグがあります。

   ```html
   <ul class="list-recent-posts menu">
       <li> ... </li>
       <li> ... </li>
       <li> ... </li>
       <li> ... </li>
       <li> ... </li>
   </ul>
   ```

3. **`ul.list-recent-posts li a`**: 最後に、`a` が追加されます。これは、上記で見つかった5つの `<li>` タグそれぞれ**直接の子要素**である `<a>` タグを探します。 各 `<li>` タグの中には1つの `<a>` タグがあるので、合計5つの `<a>` タグが見つかります。

   例えば、最初の `<li>` タグの中の `<a>` タグは以下です。

   ```html
   <li>
       <h3 class="event-title">
           <a href="https://pythoninsider.blogspot.com/2024/12/python-3140-alpha-3-is-out.html">
               Python 3.14.0 alpha 3 is out
           </a>
       </h3>
       ...
   </li>
   ```


このように、`soup.select("ul.list-recent-posts li a")` は、`class="list-recent-posts"` を持つ `<ul>` タグの子要素の `<li>` タグの子要素の `<a>` タグ、つまり記事へのリンクを正確に選択します。  そして、`select()` メソッドは、見つかった5つの `<a>` タグをリストとして返します。

コードでは、このリストを `for` ループで処理し、各 `<a>` タグから `article.text` で記事タイトル、`article.get("href")` でリンクURLを取得しています。


重要なのは、各段階で**直接の子要素**を探している点です。 例えば、`<ul>` タグの孫要素である `<a>` タグは選択されません。  これにより、意図しない要素が選択されることを防ぎ、必要な情報だけを正確に取得できます。


これが、`soup.select("ul.list-recent-posts li a")` がHTMLから記事情報を取得する仕組みです。

<br>
<br>

---

# 13

**1. ライブラリのインポート**

```python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
```
- `import numpy as np`: `numpy` ライブラリを `np` という名前でインポートします。NumPyは、数値計算を効率的に行うためのライブラリで、特に多次元配列（行列）の操作に便利です。
- `from sklearn.linear_model import LinearRegression`: `scikit-learn` ライブラリから `LinearRegression` クラスをインポートします。これは、線形回帰モデルを作成・学習するためのクラスです。
- `import matplotlib.pyplot as plt`: `matplotlib.pyplot` モジュールを `plt` という名前でインポートします。これは、グラフを描画するためのライブラリです。

**2. データ準備**

```python
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])
```
- `x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)`: 入力データ `x` をNumPy配列に変換しています。`.reshape(-1, 1)` は、配列を2次元配列に変換しています。ここで `-1` は、残りの次元を自動で計算するように指示しています。`1` は列の数を1にするという意味です。`scikit-learn` の `fit` メソッドに渡すデータは、2次元配列である必要があるため、このような変換を行っています。
- `y = np.array([2, 4, 5, 4, 5])`: 出力データ `y` をNumPy配列に変換しています。

**3. 線形回帰モデルの作成と学習**

```python
model = LinearRegression()
model.fit(x, y)
```
- `model = LinearRegression()`: `LinearRegression` クラスのインスタンスを作成し、`model` 変数に格納します。これが線形回帰モデルのオブジェクトとなります。
- `model.fit(x, y)`: モデルを学習データ `x` と `y` を使って学習させます。この `fit` メソッドが、データに基づいて回帰直線の係数（傾きと切片）を計算します。

**4. 予測**

```python
x_pred = np.array([3.5]).reshape(-1, 1)
y_pred = model.predict(x_pred)
print(y_pred)
```
- `x_pred = np.array([3.5]).reshape(-1, 1)`: 予測したい `x` の値 (3.5) をNumPy配列に変換し、`reshape(-1, 1)` で2次元配列にしています。 `scikit-learn` の `predict` メソッドに渡すデータも2次元配列である必要があるため、このような変換を行っています。
- `y_pred = model.predict(x_pred)`: 学習済みのモデル `model` を使って、`x_pred` に対する `y` の値を予測します。
- `print(y_pred)`: 予測結果 `y_pred` を表示します。

**5. グラフ描画**

```python
x_plot = np.linspace(0, 6, 100).reshape(-1, 1)
y_plot = model.predict(x_plot)
plt.scatter(x, y, label="data")
plt.plot(x_plot, y_plot, label="regression", color="red")
plt.scatter(x_pred, y_pred, label="prediction", color="green")
plt.legend()
plt.show()
```
- `x_plot = np.linspace(0, 6, 100).reshape(-1, 1)`: 0から6までの範囲で100個の値を生成し、NumPy配列に変換します。`.reshape(-1, 1)` は、2次元配列に変換します。これは、回帰直線を描画するための `x` 座標のセットです。
- `y_plot = model.predict(x_plot)`: 生成した `x_plot` の値に対応する `y` の予測値を計算します。
- `plt.scatter(x, y, label="data")`: 学習データ `x` と `y` を散布図としてプロットします。`label="data"` は凡例に表示するためのラベルです。
- `plt.plot(x_plot, y_plot, label="regression", color="red")`: 回帰直線を描画します。`label="regression"` は凡例に表示するためのラベルで、`color="red"` は線の色を赤色に指定します。
- `plt.scatter(x_pred, y_pred, label="prediction", color="green")`: 予測点 `(x_pred, y_pred)` を散布図としてプロットします。`label="prediction"` は凡例に表示するためのラベルで、`color="green"` は点の色を緑色に指定します。
- `plt.legend()`: グラフに凡例を表示します。
- `plt.show()`: グラフを表示します。

**コードのまとめ**

このコードは、与えられたデータに対して線形回帰モデルを学習し、指定された `x` の値に対する `y` の値を予測します。さらに、元のデータ、回帰直線、予測点をグラフで視覚的に表示します。`scikit-learn` ライブラリを使って線形回帰モデルを簡単に構築・利用できること、`matplotlib` ライブラリを使ってグラフを簡単に描画できることを示しています。

## [補足] reshape(-1, 1)をする理由と、その効果について

### reshape(-1, 1)とは？

`reshape(-1, 1)` は、NumPy配列の形状を調整する関数であるreshape()を用いた操作です。

* **-1の意味:** reshape()の引数に-1を指定すると、その次元における要素の数が自動的に計算されます。つまり、他の次元の要素数から、-1の部分の要素数が決まるということです。
* **(1)の意味:** 2番目の引数の1は、新しい配列の列数が1になることを意味します。

### reshape(-1, 1)をする理由

scikit-learnのような機械学習ライブラリでは、多くのモデルが2次元配列を期待します。特に、特徴量（説明変数）は、サンプル数×特徴量数の2次元配列として与えることが一般的です。

今回の例では、`x`は5つの数値の1次元配列ですが、`reshape(-1, 1)`によって、行数が5、列数が1の2次元配列に変換されます。これにより、scikit-learnの`LinearRegression`モデルに直接入力できる形式になります。

### reshape(-1, 1)の前後での値の変化

reshape操作は、配列の要素の値自体は変更しません。あくまで、配列の形状（行数と列数）のみを変更します。

**例:**

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])  # 元の配列
print(x.shape)  # (5,)

x_reshaped = x.reshape(-1, 1)
print(x_reshaped)
print(x_reshaped.shape)  # (5, 1)
```

上記のコードを実行すると、以下の出力が得られます。

```
(5,)
[[1]
 [2]
 [3]
 [4]
 [5]]
(5, 1)
```

* `x`は、形状が(5,)の1次元配列です。
* `x_reshaped`は、reshape操作によって形状が(5, 1)の2次元配列に変換されています。しかし、要素の値自体は元の`x`と同じです。

### まとめ

reshape(-1, 1)は、1次元配列をscikit-learnなどの機械学習ライブラリで扱いやすい2次元配列に変換するための一般的な手法です。特に、特徴量をモデルに入力する際に、この操作を行うことが多く見られます。

**ポイント:**

* reshape(-1, 1)は、要素の値を変更するのではなく、配列の形状を変更します。
* -1は、その次元の要素数を自動的に計算することを意味します。
* scikit-learnの多くのモデルは、特徴量を2次元配列として期待します。

この操作を理解することで、よりスムーズに機械学習のモデルを構築することができます。

<br>
<br>

---

# 17

- devcontainer.json の `"dockerFile": "Dockerfile"` を `"dockerFile": ".devcontainer/Dockerfile",` へ変更
```json
{
  "name": "AtCoder",
  // "dockerFile": "Dockerfile",
  "dockerFile": ".devcontainer/Dockerfile",
  "extensions": ["ms-python.python"]
}
```

- Dockerfile の `RUN pip install flask` 以降をコメントアウト
```Dockerfile
・・・
# Flaskのインストール
RUN pip install flask

# アプリケーションのディレクトリ作成
WORKDIR /app

RUN ls -la #  ls -la コマンドを追加

# ホストのファイルをコンテナにコピー (Practice/17の中身をコピー)
# ビルドコンテキストから見たパスを指定
COPY ./Practice/17 /app

# ポート番号を指定
EXPOSE 5000

# Flask アプリケーションの実行
CMD ["python", "app.py"]
```

- ターミナル（ローカル）から各 docker コマンドを実行する。
```bash
docker build --no-cache -t my-flask-app -f .devcontainer/Dockerfile .
docker run -d -p 8000:5000 my-flask-app
```

- http://localhost:8000/ にアクセスする。

<br>
<br>

---

# 21.py

```python
import threading

def fizzbuzz(start, end):
    for i in range(start, end+ 1 ):
        if i % 15 == 0:
            print(f"{threading.current_thread().name} : FizzBuzz")
        elif i % 3 == 0:
            print(f"{threading.current_thread().name} : Fizz")
        elif i % 5 == 0:
            print(f"{threading.current_thread().name} : Buzz")
        else:
            print(f"{threading.current_thread().name} : {i}")

if __name__ == "__main__":
    threads = []
    threads.append(threading.Thread(target=fizzbuzz, args=(1, 33), name="Thread1"))
    threads.append(threading.Thread(target=fizzbuzz, args=(36, 66), name="Thread2"))
    threads.append(threading.Thread(target=fizzbuzz, args=(67, 100), name="Thread3"))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
```

## マルチスレッド処理の基本：複数の処理を同時に進める

このプログラムは、複数の処理を「同時に」行うために、Pythonの `threading` モジュールを利用しています。

### 1. `import threading`：マルチスレッド機能を使う準備

```python
import threading
```

まず、`import threading` という行から始まります。これは、Pythonに「これからマルチスレッド機能を使いますよ」と伝えるための宣言です。`threading` モジュールには、複数の処理の流れ（スレッド）を制御するための機能がまとめられています。

### 2. `def fizzbuzz(start, end):`：スレッドで実行する処理を定義

```python
def fizzbuzz(start, end):
    for i in range(start, end+ 1 ):
        if i % 15 == 0:
            print(f"{threading.current_thread().name} : FizzBuzz")
        elif i % 3 == 0:
            print(f"{threading.current_thread().name} : Fizz")
        elif i % 5 == 0:
            print(f"{threading.current_thread().name} : Buzz")
        else:
            print(f"{threading.current_thread().name} : {i}")
```

次に、`def fizzbuzz(start, end):` という部分で、スレッドで実行する具体的な処理を定義しています。この `fizzbuzz` 関数は、指定された範囲 (`start` から `end` まで) の数値に対して、FizzBuzzのルールに従って結果を出力する処理を行います。

- `for i in range(start, end + 1):`: この行は、`start` から `end` までの数値を順番に処理するためのループです。
- `if i % 15 == 0:`、`elif i % 3 == 0:`、`elif i % 5 == 0:`、`else:`: これらの条件分岐は、FizzBuzzのルールに従って出力する内容を決定します。ここではFizzBuzzの具体的な説明は割愛しますが、それぞれの条件に応じて "FizzBuzz"、"Fizz"、"Buzz"、または数値を表示します。
- `print(f"{threading.current_thread().name} : ...")`: この行は、現在のスレッドの名前と出力結果を表示します。`threading.current_thread().name` で、どのスレッドがこの出力を行ったかを確認できます。

### 3. `if __name__ == "__main__":`：プログラムの実行開始点

```python
if __name__ == "__main__":
    # ... スレッドの作成と開始、終了待ち処理 ...
```

`if __name__ == "__main__":` という部分は、Pythonスクリプトが直接実行された場合にのみ、その中のコードが実行されるようにするための決まり文句です。

### 4. スレッドオブジェクトの作成とリストへの追加

```python
threads = []
threads.append(threading.Thread(target=fizzbuzz, args=(1, 33), name="Thread1"))
threads.append(threading.Thread(target=fizzbuzz, args=(36, 66), name="Thread2"))
threads.append(threading.Thread(target=fizzbuzz, args=(67, 100), name="Thread3"))
```

ここでは、3つのスレッドオブジェクトを作成し、`threads` というリストに追加しています。

- `threads = []`: 空のリスト `threads` を作成し、後で作成するスレッドオブジェクトを格納するために使用します。
- `threading.Thread(target=fizzbuzz, args=(1, 33), name="Thread1")`:  `threading.Thread()` を使って新しいスレッドオブジェクトを作成します。
    - `target=fizzbuzz`: このスレッドで実行する関数として、先ほど定義した `fizzbuzz` 関数を指定します。
    - `args=(1, 33)`: `fizzbuzz` 関数に渡す引数をタプルで指定します。この場合、`start` に `1`、`end` に `33` が渡されます。つまり、"Thread1" は 1 から 33 までの数値を処理します。
    - `name="Thread1"`: スレッドに "Thread1" という名前を付けます。これにより、どのスレッドが処理を行っているか区別できます。
- 同様の処理で、"Thread2" は 36 から 66 まで、"Thread3" は 67 から 100 までの数値を処理するスレッドオブジェクトが作成されます。

### 5. スレッドの開始

```python
for thread in threads:
    thread.start()
```

このループは、`threads` リストに格納されている各スレッドオブジェクトに対して `start()` メソッドを呼び出します。`start()` メソッドが呼び出されると、新しいスレッドが生成され、`target` で指定した関数 (`fizzbuzz`) の実行が開始されます。重要なのは、この時点で各スレッドは（見かけ上）同時に処理を開始するということです。

### 6. スレッドの終了待ち

```python
for thread in threads:
    thread.join()
```

このループは、`threads` リストに格納されている各スレッドオブジェクトに対して `join()` メソッドを呼び出します。`join()` メソッドは、そのスレッドの処理が完了するまで、現在のスレッド（この場合はメインスレッド）の実行を一時停止させます。言い換えれば、この部分でプログラムは、すべてのスレッドが処理を終えるのを待ってから次の処理に進むようになります。もし `join()` がないと、メインスレッドは子スレッドの完了を待たずにプログラムが終了してしまう可能性があります。

### まとめ：マルチスレッドによる並行処理

このコードは、`threading` モジュールを使って複数のスレッドを作成し、それぞれに `fizzbuzz` 関数を実行させることで、処理を並行して行う方法を示しています。各スレッドは指定された範囲の数値を独立して処理し、その結果を出力します。`start()` メソッドでスレッドを開始し、`join()` メソッドでスレッドの完了を待つ、というのがマルチスレッド処理の基本的な流れです。この並行処理によって、全体としての処理時間を短縮できる可能性があります。

<br>
<br>

---

# 22

### Dockerfile の修正
```Dockerfile
FROM python:3.11

# MeCab と関連パッケージをインストール (requirements.txt に含める場合は削除可能)
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# .devcontainer/requirements.txt をコピーしてインストール
COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# アプリケーションのディレクトリを作成し、そこに移動
WORKDIR /app

# ホストのファイルをコンテナにコピー (プロジェクトルート全体をコピーすると仮定)
COPY .. /app

# ポート番号を指定
EXPOSE 5000

# Flask アプリケーションの実行
CMD ["python", "Practice/22/app.py"]
```

### devcontainer.json の修正
```json
{
  "name": "AtCoder",
  // "dockerFile": "Dockerfile",
  "dockerFile": ".devcontainer/Dockerfile",
  "extensions": ["ms-python.python"]
}
```

### Docker イメージのビルド:
```bash
docker build -t devcontainer-exercise20 -f .devcontainer/Dockerfile .
```

### Docker コンテナの起動:
```bash
docker run --name devcontainer-exercise20-instance -p 8000:5000 -v $(pwd):/app -it devcontainer-exercise20 /bin/bash
```

### コンテナ内で Flask アプリケーションを起動:
```bash
cd Practice/22
python app.py
```

ブラウザで http://localhost:8000/users にアクセス
```
{
  "users": [
    {
      "age": 20,
      "id": 1,
      "name": "Alice"
    },
    {
      "age": null,
      "id": 2,
      "name": "Bob"
    },
  ]
}
```

### ユーザー追加:
ターミナルで curl コマンドを実行
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Charlie", "age": 30}'
```

ブラウザで http://localhost:8000/users にアクセス
```
{
  "users": [
    {
      "age": 20,
      "id": 1,
      "name": "Alice"
    },
    {
      "age": null,
      "id": 2,
      "name": "Bob"
    },
    {
      "age": 30,
      "id": 3,
      "name": "Charlie"
    }
  ]
}
```

<br>
<br>

---

# 23

## コード解説：PythonでWebページからイベント情報をスクレイピングする

### 全体的な流れ
このコードは、Pythonのライブラリである `requests` と `BeautifulSoup4` を使って、Python公式サイトからイベント情報をスクレイピングし、タイトルと開催日時を抽出するプログラムです。

1. **ライブラリのインポート:**
   - `requests`: Webページを取得するためのライブラリ
   - `BeautifulSoup4`: HTMLを解析するためのライブラリ
   - `typing`: 型ヒント（変数の型を明示的に指定する）のためのライブラリ
   - `urllib.parse`: URL操作のためのライブラリ

2. **スクレイピング関数 `scrape_events`:**
   - 引数として、対象となるURLを受け取ります。
   - 指定されたURLのページを取得し、BeautifulSoupを使ってHTMLを解析します。
   - `div.event-widget li` というセレクターで、イベントに関する情報を表すリスト要素を抽出します。
   - 各リスト要素から、タイトルと日時を抽出し、タプルとして `yield` で返します。

3. **メインブロック:**
   - `scrape_events` 関数を呼び出し、返ってきたイテレータから、タイトルと日時を順に取得して表示します。

### コードの各部分の詳細な解説

#### 1. ライブラリのインポート
```python
import requests
from bs4 import BeautifulSoup
from typing import Iterator, Tuple
from urllib.parse import urljoin
```
* `requests`: Webページを取得するための最も一般的なライブラリです。
* `BeautifulSoup4`: HTMLやXML文書を解析するためのPythonライブラリです。HTML構造を木構造のように表現し、特定の要素を検索したり、内容を抽出したりすることができます。
* `typing`: Python 3.5以降で導入された型ヒント機能を使うためのライブラリです。コードの可読性を高め、バグを防ぐのに役立ちます。
* `urllib.parse`: URLを解析したり、操作したりするためのモジュールです。

#### 2. `scrape_events` 関数
```python
def scrape_events(url: str) -> Iterator[Tuple[str, str]]:
    # ...
```
* `url: str`: 関数の引数で、スクレイピング対象のURLを文字列として受け取ります。
* `-> Iterator[Tuple[str, str]]`: 関数の戻り値の型を指定しています。`Iterator` はイテレータを表し、`Tuple[str, str]` は文字列のタプル（タイトルと日時）を要素とするイテレータを返すことを意味します。

#### 3. HTMLの解析とイベント情報の抽出
```python
soup = BeautifulSoup(response.text, "html.parser")
for item in soup.select("div.event-widget li")[:5]:
    # ...
```
* `soup.select("div.event-widget li")[:5]` の部分で、HTMLからイベントに関する情報を抽出します。
* `div.event-widget` は、イベント情報をまとめたdiv要素を指定します。
* `li` は、各イベントの情報を表すリスト要素を指定します。
* `[:5]` は、最初の5つのリスト要素だけを抽出します。

#### 4. イベントタイトルと日時の抽出
```python
tag_title = item.find('a')
tag_time = item.find('time')
if tag_title and tag_time:
    event_title = tag_title.text.strip()
    event_date = tag_time.text.strip()
    yield (event_title, event_date)
```
* `item.find('a')` と `item.find('time')` で、それぞれタイトルと日時を表すタグを見つけます。
* `tag_title.text.strip()` と `tag_time.text.strip()` で、タグの中身を取り出し、前後の空白文字を削除します。
* `yield` キーワードを使うことで、ジェネレータ関数として、一つずつ結果を返します。

### 例:
```
タイトル: PyLadies Amsterdam
日時: 2025-01-16
--------------------------------------------------
タイトル: Python Meeting Düsseldorf
日時: 2025-01-22
--------------------------------------------------
```

### さらに詳しく
* **セレクタ:** `soup.select()` メソッドは、CSSセレクタを使って要素を検索できます。
* **ジェネレータ:** `yield` キーワードを使うことで、メモリ効率の良い処理を実現できます。
* **エラー処理:** `try-except` ブロックで、エラーが発生した場合の処理を記述できます。
* **BeautifulSoupの機能:** BeautifulSoupには、他にも様々な機能があり、HTMLを柔軟に解析することができます。

### まとめ
このコードは、Python公式サイトのイベント情報をスクレイピングし、タイトルと開催日時を抽出する基本的な例です。
このコードを参考に、他のWebサイトの情報をスクレイピングすることも可能です。
**ただし、スクレイピングを行う際は、対象となるサイトの利用規約を必ず確認し、ルールに従って行うようにしましょう。**

**より高度なスクレイピングを行うためには、以下の点に注意すると良いでしょう。**
* **HTML構造の解析:** 対象となるWebサイトのHTML構造をしっかりと理解する。
* **CSSセレクタの活用:** BeautifulSoupのセレクタ機能を駆使して、効率的に要素を抽出する。
* **エラー処理:** ネットワークエラーやHTML構造の変化に対応できるよう、エラー処理を適切に行う。
* **スクレイピングの倫理:** 法律やサイトの利用規約に違反しないように注意する。

**この解説が、Pythonのスクレイピングを始める際の参考になれば幸いです。**

<br>

## [補足] タグの指定

**今回のコードでターゲットにしているHTML構造:**

今回のコードは、Python公式サイトのトップページにある「Upcoming Events」（今後のイベント）というリストから情報を取得しています。このリストは、HTMLの特定の構造で記述されています。

以下は、Python公式サイトの「Upcoming Events」リスト部分のHTMLの簡略化された例です。実際にはもっと多くの属性やクラスが付いている可能性があります。

```html
<div class="event-widget">
  <h2 class="widget-title">Upcoming Events</h2>
  <p class="give-me-more"><a href="/events/calendars/">More</a></p>
  <div class="shrubbery">
    <ul class="menu">
      <li>
        <time datetime="2025-01-16T16:15:00+00:00">2025-01-16</time>
        <a href="/events/python-user-group/1880/"> PyLadies Amsterdam</a>
      </li>
      <li>
        <time datetime="2025-01-22T17:00:00+00:00">2025-01-22</time>
        <a href="/events/python-user-group/1855/">Python Meeting Düsseldorf</a>
      </li>
      <!-- ... 他のイベント ... -->
    </ul>
  </div>
</div>
```

**コードとHTMLの対応:**

1. **`soup.select("div.event-widget li")[:5]` の役割:**

   * **`div.event-widget`**:  この部分は、HTMLの中で `class` 属性が `event-widget` である `<div>` タグを探しています。これは、イベント情報全体を囲んでいる大きな箱のようなものです。
   * **`li`**:  次に、その `<div>` タグの中にあるすべての `<li>` タグを探しています。各 `<li>` タグは、一つのイベント情報を表す行に相当します。
   * **`[:5]`**: 最後に、見つかった `<li>` タグのリストから、最初の5つだけを取り出しています。これは、「最新のイベントを5件だけ知りたい」という意図に基づいています。

   **例:** 上記のHTML例では、`class="event-widget"` を持つ `<div>` タグがイベントリスト全体を囲んでおり、その中にある各 `<li>` タグが個別のイベントに対応しています。

2. **`item.find('a')` の役割:**

   * `for item in soup.select("div.event-widget li")[:5]:` のループで、一つ一つのイベント情報 (`<li>` タグ) が `item` 変数に格納されます。
   * **`item.find('a')`**: このコードは、現在のイベント情報 (`item`、つまり一つの `<li>` タグ) の中にある最初の `<a>` (アンカー) タグを探しています。この `<a>` タグは、通常イベントのタイトルを表し、イベントの詳細ページへのリンクにもなっています。

   **例:** 各 `<li>` タグの中には、イベントのタイトルである "PyLadies Amsterdam" や "Python Meeting Düsseldorf" が `<a>` タグで囲まれています。

3. **`item.find('time')` の役割:**

   * **`item.find('time')`**: このコードは、現在のイベント情報 (`item`) の中にある最初の `<time>` タグを探しています。この `<time>` タグは、イベントの開催日時を表します。`datetime` 属性には、機械が理解しやすい形式で日時が格納されていますが、`time_tag.text` で取得するのは、人間が読みやすい形式の日時です。

   **例:** 各 `<li>` タグの中には、開催日時である "2025-01-16" や "2025-01-22" が `<time>` タグで囲まれています。

4. **`event_title = tag_title.text.strip()` と `event_date = tag_time.text.strip()`:**

   * `tag_title.text` は、見つけた `<a>` タグの中のテキスト部分（イベントタイトル）を取得します。
   * `tag_time.text` は、見つけた `<time>` タグの中のテキスト部分（開催日時）を取得します。
   * `.strip()` は、取得したテキストの前後の空白や改行を削除して、情報を綺麗にします。

**初心者が理解するためのポイント:**

* **HTMLのタグ:** HTMLは、`<タグ名>` で始まり、`</タグ名>` で終わる要素の集まりで構成されています。例えば、`<div>` は領域を区切るタグ、`<a>` はリンクを作るタグ、`<time>` は日時を表すタグです。
* **クラス属性 (`class="..."`)**: HTML要素にスタイルやJavaScriptの動作を適用するために使われる名前です。同じクラス名を持つ要素は、同じような見た目や動作を持つことが多いです。BeautifulSoupでは、このクラス属性を使って特定の要素を効率的に探し出すことができます。
* **BeautifulSoupのメソッド:**
    * **`soup.select()`**: CSSセレクタを使って、HTML文書から特定の要素をリストとして抽出します。CSSセレクタは、HTMLの構造をパターンで指定する方法です。
    * **`find()`**: 特定のタグの中で、最初に見つかった要素を返します。

**まとめ:**

このコードは、まるでPython公式サイトのHTMLという地図を読み解き、特定の場所（`div` タグで囲まれたイベントリストの中の `li` タグ）に注目し、そこから「イベントタイトル」と「開催日時」が書かれた看板 (`<a>` タグと `<time>` タグ) を見つけ出して、情報を抜き出しているのです。

Webページの構造は変更される可能性があるため、もしPython公式サイトのデザインが変わると、このコードも修正が必要になる場合があります。しかし、基本的な考え方は同じで、「目的の情報がHTMLのどこに、どのようなタグで囲まれているか」を理解することが、Webスクレイピングの第一歩となります。


<br>
<br>

---

# 24

```python
import os
from PIL import Image

folder_in = "images"
folder_out = "resized_images"
target_width = 500

def resize_images(folder_in, folder_out, target_width):
    if not os.path.exists(folder_out):
        os.makedirs(folder_out)

    for file in os.listdir(folder_in):
        if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
            try:
                # open the image
                image_path = os.path.join(folder_in, file)
                img = Image.open(image_path)
                # convert the image to RGB if it's not
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # get the original size
                original_width, original_height = img.size
                # calculate the aspect ratio
                aspect_ratio = original_width / original_height
                # calculate the new height after resizing
                new_height = int(target_width / aspect_ratio)
                # resize the image
                resized_img = img.resize((target_width, new_height), Image.LANCZOS)
                # save the resized image
                output_path = os.path.join(folder_out, file)
                resized_img.save(output_path)

                print(f'{file} was resized successfully')

            except Exception as e:
                print(f'Error resizing {file}: {str(e)}')

if __name__ == '__main__':
    resize_images(folder_in, folder_out, target_width)
    print(f'Successfully resized all images in {folder_in} folder')
```

**コード全体の概要**

このプログラムは、指定されたフォルダ (`images`) 内の画像ファイルを、指定された幅 (`500`ピクセル) にリサイズし、リサイズ後の画像を別のフォルダ (`resized_images`) に保存するものです。縦のサイズは、元の画像の縦横比（アスペクト比）を維持するように自動的に計算されます。

**コードの先頭部分**

```python
import os
from PIL import Image
```

* **`import os`**:  これは「os」という名前の機能の詰まった箱をプログラムに持ってきて使えるようにする命令です。この箱には、パソコンのファイルやフォルダを操作するための道具がたくさん入っています。例えば、「指定したフォルダの中にどんなファイルがあるか調べてきて！」とか、「新しいフォルダを作って！」といったお願いができます。

* **`from PIL import Image`**:  これは「PIL (Pillow)」という画像処理専門の道具箱の中から、「Image」という特別な道具だけを取り出して使えるようにする命令です。この「Image」という道具を使うと、画像を開いたり、サイズを変えたり、色を変えたり、保存したりといった、画像に関する色々な作業ができるようになります。

**設定部分**

```python
folder_in = "images"
folder_out = "resized_images"
target_width = 500
```

ここでは、プログラムで使う設定値を名前をつけて保存しています。

* **`folder_in = "images"`**: リサイズしたい画像が入っているフォルダの名前を「`images`」として覚えておきます。「入力フォルダはここだよ！」とプログラムに教えるようなものです。
* **`folder_out = "resized_images"`**: リサイズが終わった画像を保存するフォルダの名前を「`resized_images`」として覚えておきます。「リサイズ後の画像はここに保存してね！」と指示するイメージです。
* **`target_width = 500`**: リサイズ後の画像の幅を `500` ピクセルにすることを覚えておきます。「リサイズ後の画像の横幅は500ピクセルにしてね！」という設定です。

**`resize_images` 関数**

```python
def resize_images(folder_in, folder_out, target_width):
    # ... (関数の処理内容)
```

`def resize_images(folder_in, folder_out, target_width):` は、画像をリサイズする一連の処理をまとめた「resize_images」という名前の箱を作る命令です。この箱には、入力フォルダ名 (`folder_in`)、出力フォルダ名 (`folder_out`)、目標の幅 (`target_width`) という３つの入口があります。必要なものを入口から入れてあげると、箱の中でリサイズの処理が行われるイメージです。

**出力フォルダの作成**

```python
    if not os.path.exists(folder_out):
        os.makedirs(folder_out)
```

* **`if not os.path.exists(folder_out):`**:  ここで、`os`箱に入っている `path.exists` という道具を使って、「`folder_out`」で指定された名前のフォルダがすでに存在するかどうかを確認しています。`not` が付いているので、「もし存在していなかったら」という意味になります。
    * 例えば、`folder_out` が "resized_images" だった場合、「resized_images という名前のフォルダ、もうあるかな？」と確認します。
* **`os.makedirs(folder_out)`**:  もしフォルダが存在していなかった場合、`os`箱に入っている `makedirs` という道具を使って、指定された名前のフォルダを作成します。
    * 例えば、"resized_images" フォルダがなかったら、「よし、resized_images という名前のフォルダを作ろう！」と実行します。これで、リサイズ後の画像を保存する場所が確保できます。

**フォルダ内のファイルを処理するループ**

```python
    for file in os.listdir(folder_in):
        if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
            # ... (画像処理のコード)
```

* **`for file in os.listdir(folder_in):`**: `os`箱に入っている `listdir` という道具を使って、入力フォルダ (`folder_in`) の中にあるすべてのファイルやフォルダの名前をリスト形式で取得し、一つずつ順番に `file` という名前の箱に入れて、以下の処理を繰り返します。
    * 例えば、`folder_in` が "images" フォルダで、中に "photo1.jpg", "logo.png", "document.txt" というファイルがあった場合、最初に `file` に "photo1.jpg" が入り、次に "logo.png" が入り、最後に "document.txt" が入ります。
* **`if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):`**:  `file` に入っているファイル名が、指定された拡張子 (`.jpg`, `.jpeg`, `.png`, `.gif`) のいずれかで終わっているかどうかを確認します。
    * `.lower()` を使うことで、大文字・小文字を区別せずにチェックできます。例えば、"Photo.JPG" も "photo.jpg" と同じように扱われます。
    * 例えば、`file` が "photo1.jpg" の場合、`.jpg` で終わっているので、`if` の条件は `True` になり、以下の画像処理のコードが実行されます。しかし、`file` が "document.txt" の場合、`.txt` で終わっているので、`if` の条件は `False` になり、画像処理のコードはスキップされます。

**画像処理 (try...except ブロック)**

```python
            try:
                # open the image
                image_path = os.path.join(folder_in, file)
                img = Image.open(image_path)
                # convert the image to RGB if it's not
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # get the original size
                original_width, original_height = img.size
                # calculate the aspect ratio
                aspect_ratio = original_width / original_height
                # calculate the new height after resizing
                new_height = int(target_width / aspect_ratio)
                # resize the image
                resized_img = img.resize((target_width, new_height), Image.LANCZOS)
                # save the resized image
                output_path = os.path.join(folder_out, file)
                resized_img.save(output_path)

                print(f'{file} was resized successfully')

            except Exception as e:
                print(f'Error resizing {file}: {str(e)}')
```

* **`try:`**:  ここでは、「これから行う処理でエラーが起きるかもしれないけど、もしエラーが起きたら、教えてね！」とプログラムにお願いしています。
* **`image_path = os.path.join(folder_in, file)`**: `os`箱に入っている `path.join` という道具を使って、入力フォルダ名 (`folder_in`) とファイル名 (`file`) を組み合わせて、画像ファイルの正確な場所（パス）を作成します。
    * 例えば、`folder_in` が "images" で、`file` が "photo1.jpg" の場合、`image_path` は "images/photo1.jpg" になります。
* **`img = Image.open(image_path)`**: `PIL`箱から取り出した `Image` 道具に入っている `open` 機能を使って、指定されたパスの画像ファイルを開き、その画像データを `img` という名前の箱に入れます。これで、画像ファイルの中身を操作できるようになります。
    * 例えば、"images/photo1.jpg" の画像ファイルを開いて、そのデータを `img` に入れます。
* **`if img.mode != 'RGB':`**: 画像のカラーモードが RGB (Red, Green, Blue の３つの色の組み合わせで色を表現する方法) でないかどうかを確認します。
* **`img = img.convert('RGB')`**:  もし画像のカラーモードが RGB でない場合、`convert('RGB')` 機能を使って、画像を RGB モードに変換します。これは、JPEG 形式で画像を保存するためによく行われる処理です。例えば、RGBA (透明度情報を持つ RGB) モードの PNG 画像を JPEG に保存する場合などに、この変換が必要になります。
* **`original_width, original_height = img.size`**:  開いた画像 (`img`) の元の幅と高さを取得して、それぞれ `original_width` と `original_height` という名前の箱に入れます。
    * 例えば、`img` が 1920x1080 の画像だった場合、`original_width` には 1920 が、`original_height` には 1080 が入ります。
* **`aspect_ratio = original_width / original_height`**:  元の画像の縦横比（アスペクト比）を計算します。これは、元の幅を高さで割ることで求められます。
    * 例えば、元の画像が 1920x1080 の場合、アスペクト比は 1920 / 1080 = 1.777... となります。
* **`new_height = int(target_width / aspect_ratio)`**:  リサイズ後の新しい高さを計算します。目標の幅 (`target_width`) をアスペクト比で割ることで求められます。`int()` を使うことで、計算結果を整数にします。
    * 例えば、`target_width` が 500 で、アスペクト比が 1.777... の場合、新しい高さは 500 / 1.777... = 281.25... となり、`int()` によって 281 になります。
* **`resized_img = img.resize((target_width, new_height), Image.LANCZOS)`**:  `PIL`箱の `Image` 道具に入っている `resize` 機能を使って、画像 (`img`) のサイズを新しい幅 (`target_width`) と新しい高さ (`new_height`) に変更します。`Image.LANCZOS` は、リサイズの際に画質を良くするための高品質なアルゴリズムを指定しています。
    * 例えば、画像を (500, 281) のサイズにリサイズします。
* **`output_path = os.path.join(folder_out, file)`**:  リサイズ後の画像を保存する場所の正確なパスを作成します。出力フォルダ名 (`folder_out`) と元のファイル名 (`file`) を組み合わせます。
    * 例えば、`folder_out` が "resized_images" で、`file` が "photo1.jpg" の場合、`output_path` は "resized_images/photo1.jpg" になります。
* **`resized_img.save(output_path)`**:  リサイズされた画像 (`resized_img`) を、作成したパス (`output_path`) に保存します。
    * 例えば、リサイズされた画像を "resized_images/photo1.jpg" という名前で保存します。
* **`print(f'{file} was resized successfully')`**:  リサイズが成功した場合、どのファイルがリサイズされたかを示すメッセージを画面に表示します。
    * 例えば、「photo1.jpg was resized successfully」と表示されます。
* **`except Exception as e:`**:  `try` ブロックの中で何らかのエラーが発生した場合、そのエラーの内容を `e` という名前の箱に入れて、ここから処理を行います。「もしエラーが起きたら、この処理をしてね！」という意味です。
* **`print(f'Error resizing {file}: {str(e)}')`**:  リサイズ中にエラーが発生した場合、どのファイルでどのようなエラーが起きたかを示すメッセージを画面に表示します。
    * 例えば、「Error resizing photo2.png: cannot write mode RGBA as JPEG」のように表示されます。

**プログラムの実行部分**

```python
if __name__ == '__main__':
    resize_images(folder_in, folder_out, target_width)
    print(f'Successfully resized all images in {folder_in} folder')
```

* **`if __name__ == '__main__':`**:  この行は、「このPythonファイルがプログラムとして直接実行された場合にだけ、以下のコードを実行してください」という意味のおまじないのようなものです。
* **`resize_images(folder_in, folder_out, target_width)`**:  先ほど作った `resize_images` という名前の処理の箱を動かす命令です。箱の入口に、入力フォルダ名 (`folder_in`)、出力フォルダ名 (`folder_out`)、目標の幅 (`target_width`) を入れてあげます。
* **`print(f'Successfully resized all images in {folder_in} folder')`**:  すべての画像のリサイズ処理が正常に完了した場合に、その旨を知らせるメッセージを画面に表示します。
    * 例えば、「Successfully resized all images in images folder」と表示されます。
<<<<<<< HEAD
=======

<br>
<br>

---

# 25

## 1. ライブラリのインポート

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
```

このセクションでは、プログラムで使用する様々な機能を提供するライブラリをインポートしています。

*   `import torch`:  PyTorchの基本的な機能を提供します。テンソル演算、自動微分などのコア機能が含まれます。
*   `import torch.nn as nn`: ニューラルネットワークを構築するための様々なモジュールを提供します。例えば、線形層 (`nn.Linear`)、畳み込み層 (`nn.Conv2d`)、活性化関数 (`torch.relu`) などが含まれます。`nn` というエイリアスで参照できるようにしています。
*   `import torch.optim as optim`:  ニューラルネットワークのパラメータを最適化するための様々なアルゴリズムを提供します。例えば、確率的勾配降下法 (`optim.SGD`)、Adam (`optim.Adam`) などが含まれます。`optim` というエイリアスで参照できるようにしています。
*   `from torchvision import datasets, transforms`:  画像処理に特化したライブラリ `torchvision` から、データセット (`datasets`) とデータ変換 (`transforms`) に関連するモジュールをインポートしています。`datasets` には MNIST のような一般的な画像データセットが含まれており、`transforms` には画像のテンソル化、正規化などの前処理を行うための関数が含まれています。
*   `from torch.utils.data import DataLoader`:  データセットからミニバッチを作成し、学習時にデータを効率的に供給するためのユーティリティクラス `DataLoader` をインポートしています。

## 2. ハイパーパラメータの設定

```python
# setting a hyperparameters
batch_size = 64
learging_rate = 0.001
num_epochs = 3
```

ここでは、ニューラルネットワークの学習プロセスを制御するための重要なパラメータ（ハイパーパラメータ）を設定しています。

*   `batch_size = 64`:  学習時に一度に処理するデータの数（ミニバッチサイズ）を指定します。64 に設定した場合、訓練データセットから 64 個のデータサンプルをまとめてモデルに入力し、それらの平均的な勾配に基づいてモデルのパラメータを更新します。バッチサイズを大きくすると、勾配の計算が安定しやすくなりますが、メモリ使用量が増加します。
*   `learging_rate = 0.001`:  最適化アルゴリズムにおける学習率を設定します。学習率は、損失関数の勾配に基づいてモデルのパラメータを更新する際のステップサイズを決定します。学習率が大きいと、パラメータの更新幅が大きくなり、学習が早く進む可能性がありますが、最適解を飛び越えてしまうリスクがあります。学習率が小さいと、パラメータの更新幅が小さくなり、学習は安定しますが、収束に時間がかかる場合があります。
*   `num_epochs = 3`:  訓練データセット全体を何回繰り返して学習するかを指定します。1 エポックとは、訓練データセット全体を一度通して学習することを意味します。エポック数を増やすことで、モデルは訓練データからより多くのパターンを学習できますが、過学習のリスクも高まります。

## 3. データの前処理

```python
# preproccesing data (grayscale, normalization, etc.)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1037,), (0.3081,))
])
```

このセクションでは、MNIST データセットの画像をニューラルネットワークに入力する前に適切な形式に変換する処理を定義しています。

*   `transforms.Compose([...])`:  複数の変換処理を順番に適用するためのコンテナです。リスト内に記述された変換処理が順番に実行されます。
*   `transforms.ToTensor()`:  PIL 画像または NumPy 配列を PyTorch のテンソルに変換します。この際、画素値は 0 から 1 の範囲に正規化されます（元の画素値が 0 から 255 の場合、255 で割られます）。これは、ニューラルネットワークが数値データを扱いやすくするためです。
*   `transforms.Normalize((0.1037,), (0.3081,))`:  テンソル化された画像の画素値を正規化します。具体的には、各チャンネル（MNIST の場合はグレースケールなので 1 チャンネル）の画素値から平均値 (`0.1037`) を引き、標準偏差 (`0.3081`) で割ります。この正規化により、画素値の分布が特定の範囲に収まり、学習が安定しやすくなる効果があります。これらの平均値と標準偏差は、MNIST データセット全体の画素値から計算された値です。

## 4. MNISTデータセットのダウンロードと読み込み

```python
# download and load the MNIST data
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
```

ここでは、MNIST データセットをダウンロードし、学習用と評価用に分割して読み込んでいます。

*   `train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)`:  `torchvision.datasets.MNIST` クラスを使用して、MNIST データセットの訓練用データを読み込みます。
    *   `'./data'` はデータセットをダウンロードするディレクトリ、または既にダウンロード済みのデータセットが保存されているディレクトリを指定します。
    *   `train=True` は訓練用データを読み込むことを指定します。
    *   `download=True` は、指定されたディレクトリにデータセットが存在しない場合に自動的にダウンロードすることを指定します。
    *   `transform=transform` は、先ほど定義した前処理 (`transform`) を読み込んだデータに適用することを指定します。
*   `test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)`:  同様に、MNIST データセットのテスト用データを読み込みます。`train=False` を指定することで、評価用のデータが読み込まれます。
*   `train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)`:  `torch.utils.data.DataLoader` クラスを使用して、訓練データセットからミニバッチを作成します。
    *   `train_dataset` は、読み込んだ訓練データセットを指定します。
    *   `batch_size=batch_size` は、ミニバッチのサイズを、先ほど設定した `batch_size` の値（ここでは 64）に設定します。
    *   `shuffle=True` は、各エポックの開始時にデータセット内のサンプルの順序をシャッフルすることを指定します。これにより、モデルが特定の順序に依存して学習することを防ぎ、汎化性能の向上に貢献します。
*   `test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)`:  同様に、テストデータセットからミニバッチを作成します。`shuffle=False` とすることで、評価時にはデータの順序を固定します。

## 5. ニューラルネットワークモデルの定義

```python
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 256)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

ここでは、手書き数字認識を行うためのニューラルネットワークモデルのアーキテクチャを定義しています。

*   `class Net(nn.Module):`:  `Net` という名前のクラスを定義し、`torch.nn.Module` を継承しています。`nn.Module` は、PyTorch でニューラルネットワークを構築するための基本的なクラスです。
*   `def __init__(self):`:  モデルのインスタンスが生成される際に実行される初期化メソッドです。ここで、モデルで使用する各層を定義します。
    *   `super(Net, self).__init__()`:  親クラス (`nn.Module`) の初期化メソッドを呼び出します。これは必須の記述です。
    *   `self.conv1 = nn.Conv2d(1, 32, 3, padding=1)`:  最初の畳み込み層を定義します。
        *   `1` は入力チャンネル数（MNIST はグレースケール画像なので 1 チャンネル）。
        *   `32` は出力チャンネル数（32 種類の特徴マップを生成）。
        *   `3` は畳み込みカーネルのサイズ（3x3 のフィルターを使用）。
        *   `padding=1` は入力の特徴マップの周囲に 1 ピクセルのパディングを追加します。これにより、畳み込み演算後も特徴マップのサイズが維持され、画像の端の情報を失いにくくなります。
    *   `self.conv2 = nn.Conv2d(32, 64, 3, padding=1)`:  2 番目の畳み込み層を定義します。
        *   `32` は入力チャンネル数（前の畳み込み層の出力チャンネル数）。
        *   `64` は出力チャンネル数（64 種類の特徴マップを生成）。
        *   その他のパラメータは `conv1` と同様です。
    *   `self.pool = nn.MaxPool2d(2, 2)`:  最大プーリング層を定義します。
        *   `2` はプーリングウィンドウのサイズ（2x2 の領域）。
        *   `2` はストライド（プーリングウィンドウを移動させる幅）。この設定では、2x2 の領域から最大の値を取り出し、特徴マップのサイズを縦横それぞれ 1/2 にします。
    *   `self.fc1 = nn.Linear(64 * 7 * 7, 256)`:  最初の全結合層（線形層）を定義します。
        *   `64 * 7 * 7` は入力の特徴数です。2 つの畳み込み層とプーリング層を通過した後の特徴マップのサイズは (batch_size, 64, 7, 7) となり、これを 1 次元にflatten すると 64 \* 7 \* 7 個の特徴量になります。
        *   `256` は出力の特徴数（この層のニューロン数）。
    *   `self.fc2 = nn.Linear(256, 10)`:  2 番目の全結合層を定義します。
        *   `256` は入力の特徴数（前の全結合層の出力数）。
        *   `10` は出力の特徴数です。MNIST は 10 クラス分類問題（0 から 9 の数字を識別）なので、出力は 10 個になります。各出力は、対応する数字である確率を表します。
*   `def forward(self, x):`:  モデルにデータが入力された際に実行される順伝播処理を定義します。
    *   `x = self.pool(torch.relu(self.conv1(x)))`:  入力 `x` に最初の畳み込み層 (`self.conv1`) を適用し、その出力に ReLU 活性化関数を適用した後、最大プーリング層 (`self.pool`) を適用します。ReLU は、負の値を 0 に、正の値をそのまま出力する非線形活性化関数です。
    *   `x = self.pool(torch.relu(self.conv2(x)))`:  同様に、2 番目の畳み込み層と ReLU、最大プーリング層を適用します。
    *   `x = x.view(-1, 64 * 7 * 7)`:  畳み込み層とプーリング層を通過した特徴マップを、全結合層に入力できるように 2 次元テンソルにreshapeします。`-1` はバッチサイズの次元を自動的に推論することを意味します。
    *   `x = torch.relu(self.fc1(x))`:  最初の全結合層を適用し、ReLU 活性化関数を適用します。
    *   `x = self.fc2(x)`:  最後の全結合層を適用します。この層の出力が、各クラスの確率（またはロジット）となります。
    *   `return x`:  最終的な出力を返します。

## 6. モデルのインスタンス化

```python
# instantiating the model
model = Net()
```

ここでは、先ほど定義した `Net` クラスのインスタンスを作成し、`model` という変数に代入しています。これにより、定義したニューラルネットワークモデルを実際に使用できるようになります。

## 7. 損失関数と最適化アルゴリズムの定義

```python
# defining the loss function and optimization algorithm
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learging_rate)
```

ここでは、モデルの学習に使用する損失関数と最適化アルゴリズムを定義しています。

*   `criterion = nn.CrossEntropyLoss()`:  損失関数として交差エントロピー損失関数を選択しています。交差エントロピー損失関数は、多クラス分類問題でよく用いられる損失関数で、モデルの予測確率分布と真のラベルの確率分布との間の差異を測ります。
*   `optimizer = optim.Adam(model.parameters(), lr=learging_rate)`:  最適化アルゴリズムとして Adam を選択しています。Adam は、勾配降下法を改良した最適化アルゴリズムの一つで、学習率を自動的に調整する機能があります。
    *   `model.parameters()` は、学習対象となるモデルのパラメータ（重みとバイアス）を返します。
    *   `lr=learging_rate` は、最適化アルゴリズムの学習率を、先ほど設定した `learging_rate` の値に設定します。

## 8. 訓練

```python
# training
for epoch in range(num_epochs):
    model.train()
    train_loss = 0
    correct_train = 0
    total_train = 0
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        # Printing statistics
        train_loss += loss.item()
        _, predicted = output.max(1)
        total_train += target.size(0)
        correct_train += predicted.eq(target).sum().item()

        if batch_idx % 200 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()
            ))

    train_accuracy = 100 * correct_train / total_train
    print(f'Epoch {epoch}: Train Loss: {train_loss / len(train_loader):.4f}, Train Accuracy: {train_accuracy:.2f}%')
```

ここでは、ニューラルネットワークモデルを訓練データを用いて学習させるプロセスを記述しています。

*   `for epoch in range(num_epochs):`:  指定したエポック数だけ学習を繰り返します。
*   `model.train()`:  モデルを訓練モードに設定します。訓練モードでは、ドロップアウトやバッチ正規化などの層が学習に適した挙動をします。
*   `train_loss = 0`, `correct_train = 0`, `total_train = 0`:  各エポックにおける損失と正解数を初期化します。
*   `for batch_idx, (data, target) in enumerate(train_loader):`:  `train_loader` からミニバッチ単位で訓練データ (`data`) とそのラベル (`target`) を取得し、反復処理を行います。
*   `optimizer.zero_grad()`:  各ミニバッチの学習前に、オプティマイザに蓄積されている勾配情報をリセットします。
*   `output = model(data)`:  ミニバッチの入力データ `data` をモデルに入力し、予測結果 `output` を取得します。
*   `loss = criterion(output, target)`:  予測結果 `output` と正解ラベル `target` を損失関数に入力し、損失値を計算します。
*   `loss.backward()`:  計算された損失値に基づいて、モデルの各パラメータに対する勾配を計算します（バックプロパゲーション）。
*   `optimizer.step()`:  計算された勾配に基づいて、モデルのパラメータを更新します。
*   `(Printing statistics)`:  訓練の進行状況を表示します。
    *   `train_loss += loss.item()`:  現在のバッチの損失値を累積します。`.item()` を使用することで、テンソルから Python の数値を取得できます。
    *   `_, predicted = output.max(1)`:  予測結果 `output` の各行（各サンプルの予測）の中で、最も確率の高いクラスのインデックスを取得します。`_` は最大値自体を無視するために使用します。
    *   `total_train += target.size(0)`:  処理した訓練データの総数を累積します。
    *   `correct_train += predicted.eq(target).sum().item()`:  予測が正解だった数を累積します。`predicted.eq(target)` は、予測と正解ラベルが一致する箇所に `True`、それ以外に `False` を持つブール値テンソルを生成し、`.sum()` で `True` の数を合計し、`.item()` で Python の数値に変換します。
    *   `if batch_idx % 200 == 0:`:  200 バッチごとに訓練の状況を表示します。
*   `train_accuracy = 100 * correct_train / total_train`:  エポック終了時の訓練データの正解率を計算します。
*   `print(f'Epoch {epoch}: Train Loss: {train_loss / len(train_loader):.4f}, Train Accuracy: {train_accuracy:.2f}%')`:  エポックごとの平均損失と訓練データの正解率を表示します。

## 9. 評価

```python
# evaluation
model.eval()
test_loss = 0
correct_test = 0
total_test = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        test_loss += criterion(output, target).item()
        _, predicted = output.max(1)
        total_test += target.size(0)
        correct_test += predicted.eq(target).sum().item()

test_accuracy = 100. * correct_test / total_test
print(f'Test Loss: {test_loss / len(test_loader):.4f}, Test Accuracy: {test_accuracy:.2f}%')
```

ここでは、訓練済みのモデルの汎化性能を評価するために、テストデータセットに対する性能を測定しています。

*   `model.eval()`:  モデルを評価モードに設定します。評価モードでは、訓練時とは異なる挙動をする層（ドロップアウト層など）が評価に適した挙動をします。例えば、ドロップアウト層は無効になります。
*   `test_loss = 0`, `correct_test = 0`, `total_test = 0`:  テストデータに対する損失と正解数を初期化します。
*   **`with torch.no_grad():`**:  このブロック内の処理では、勾配計算を行わないことを指定します。評価時にはモデルのパラメータを更新する必要がないため、勾配計算を無効にすることで、メモリ使用量を削減し、処理を高速化できます。
*   **`for data, target in test_loader:`**:  `test_loader` からミニバッチ単位でテストデータとそのラベルを取得し、反復処理を行います。
*   **`output = model(data)`**:  テストデータをモデルに入力し、予測結果を取得します。
*   **`test_loss += criterion(output, target).item()`**:  予測結果と正解ラベルから損失値を計算し、累積します。
*   **`_, predicted = output.max(1)`**:  予測結果から最も確率の高いクラスを予測ラベルとして取得します。
*   **`total_test += target.size(0)`**:  処理したテストデータの総数を累積します。
*   **`correct_test += predicted.eq(target).sum().item()`**:  予測が正解だった数を累積します。
*   **`test_accuracy = 100. * correct_test / total_test`**:  テストデータに対する正解率を計算します。
*   **`print(f'Test Loss: {test_loss / len(test_loader):.4f}, Test Accuracy: {test_accuracy:.2f}%')`**:  テストデータに対する平均損失と正解率を表示します。

## 10. 正解率の確認:

```python
# Checking accuracy
if train_accuracy >= 90.0 and test_accuracy >= 85.0:
    print("The target accuracy rate was achieved.")
else:
    print("The target accuracy rate was not achieved.")
```

ここでは、訓練データとテストデータで達成された正解率を、事前に設定された目標値と比較し、結果を出力しています。訓練データの正解率が 90% 以上、かつテストデータの正解率が 85% 以上であれば、目標精度を達成したと判断します。

### [参考] log

```bash
Train Epoch: 0 [0/60000 (0%)]   Loss: 2.292500
Train Epoch: 0 [12800/60000 (21%)]      Loss: 0.107222
Train Epoch: 0 [25600/60000 (43%)]      Loss: 0.023011
Train Epoch: 0 [38400/60000 (64%)]      Loss: 0.062600
Train Epoch: 0 [51200/60000 (85%)]      Loss: 0.098606
Epoch 0: Train Loss: 0.1213, Train Accuracy: 96.30%
Train Epoch: 1 [0/60000 (0%)]   Loss: 0.030439
Train Epoch: 1 [12800/60000 (21%)]      Loss: 0.016119
Train Epoch: 1 [25600/60000 (43%)]      Loss: 0.018514
Train Epoch: 1 [38400/60000 (64%)]      Loss: 0.066887
Train Epoch: 1 [51200/60000 (85%)]      Loss: 0.069259
Epoch 1: Train Loss: 0.0384, Train Accuracy: 98.82%
Train Epoch: 2 [0/60000 (0%)]   Loss: 0.003613
Train Epoch: 2 [12800/60000 (21%)]      Loss: 0.020767
Train Epoch: 2 [25600/60000 (43%)]      Loss: 0.014143
Train Epoch: 2 [38400/60000 (64%)]      Loss: 0.027359
Train Epoch: 2 [51200/60000 (85%)]      Loss: 0.037601
Epoch 2: Train Loss: 0.0250, Train Accuracy: 99.19%
Test Loss: 0.0269, Test Accuracy: 99.06%
The target accuracy rate was achieved.
```
>>>>>>> master

<br>
<br>

---

# 26

## このプログラムは何をするもの？

このプログラムは、指定されたテキストファイルから文章を読み込み、その文章の中で特によく使われている名詞（物の名前など）を上位10個表示するものです。例えば、あるニュース記事やブログ記事のテキストファイルを与えると、その記事の中で頻繁に使われているキーワードとなる名詞を知ることができます。

プログラムは以下の手順で処理を行います。

1. **テキストファイルの読み込み:** プログラムが解析対象とする文章が書かれたテキストファイルを読み込みます。
2. **形態素解析による名詞抽出:** 読み込んだ文章をMeCabというツールを使って細かく分解し、その中から名詞だけを取り出します。
3. **名詞の出現回数の集計:** 取り出した名詞がそれぞれ何回文章中に出てきたかを数えます。
4. **出現頻度の高い順に並び替え:** 名詞を出現回数が多い順に並べ替えます。
5. **上位10個の名詞の表示:** 並び替えた結果の上位10個の名詞とその出現回数を表示します。

## プログラムを実行する前の準備

このプログラムを動かすには、以下の準備が必要です。

1. **MeCabのインストール:** 日本語の文章を解析するためのツール「MeCab」があなたのパソコンにインストールされている必要があります。もしインストールされていない場合は、インストール作業が必要です。（インストール方法については、MeCabの公式サイトなどを参照してください。）
2. **テキストファイルの準備:** 解析したい文章を記述したテキストファイルを用意します。このプログラムでは、デフォルトで「./data/sample.txt」という名前のファイルを探します。例えば、「./data/sample.txt」ファイルに以下のような文章が書かれているとします。

   ```
   今日は天気が良いので、公園で遊びます。子供たちが楽しそうに遊んでいます。公園には花も咲いていて綺麗です。
   ```

## プログラムのコード解説

それでは、プログラムのコードを順番に見ていきましょう。

```python
import MeCab
```
この行は、プログラムの中でMeCabという機能を使うために必要な準備をしています。「import」は、外部の機能を取り込むための命令です。

```python
def extract_nouns(text, mecabrc_path):
    tagger = MeCab.Tagger(f"-r {mecabrc_path}")
    node = tagger.parseToNode(text)
    nouns = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            nouns.append(node.surface)
        node = node.next
    return nouns
```
この部分は、文章から名詞を抽出する処理をまとめたものです。

* **`def extract_nouns(text, mecabrc_path):`**:  これは「extract_nouns」という名前の機能（関数）を定義しています。この関数は、「text」（解析する文章）と「mecabrc_path」（MeCabの設定ファイルの場所）の2つの情報を受け取ります。
* **`tagger = MeCab.Tagger(f"-r {mecabrc_path}")`**: MeCabを使って文章を解析するための準備をしています。`mecabrc_path`はMeCabの動作設定を指定するファイルです。
* **`node = tagger.parseToNode(text)`**: 渡された文章 (`text`) をMeCabに解析させ、その結果を`node`という変数に格納します。MeCabは文章を単語ごとに区切り、それぞれの単語の品詞などの情報を付与します。
   例えば、「今日は天気」という部分を解析すると、以下のような情報が得られます。

   ```
   今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー
   は	助詞,係助詞,*,*,*,*,は,ハ,ワ
   天気	名詞,一般,*,*,*,*,天気,テンキ,テンキ
   ```
   各行が単語に対応し、単語の表記、品詞などの情報が含まれます。
* **`nouns = []`**: 名詞を格納するための空のリストを作成します。
* **`while node:`**:  MeCabによって解析された単語の情報を順番に処理するための繰り返し処理です。
* **`if node.feature.split(",")[0] == "名詞":`**: 現在処理している単語が名詞かどうかを判定しています。`node.feature`には品詞などの情報がカンマ区切りで含まれており、最初の要素が品詞名です。
* **`nouns.append(node.surface)`**: もし名詞であれば、その単語の表面形（実際の表記）を`nouns`リストに追加します。例えば、「今日」や「天気」が追加されます。
* **`node = node.next`**: 次の単語の情報に進みます。
* **`return nouns`**:  抽出された名詞のリストを関数の結果として返します。

```python
def get_noun_frequencies(nouns):
    dict_nouns = {}
    for noun in nouns:
        if noun in dict_nouns:
            dict_nouns[noun] += 1
        else:
            dict_nouns[noun] = 1
    return sorted(dict_nouns.items(), key=lambda x: x[1], reverse=True)
```
この部分は、抽出された名詞の出現回数を数える処理です。

* **`def get_noun_frequencies(nouns):`**: 「get_noun_frequencies」という名前の関数を定義しています。この関数は、名詞のリスト (`nouns`) を受け取ります。
* **`dict_nouns = {}`**: 名詞とその出現回数を記録するための空の辞書を作成します。辞書はキーと値のペアを格納するデータ構造です。ここでは、名詞をキー、出現回数を値として使います。
* **`for noun in nouns:`**:  名詞のリストの中身を一つずつ処理する繰り返し処理です。
* **`if noun in dict_nouns:`**: 現在処理している名詞が、すでに辞書にキーとして存在するかどうかを確認します。
* **`dict_nouns[noun] += 1`**: もし辞書に存在すれば、その名詞の出現回数を1増やします。
* **`else:`**: もし辞書に存在しなければ、
* **`dict_nouns[noun] = 1`**: その名詞をキーとして辞書に登録し、出現回数を1とします。
* **`return sorted(dict_nouns.items(), key=lambda x: x[1], reverse=True)`**: 辞書の内容を、出現回数が多い順に並び替えたリストとして返します。`sorted()`関数はリストの要素を並び替える関数で、`key=lambda x: x[1]`は並び替えの基準を各要素の2番目の値（出現回数）とすることを指定し、`reverse=True`は降順で並び替えることを指定します。

```python
def display_top_n(sorted_nouns, n):
    for noun, count in sorted_nouns[:n]:
        print(f"{noun}: {count}")
```
この部分は、出現回数の多い名詞を上位から指定された数だけ表示する処理です。

* **`def display_top_n(sorted_nouns, n):`**: 「display_top_n」という名前の関数を定義しています。この関数は、並び替えられた名詞のリスト (`sorted_nouns`) と、表示する上位の数 (`n`) を受け取ります。
* **`for noun, count in sorted_nouns[:n]:`**: 並び替えられたリストの先頭から`n`個の要素を取り出し、順番に処理します。
* **`print(f"{noun}: {count}")`**: 取り出した名詞とその出現回数を表示します。例えば、「公園: 2」のように表示されます。

```python
def main():
    mecabrc_path = "/etc/mecabrc"
    file_path = "./data/sample.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        exit()

    nouns = extract_nouns(text, mecabrc_path)
    if nouns:
        noun_frequencies = get_noun_frequencies(nouns)
        display_top_n(noun_frequencies, 10)
```
この部分は、プログラム全体の実行順序を定義しています。

* **`def main():`**: 「main」という名前の関数を定義しています。これがプログラムの主な処理の流れを記述する場所です。
* **`mecabrc_path = "/etc/mecabrc"`**: MeCabの設定ファイルへのパスを`mecabrc_path`変数に設定します。
* **`file_path = "./data/sample.txt"`**: 解析対象のテキストファイルへのパスを`file_path`変数に設定します。
* **`try:` ~ `except FileNotFoundError:`**:  ファイルを読み込む際にエラーが発生した場合の処理を記述しています。`try`ブロック内の処理が失敗した場合、`except`ブロックの処理が実行されます。ここでは、指定されたファイルが見つからない場合にエラーメッセージを表示してプログラムを終了します。
* **`with open(file_path, "r", encoding="utf-8") as f:`**:  指定されたテキストファイルを読み込みモード（"r"）で開き、ファイルオブジェクトを`f`という名前で扱えるようにします。`encoding="utf-8"`は、ファイルがUTF-8形式でエンコードされていることを指定します。
* **`text = f.read()`**: 開いたファイルの内容をすべて読み込み、`text`変数に格納します。
* **`nouns = extract_nouns(text, mecabrc_path)`**:  `extract_nouns`関数を呼び出し、読み込んだテキストから名詞を抽出します。
* **`if nouns:`**: 抽出された名詞が存在する場合に、
* **`noun_frequencies = get_noun_frequencies(nouns)`**:  `get_noun_frequencies`関数を呼び出し、名詞の出現回数を集計します。
* **`display_top_n(noun_frequencies, 10)`**:  `display_top_n`関数を呼び出し、出現回数の多い名詞上位10個を表示します。

```python
if __name__ == "__main__":
    main()
```
この部分は、プログラムが直接実行された場合に`main()`関数を呼び出すための記述です。

## プログラムの実行

このプログラムを実行するには、まずプログラムのコードを「.py」という拡張子のファイルに保存します（例：`noun_analyzer.py`）。次に、ターミナルやコマンドプロンプトを開き、プログラムを保存したディレクトリに移動して、以下のコマンドを実行します。

```bash
python noun_analyzer.py
```

「./data/sample.txt」ファイルに前述の例のような文章が書かれていれば、プログラムは以下のような出力を表示します。

```
公園: 2
今日: 1
天気: 1
子供: 1
花: 1
```

これは、文章中で「公園」という名詞が2回、「今日」「天気」「子供」「花」という名詞がそれぞれ1回出現したことを示しています。

この解説で、プログラムの各部分の役割と処理の流れを理解していただければ幸いです。

<br>
<br>

---

# 27

**プログラムの全体的な流れ**

このプログラムは、Irisデータセットを用いて、機械学習によってアヤメの種類を分類するモデルを構築し、その性能を評価するものです。具体的には、以下の手順で処理が進みます。

1. **データセットの読み込み:** アヤメの特徴量と種類が格納されたデータセットを読み込みます。
2. **データ分割:** 読み込んだデータを、モデルの学習に使用する訓練データと、モデルの性能評価に使用するテストデータに分割します。
3. **モデルの選択と学習:**  選択した機械学習モデル（今回はロジスティック回帰）を、訓練データを用いて学習させます。
4. **モデルの評価:** 学習済みのモデルを用いて、訓練データとテストデータに対する予測を行い、その正解率を計算してモデルの性能を評価します。

**コードの各部分の詳細な解説**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
```

この部分は、プログラムで使用するライブラリやモジュールから必要な機能をインポートしています。

*   `from sklearn.datasets import load_iris`: scikit-learnライブラリの`datasets`モジュールから、Irisデータセットを読み込むための関数`load_iris`をインポートします。
*   `from sklearn.model_selection import train_test_split`: scikit-learnライブラリの`model_selection`モジュールから、データを訓練用とテスト用に分割するための関数`train_test_split`をインポートします。
*   `from sklearn.linear_model import LogisticRegression`: scikit-learnライブラリの`linear_model`モジュールから、分類アルゴリズムの一つであるロジスティック回帰モデルのクラス`LogisticRegression`をインポートします。
*   `from sklearn.ensemble import RandomForestClassifier`: scikit-learnライブラリの`ensemble`モジュールから、分類アルゴリズムの一つであるランダムフォレストモデルのクラス`RandomForestClassifier`をインポートします。この行はコメントアウトされていますが、別の分類器を使用する場合のために記述されています。
*   `from sklearn.metrics import accuracy_score`: scikit-learnライブラリの`metrics`モジュールから、モデルの性能評価指標である正解率を計算するための関数`accuracy_score`をインポートします。

```python
iris = load_iris()
X = iris.data
y = iris.target
```

ここでは、Irisデータセットを読み込み、特徴量とターゲット変数に分割しています。

*   `iris = load_iris()`: `load_iris`関数を実行して、Irisデータセットをオブジェクトとして読み込み、変数`iris`に格納します。
*   `X = iris.data`:  `iris`オブジェクトの`data`属性には、アヤメの特徴量データ（がく片の長さ、がく片の幅、花弁の長さ、花弁の幅）がNumPy配列として格納されています。これを変数`X`に代入します。
*   `y = iris.target`: `iris`オブジェクトの`target`属性には、アヤメの種類を示すターゲット変数（0: セトサ, 1: バーシクル, 2: バージニカ）がNumPy配列として格納されています。これを変数`y`に代入します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```

ここでは、データを訓練データとテストデータに分割しています。

*   `train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)`:  `train_test_split`関数を用いて、特徴量データ`X`とターゲット変数`y`を分割します。
    *   `test_size=0.2`:  テストデータとして使用するデータの割合を20%に設定しています。残りの80%が訓練データとして使用されます。
    *   `random_state=42`: データ分割の際の乱数シードを固定しています。これにより、コードを何度実行しても同じデータ分割結果が得られ、再現性が確保されます。
    *   `stratify=y`:  ターゲット変数`y`に基づいて層化抽出を行います。これにより、訓練データとテストデータにおける各クラス（アヤメの種類）の割合が、元のデータセットにおける割合とほぼ同じになるように分割されます。クラスの偏りを防ぎ、より公平なモデル評価を行うために有効です。
*   `X_train, X_test, y_train, y_test = ...`: 分割されたデータは、それぞれ以下の変数に格納されます。
    *   `X_train`: 訓練用の特徴量データ
    *   `X_test`: テスト用の特徴量データ
    *   `y_train`: 訓練用のターゲット変数
    *   `y_test`: テスト用のターゲット変数

```python
model = LogisticRegression(random_state=42, max_iter=1000)
# model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)
```

ここでは、分類モデルの選択と学習を行っています。

*   `model = LogisticRegression(random_state=42, max_iter=1000)`: ロジスティック回帰モデルのインスタンスを作成し、変数`model`に代入します。
    *   `random_state=42`: モデルの初期化に使用する乱数シードを固定しています。これにより、毎回同じ初期状態で学習が開始され、結果の再現性が高まります。
    *   `max_iter=1000`: モデルの学習における最大反復回数を設定しています。モデルが収束しない場合に増やします。
*   `# model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)`: ランダムフォレストモデルを使用する場合のコードです。コメントアウトされているため、現在は実行されません。
    *   `n_estimators=100`: ランダムフォレストに含まれる決定木の数を指定します。
    *   `max_depth=5`: 決定木の最大の深さを指定します。
    *   `random_state=42`: ランダムフォレストの初期化に使用する乱数シードを固定します。
*   `model.fit(X_train, y_train)`:  作成したモデル(`model`)に対して、訓練データの特徴量`X_train`とターゲット変数`y_train`を与え、モデルを学習させます。学習により、モデルは特徴量とターゲット変数の間の関係性を学習します。

```python
y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
print(f'Accuracy rate of training data: {train_accuracy:.4f}')

y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f'Accuracy rate of test data: {test_accuracy:.4f}')
```

ここでは、学習済みモデルの評価を行っています。

*   `y_train_pred = model.predict(X_train)`: 学習済みモデル(`model`)を用いて、訓練データの特徴量`X_train`に対する予測を行い、その結果を`y_train_pred`に格納します。
*   `train_accuracy = accuracy_score(y_train, y_train_pred)`:  訓練データの実際のターゲット変数`y_train`と、モデルによる予測結果`y_train_pred`を比較し、正解率を計算します。
*   `print(f'Accuracy rate of training data: {train_accuracy:.4f}')`: 計算された訓練データの正解率を表示します。
*   `y_test_pred = model.predict(X_test)`: 学習済みモデル(`model`)を用いて、テストデータの特徴量`X_test`に対する予測を行い、その結果を`y_test_pred`に格納します。
*   `test_accuracy = accuracy_score(y_test, y_test_pred)`: テストデータの実際のターゲット変数`y_test`と、モデルによる予測結果`y_test_pred`を比較し、正解率を計算します。
*   `print(f'Accuracy rate of test data: {test_accuracy:.4f}')`: 計算されたテストデータの正解率を表示します。

```python
# print(f'==============================')
# for feature_name, importance in zip(iris.feature_names, model.feature_importances_):
#     print(f'{feature_name}: {importance:.2f}')
```

この部分はコメントアウトされており、現在は実行されません。これは、ランダムフォレストモデルを使用した場合に、各特徴量の重要度を表示するためのコードです。

*   `iris.feature_names`: Irisデータセットの特徴量の名前（例: 'sepal length (cm)', 'sepal width (cm)', ...）が格納されています。
*   `model.feature_importances_`: 学習済みのランダムフォレストモデルにおける各特徴量の重要度が格納されています。この属性は、ロジスティック回帰モデルには存在しません。
*   `zip(iris.feature_names, model.feature_importances_)`: 特徴量の名前とその重要度をペアにして反復処理を行います。
*   `print(f'{feature_name}: {importance:.2f}')`: 各特徴量の名前と重要度をフォーマットして表示します。

このコードを実行することで、Irisデータセットを用いたアヤメの品種分類モデルの構築と評価が行われ、訓練データとテストデータにおける正解率が確認できます。


<br>
<br>

---

# 30

このコードは、ワインの成分データを使って、そのワインがどの種類（クラス）に属するかを予測するプログラムです。具体的には、以下の手順で処理を進めています。

## 1. ライブラリのインポート

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
```

この部分では、プログラムで使う便利な道具箱（ライブラリ）を準備しています。それぞれのライブラリは、特定の作業を効率的に行うための機能を提供しています。

*   **`import pandas as pd`**:  `pandas` は、表形式のデータを扱うのに非常に強力なライブラリです。データの読み込み、整理、加工など、データ分析の基礎となる作業で利用します。`as pd` とすることで、以降 `pandas` を `pd` という短い名前で使えるようにしています。

    *   **例:**  ワインのデータを表として読み込んだり、表の一部の列を選んだりする際に使います。

*   **`import matplotlib.pyplot as plt`**: `matplotlib` は、グラフを描画するための基本的なライブラリです。データの可視化に役立ちます。`as plt` とすることで、以降 `matplotlib.pyplot` を `plt` という短い名前で使えるようにしています。

    *   **例:**  混同行列や特徴量の重要度を棒グラフで表示する際に使います。

*   **`import seaborn as sns`**: `seaborn` は、`matplotlib` をベースにした、より洗練された統計グラフを描画するためのライブラリです。ヒートマップなどの複雑なグラフを簡単に作成できます。`as sns` とすることで、以降 `seaborn` を `sns` という短い名前で使えるようにしています。

    *   **例:**  混同行列を色分けされたヒートマップとして見やすく表示する際に使います。

*   **`from sklearn.model_selection import train_test_split, cross_val_score, KFold`**: `sklearn` (scikit-learn) は、機械学習のための様々な機能を提供するライブラリです。`model_selection` モジュールには、データを分割したり、モデルの性能を評価したりするためのツールが含まれています。

    *   **`train_test_split`**:  データを訓練用とテスト用に分割する際に使います。
    *   **`cross_val_score`**: 交差検証という手法でモデルの性能を評価する際に使います。
    *   **`KFold`**: 交差検証を行う際に、データをどのように分割するかを指定するために使います。

*   **`from sklearn.ensemble import RandomForestClassifier`**: `sklearn.ensemble` モジュールには、複数の決定木を組み合わせた強力な分類アルゴリズムであるランダムフォレストが含まれています。

    *   **例:**  ワインの種類を予測するモデルとしてランダムフォレストを使います。

*   **`from sklearn.metrics import accuracy_score, confusion_matrix`**: `sklearn.metrics` モジュールには、モデルの性能を評価するための指標が用意されています。

    *   **`accuracy_score`**: モデルの予測がどれくらい正確か（正解率）を計算する際に使います。
    *   **`confusion_matrix`**: モデルの予測結果が、実際の結果とどのように異なっているかを示す表（混同行列）を作成する際に使います。

*   **`from sklearn.preprocessing import StandardScaler`**: `sklearn.preprocessing` モジュールには、データの前処理を行うためのツールが含まれています。今回は使用していませんが、例えば、特徴量の値を一定の範囲に収める（標準化）などの処理に使われます。

## 2. データセットの読み込み

```python
# Wine recognition datasetの読み込み
# https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df = pd.read_csv(url, header=None)
df.columns = ['class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
```

ここでは、インターネット上にあるワインのデータセットを読み込んでいます。

*   **`url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"`**:  ワインのデータが置いてある場所（URL）を変数 `url` に格納しています。
*   **`df = pd.read_csv(url, header=None)`**: `pandas` の `read_csv` 関数を使って、指定されたURLからデータを読み込み、`df` という名前の表形式のデータ（DataFrame）として保存しています。`header=None` は、データに列名が含まれていないことを示しています。

    *   **例:**  この行を実行すると、ワインの成分に関する数値データが、行と列からなる表として `df` に格納されます。
*   **`df.columns = ['class', 'Alcohol', 'Malic acid', ... , 'Proline']`**:  読み込んだデータに列名を付けています。元のデータには列名がなかったので、それぞれの列が何を表しているかを明確にするために、リスト形式で列名を指定しています。

    *   **例:**  `df` に格納されたデータの最初の列はワインの種類を表す `class`、2番目の列はアルコール度数を表す `Alcohol`、といった具合に名前が付けられます。

## 3. データの確認

```python
# データの先頭5行を表示して確認
print(df.head())
```

読み込んだデータが正しく読み込まれているかを確認するために、`df.head()` を使ってデータの最初の5行を表示しています。これにより、データの形式や内容をざっと把握できます。

*   **例:**  実行すると、`df` に格納されたデータの最初の5行が画面に表示されます。各行が個々のワインのデータに対応し、各列がワインの成分の値や種類を表していることが確認できます。

## 4. 特徴量と目的変数の分離

```python
# 特徴量と目的変数の分離
X = df.drop('class', axis=1)
y = df['class']
```

機械学習では、予測に使いたい情報（特徴量）と、予測したい対象（目的変数）を分けて扱う必要があります。

*   **`X = df.drop('class', axis=1)`**:  `df` から `class` という列を削除し、残りの列を特徴量として `X` に格納しています。`axis=1` は列方向の操作を示す指定です。

    *   **例:**  `X` には、アルコール度数、リンゴ酸の量など、ワインの種類を予測するために使う13個の成分データが格納されます。
*   **`y = df['class']`**:  `df` から `class` という列だけを抽出し、目的変数として `y` に格納しています。これが予測したいワインの種類です。

    *   **例:**  `y` には、各ワインがどの種類（1, 2, または 3）に属するかの情報が格納されます。

## 5. 分類モデルの選択

```python
# 分類モデルの選択 (例: ランダムフォレスト)
model = RandomForestClassifier(random_state=42)
```

ここでは、ワインの種類を予測するために使う機械学習のアルゴリズム（モデル）を選択しています。今回は、`RandomForestClassifier` という、比較的精度が高く、扱いやすいアルゴリズムを選んでいます。

*   **`model = RandomForestClassifier(random_state=42)`**:  `RandomForestClassifier` モデルのインスタンスを作成し、`model` という変数に格納しています。`random_state=42` は、結果の再現性を確保するために乱数の生成を固定する設定です。

    *   **例:**  `model` は、これからワインの成分データに基づいて種類を予測するための「予測器」のようなものになります。

## 6. 交差検証の実行

```python
# 交差検証の実行 (KFold)
kf = KFold(n_splits=5, shuffle=True, random_state=42)  # 5分割交差検証
cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
```

交差検証は、モデルの性能をより正確に評価するための手法です。データをいくつかのグループに分割し、それぞれを評価に使用することで、偶然による偏りを減らすことができます。

*   **`kf = KFold(n_splits=5, shuffle=True, random_state=42)`**:  `KFold` を使って、データを5つのグループに分割する設定を作成しています。`shuffle=True` はデータをシャッフルしてから分割することを意味し、`random_state=42` はシャッフルのランダム性を固定します。

    *   **例:**  178個のワインデータを、ほぼ均等な5つのグループに分けます。
*   **`cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')`**:  作成したモデル (`model`) とデータ (`X`, `y`) を使い、`kf` で設定した分割方法で交差検証を実行しています。`scoring='accuracy'` は、モデルの性能を正解率で評価することを指定しています。`cross_val_score` は、各分割での評価結果（正解率）をリストとして返します。

    *   **例:**  5つのグループを使って、5回モデルの訓練と評価を行います。例えば、1回目の評価では最初のグループをテストデータ、残りの4つのグループを訓練データとして使用します。`cv_scores` には、それぞれの評価での正解率が格納されます。

## 7. 交差検証の結果表示

```python
# 交差検証の結果表示
print("各分割の正解率:", cv_scores)
print("平均正解率:", cv_scores.mean())
```

交差検証で得られた結果を表示しています。

*   **`print("各分割の正解率:", cv_scores)`**:  各分割ごとの正解率をリスト形式で表示します。
*   **`print("平均正解率:", cv_scores.mean())`**:  すべての分割の正解率の平均値を計算し、表示します。この平均値が、モデルの汎化性能（未知のデータに対する予測能力）のおおよその目安となります。

    *   **例:**  「各分割の正解率: [0.972..., 1.        , 0.944..., 0.971..., 1.        ]」のように表示され、それぞれの数値が各分割での正解率を表します。「平均正解率: 0.977...」のように表示され、モデルのおおよその予測精度がわかります。

## 8. データセットの分割（訓練データとテストデータ）

```python
# オプション: データセットを訓練データとテストデータに分割して最終評価
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

モデルの最終的な性能を評価するために、データを訓練用とテスト用に分割します。訓練データでモデルを学習させ、テストデータで学習したモデルの性能を評価します。

*   **`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`**:  `train_test_split` 関数を使って、特徴量 (`X`) と目的変数 (`y`) を、訓練用とテスト用に分割しています。
    *   `test_size=0.2` は、データ全体の20%をテストデータとして使用することを指定しています。残りの80%が訓練データになります。
    *   `random_state=42` は、分割の際のランダム性を固定するための設定です。これにより、何度実行しても同じデータ分割が行われます。

    *   **例:**  178個のワインデータのうち、約142個が訓練データ、約36個がテストデータとして分割されます。`X_train` と `y_train` には訓練用の特徴量と目的変数が、`X_test` と `y_test` にはテスト用の特徴量と目的変数が格納されます。

## 9. モデルの学習

```python
# モデルの学習
model.fit(X_train, y_train)
```

分割した訓練データを使って、選択したモデル (`RandomForestClassifier`) にワインの成分と種類の関係を学習させます。

*   **`model.fit(X_train, y_train)`**:  `fit` メソッドを使って、訓練用の特徴量 (`X_train`) と対応する正解ラベル (`y_train`) をモデルに与え、学習を実行します。

    *   **例:**  モデルは、訓練データに含まれる様々なワインの成分と、それらがどの種類に分類されるかのパターンを学習します。

## 10. テストデータでの予測

```python
# テストデータでの予測
y_pred = model.predict(X_test)
```

学習済みのモデルを使って、テストデータに含まれるワインの種類を予測します。

*   **`y_pred = model.predict(X_test)`**:  `predict` メソッドにテスト用の特徴量 (`X_test`) を与えることで、モデルは各ワインがどの種類に属するかを予測し、その結果を `y_pred` に格納します。

    *   **例:**  モデルは、まだ見たことのないテストデータのワインの成分情報に基づいて、そのワインの種類を予測します。`y_pred` には、モデルが予測した種類（1, 2, または 3）が格納されます。

## 11. テストデータの正解率

```python
# テストデータの正解率
test_accuracy = accuracy_score(y_test, y_pred)
print("テストデータの正解率:", test_accuracy)
```

予測結果がどれくらい正確だったかを評価します。

*   **`test_accuracy = accuracy_score(y_test, y_pred)`**:  `accuracy_score` 関数を使って、テストデータの実際のラベル (`y_test`) とモデルの予測結果 (`y_pred`) を比較し、正解率を計算します。
*   **`print("テストデータの正解率:", test_accuracy)`**:  計算された正解率を表示します。

    *   **例:**  「テストデータの正解率: 0.972...」のように表示され、モデルがテストデータ中のワインの種類を約97%の精度で正しく予測できたことを示します。

## 12. 混同行列の表示

```python
# 混同行列の表示
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=df['class'].unique(),
            yticklabels=df['class'].unique())
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()
```

混同行列は、モデルの予測結果の詳細を示す表です。どの種類のワインが、どの種類と誤って予測されたのかを確認できます。

*   **`cm = confusion_matrix(y_test, y_pred)`**:  `confusion_matrix` 関数を使って、テストデータの実際のラベル (`y_test`) とモデルの予測結果 (`y_pred`) から混同行列を作成し、`cm` に格納します。
*   **`plt.figure(figsize=(8, 6))`**:  グラフのサイズを指定します。
*   **`sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=df['class'].unique(), yticklabels=df['class'].unique())`**:  `seaborn` の `heatmap` 関数を使って、混同行列をヒートマップとして表示します。
    *   `annot=True`: 各セルに数値を表示します。
    *   `fmt='d'`: 数値を整数形式で表示します。
    *   `cmap='Blues'`:  使用する色を指定します。
    *   `xticklabels` と `yticklabels`:  X軸とY軸のラベルをワインの種類（クラス）にします。
*   **`plt.xlabel('Predicted Label')`**:  X軸のラベルを設定します。
*   **`plt.ylabel('True Label')`**:  Y軸のラベルを設定します。
*   **`plt.title('Confusion Matrix')`**:  グラフのタイトルを設定します。
*   **`plt.show()`**:  グラフを表示します。

    *   **例:**  ヒートマップが表示され、例えば、実際の種類が「1」のワインのうち、いくつが正しく「1」と予測され、いくつが誤って「2」や「3」と予測されたかがわかります。

## 13. 特徴量の重要度

```python
# 特徴量の重要度
feature_importances = model.feature_importances_
feature_names = X.columns
indices = sorted(range(len(feature_importances)), key=lambda k: feature_importances[k], reverse=True)

plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importances)), feature_importances[indices], align='center')
plt.xticks(range(len(feature_importances)), [feature_names[i] for i in indices], rotation=45, ha='right')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()
```

ランダムフォレストのようなモデルでは、学習の過程で各特徴量が予測にどれくらい貢献したかを評価する「特徴量の重要度」という指標が得られます。この部分では、どの成分がワインの種類を予測する上で重要だったかを可視化しています。

*   **`feature_importances = model.feature_importances_`**:  学習済みモデルから特徴量の重要度を取得し、`feature_importances` に格納します。
*   **`feature_names = X.columns`**:  特徴量の名前（列名）を `feature_names` に格納します。
*   **`indices = sorted(range(len(feature_importances)), key=lambda k: feature_importances[k], reverse=True)`**:  特徴量の重要度が高い順に、特徴量のインデックスをソートしています。
*   **`plt.figure(figsize=(10, 6))`**:  グラフのサイズを指定します。
*   **`plt.bar(range(len(feature_importances)), feature_importances[indices], align='center')`**:  棒グラフを作成します。X軸は特徴量の数、Y軸は重要度を表します。
*   **`plt.xticks(range(len(feature_importances)), [feature_names[i] for i in indices], rotation=45, ha='right')`**:  X軸のラベルを特徴量の名前に設定し、見やすいように回転させています。
*   **`plt.xlabel('Feature')`**:  X軸のラベルを設定します。
*   **`plt.ylabel('Importance')`**:  Y軸のラベルを設定します。
*   **`plt.title('Feature Importance')`**:  グラフのタイトルを設定します。
*   **`plt.tight_layout()`**:  グラフの要素が重ならないようにレイアウトを調整します。
*   **`plt.show()`**:  グラフを表示します。

    *   **例:**  棒グラフが表示され、例えば「Flavanoids」という成分が最も重要度が高く、次いで「Proline」が高いといったように、どの成分がワインの種類を予測する上で重要だったかが一目でわかります。


<br>
<br>

---

# 32

このコードは、時系列データにおける自己相関関数を計算し、その結果をグラフで表示するPythonプログラムです。以下に、コードの各部分について、処理過程や具体的な例を交えながら詳しく解説します。

**コード全体の概要**

このプログラムは、過去の自分のデータが、どれくらい後の自分のデータに影響を与えているかを分析する「自己相関分析」を行うものです。例えば、今日の気温が、数日後の気温にどれくらい関係があるのかを調べることができます。

**使用しているライブラリ**

プログラムの最初に、以下のライブラリを読み込んでいます。

* `numpy as np`: 数値計算を行うためのライブラリです。特に、配列（たくさんの数字をまとめたもの）の操作に便利です。
* `pandas as pd`: 表形式のデータ（例えば、CSVファイルのようなデータ）を扱うためのライブラリです。
* `statsmodels.graphics.tsaplots import plot_acf`: 時系列データの自己相関関数をグラフで表示するための関数が含まれるライブラリです。
* `matplotlib.pyplot as plt`: グラフを描画するためのライブラリです。

**コードの各部分の詳細**

## 1. **関数の定義 (`calculate_autocorrelation`)**

   ```python
   def calculate_autocorrelation(data: np.ndarray, maxlag: int) -> np.ndarray:
       """
       自己相関を計算する関数

       Args:
           data: 時系列データ (numpy.ndarray)
           maxlag: 最大ラグ (int)

       Returns:
           自己相関係数の配列 (numpy.ndarray)
       """
       autocorr = np.correlate(data, data, mode='full')
       autocorr = autocorr[autocorr.size//2 : autocorr.size//2 + maxlag+1]
       return autocorr / autocorr[0]
   ```

   この部分は、自己相関関数を計算する処理をまとめたものです。

   * **`def calculate_autocorrelation(data: np.ndarray, maxlag: int) -> np.ndarray:`**:  `calculate_autocorrelation` という名前の関数を定義しています。この関数は、`data`（分析する時系列データ）と `maxlag`（自己相関を計算する最大の時間差）という2つの情報を入力として受け取り、計算結果である自己相関係数の配列を返します。
      * `data: np.ndarray`:  `data` はNumPyの配列（`ndarray`）であることを指定しています。例えば、`[10, 12, 15, 13, 11]` のような気温のデータが入ります。
      * `maxlag: int`: `maxlag` は整数（`int`）であることを指定しています。例えば、`10` と指定した場合、10日後までの自己相関を計算します。
      * `-> np.ndarray`:  この関数がNumPyの配列を返すことを指定しています。

   * **`autocorr = np.correlate(data, data, mode='full')`**: NumPyの `correlate` 関数を使って、データ自身の相関を計算しています。
      * 具体例として、`data` が `[1, 2, 3]` の場合、`np.correlate(data, data, mode='full')` は `[3, 8, 14, 8, 3]` のような結果を返します。これは、データのすべての可能な組み合わせにおける相関を計算したものです。

   * **`autocorr = autocorr[autocorr.size//2 : autocorr.size//2 + maxlag+1]`**:  `np.correlate` で計算された相関の中から、必要な部分（0から`maxlag`までの時間差に対応する部分）を抽出しています。
      * 例えば、`maxlag` が 2 の場合、上記の結果から中央付近の3つの要素 `[8, 14, 8]` が抽出されます。これらは、0日後、1日後、2日後の自己相関に対応します。

   * **`return autocorr / autocorr[0]`**: 計算された自己相関の値を、0日後の自己相関（これは常に1になります）で割ることで正規化しています。これにより、自己相関係数の値が-1から1の範囲に収まり、解釈しやすくなります。

## 2. **関数の定義 (`find_max_autocorrelation_lag`)**

   ```python
   def find_max_autocorrelation_lag(autocorr: np.ndarray) -> int or None:
       """
       自己相関係数が最大となるラグを返す関数

       Args:
           autocorr: 自己相関係数の配列 (numpy.ndarray)

       Returns:
           最大のラグ (int) または データが不十分な場合は None
       """
       if len(autocorr) <= 1:
           return None
       max_lag_index = np.argmax(autocorr[1:]) + 1
       return max_lag_index
   ```

   この部分は、計算された自己相関係数の中で、最も強い相関を示す時間差（ラグ）を見つける処理をまとめたものです。

   * **`def find_max_autocorrelation_lag(autocorr: np.ndarray) -> int or None:`**: `find_max_autocorrelation_lag` という名前の関数を定義しています。この関数は、自己相関係数の配列を入力として受け取り、最大の自己相関係数を示す時間差を返します。
      * `autocorr: np.ndarray`: `autocorr` はNumPyの配列であることを指定しています。これは、`calculate_autocorrelation` 関数から返された自己相関係数の配列です。
      * `-> int or None`: この関数が整数（最大のラグ）または `None` を返すことを指定しています。`None` は、自己相関を計算するのに十分なデータがない場合に返されます。

   * **`if len(autocorr) <= 1:`**: 自己相関を計算するのに十分なデータがない場合（例えば、計算された自己相関係数が1つ以下の場合）は、`None` を返します。

   * **`max_lag_index = np.argmax(autocorr[1:]) + 1`**: NumPyの `argmax` 関数を使って、自己相関係数の配列の中で、2番目以降の要素（0日後の自己相関は常に最大なので除外します）の中で最も大きな値を持つ要素のインデックスを取得し、それに1を足しています。これが、最大の自己相関を示す時間差（ラグ）になります。
      * 例えば、`autocorr` が `[1.0, 0.8, 0.5, 0.9, 0.3]` の場合、`autocorr[1:]` は `[0.8, 0.5, 0.9, 0.3]` となり、この中で最も大きい値は `0.9` で、そのインデックスは 2 です。`2 + 1` で `3` が返されます。これは、3日後の自己相関が最も強いことを意味します。

## 3. **メインの処理 (`if __name__ == "__main__":`)**

   ```python
   if __name__ == "__main__":
       try:
           # データの読み込み
           df = pd.read_csv("https://raw.githubusercontent.com/aweglteo/tokyo_weather_data/main/data.csv", parse_dates=True, index_col=0)
       except Exception as e:
           print(f"データの読み込み中にエラーが発生しました: {e}")
           exit()

       # 分析対象の列
       target_column = "ave_tmp"

       if target_column not in df.columns:
           print(f"エラー：指定された列 '{target_column}' はデータフレームに存在しません。")
           exit()

       # NaN値を処理
       data = df[target_column].dropna().values

       # 最大ラグの設定
       max_lag = 40

       # 自己相関の計算
       autocorr = calculate_autocorrelation(data, max_lag)

       # 最大のラグ
       max_lag_index = find_max_autocorrelation_lag(autocorr)
       if max_lag_index is not None:
           print(f"'{target_column}' の自己相関係数が最大となるタイムラグ: {max_lag_index} 日")
       else:
           print("自己相関を計算するのに十分なデータがありません。")

       # 自己相関プロット (statsmodelsを使用)
       fig, ax = plt.subplots(figsize=(10, 6))
       plot_acf(data, lags=max_lag, ax=ax, title=f"{target_column}の自己相関プロット (statsmodels)")
       plt.show()
   ```

   この部分は、プログラムが実際に実行されるときに実行される処理を記述しています。

   * **`try...except` ブロック**: ファイルの読み込み中にエラーが発生した場合でも、プログラムが異常終了しないようにするための仕組みです。
      * **`df = pd.read_csv("https://raw.githubusercontent.com/aweglteo/tokyo_weather_data/main/data.csv", parse_dates=True, index_col=0)`**: `pandas` の `read_csv` 関数を使って、インターネット上にあるCSVファイルを読み込んでいます。
         * `"https://raw.githubusercontent.com/aweglteo/tokyo_weather_data/main/data.csv"` は、読み込むCSVファイルのURLです。このファイルには、東京の毎日の気象データが含まれています。
         * `parse_dates=True` は、日付に関する列を自動的に日付型として認識するように指示しています。
         * `index_col=0` は、CSVファイルの最初の列をデータのインデックスとして使用するように指示しています。
         * 読み込まれたデータは、`df` という名前の pandas の DataFrame オブジェクトに格納されます。DataFrame は、表形式のデータを扱うのに便利なデータ構造です。例えば、このCSVファイルには、日付、平均気温、最高気温などの列が含まれています。
      * **`except Exception as e:`**:  `try` ブロック内でエラーが発生した場合、この部分が実行されます。
         * `print(f"データの読み込み中にエラーが発生しました: {e}")`: エラーが発生したことをユーザーに知らせるメッセージを表示します。`e` には、発生したエラーの内容が格納されています。
         * `exit()`: プログラムを終了します。

   * **`target_column = "ave_tmp"`**:  分析したいデータの列名を指定しています。ここでは、平均気温 (`ave_tmp`) の自己相関を分析することにしています。

   * **`if target_column not in df.columns:`**: 指定された列名が、読み込んだデータ (`df`) に存在するかどうかを確認しています。
      * 存在しない場合は、エラーメッセージを表示してプログラムを終了します。

   * **`data = df[target_column].dropna().values`**:  指定された列のデータ (`df[target_column]`) を抽出し、欠損値 (NaN) を取り除き (`dropna()`)、NumPy の配列形式に変換しています (`values`)。
      * 例えば、`df['ave_tmp']` が `[15.0, 16.5, NaN, 18.0]` のようなデータだった場合、`dropna()` を適用すると `[15.0, 16.5, 18.0]` となり、最後に `.values` を適用すると NumPy 配列 `[15.0, 16.5, 18.0]` に変換されます。

   * **`max_lag = 40`**:  自己相関関数を計算する際の最大ラグ（時間差）を40日に設定しています。

   * **`autocorr = calculate_autocorrelation(data, max_lag)`**: 先ほど定義した `calculate_autocorrelation` 関数を呼び出し、平均気温の自己相関関数を計算しています。

   * **`max_lag_index = find_max_autocorrelation_lag(autocorr)`**: 先ほど定義した `find_max_autocorrelation_lag` 関数を呼び出し、自己相関係数が最大となるタイムラグを求めています。

   * **`if max_lag_index is not None:`**: 最大のラグが見つかったかどうかで処理を分岐しています。
      * 見つかった場合は、そのタイムラグを「日」単位で表示します。
      * 見つからなかった場合は、自己相関を計算するのに十分なデータがないことを示すメッセージを表示します。

   * **`fig, ax = plt.subplots(figsize=(10, 6))`**:  `matplotlib` を使ってグラフを描画するための準備をしています。
      * `figsize=(10, 6)` は、グラフのサイズを幅10インチ、高さ6インチに設定しています。

   * **`plot_acf(data, lags=max_lag, ax=ax, title=f"{target_column}の自己相関プロット (statsmodels)")`**:  `statsmodels` の `plot_acf` 関数を使って、自己相関関数のグラフを描画しています。
      * `data`:  自己相関を計算するために使用した時系列データです。
      * `lags=max_lag`: グラフに表示するラグの最大値を指定します。
      * `ax=ax`:  グラフを描画する領域を指定します。
      * `title=f"{target_column}の自己相関プロット (statsmodels)"`: グラフのタイトルを設定します。

   * **`plt.show()`**: 描画したグラフを画面に表示します。

<br>
<br>

## [補足]自己相関関数について

### 自己相関とは？

自己相関とは、ある時系列データにおいて、過去のデータと現在のデータがどの程度似ているか、つまり、どれだけ相関しているかを表す指標です。

例えば、気温のデータで考えてみましょう。今日の気温と昨日の気温は、ある程度似ていることが多いですよね。つまり、ある程度の相関があると言えます。これが自己相関の簡単な例です。

### 自己相関関数で何ができるのか？

* **時系列データの特性把握:**
   * データに周期性があるか（季節変動など）
   * データにトレンドがあるか
   * 過去のデータが将来のデータにどの程度影響するか
   * などを調べることができます。
* **時系列モデルの構築:**
   * ARIMAモデルなどの時系列モデルのパラメータを決定する際に、自己相関関数が利用されます。
* **異常検知:**
   * 自己相関から外れるデータは、異常値である可能性があります。

### 自己相関関数の計算とグラフ（コレログラム）

先ほどの気温の例で考えてみましょう。

1. **データの準備:**
   * 過去の気温データ（例えば、過去1年の毎日の気温）を準備します。

2. **自己相関の計算:**
   * 今日の気温と昨日の気温の相関係数を計算します。
   * 今日の気温と2日前の気温の相関係数を計算します。
   * これを、最大ラグ（過去のどの時点まで相関を調べるか）まで繰り返します。

3. **コレログラムの作成:**
   * 横軸にラグ（時間差）、縦軸に自己相関係数をプロットしたグラフを作成します。これをコレログラムといいます。

**コレログラムの見方:**

* **自己相関係数が正:** 過去の値と現在の値が同じ方向に動いていることを示します。
* **自己相関係数が負:** 過去の値と現在の値が逆の方向に動いていることを示します。
* **自己相関係数が0に近い:** 過去の値と現在の値にほとんど相関がないことを示します。
* **周期性:** 特定のラグで自己相関係数が大きくなっていれば、その周期でデータが変動している可能性があります。

### コードの処理内容

あなたのコードでは、以下の処理を行っています。

1. **データの読み込み:** 気温のデータを読み込みます。
2. **自己相関の計算:** `calculate_autocorrelation`関数で、様々なラグにおける自己相関を計算します。
3. **最大ラグの特定:** `find_max_autocorrelation_lag`関数で、自己相関係数が最大となるラグを特定します。
4. **コレログラムの描画:** `plot_acf`関数を使って、コレログラムを描画します。

### 例

例えば、気温データの自己相関が次のようになったとします。

| ラグ | 自己相関係数 |
|---|---|
| 0 | 1.0 |
| 1 | 0.8 |
| 2 | 0.6 |
| 3 | 0.4 |
| ... | ... |

この場合、今日の気温は昨日の気温と強い正の相関があり、2日前、3日前とも正の相関があることがわかります。つまり、気温は徐々に変化していく傾向があると考えられます。

### まとめ

自己相関分析は、時系列データの特性を把握する上で非常に重要な手法です。コレログラムを見ることで、データの周期性やトレンド、過去のデータが将来のデータに与える影響などを視覚的に捉えることができます。

<br>
<br>

---

# 33

**プログラム全体の目的**

このプログラムは、モンテカルロ法という手法を使って、円周率（π）のおおよその値を計算します。モンテカルロ法は、乱数を使って問題を解決する計算方法の一つです。このプログラムでは、円の面積と、その円をぴったり囲む正方形の面積の関係を利用して円周率を推定します。

**モンテカルロ法の基本的な考え方**

半径1の円を考え、その円をぴったりと囲む正方形を考えます。この正方形の一辺の長さは2になります。

* 円の面積は `π * 半径の2乗` なので、半径1の場合、円の面積は `π * 1 * 1 = π` です。
* 正方形の面積は `一辺の長さ * 一辺の長さ` なので、一辺の長さが2の場合、正方形の面積は `2 * 2 = 4` です。

もし、この正方形の中にランダムな点をたくさん打つと、円の中に入る点の割合は、円の面積と正方形の面積の割合に近づくと考えられます。つまり、

`(円の中に入った点の数) / (打った点の総数)` は、おおよそ `(円の面積) / (正方形の面積)` に等しくなります。

上記の面積の計算結果を当てはめると、

`(円の中に入った点の数) / (打った点の総数)` は、おおよそ `π / 4` に等しくなります。

この関係を利用すると、円周率 `π` は、

`π ≒ 4 * (円の中に入った点の数) / (打った点の総数)`

という式で推定できることになります。このプログラムはこの考え方をコードにしたものです。

**コード全体の構造**

このプログラムは大きく分けて3つの部分から構成されています。

1. **`import random`**: 乱数を生成するための準備
2. **`def estimate_pi(n):`**: 円周率を推定する処理をまとめた関数
3. **`if __name__ == '__main__':`**: プログラムを実行する部分

## 1. `import random`

```python
import random
```

この行は、Pythonの標準ライブラリである `random` モジュールをプログラムで使えるようにしています。`random` モジュールには、ランダムな数を生成するための機能が含まれています。このプログラムでは、正方形の中にランダムな点を打つためにこの機能を利用します。

## 2. `def estimate_pi(n):`

```python
def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / n) * 4
    return pi_estimate
```

この部分は、円周率を推定するための処理をまとめた関数を定義しています。関数の名前は `estimate_pi` で、`n` という名前の引数を受け取ります。この `n` は、ランダムな点を打つ回数（試行回数）を表します。

* **`inside_circle = 0`**:  円の中に入った点の数を数えるための変数を定義し、最初に0を設定しています。

* **`for _ in range(n):`**: この行は、`n` 回だけ以下の処理を繰り返すためのループを開始します。例えば、`n` が100の場合、このループの中の処理が100回実行されます。`_` は、ループの中でカウンター変数を使わないことを示す慣習的な書き方です。

* **`x = random.uniform(-1, 1)`**:  `-1` 以上 `1` 以下の範囲でランダムな実数（浮動小数点数）を生成し、変数 `x` に代入します。これは、正方形の横方向の位置を表すランダムな点を生成しています。

* **`y = random.uniform(-1, 1)`**:  `-1` 以上 `1` 以下の範囲でランダムな実数を生成し、変数 `y` に代入します。これは、正方形の縦方向の位置を表すランダムな点を生成しています。
    * **例:** 最初のループでは、`x` に `0.34`、`y` に `-0.78` のようなランダムな値が生成されるかもしれません。次のループでは、`x` に `-0.12`、`y` に `0.55` のような別のランダムな値が生成されるかもしれません。

* **`if x**2 + y**2 <= 1:`**: 生成された点 `(x, y)` が円の中に入っているかどうかを判定します。
    * 原点（0, 0）を中心とする半径1の円の場合、円の内側にある点の座標 `(x, y)` は `x` の2乗と `y` の2乗の和が 1 以下になるという性質があります。
    * **例:**
        * 生成された点が `(0.2, 0.3)` の場合、`0.2**2 + 0.3**2 = 0.04 + 0.09 = 0.13` となり、これは `1` 以下なので、この点は円の内側にあると判定されます。
        * 生成された点が `(0.8, 0.9)` の場合、`0.8**2 + 0.9**2 = 0.64 + 0.81 = 1.45` となり、これは `1` より大きいので、この点は円の外側にあると判定されます。

* **`inside_circle += 1`**:  もし点が円の内側にあると判定された場合、`inside_circle` の値を1増やします。

* **`pi_estimate = (inside_circle / n) * 4`**:  ループが終了した後、円周率の推定値を計算します。
    * `inside_circle / n` は、打った点の総数に対する円の中に入った点の割合を表します。
    * これに `4` を掛けることで、円周率のおおよその値を得ます（上記のモンテカルロ法の基本的な考え方の説明を参照）。
    * **例:** 100回点を打って、そのうち78点が円の中に入った場合、`pi_estimate = (78 / 100) * 4 = 0.78 * 4 = 3.12` と計算されます。

* **`return pi_estimate`**: 計算された円周率の推定値を関数の結果として返します。

## 3. `if __name__ == '__main__':`

```python
if __name__ == '__main__':
    num_traials = [100, 1000, 10000, 100000, 1000000]
    for n in num_traials:
        estimated_pi = estimate_pi(n)
        print(f"Estimated value of pi for {n} trials is {estimated_pi}")
```

この部分は、プログラムが直接実行された場合にのみ実行されるコードです。

* **`num_traials = [100, 1000, 10000, 100000, 1000000]`**:  試行回数のリストを定義しています。このリストには、`estimate_pi` 関数を呼び出す際に使用する様々な試行回数が含まれています。

* **`for n in num_traials:`**: この行は、`num_traials` リストに含まれるそれぞれの試行回数に対して、以下の処理を繰り返すためのループを開始します。例えば、最初のループでは `n` は `100` になり、次のループでは `n` は `1000` になります。

* **`estimated_pi = estimate_pi(n)`**:  `estimate_pi` 関数を現在の試行回数 `n` を引数として呼び出し、返ってきた円周率の推定値を `estimated_pi` という名前の変数に代入します。
    * **例:** 最初のループで `n` が `100` の場合、`estimate_pi(100)` が呼び出され、100回の試行に基づいて円周率が推定されます。もし推定値が `3.12` だった場合、`estimated_pi` に `3.12` が格納されます。

* **`print(f"Estimated value of pi for {n} trials is {estimated_pi}")`**:  現在の試行回数 `n` と、計算された円周率の推定値 `estimated_pi` を画面に表示します。
    * **例:** 最初のループでは、`"Estimated value of pi for 100 trials is 3.12"` のように表示されます。次のループでは、`"Estimated value of pi for 1000 trials is 3.148"` のように、試行回数とそれに対応する推定値が表示されます。

このプログラムを実行すると、様々な試行回数で円周率が推定され、その結果が表示されます。試行回数を増やすほど、モンテカルロ法による円周率の推定値は真の値（約3.14159）に近づくことが期待できます。


<br>
<br>

---

# 34

## コードの解説

このコードは、映画の推薦システムを作るためのPythonプログラムです。具体的には、過去の映画の評価データを使って、あるユーザーがまだ見ていない映画の中から、そのユーザーが好きそうな映画を予測して推薦します。

### 1. データの準備

```python
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# 1. MovieLensデータセットの読み込み
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')
movies_df = pd.read_csv('ml-latest-small/movies.csv')
```

最初に、必要な機能をまとめた部品（ライブラリ）を読み込みます。

*   **pandas (pd):** 表形式のデータを扱うのに便利なライブラリです。
*   **sklearn.neighbors.NearestNeighbors:**  機械学習の機能で、似ているものを探すのに使います。
*   **numpy (np):** 数値計算を行うための基本的なライブラリです。

次に、映画の評価データと映画の情報をファイルから読み込みます。

*   `ratings.csv` には、ユーザーがどの映画を何点で評価したかのデータが入っています。例えば、「ユーザーIDが1の人が、映画IDが31の映画を2.5点で評価した」といった情報が含まれています。このデータは `ratings_df` という名前の表形式のデータとしてプログラム内で扱われます。
*   `movies.csv` には、映画のIDとタイトルなどの情報が入っています。例えば、「映画IDが31の映画のタイトルは'Dangerous Minds'である」といった情報が含まれています。このデータは `movies_df` という名前の表形式のデータとしてプログラム内で扱われます。

### 2. ユーザー-アイテム行列の作成

```python
# ユーザー-アイテム行列の作成
def create_user_item_matrix(ratings):
    return ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

user_item_matrix = create_user_item_matrix(ratings_df)
```

ユーザーと映画の関係を表す表（ユーザー-アイテム行列）を作成します。

*   `create_user_item_matrix(ratings)` という関数は、評価データ (`ratings_df`) を受け取り、ユーザーIDを縦の列、映画IDを横の列として、それぞれのユーザーがそれぞれの映画に付けた評価値を表の要素とするような表を作成します。まだ評価していない映画の箇所は空欄になります。
*   `.fillna(0)` は、空欄になっている箇所を0で埋めます。これは、後で似ているユーザーを探す際に、まだ評価していない映画を「評価が0」とみなすためです。
*   作成された表は `user_item_matrix` という名前で保存されます。例えば、`user_item_matrix` のある行は特定のユーザーの評価傾向を表し、その行の各列の値はそのユーザーが各映画に付けた評価値を表します。

### 3. 類似ユーザー検索モデルの学習

```python
# NearestNeighborsモデルの学習
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(user_item_matrix)
```

似ているユーザーを見つけるための準備をします。

*   `NearestNeighbors(metric='cosine', algorithm='brute')` は、ユーザー間の類似度を計算するためのモデルを作成します。
    *   `metric='cosine'` は、類似度を測る方法としてコサイン類似度を使うことを指定しています。コサイン類似度は、2つのベクトルの向きがどれくらい似ているかを測る指標で、ここではユーザーの評価傾向の類似度を測るために使われます。
    *   `algorithm='brute'` は、すべてのユーザーの組み合わせを調べて最も類似したユーザーを見つける方法を指定しています。
*   `knn.fit(user_item_matrix)` は、作成したモデルに `user_item_matrix` のデータを学習させます。これにより、モデルはユーザー間の類似度を効率的に計算できるようになります。

### 4. 特定のユーザーの評価履歴を取得する関数

```python
def get_user_ratings(user_id, ratings_df, movies_df):
    """
    特定のユーザーの評価履歴を取得する関数。
    """
    user_ratings = ratings_df[ratings_df['userId'] == user_id].merge(movies_df, on='movieId')
    return user_ratings[['movieId', 'title', 'rating']]
```

特定のユーザーが過去に評価した映画のリストを取得するための関数を定義します。

*   `get_user_ratings(user_id, ratings_df, movies_df)` は、ユーザーID、評価データ、映画データを受け取ります。
*   `ratings_df[ratings_df['userId'] == user_id]` は、評価データの中から、指定されたユーザーIDと一致する行（つまり、そのユーザーの評価データ）を抽出します。
*   `.merge(movies_df, on='movieId')` は、抽出した評価データと映画データを、共通の列である `movieId` をキーとして結合します。これにより、評価データに映画のタイトルなどの情報が追加されます。
*   `return user_ratings[['movieId', 'title', 'rating']]` は、結合後のデータから、映画ID、タイトル、評価の列だけを選択して返します。

### 5. 映画を推薦する関数

```python
def recommend_movies(user_id, user_item_matrix, movies_df, knn, top_n=5, n_neighbors=10):
    """
    特定のユーザーに映画をレコメンドし、根拠となる情報も返す関数。
    """
    if user_id not in user_item_matrix.index:
        print(f"ユーザーID {user_id} は評価履歴がありません。")
        return None

    user_row = user_item_matrix.loc[[user_id]]
    distances, neighbor_indices = knn.kneighbors(user_row, n_neighbors=n_neighbors + 1) # 自分自身を含むため + 1

    # 類似ユーザーのIDと類似度を取得 (自分自身を除く)
    similar_users = pd.DataFrame({'neighborId': user_item_matrix.index[neighbor_indices.flatten()[1:]],
                                  'similarity': 1 - distances.flatten()[1:]})
    print(f"\nユーザーID {user_id} と類似度の高いユーザー:")
    print(similar_users)

    # 予測評価値の計算
    n_neighbors_for_pred = min(n_neighbors, len(similar_users))  # 類似ユーザー数がn_neighborsより少ない場合を考慮
    if n_neighbors_for_pred == 0:
        print("類似ユーザーが見つかりませんでした。人気映画からレコメンドします。")
        # 人気映画からレコメンド (例として平均評価の高い映画)
        mean_ratings = ratings_df.groupby('movieId')['rating'].mean().sort_values(ascending=False)
        popular_movies = movies_df[movies_df['movieId'].isin(mean_ratings.head(top_n).index)]
        return popular_movies.merge(mean_ratings, on='movieId').rename(columns={'rating': 'predicted_rating'})

    relevant_neighbors = similar_users['neighborId'].head(n_neighbors_for_pred)
    neighbor_ratings = user_item_matrix.loc[relevant_neighbors]

    # ユーザーがまだ評価していない映画を取得
    unrated_movie_ids = user_item_matrix.columns[user_item_matrix.loc[user_id] == 0]

    predicted_ratings = pd.Series(0.0, index=unrated_movie_ids)
    for movie_id in unrated_movie_ids:
        numerator = 0
        denominator = 0
        for neighbor_id in relevant_neighbors:
            similarity = similar_users[similar_users['neighborId'] == neighbor_id]['similarity'].iloc[0]
            rating = neighbor_ratings.at[neighbor_id, movie_id]
            numerator += similarity * rating
            denominator += abs(similarity)

        if denominator > 0:
            predicted_ratings[movie_id] = numerator / denominator

    print("\n予測評価値:")
    print(predicted_ratings.head(20))

    # レコメンド結果の作成
    recommended_movie_ids = predicted_ratings.sort_values(ascending=False).head(top_n).index
    recommended_movies = movies_df[movies_df['movieId'].isin(recommended_movie_ids)].copy()
    if not recommended_movies.empty:
        recommended_movies['predicted_rating'] = recommended_movies['movieId'].map(predicted_ratings)
    else:
        print("\nレコメンドできる映画が見つかりませんでした。")
        return None

    print("\n予測評価値 (上位):")
    print(predicted_ratings.sort_values(ascending=False).head(top_n))

    return recommended_movies.sort_values(by='predicted_rating', ascending=False)
```

特定のユーザーに映画を推薦する中心となる関数です。

1. **ユーザーの存在確認:**  指定された `user_id` が `user_item_matrix` に存在するかどうかを確認します。もし存在しなければ、「評価履歴がない」というメッセージを表示して、何も推薦せずに処理を終えます。

2. **類似ユーザーの特定:**
    *   `user_row = user_item_matrix.loc[[user_id]]` で、指定されたユーザーの評価データを `user_item_matrix` から取り出します。
    *   `knn.kneighbors(user_row, n_neighbors=n_neighbors + 1)` で、学習済みの `knn` モデルを使って、このユーザーと評価傾向が似ているユーザーを探します。`n_neighbors` は何人の類似ユーザーを探すかを指定するパラメータで、デフォルトでは10です。 `+ 1` しているのは、自分自身も結果に含まれてしまうため、それを含めて指定した人数 + 1 人のユーザーを取得するためです。
    *   結果として、類似ユーザーとの距離 (`distances`) と、`user_item_matrix` におけるそれらのユーザーのインデックス (`neighbor_indices`) が得られます。
    *   `similar_users` というデータフレームを作成し、類似ユーザーのID (`neighborId`) と類似度 (`similarity`) を格納します。類似度は、距離の逆数として計算されます。

3. **類似ユーザーがいない場合の処理:**
    *   もし類似ユーザーが見つからなかった場合 (`n_neighbors_for_pred == 0`) は、人気のある映画を推薦します。
    *   映画の平均評価を計算し、評価の高い順に並べ、上位 `top_n` 件の映画を推薦します。

4. **まだ評価していない映画の予測評価値を計算:**
    *   類似ユーザーの評価情報を使って、指定されたユーザーがまだ評価していない映画に対して、どの程度興味を持つかを予測します。
    *   `unrated_movie_ids` で、指定されたユーザーがまだ評価していない映画のIDを取得します。
    *   各未評価映画について、類似ユーザーの評価と類似度を使って予測評価値を計算します。具体的には、類似ユーザーがその映画に高い評価をつけていれば、そのユーザーも興味を持つ可能性が高いと判断します。

5. **レコメンド結果の作成:**
    *   計算された予測評価値が高い順に映画を並べ、上位 `top_n` 件の映画を推薦リストとして選択します。
    *   推薦された映画のIDを使って、映画のタイトルなどの情報を `movies_df` から取得し、予測評価値と合わせて表示します。

### 6. メインの処理部分

```python
if __name__ == "__main__":
    print("利用可能なユーザーID:")
    print(user_item_matrix.index.tolist())

    while True:
        try:
            user_id_input = int(input("レコメンドを実行するユーザーIDを入力してください (終了するには '0' を入力): "))
            if user_id_input == 0:
                break

            if user_id_input in user_item_matrix.index:
                print(f"\nユーザーID {user_id_input} の評価履歴:")
                user_ratings = get_user_ratings(user_id_input, ratings_df, movies_df)
                print(user_ratings)

                recommended = recommend_movies(user_id_input, user_item_matrix, movies_df, knn, top_n=10) # top_n を 10 に変更
                if recommended is not None:
                    print(f"\nユーザーID {user_id_input} へのレコメンド結果:")
                    print(recommended[['movieId', 'title', 'predicted_rating']])
            else:
                print("入力されたユーザーIDは存在しません。")
        except ValueError:
            print("有効な整数を入力してください。")
```

この部分は、プログラムを実行したときに最初に実行されるコードです。

1. **利用可能なユーザーIDの表示:**  `user_item_matrix` に含まれるユーザーIDのリストを表示し、ユーザーが誰の推薦結果を見たいかを選択できるようにします。
2. **ユーザーからの入力を受け付けるループ:**
    *   `while True:` で無限ループを開始し、ユーザーからの入力を待ち続けます。
    *   `try:` ブロックは、エラーが発生する可能性のあるコードを囲みます。ここでは、ユーザーが整数を入力しない場合に発生するエラーを捕捉します。
    *   `input()` 関数でユーザーにユーザーIDの入力を促します。
    *   ユーザーが `0` を入力すると、 `break` でループを終了し、プログラムを終了します。
    *   入力されたユーザーIDが `user_item_matrix` に存在するかどうかを確認します。
        *   存在する場合、そのユーザーの評価履歴を表示し、`recommend_movies` 関数を使って映画を推薦します。推薦された映画のリストと予測評価値を表示します。
        *   存在しない場合、「入力されたユーザーIDは存在しません。」というメッセージを表示します。
    *   `except ValueError:` は、ユーザーが整数以外の文字を入力した場合に実行され、「有効な整数を入力してください。」というメッセージを表示します。


## [補足] データの中身  (34_data.py)

```bash
root@00a1890e9919:/workspaces/AtCoder/Practice/34# python 34_data.py
ratings_df の情報:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100836 entries, 0 to 100835
Data columns (total 4 columns):
 #   Column     Non-Null Count   Dtype
---  ------     --------------   -----
 0   userId     100836 non-null  int64
 1   movieId    100836 non-null  int64
 2   rating     100836 non-null  float64
 3   timestamp  100836 non-null  int64
dtypes: float64(1), int64(3)
memory usage: 3.1 MB
None

ratings_df の先頭5行:
   userId  movieId  rating  timestamp
0       1        1     4.0  964982703
1       1        3     4.0  964981247
2       1        6     4.0  964982224
3       1       47     5.0  964983815
4       1       50     5.0  964982931

ratings_df の統計量:
              userId        movieId         rating     timestamp
count  100836.000000  100836.000000  100836.000000  1.008360e+05
mean      326.127564   19435.295718       3.501557  1.205946e+09
std       182.618491   35530.987199       1.042529  2.162610e+08
min         1.000000       1.000000       0.500000  8.281246e+08
25%       177.000000    1199.000000       3.000000  1.019124e+09
50%       325.000000    2991.000000       3.500000  1.186087e+09
75%       477.000000    8122.000000       4.000000  1.435994e+09
max       610.000000  193609.000000       5.000000  1.537799e+09

ratings_df の欠損値の数:
userId       0
movieId      0
rating       0
timestamp    0
dtype: int64

ratings_df のユニークなユーザー数: 610
ratings_df のユニークな映画数: 9724

ratings_df の評価値の分布:
rating
0.5     1370
1.0     2811
1.5     1791
2.0     7551
2.5     5550
3.0    20047
3.5    13136
4.0    26818
4.5     8551
5.0    13211
Name: count, dtype: int64

movies_df の情報:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9742 entries, 0 to 9741
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   movieId  9742 non-null   int64
 1   title    9742 non-null   object
 2   genres   9742 non-null   object
dtypes: int64(1), object(2)
memory usage: 228.5+ KB
None

movies_df の先頭5行:
   movieId                               title                                       genres
0        1                    Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy
1        2                      Jumanji (1995)                   Adventure|Children|Fantasy
2        3             Grumpier Old Men (1995)                               Comedy|Romance
3        4            Waiting to Exhale (1995)                         Comedy|Drama|Romance
4        5  Father of the Bride Part II (1995)                                       Comedy

movies_df の欠損値の数:
movieId    0
title      0
genres     0
dtype: int64

movies_df のユニークな映画数: 9742

movies_df の genres のユニークな値:
951

movies_df の genres の上位10個:
genres
Drama                   1053
Comedy                   946
Comedy|Drama             435
Comedy|Romance           363
Drama|Romance            349
Documentary              339
Comedy|Drama|Romance     276
Drama|Thriller           168
Horror                   167
Horror|Thriller          135
Name: count, dtype: int64
```

## [補足] 実行結果 (34.py)

```bash
root@00a1890e9919:/workspaces/AtCoder/Practice/34# python 34.py
利用可能なユーザーID:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610]
レコメンドを実行するユーザーIDを入力してください (終了するには '0' を入力): 1

ユーザーID 1 の評価履歴:
     movieId                           title  rating
0          1                Toy Story (1995)     4.0
1          3         Grumpier Old Men (1995)     4.0
2          6                     Heat (1995)     4.0
3         47     Seven (a.k.a. Se7en) (1995)     5.0
4         50      Usual Suspects, The (1995)     5.0
..       ...                             ...     ...
227     3744                    Shaft (2000)     4.0
228     3793                    X-Men (2000)     5.0
229     3809          What About Bob? (1991)     4.0
230     4006  Transformers: The Movie (1986)     4.0
231     5060    M*A*S*H (a.k.a. MASH) (1970)     5.0

[232 rows x 3 columns]

ユーザーID 1 と類似度の高いユーザー:
   neighborId  similarity
0         266    0.357408
1         313    0.351562
2         368    0.345127
3          57    0.345034
4          91    0.334727
5         469    0.330664
6          39    0.329782
7         288    0.329700
8         452    0.328048
9          45    0.327922

予測評価値:
movieId
2     0.492187
4     0.000000
5     0.486147
7     0.291057
8     0.000000
9     0.000000
10    2.251762
11    0.890794
12    0.195090
13    0.195090
14    0.000000
15    0.000000
16    1.382797
17    0.447150
18    0.000000
19    0.634650
20    0.000000
21    2.209931
22    0.652942
23    0.000000
dtype: float64

予測評価値 (上位):
movieId
589     4.195979
1200    4.119903
2762    3.971041
1610    3.957980
858     3.885992
924     3.855366
1036    3.805436
541     3.710023
1221    3.581387
1968    3.574258
dtype: float64

ユーザーID 1 へのレコメンド結果:
      movieId                              title  predicted_rating
507       589  Terminator 2: Judgment Day (1991)          4.195979
902      1200                      Aliens (1986)          4.119903
2078     2762            Sixth Sense, The (1999)          3.971041
1211     1610   Hunt for Red October, The (1990)          3.957980
659       858              Godfather, The (1972)          3.885992
706       924       2001: A Space Odyssey (1968)          3.855366
793      1036                    Die Hard (1988)          3.805436
474       541                Blade Runner (1982)          3.710023
922      1221     Godfather: Part II, The (1974)          3.581387
1445     1968         Breakfast Club, The (1985)          3.574258
レコメンドを実行するユーザーIDを入力してください (終了するには '0' を入力):
```

<br>
<br>

---

# 35

**全体の流れ**

1. **準備:** Selenium ライブラリに必要な機能を読み込み、検索したいキーワードを設定します。
2. **ブラウザの起動:**  指定された Web ブラウザ（ここでは Chrome）をプログラムから起動します。
3. **Google 検索:** 起動したブラウザで Google のウェブサイトを開き、設定したキーワードで検索を実行します。
4. **検索結果の取得:** 検索結果の中から、上位 5 件のリンクを見つけ出します。
5. **各ページへのアクセスとタイトル表示:** 見つけた 5 つのリンク先のウェブページを順番に開き、それぞれのページのタイトルを表示します。
6. **終了:**  すべての処理が終わったら、起動したブラウザを閉じます。

**コードの行ごとの詳細な解説**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Serviceクラスをインポート
import time
```

- **`from selenium import webdriver`**:  Selenium ライブラリの中で、Web ブラウザを操作するための主要な機能 (`webdriver`) を使えるようにします。例: ブラウザの起動やページの移動など。
- **`from selenium.webdriver.common.by import By`**:  ウェブページ上の特定の要素（例えば、検索窓やリンクなど）を、その種類や属性に基づいて見つけ出すための方法 (`By`) を使えるようにします。例: 名前で探す、CSS セレクタで探すなど。
- **`from selenium.webdriver.common.keys import Keys`**: キーボードのキー操作（Enter キー、Esc キーなど）をプログラムからシミュレートするための機能 (`Keys`) を使えるようにします。
- **`from selenium.webdriver.chrome.service import Service`**:  Chrome ブラウザを起動・管理するための機能 (`Service`) を使えるようにします。これは Selenium の比較的新しいバージョンで ChromeDriver のパスを指定する際に使われます。ただし、現在のコードでは直接は使用していません。
- **`import time`**: プログラムの実行を一時的に停止させる機能 (`time.sleep()`) を使えるようにします。これは、ウェブページの読み込みを待つためなどに使用します。

```python
# 検索キーワード
search_keyword = "Selenium Python ブラウザ自動化"
```

- **`search_keyword = "Selenium Python ブラウザ自動化"`**:  変数 `search_keyword` に、Google 検索で使用するキーワード（ここでは "Selenium Python ブラウザ自動化"）を文字列として設定します。このキーワードを使って Google 検索を行います。

```python
# ChromeDriverのパス (ご自身の環境に合わせて修正)
chromedriver_path = "./chromedriver"  # スクリプトと同じディレクトリに置いた場合
```

- **`chromedriver_path = "./chromedriver"`**:  変数 `chromedriver_path` に、ChromeDriver という外部プログラムのファイルが置かれている場所を指定します。ChromeDriver は、Selenium が Chrome ブラウザを操作するために必要なツールです。`"./chromedriver"` は、Python スクリプトファイルと同じディレクトリに ChromeDriver が置かれている場合を示します。**重要:** 実際にこのコードを動かすには、適切なバージョンの ChromeDriver をダウンロードし、このパスがそのファイルの場所を正しく指しているように設定する必要があります。

```python
# ブラウザの起動 (今回はChromeを使用)
driver = webdriver.Chrome()
```

- **`driver = webdriver.Chrome()`**:  Selenium の機能を使って Chrome ブラウザを起動します。起動されたブラウザの操作は、変数 `driver` を通して行います。この行が実行されると、通常、新しい Chrome のウィンドウが開きます。

```python
try:
    # Google検索にアクセス
    driver.get("https://www.google.com/")
```

- **`driver.get("https://www.google.com/")`**:  `driver` (起動した Chrome ブラウザ) を使って、Google のウェブサイト (`https://www.google.com/`) を開きます。これにより、プログラムで操作している Chrome ウィンドウが Google のホームページを表示します。

```python
    # 検索窓の要素を特定してキーワードを入力
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)  # Enterキーを押して検索
```

- **`search_box = driver.find_element(By.NAME, "q")`**:  開いた Google のページから、名前属性が "q" である要素（これは Google の検索窓です）を見つけ出し、その要素を `search_box` という変数に格納します。
- **`search_box.send_keys(search_keyword)`**:  `search_box` (検索窓) に、事前に設定した検索キーワード (`search_keyword`) を入力します。これは、手動で検索窓にキーワードを入力するのと同じ操作です。
- **`search_box.send_keys(Keys.RETURN)`**:  検索窓で Enter キーが押されたことをシミュレートします。これにより、入力されたキーワードでの検索が開始されます。

```python
    # 検索結果が表示されるまで少し待機
    time.sleep(2)
```

- **`time.sleep(2)`**:  プログラムの実行を 2 秒間一時停止します。これは、Google の検索結果が完全に表示されるのを待つために行います。ネットワーク環境などによっては、もう少し長く待つ必要があるかもしれません。

```python
    # 検索結果の上位5件の要素を取得
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")[:5]
```

- **`search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")[:5]`**:  検索結果のページから、CSS セレクタ `"div.g"` に一致するすべての要素を見つけ出し、そのうち最初の 5 つを `search_results` という変数に格納します。`"div.g"` は、Google の検索結果 1 件分の情報を囲む HTML 要素の CSS クラス名です。これにより、上位 5 件の検索結果の塊を取得できます。

```python
    # 上位5件のページにアクセスしてタイトルを表示
    print(f"「{search_keyword}」の検索結果上位5件のページタイトル:")
    for i, result in enumerate(search_results):
        try:
            # 検索結果からリンク要素を取得
            link_element = result.find_element(By.CSS_SELECTOR, "a")
            link_url = link_element.get_attribute("href")
```

- **`print(f"「{search_keyword}」の検索結果上位5件のページタイトル:")`**:  プログラムの出力として、検索キーワードとこれから表示する内容のプレフィックスを表示します。
- **`for i, result in enumerate(search_results):`**:  取得した検索結果 (`search_results`) を一つずつ処理するループを開始します。`enumerate` を使うことで、各検索結果の要素 (`result`) とそのインデックス (`i`) を同時に取得できます。
- **`link_element = result.find_element(By.CSS_SELECTOR, "a")`**:  現在の検索結果 (`result`) の中から、CSS セレクタ `"a"` に一致する要素（これはリンクを表す HTML タグです）を見つけ出し、`link_element` という変数に格納します。
- **`link_url = link_element.get_attribute("href")`**:  見つけたリンク要素 (`link_element`) から、`href` 属性の値（リンク先の URL）を取得し、`link_url` という変数に格納します。

```python
            # 新しいタブでページを開く
            driver.execute_script("window.open(arguments[0]);", link_url)

            # 新しいタブに切り替え
            driver.switch_to.window(driver.window_handles[-1])

            # ページが完全にロードされるまで少し待機 (より確実に)
            time.sleep(3)
```

- **`driver.execute_script("window.open(arguments[0]);", link_url)`**:  JavaScript のコードを実行して、新しいタブで `link_url` のページを開きます。
- **`driver.switch_to.window(driver.window_handles[-1])`**:  Selenium の操作対象を、新しく開いたタブに切り替えます。`driver.window_handles` は開いているすべてのタブのリストで、`[-1]` は最後のタブ（つまり新しく開いたタブ）を指します。
- **`time.sleep(3)`**:  新しいタブで開いたページが完全に読み込まれるまで、3 秒間プログラムの実行を一時停止します。

```python
            # ページタイトルを取得して表示
            page_title = driver.title
            print(f"{i+1}: {page_title}")

            # タブを閉じる
            driver.close()

            # 元のタブに戻る
            driver.switch_to.window(driver.window_handles[0])
```

- **`page_title = driver.title`**:  現在操作しているタブ（新しく開いたページ）のタイトルを取得し、`page_title` という変数に格納します。
- **`print(f"{i+1}: {page_title}")`**:  取得したページタイトルを、番号付きでプログラムの出力として表示します。
- **`driver.close()`**:  現在操作しているタブ（新しく開いたページ）を閉じます。
- **`driver.switch_to.window(driver.window_handles[0])`**:  Selenium の操作対象を、最初のタブ（Google の検索結果が表示されているタブ）に戻します。

```python
        except Exception as e:
            print(f"{i+1}: ページへのアクセスに失敗しました: {e}")
```

- **`except Exception as e:`**:  `try` ブロック内で何らかのエラーが発生した場合に実行される処理を記述します。
- **`print(f"{i+1}: ページへのアクセスに失敗しました: {e}")`**:  エラーが発生した場合、その旨とエラー内容をプログラムの出力として表示します。

```python
except Exception as e:
    print(f"エラーが発生しました: {e}")
```

- これは、Google 検索へのアクセスや検索キーワードの入力など、`try` ブロックのより広い範囲でエラーが発生した場合に実行される処理です。エラーが発生した場合、その旨とエラー内容をプログラムの出力として表示します。

```python
finally:
    # ブラウザを閉じる
    driver.quit()
```

- **`finally:`**:  `try` ブロック内の処理が正常に終了した場合でも、エラーが発生した場合でも、**必ず**実行される処理を記述します。
- **`driver.quit()`**:  起動した Chrome ブラウザを完全に閉じます。これにより、プログラム実行後にブラウザが残り続けるのを防ぎます。

このコードを実行すると、Chrome ブラウザが自動的に操作され、指定したキーワードで Google 検索を行い、上位 5 件の検索結果のページのタイトルが表示されます。

<br>
<br>

---

# 36

## **コードの概要**

このプログラムは、映画レビューの文章を読み込み、そのレビューが肯定的か否定的かを自動的に分類するものです。具体的には、IMDbという映画レビューのデータセットを使って、文章の特徴を捉え、それを元にレビューが肯定的な意見を含んでいるか、否定的な意見を含んでいるかを判断します。

## **コードの各部分の詳細な解説**

### 1. **ライブラリのインポート**

   ```python
   import numpy as np
   from sklearn.datasets import load_files
   from sklearn.model_selection import train_test_split
   from sklearn.feature_extraction.text import TfidfVectorizer
   from sklearn.linear_model import LogisticRegression
   from sklearn.metrics import accuracy_score
   from sklearn.pipeline import Pipeline
   ```

   - `import numpy as np`:  `numpy` は、数値計算を効率的に行うためのライブラリです。ここでは、配列などの数値を扱うために使用します。`np` という名前で `numpy` を使えるようにしています。
   - `from sklearn.datasets import load_files`: `sklearn` (scikit-learn) は、機械学習のための様々な機能を提供するライブラリです。`sklearn.datasets` モジュールには、データセットを読み込むための機能が含まれています。`load_files` は、特定のフォルダ構造を持つテキストデータを読み込むために使用します。
   - `from sklearn.model_selection import train_test_split`: `sklearn.model_selection` モジュールには、データを訓練用とテスト用に分割する機能が含まれています。今回は使用していませんが、一般的にはモデルの性能を評価するためにデータを分割することが多いです。
   - `from sklearn.feature_extraction.text import TfidfVectorizer`: `sklearn.feature_extraction.text` モジュールには、テキストデータから特徴量を抽出する機能が含まれています。`TfidfVectorizer` は、文章中の単語の重要度を数値化するために使用します。
   - `from sklearn.linear_model import LogisticRegression`: `sklearn.linear_model` モジュールには、線形モデルを用いた分類や回帰の機能が含まれています。`LogisticRegression` は、ロジスティック回帰という分類アルゴリズムのクラスです。
   - `from sklearn.metrics import accuracy_score`: `sklearn.metrics` モジュールには、モデルの性能を評価するための指標が含まれています。`accuracy_score` は、正解率を計算するために使用します。
   - `from sklearn.pipeline import Pipeline`: `sklearn.pipeline` モジュールには、一連の処理をまとめて実行するための `Pipeline` クラスが含まれています。ここでは、テキストのベクトル化とモデルの学習を順番に行うために使用します。

### 2. **データセットのロード**

   ```python
   # 今回は、事前にダウンロードしたIMDbデータセットをロードします。
   # scikit-learnのload_files関数を利用して、フォルダ構造からデータを読み込みます。
   reviews_train = load_files('./aclImdb/train', categories=['pos', 'neg'])
   text_train, y_train = reviews_train.data, reviews_train.target

   reviews_test = load_files('./aclImdb/test', categories=['pos', 'neg'])
   text_test, y_test = reviews_test.data, reviews_test.target
   ```

   - `load_files('./aclImdb/train', categories=['pos', 'neg'])`:  `load_files` 関数を使って、指定されたフォルダ (`./aclImdb/train`) からテキストデータを読み込みます。
     - `'./aclImdb/train'` は、訓練データが格納されているフォルダのパスです。このフォルダの中に、肯定的なレビューが格納された `pos` フォルダと、否定的なレビューが格納された `neg` フォルダがあることを前提としています。
     - `categories=['pos', 'neg']` は、読み込む対象のサブフォルダを指定します。`pos` フォルダのファイルは肯定的なレビュー、`neg` フォルダのファイルは否定的なレビューとして扱われます。
     - 読み込まれたデータは `reviews_train` に格納されます。`reviews_train` は、レビューのテキストデータと、そのレビューが肯定的なものか否定的なものかを示すラベル（0または1）を含んでいます。

   - `text_train, y_train = reviews_train.data, reviews_train.target`: `reviews_train` から、レビューのテキストデータを `text_train` に、対応するラベル（0: 否定, 1: 肯定）を `y_train` にそれぞれ取り出します。

   - 同様の処理をテストデータに対しても行います。`reviews_test` にはテストデータが、`text_test` にはテストデータのテキスト、`y_test` にはテストデータのラベルが格納されます。

   **具体的な処理の例:**
   `./aclImdb/train/pos` フォルダの中に `0_9.txt` というファイルがあり、その内容が "This movie was great!" だったとします。`load_files` はこのファイルを読み込み、`text_train` のどこかの要素に "This movie was great!" という文字列が格納されます。また、このレビューが `pos` フォルダにあったため、`y_train` の対応する要素には 1 （肯定）というラベルが格納されます。`neg` フォルダのレビューについても同様に処理されます。

### 3. **データセットの確認**

   ```python
   # データセットの確認
   print(f"訓練データ数: {len(text_train)}")
   print(f"テストデータ数: {len(text_test)}")
   print(f"クラスラベル (訓練データ): {np.unique(y_train)}")
   ```

   - `print(f"訓練データ数: {len(text_train)}")`: 訓練データ（レビューの文章）がいくつ読み込まれたかを画面に表示します。`len(text_train)` は、`text_train` リストの要素数を返します。
   - `print(f"テストデータ数: {len(text_test)}")`: テストデータがいくつ読み込まれたかを画面に表示します。
   - `print(f"クラスラベル (訓練データ): {np.unique(y_train)}")`: 訓練データのラベルの種類を画面に表示します。`np.unique(y_train)` は、`y_train` 配列に含まれるユニークな要素（ここでは 0 と 1）を返します。

   **出力例:**
   ```
   訓練データ数: 25000
   テストデータ数: 25000
   クラスラベル (訓練データ): [0 1]
   ```
   これは、訓練データとテストデータそれぞれに25000件のレビューがあり、ラベルは 0（否定）と 1（肯定）の2種類であることを示しています。

### 4. **Pipelineの構築**

   ```python
   # テキストデータのベクトル化とモデルの学習をPipelineで組み合わせる
   pipeline = Pipeline([
       ('tfidf', TfidfVectorizer(
           stop_words='english',  # ストップワードの除去
           max_df=0.7,           # ドキュメント頻度が最大の70%を超える単語は無視
           min_df=5              # 少なくとも5つのドキュメントに現れる単語のみを考慮
       )),
       ('clf', LogisticRegression(solver='liblinear', random_state=42)) # ロジスティック回帰を使用
   ])
   ```

   - `Pipeline(...)`:  `Pipeline` は、一連のデータ変換とモデル学習のステップを順番に実行するための仕組みです。これにより、コードを整理しやすくなります。
   - `('tfidf', TfidfVectorizer(...))`:  最初のステップとして、テキストデータを数値データに変換する処理を行います。
     - `TfidfVectorizer`:  テキストデータから特徴量を抽出するクラスです。各単語の TF-IDF という値を計算し、それをレビューの特徴量として用います。
       - `stop_words='english'`:  英語のストップワード（"the", "a", "is" など、文章中で頻繁に出現するが意味を持たない単語）を分析対象から除外します。これにより、重要度の低い単語に影響されにくくなります。
       - `max_df=0.7`:  全レビューの中で、70%以上のレビューに出現する単語は、特徴量として考慮しません。これは、あまりにも多くのレビューに出現する単語は、レビューの肯定的・否定的な性質を区別するのに役立たないと考えられるためです。
       - `min_df=5`:  5つ未満のレビューにしか出現しない単語は、特徴量として考慮しません。これは、出現頻度の低い単語はノイズとなる可能性が高いためです。

   - `('clf', LogisticRegression(...))`: 次のステップとして、分類モデルの学習を行います。
     - `LogisticRegression`: ロジスティック回帰という分類アルゴリズムを使用します。このアルゴリズムは、入力された特徴量に基づいて、レビューが肯定的なものである確率を計算します。
       - `solver='liblinear'`: ロジスティック回帰の学習に使用するアルゴリズムを指定します。`liblinear` は、比較的小規模なデータセットに適したソルバーです。
       - `random_state=42`: 乱数のシード値を指定します。これにより、コードを何度実行しても同じ結果が得られるようになります。

   **具体的な処理の例:**
   レビューの文章 "This movie was very good, I enjoyed it a lot." が `TfidfVectorizer` に入力されると、まずストップワード ("this", "was", "very", "a") が取り除かれ、残りの単語 ("movie", "good", "I", "enjoyed", "it", "lot") の TF-IDF 値が計算されます。例えば、"good" という単語が肯定的なレビューに多く出現する場合、高い TF-IDF 値を持つ可能性があります。これらの TF-IDF 値が、このレビューの数値的な特徴量として `LogisticRegression` に入力され、レビューが肯定的か否定的かの確率が計算されます。

### 5. **モデルの訓練**

   ```python
   # モデルの訓練
   pipeline.fit(text_train, y_train)
   ```

   - `pipeline.fit(text_train, y_train)`:  構築した `pipeline` を使って、訓練データ (`text_train`) とそれに対応するラベル (`y_train`) からモデルを学習させます。
     - 内部的には、まず `TfidfVectorizer` が `text_train` を解析し、単語ごとの TF-IDF 値を計算します。
     - 次に、計算された TF-IDF 値と `y_train` のラベルを元に、`LogisticRegression` がレビューが肯定的か否定的かを予測するためのルール（各単語の重要度など）を学習します。

   **具体的な処理の例:**
   `pipeline.fit` は、大量の訓練データ（肯定的なレビューと否定的なレビューの文章とそのラベル）を `LogisticRegression` に与え、「good」や「excellent」のような単語は肯定的なレビューによく現れる傾向がある、「bad」や「terrible」のような単語は否定的なレビューによく現れる傾向がある、といったパターンを学習します。

### 6. **訓練データでの予測と評価**

   ```python
   # 訓練データでの予測と評価
   y_train_pred = pipeline.predict(text_train)
   train_accuracy = accuracy_score(y_train, y_train_pred)
   print(f"訓練データの正解率: {train_accuracy:.4f}")
   ```

   - `y_train_pred = pipeline.predict(text_train)`: 学習済みの `pipeline` を使って、訓練データ (`text_train`) に対する予測ラベルを生成します。つまり、訓練データ中の各レビューが肯定的か否定的かをモデルに判断させます。
   - `train_accuracy = accuracy_score(y_train, y_train_pred)`:  予測されたラベル (`y_train_pred`) と実際のラベル (`y_train`) を比較し、正解率を計算します。正解率は、全データ中で正しく分類できた割合を示します。
   - `print(f"訓練データの正解率: {train_accuracy:.4f}")`: 計算された訓練データの正解率を画面に表示します。

   **具体的な処理の例:**
   学習済みのモデルに、訓練データに含まれる "This movie was great!" というレビューを入力すると、モデルは過去の学習結果から、このレビューに含まれる単語 ("movie", "great" など) の特徴に基づいて、高い確率で肯定的なレビューであると予測します。`accuracy_score` は、このような予測が訓練データ全体でどの程度正しかったかを計算します。例えば、訓練データ100件のうち95件の予測が正しければ、正解率は 0.95 となります。

### 7. **テストデータでの予測と評価**

   ```python
   # テストデータでの予測と評価
   y_test_pred = pipeline.predict(text_test)
   test_accuracy = accuracy_score(y_test, y_test_pred)
   print(f"テストデータの正解率: {test_accuracy:.4f}")
   ```

   - 訓練データでの予測と評価と同様の処理を、テストデータ (`text_test`, `y_test`) に対して行います。テストデータは、モデルの学習には一切使用していない、未知のデータです。このデータに対する正解率を評価することで、モデルの汎化性能（未知のデータに対する予測能力）を測ることができます。

   **具体的な処理の例:**
   学習済みのモデルに、テストデータに含まれる、学習時には見ていない "The acting was terrible, I wouldn't recommend it." というレビューを入力すると、モデルは同様に単語の特徴から否定的なレビューであると予測します。テストデータの正解率は、モデルが未知のレビューを正しく分類できる能力を示します。

### 8. **目標性能の確認**

   ```python
   # 目標性能の確認
   train_goal_achieved = train_accuracy >= 0.90
   test_goal_achieved = test_accuracy >= 0.85

   print(f"訓練データの目標達成: {train_goal_achieved}")
   print(f"テストデータの目標達成: {test_goal_achieved}")
   ```

   - 計算された訓練データの正解率とテストデータの正解率が、事前に設定した目標値（訓練データ: 90%以上、テストデータ: 85%以上）を満たしているかどうかを確認し、その結果を画面に表示します。

### 9. **モデルのチューニング（オプション）**

   ```python
   # 必要に応じてモデルのチューニング (例: ハイパーパラメータの調整)
   from sklearn.model_selection import GridSearchCV
   parameters = {
       'tfidf__ngram_range': [(1, 1), (1, 2)],
       'clf__C': [0.1, 1, 10]
   }
   grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
   grid_search.fit(text_train, y_train)
   print(f"Best score: {grid_search.best_score_}")
   print(f"Best parameters: {grid_search.best_params_}")

   # 最適なパラメータで再度評価
   best_pipeline = grid_search.best_estimator_
   y_test_pred_best = best_pipeline.predict(text_test)
   test_accuracy_best = accuracy_score(y_test, y_test_pred_best)
   print(f"チューニング後のテストデータの正解率: {test_accuracy_best:.4f}")
   ```

   - この部分は、モデルの性能をさらに向上させるために、モデルのハイパーパラメータを調整する処理です。

   - `GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)`:  `GridSearchCV` は、指定されたハイパーパラメータの候補の中から、最適な組み合わせを見つけ出すための機能です。
     - `pipeline`:  調整対象のモデル（ここでは、テキストのベクトル化とロジスティック回帰を組み合わせた `pipeline`）を指定します。
     - `parameters`: 調整するハイパーパラメータとその候補値を辞書形式で指定します。
       - `'tfidf__ngram_range': [(1, 1), (1, 2)]`: `TfidfVectorizer` の `ngram_range` パラメータを `(1, 1)`（単語単位）と `(1, 2)`（単語と2単語の組み合わせ）で試します。例えば、`(1, 2)` を指定すると、"good movie" のような連続する2つの単語も特徴量として考慮されます。
       - `'clf__C': [0.1, 1, 10]`: `LogisticRegression` の `C` パラメータを `0.1`, `1`, `10` で試します。`C` は正則化の強さを調整するパラメータで、過学習を防ぐために使用します。
     - `cv=5`:  交差検証の分割数を指定します。データを5つに分割し、そのうち4つを訓練データ、1つを検証データとして、パラメータの評価を5回繰り返します。これにより、単一の分割に依存しない、より安定した評価が可能になります。
     - `n_jobs=-1`:  利用可能なすべてのCPUコアを使用して並列処理を行います。これにより、パラメータの探索を高速化できます。

   - `grid_search.fit(text_train, y_train)`:  指定されたハイパーパラメータのすべての組み合わせについて、交差検証を行い、最適なパラメータを見つけ出します。

   - `print(f"Best score: {grid_search.best_score_}")`: 交差検証で最も良い性能を示したスコア（デフォルトでは正解率）を表示します。

   - `print(f"Best parameters: {grid_search.best_params_}")`: 最も良いスコアが得られた時のハイパーパラメータの組み合わせを表示します。

   - `best_pipeline = grid_search.best_estimator_`:  見つかった最適なハイパーパラメータで学習済みのモデルを取得します。

   - `y_test_pred_best = best_pipeline.predict(text_test)`: 最適なモデルを使って、再度テストデータの予測を行います。

   - `test_accuracy_best = accuracy_score(y_test, y_test_pred_best)`: 最適なモデルでのテストデータの正解率を計算します。

   - `print(f"チューニング後のテストデータの正解率: {test_accuracy_best:.4f}")`: チューニング後のテストデータの正解率を画面に表示します。

   **具体的な処理の例:**
   `GridSearchCV` は、例えば `ngram_range=(1, 1)` かつ `C=0.1` の場合、`ngram_range=(1, 2)` かつ `C=1` の場合など、指定されたすべてのパラメータの組み合わせでモデルを学習・評価します。交差検証では、訓練データをさらに分割し、学習に使用するデータと性能評価に使用するデータを切り替えながら評価を行います。最も良い性能を示したパラメータの組み合わせが「最適なパラメータ」として選択され、そのパラメータで再度学習されたモデルが最終的な評価に使用されます。

## [ref] log

```bash
root@00a1890e9919:/workspaces/AtCoder/Practice/36# python 36.py
訓練データ数: 25000
テストデータ数: 25000
クラスラベル (訓練データ): [0 1]
訓練データの正解率: 0.9339
テストデータの正解率: 0.8793
訓練データの目標達成: True
テストデータの目標達成: True
Best score: 0.89604
Best parameters: {'clf__C': 10, 'tfidf__ngram_range': (1, 2)}
チューニング後のテストデータの正解率: 0.8834
```
