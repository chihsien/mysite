

# 1.匯入selenium
from selenium import webdriver

import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options 

options = Options()
options.add_argument("headless")
driver = webdriver.Edge(options = options)

#driver.implicitly_wait(5)

# 3.開啟註冊A頁面(頁面地址根據自己的需要修改)
url = "http://biz.coolsax.work/python/fileupload.html"
driver.get(url)
#driver.maximize_window()


# 4.定位上傳檔案按鈕
driver.find_element(By.ID,"file-upload").send_keys("D:\\測試上傳檔案.txt");
time.sleep(2)

driver.find_element(By.NAME, "btnUpload").click()

time.sleep(2)

if driver.page_source.find("Not Allowed"):
    print ("OK")
else:
    print ("Upload Failed")    


# write log
date_time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
path = 'output.txt'
f = open(path, 'a')
f.write(date_time )
f.write("\n" )
f.close()


# 5.使用send_keys方法上傳檔案
#upfile.send_keys(r"D:\測試上傳檔案.txt")

# 6.關閉瀏覽器
driver.quit()