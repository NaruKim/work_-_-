
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL="https://www.rankey.com/rank/rank_site_all.php#"
ID = "jness1012"
PW = "jness1012"
TXT = "C:\이름.text"
TXT2 = "C:\링크.text"

driver = webdriver.Chrome('C:\selenium\chromedriver')
driver.get(URL)

beginning_login = '/html/body/div[1]/table/tbody/tr/td[4]/table/tbody/tr[1]/td[1]'
id_place = '//*[@id="id"]'
pw_place = '//*[@id="passwd"]'
login = '//*[@id="Table_01"]/tbody/tr[2]/td[4]/a/img'
# //*[@id="Table_01"]/tbody/tr[2]/td[4]

start_login=driver.find_element_by_xpath(beginning_login)
start_login.click()

id_input = driver.find_element_by_xpath(id_place)
id_input.send_keys("jness1012")

pw_input = driver.find_element_by_xpath(pw_place)
pw_input.send_keys("jness1012")

login_button=driver.find_element_by_xpath(login)
login_button.click()

driver.find_element_by_xpath('//*[@id="rank_to"]').send_keys('00')
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a/img').click()
file1=open("C:\이름.text", mode='w')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[3]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[4]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[5]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[6]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[7]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[8]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[9]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[10]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[11]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[12]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[13]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[14]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[15]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[16]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[17]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[18]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[19]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[20]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[21]/td[2]/a').text)
file1.write('\n')
file1.write(driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[22]/td[2]/a').text)
file1.write('\n')

time.sleep(0.9)

driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[3]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[4]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[5]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[6]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[7]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[8]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[9]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[10]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[11]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[12]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[13]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[14]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[15]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[16]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[17]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[18]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[19]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[20]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[21]/td[2]/a').send_keys(Keys.CONTROL+"\n")
driver.find_element_by_xpath('//*[@id="oTable"]/tbody/tr[22]/td[2]/a').send_keys(Keys.CONTROL+"\n")
file1.close()

time.sleep(2)

file2=open("C:\링크.text", mode='w')
i=1
while (i<21):
    driver.switch_to.window(driver.window_handles[-i])
    file2.write(driver.current_url)
    file2.write('\n')
    i=i+1

# driver.switch_to.window(driver.window_handles[0])
# next = driver.find_element_by_xpath('//*[@id="oPage"]/tbody/tr/td[3]/input')
# next.click()
# next.send_keys(Keys.CONTROL+'a')
# next.send_keys(Keys.BACKSPACE)
# next.send_keys('2',"\n")
# time.sleep(0.9)
# next.send_keys(Keys.CONTROL+'a')
# next.send_keys(Keys.BACKSPACE)
# next.send_keys('3',"\n")
# driver.find_element_by_tag_name('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[3]/a').send_keys(Keys.COMMAND + 't')

# driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[8]/a').click()