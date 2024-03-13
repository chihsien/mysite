

# 1.匯入selenium
from selenium import webdriver

import time
from selenium.webdriver.common.by import By
#from pynput.keyboard import Key, Controller


# 2.開啟瀏覽器
driver = webdriver.Edge()

#driver.implicitly_wait(5)

# 3.開啟註冊A頁面(頁面地址根據自己的需要修改)
url = "http://biz.coolsax.work/python/fileupload.html"
driver.get(url)
#driver.maximize_window()

time.sleep(5)

# 4.定位上傳檔案按鈕
driver.find_element(By.ID,"file-upload").send_keys("D:\\測試上傳檔案.txt");
time.sleep(5)

driver.find_element(By.NAME, "btnUpload").click()

time.sleep(5)

if driver.page_source.find("Not Allowed"):
    print ("OK")
else:
    print ("Upload Failed")    

time.sleep(2)


# 5.使用send_keys方法上傳檔案
#upfile.send_keys(r"D:\測試上傳檔案.txt")

# 6.關閉瀏覽器
driver.quit()