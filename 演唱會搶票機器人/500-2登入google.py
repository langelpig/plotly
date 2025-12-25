from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time

# --- 1. 設定變數 ---
target_url = "https://tixcraft.com/"
# 會員登入按鈕的 CSS 選擇器
LOGIN_SELECTOR = 'a[href="#login"]' 
# Google 登入按鈕的 ID 屬性
GOOGLE_LOGIN_ID = 'google'
# Cookie 接受按鈕的常見 XPath 
COOKIE_XPATH = "//button[contains(text(), '接受') or contains(text(), '同意') or contains(text(), '我知道了')]"

# --- 2. 初始化瀏覽器 ---
def initialize_driver():
    """初始化並設定 Chrome 瀏覽器驅動程式"""
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print("初始化 WebDriver 失敗。請檢查您的 Chrome 瀏覽器是否已安裝。")
        print(f"錯誤信息: {e}")
        return None

# --- 3. 主要操作函式 ---
def automate_tixcraft_login():
    driver = initialize_driver()
    if driver is None:
        return

    # 設定最長等待 20 秒
    wait = WebDriverWait(driver, 20) 
    
    print(f"🚗 正在開啟網址：{target_url}")
    try:
        # 1. 開啟網頁
        driver.get(target_url)
        
        # ====================================================
        # A. 第一步：處理 Cookie 橫幅 (點擊「接受」)
        # ====================================================
        print("🍪 嘗試點擊 '接受所有 cookies' 按鈕...")
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, COOKIE_XPATH))
            )
            cookie_button.click()
            print("✅ 成功點擊 Cookie 接受按鈕。")
            time.sleep(1)
            
        except TimeoutException:
            print("⚠️ 警告：在 20 秒內未找到 Cookie 接受按鈕。繼續下一步。")
        except ElementClickInterceptedException:
            print("⚠️ 警告：Cookie 按鈕被遮擋，嘗試使用 JavaScript 點擊。")
            driver.execute_script("arguments[0].click();", cookie_button)
            print("✅ 成功使用 JavaScript 點擊 Cookie 接受按鈕。")
            time.sleep(1)


        # ====================================================
        # B. 第二步：點擊 會員登入
        # ====================================================
        print("🔍 嘗試點擊 '會員登入' 按鈕...")
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_SELECTOR))
        )
        login_button.click()
        print("✅ 已點擊 '會員登入'，登入彈窗應該已彈出。")

        # ====================================================
        # C. 第三步：點擊 Google 登入
        # ====================================================
        print("🚀 嘗試點擊 '使用 Google 登入' 按鈕...")
        
        # 等待 Google 登入的圖片元素在彈窗中出現並可點擊
        google_login_img = wait.until(
            EC.element_to_be_clickable((By.ID, GOOGLE_LOGIN_ID))
        )
        
        # 點擊按鈕
        google_login_img.click()
        
        print("🎉 成功點擊 'Google 登入'！瀏覽器將跳轉至 Google 登入頁面。")

    except NoSuchElementException:
        print("❌ 錯誤：找不到指定的元素。請檢查選擇器或網頁結構是否變更。")
    except TimeoutException:
        print("❌ 錯誤：等待元素超時。可能網速慢或頁面未完全載入。")
    except Exception as e:
        print(f"❌ 發生其他錯誤: {e}")
        
# 執行函式
automate_tixcraft_login()