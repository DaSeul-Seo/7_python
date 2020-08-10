from selenium import webdriver

# 해당 코드를 실행시키면 빈 웹브라우저가 뜸
driver = webdriver.Chrome('chromedriver.exe')

# 웹 브라우저와 웹 드라이버만 설치되어 있다면 다양한 웹 브라우저 활용가능
chrome_driver = webdriver.chrome('chromedrivr.exe')
iexplore_driver = webdriver.li('IEDriverServer')
firefox_driver = webdriver.Firefox('FirefoxDriver')
