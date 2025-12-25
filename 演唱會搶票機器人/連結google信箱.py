from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import time
import random

# --- 1. 配置瀏覽器選項，讓它看起來像真人 ---
def get_chrome_options():
    options = webdriver.ChromeOptions()
    
    # 設置一個標準的 User-Agent 字符串
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    
    # 忽略一些常見的 Selenium 檢測信息
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # 隱藏 '正在受自動化軟體控制' 的信息
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # 可以選擇開啟無頭模式 (背景執行，不顯示 UI)
    # options.add_argument("--headless")
    
    return options

# --- 2. 模擬輸入文字的函數 (帶有隨機延遲) ---
def simulate_typing(element, text):
    """逐字輸入文字，模擬人類的輸入速度。"""
    for char in text:
        element.send_keys(char)
        # 每次按鍵後隨機等待 0.05 到 0.2 秒
        time.sleep(random.uniform(0.05, 0.2))

# --- 3. 主程序 ---
def automated_browser_task():
    # 設置 WebDriver 服務（讓 Selenium 知道如何啟動 Chrome）
    # 如果您已將 chromedriver 放在系統 PATH 中，可以省略 Service
    # 這裡假設您的 ChromeDriver 路徑
    # service = Service(executable_path="/path/to/your/chromedriver") # 請替換為您的路徑
    
    try:
        # 啟動配置好的 Chrome 瀏覽器
        driver = webdriver.Chrome(options=get_chrome_options())
        
        # 設置隱式等待：等待元素出現的最大時間 (像人類一樣不會立即操作)
        driver.implicitly_wait(10) 
        
        print("瀏覽器啟動成功，開始訪問 Google...")
        driver.get("https://www.google.com/")
        
        # 隨機等待一段時間，模擬頁面加載時的思考
        time.sleep(random.uniform(2, 4))
        
        # 找到搜尋輸入框 (使用 name 屬性)
        search_box = driver.find_element(By.NAME, "q")
        
        search_term = "Python Selenium 自動化"
        print(f"正在模擬輸入: '{search_term}'")
        
        # 使用模擬輸入函數
        simulate_typing(search_box, search_term)
        
        # 隨機等待一段時間，模擬輸入後的思考
        time.sleep(random.uniform(1, 2))
        
        # 提交表單 (等同於按下 Enter 鍵)
        search_box.submit()
        
        print("搜尋已提交，等待結果...")
        time.sleep(random.uniform(3, 5))
        
        print(f"當前頁面標題: {driver.title}")
        
    except TimeoutException:
        print("操作超時。")
    except Exception as e:
        print(f"發生錯誤: {e}")
    finally:
        # 務必關閉瀏覽器
        if 'driver' in locals():
            print("任務完成，關閉瀏覽器。")
            driver.quit()

if __name__ == "__main__":
    automated_browser_task()