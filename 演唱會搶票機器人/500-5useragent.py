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

# Google 登入頁面的電子郵件輸入框 ID
EMAIL_INPUT_ID = 'identifierId'
# 您的電子郵件地址
USER_EMAIL = 'langelpig01@gmail.com'

# Google 登入頁面的下一步按鈕 ID（用於點擊）
NEXT_BUTTON_XPATH = "//button/span[contains(text(), '下一步')]"

# 新增：常見的 Chrome User-Agent 字符串
# 這是 Windows 10 上的 Chrome 120 範例
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


# --- 2. 初始化瀏覽器 ---
def initialize_driver():
    """初始化並設定 Chrome 瀏覽器驅動程式，新增 User-Agent"""
    chrome_options = Options()
    # 保持瀏覽器開啟
    chrome_options.add_experimental_option("detach", True)
    
    # *** 關鍵修改：新增 User-Agent ***
    print(f"⚙️ 設定 User-Agent: {USER_AGENT}")
    chrome_options.add_argument(f"user-agent={USER_AGENT}")
    # *********************************
    
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
        # A. 第一步：處理 Cookie 橫幅
        # ====================================================
        print("🍪 嘗試點擊 '接受所有 cookies' 按鈕...")
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, COOKIE_XPATH)))
            cookie_button.click()
            print("✅ 成功點擊 Cookie 接受按鈕。")
            time.sleep(1)
        except (TimeoutException, ElementClickInterceptedException):
            print("⚠️ 警告：Cookie 處理異常或橫幅未出現。繼續下一步。")


        # ====================================================
        # B. 第二步：點擊 會員登入
        # ====================================================
        print("🔍 嘗試點擊 '會員登入' 按鈕...")
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_SELECTOR)))
        login_button.click()
        print("✅ 已點擊 '會員登入'，登入彈窗彈出。")

        # ====================================================
        # C. 第三步：點擊 Google 登入
        # ====================================================
        print("🚀 嘗試點擊 '使用 Google 登入' 按鈕...")
        google_login_img = wait.until(EC.element_to_be_clickable((By.ID, GOOGLE_LOGIN_ID)))
        google_login_img.click()
        print("🎉 成功點擊 'Google 登入'！等待跳轉到 Google 登入頁面...")
        
        
        # ====================================================
        # D. 第四步：輸入電子郵件地址
        # ====================================================
        # ⚠️ 注意：由於 Google 登入會在新視窗或分頁開啟，您可能需要切換到該視窗
        # 在這裡我們先假設它在當前視窗載入，如果實際執行時出錯，我們需要再新增視窗切換邏輯。
        
        print(f"📧 正在輸入電子郵件：{USER_EMAIL}")
        
        # 等待 Google 登入頁面的電子郵件輸入框出現 (By.ID)
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, EMAIL_INPUT_ID))
        )
        
        # 輸入電子郵件地址
        email_input.send_keys(USER_EMAIL)
        print("✅ 電子郵件輸入完成。")
        
        # ====================================================
        # E. 第五步：點擊「下一步」按鈕
        # ====================================================
        print("➡️ 嘗試點擊 '下一步' 按鈕...")
        
        # 等待「下一步」按鈕出現並可點擊 (使用 XPath 尋找包含「下一步」文字的按鈕)
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, NEXT_BUTTON_XPATH))
        )
        next_button.click()
        print("✅ 成功點擊 '下一步'。等待跳轉到密碼輸入頁面。")
        

    except NoSuchElementException:
        print("❌ 錯誤：找不到指定的元素。請檢查選擇器或網頁結構是否變更。")
    except TimeoutException:
        print("❌ 錯誤：等待元素超時。請檢查網路連線或元素 ID/選擇器是否正確。")
    except Exception as e:
        print(f"❌ 發生其他錯誤: {e}")
        
# 執行函式
automate_tixcraft_login()