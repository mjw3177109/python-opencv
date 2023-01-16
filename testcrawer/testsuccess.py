
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#get直接返回，不再等待界面加载完成

desired_capabilities = DesiredCapabilities.CHROME

desired_capabilities["pageLoadStrategy"] = "none"

driver = webdriver.Chrome()


driver.get("https://www.haoxinqing.cn/doctor")

print('success')

# driver.close()