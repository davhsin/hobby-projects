##### 虛擬環境基本命令：
1. $ python3 -m venv venv           # 建立虛擬環境
2. $ source venv/bin/activate       # 啟動虛擬環境
3. $ pip3 freeze > requirements.txt # 建立所需的dependencies文件
4. $ deactivate                     # 退出虛擬環境

### code explanation:
```python
    # 用來引入 Chrome 瀏覽器的選項設定（Options）
    from selenium.webdriver.chrome.options import Options 

    # 提供了不同的方法或函式，用於定位網頁元素。
    from selenium.webdriver.common.by import By 

    # "detach" 是一個選項名稱，這個選項告訴 Chrome 瀏覽器在測試完成後不要自動關閉瀏覽器窗口
    # Selenium 測試結束後，讓 Chrome 視窗保持開啟，方便進行後續 debug 
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # 改用 Firefox
    browser = webdriver.Firefox()
```
### FAQ:
Q: What is -m meaning? 
A: -m mod : run library module as a script (terminates option list)

Q: What is venv?
A: 用來建立與管理虛擬環境的模組，由python提供。

### Deprecated Code:
```python
    # Press cookie button
    reject_cookie = WebDriverWait(browser, 10).until(
        # 註：原版為class='button rejectAll'，所以腳本隨時會不能動
         EC.element_to_be_clickable(
             (By.XPATH, "//*[@class='rejectAll']") 
         )
    ).click()

    word_mode = WebDriverWait(browser, 10).until(
         EC.element_to_be_clickable(
             (By.XPATH, "//div[@class='textButton' and @mode='words']")
         )
    ).click()
```

```python
""" Time mode """
    time.sleep(1.0) # wait for web element to load
    # 開始計時
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if (elapsed_time > 30): break

    # 找到元素
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='word active']")
        )
    )
    # 輸入文字
    input_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='wordsInput']")
        )
    ).send_keys(element.text + ' ') 

```


### legacy code, less readability:
```python

 # Init
 chrome_options = Options()
 chrome_options.add_experimental_option("detach", True)
 browser = webdriver.Chrome(options=chrome_options)  
 browser.get('https://monkeytype.com/')

 word_mode = WebDriverWait(browser, 5).until(
     EC.element_to_be_clickable(
         (By.XPATH, "//button[@mode='words']")
     )
 ).click()

 time.sleep(1.0) # wait for web element to load

 for i in range(0, 51):
     # 找到元素
     element = WebDriverWait(browser, 10).until(
         EC.visibility_of_element_located(
             (By.XPATH, "//div[@class='word active']")
         )
     )
     # 輸入文字
     input_element = WebDriverWait(browser, 10).until(
         EC.presence_of_element_located(
             (By.XPATH, "//input[@id='wordsInput']")
         )
     ).send_keys(element.text + ' ') 

time.sleep(5)
browser.quit()
```
