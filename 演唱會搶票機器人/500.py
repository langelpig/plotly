from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# # 指定您想開啟的網址
# target_url = "https://tixcraft.com/"

# def open_website(url):
#     """
#     使用系統預設的瀏覽器開啟指定的網址。
#     """
#     print(f"嘗試開啟網址：{url}")
#     # webbrowser.open(url) 會在一個新的瀏覽器視窗/分頁中開啟網址
#     webbrowser.open(url)
#     print("已發出開啟瀏覽器的指令。")

# # 執行函式
# open_website(target_url)

"======================================================"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# --- 1. 設定變數 ---
target_url = "https://tixcraft.com/"
# 您提供的會員登入按鈕的特徵是 href="#login"
LOGIN_SELECTOR = 'a[href="#login"]' 

# --- 2. 初始化瀏覽器 ---
def initialize_driver():
    """初始化並設定 Chrome 瀏覽器驅動程式"""
    # 選項：保持瀏覽器開啟直到手動關閉 (方便觀察)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    # 初始化 WebDriver，Selenium 會嘗試自動找到並使用 Chrome 驅動程式
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print("初始化 WebDriver 失敗，請檢查您的 Chrome 瀏覽器是否已安裝。")
        print(f"錯誤信息: {e}")
        return None

# --- 3. 主要操作函式 ---
def open_and_click_login():
    driver = initialize_driver()
    if driver is None:
        return

    print(f"🚗 正在開啟網址：{target_url}")
    try:
        # 開啟網頁
        driver.get(target_url)
        # 等待網頁載入完成 (可選，但建議使用)
        time.sleep(5) 
        
        print("🔍 嘗試尋找 '會員登入' 按鈕...")
        
        # 尋找會員登入按鈕 (使用 CSS Selector)
        login_button = driver.find_element(By.CSS_SELECTOR, LOGIN_SELECTOR)
        
        # 點擊按鈕
        print("🖱️ 找到按鈕，正在點擊...")
        login_button.click()
        
        print("✅ 已點擊 '會員登入'，登入彈窗應該已出現。")

        # 點擊後，您可以手動檢查網頁，因為 detach=True 保持瀏覽器開啟

    except NoSuchElementException:
        print(f"❌ 錯誤：找不到 CSS Selector 為 '{LOGIN_SELECTOR}' 的元素。請檢查選擇器或網頁結構是否變更。")
    except TimeoutException:
        print("❌ 錯誤：載入網頁超時。")
    except Exception as e:
        print(f"❌ 發生其他錯誤: {e}")
        
# 執行函式
open_and_click_login()

# 注意：因為 detach=True，瀏覽器會保持開啟，
# 您不需要在程式碼結尾加入 driver.quit()。