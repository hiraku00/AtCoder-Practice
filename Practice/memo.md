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

行しました。以下に修正版のコード解説を示します。

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
