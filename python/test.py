
from selenium.webdriver.common.by import By

# 1.匯入selenium
from selenium import webdriver


# 2.開啟瀏覽器
driver = webdriver.Chrome()

# 3.開啟註冊A頁面(頁面地址根據自己的需要修改)
url = "file:///D:/SourceControl/Github/mysite/fileupload.html"
driver.get(url)
#driver.maximize_window()

# 4.定位上傳檔案按鈕
#upfile = driver.find_element_by_name("upfile")
#upfile = driver.find_element("name","upfile")
upfile = driver.find_elements(By.NAME,"upfile")

#elem = driver.find_element_by_xpath('//*[@id="upfile"]')
#id = (elem.text)
#print(id)


# 5.使用send_keys方法上傳檔案
#upfile.send_keys(r"D:\測試上傳檔案.txt")

# 6.關閉瀏覽器
# driver.quit()