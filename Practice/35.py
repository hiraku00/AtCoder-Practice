from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Serviceクラスをインポート
import time

# 検索キーワード
search_keyword = "Selenium Python ブラウザ自動化"

# ChromeDriverのパス (ご自身の環境に合わせて修正)
chromedriver_path = "./chromedriver"  # スクリプトと同じディレクトリに置いた場合

# ブラウザの起動 (今回はChromeを使用)
driver = webdriver.Chrome()

try:
    # Google検索にアクセス
    driver.get("https://www.google.com/")

    # 検索窓の要素を特定してキーワードを入力
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)  # Enterキーを押して検索

    # 検索結果が表示されるまで少し待機
    time.sleep(2)

    # 検索結果の上位5件の要素を取得
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")[:5]

    # 上位5件のページにアクセスしてタイトルを表示
    print(f"「{search_keyword}」の検索結果上位5件のページタイトル:")
    for i, result in enumerate(search_results):
        try:
            # 検索結果からリンク要素を取得
            link_element = result.find_element(By.CSS_SELECTOR, "a")
            link_url = link_element.get_attribute("href")

            # 新しいタブでページを開く
            driver.execute_script("window.open(arguments[0]);", link_url)

            # 新しいタブに切り替え
            driver.switch_to.window(driver.window_handles[-1])

            # ページが完全にロードされるまで少し待機 (より確実に)
            time.sleep(3)

            # ページタイトルを取得して表示
            page_title = driver.title
            print(f"{i+1}: {page_title}")

            # タブを閉じる
            driver.close()

            # 元のタブに戻る
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"{i+1}: ページへのアクセスに失敗しました: {e}")

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # ブラウザを閉じる
    driver.quit()
