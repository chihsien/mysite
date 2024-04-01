

# 1.匯入selenium
from selenium import webdriver

import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options 

# write log
path = 'output.txt'
f = open(path, 'a')

options = Options()
options.add_argument("headless")
driver = webdriver.Edge(options = options)

step1 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
f.write(step1 + ' Silent Mode 開啟瀏覽器' )
f.write("\n" )


#driver.implicitly_wait(5)

# 3.開啟註冊A頁面(頁面地址根據自己的需要修改)
url = "http://biz.coolsax.work/python/fileupload.html"
driver.get(url)
#driver.maximize_window()

step2 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
f.write(step2 + ' 開啟註冊A頁面' )
f.write("\n" )

# 4.定位上傳檔案按鈕
driver.find_element(By.ID,"file-upload").send_keys("D:\\測試上傳檔案.txt");
step3 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
f.write(step3 + ' 定位上傳檔案按鈕' )
f.write("\n" )

time.sleep(2)

# 按下上傳Button
driver.find_element(By.NAME, "btnUpload").click()

step4 = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
f.write(step4 + ' 按下上傳Button' )
f.write("\n" )

f.close()


if driver.page_source.find("Not Allowed"):
    print ("OK")
else:
    print ("Upload Failed")    


# 5.使用send_keys方法上傳檔案
#upfile.send_keys(r"D:\測試上傳檔案.txt")

# 6.關閉瀏覽器
driver.quit()