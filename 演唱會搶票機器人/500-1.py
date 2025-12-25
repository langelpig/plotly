from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time

# --- 1. 設定變數 ---
target_url = "https://tixcraft.com/"
# 您提供的會員登入按鈕的 CSS 選擇器 (基於 href="#login")
LOGIN_SELECTOR = 'a[href="#login"]' 
# Cookie 接受按鈕的常見 XPath (需要根據網頁實際文字調整)
# 嘗試尋找包含「接受」或「同意」等關鍵字的按鈕
COOKIE_XPATH = "//button[contains(text(), '接受') or contains(text(), '同意') or contains(text(), '我知道了')]"

# --- 2. 初始化瀏覽器 ---
def initialize_driver():
    """初始化並設定 Chrome 瀏覽器驅動程式"""
    chrome_options = Options()
    # 保持瀏覽器開啟直到手動關閉
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
            # 等待 Cookie 按鈕出現並可點擊
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, COOKIE_XPATH))
            )
            cookie_button.click()
            print("✅ 成功點擊 Cookie 接受按鈕。")
            time.sleep(1) # 短暫等待橫幅消失
            
        except TimeoutException:
            print("⚠️ 警告：在 20 秒內未找到 Cookie 接受按鈕。可能沒有彈出橫幅。繼續下一步。")
        except ElementClickInterceptedException:
            # 如果按鈕被遮擋，嘗試使用 JavaScript 強制點擊
            print("⚠️ 警告：Cookie 按鈕被遮擋，嘗試使用 JavaScript 點擊。")
            driver.execute_script("arguments[0].click();", cookie_button)
            print("✅ 成功使用 JavaScript 點擊 Cookie 接受按鈕。")
            time.sleep(1)


        # ====================================================
        # B. 第二步：點擊 會員登入 (使用您提供的元素)
        # ====================================================
        print("🔍 嘗試點擊 '會員登入' 按鈕...")
        
        # 等待登入按鈕出現並可點擊
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_SELECTOR))
        )
        
        # 點擊按鈕
        login_button.click()
        
        print("✅ 已點擊 '會員登入'，登入彈窗應該已彈出。")

    except NoSuchElementException:
        print(f"❌ 錯誤：找不到 CSS Selector 為 '{LOGIN_SELECTOR}' 的元素。請檢查選擇器。")
    except TimeoutException:
        print("❌ 錯誤：載入網頁超時或目標元素（會員登入）未出現。")
    except Exception as e:
        print(f"❌ 發生其他錯誤: {e}")
        
# 執行函式
automate_tixcraft_login()