from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
element = driver.find_elements_by_xpath('//a[@id="thumbnail"]')
video = []
#print (element)
for i in range(len(element)):
    s = element[i].get_attribute('href')
    video.append(s)
for j in range(10):
    mp4 = 'window.open("https://yt1s.com/youtube-to-mp4/zh-tw");'
    driver.execute_script(mp4)
    time.sleep(5)
    window_frist = driver.window_handles[-1]
    driver.switch_to_window(window_frist)
    url = driver.find_element_by_xpath('//*[@id="s_input"]')
    url.send_keys(video[j+1])
    button = driver.find_element_by_xpath('//*[@id="btn-convert"]')
    button.click()
    time.sleep(5)
    button2 = driver.find_element_by_xpath('//*[@id="btn-action"]')
    button2.click()
    time.sleep(5)
    button3 = driver.find_element_by_xpath('//*[@id="asuccess"]')
    button3.click()
    time.sleep(5)
