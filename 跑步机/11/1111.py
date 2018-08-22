# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path='/Users/admin/Desktop/chromedriver')
print('设置浏览器宽1280，高800显示')
browser.set_window_size(1280, 800)
time.sleep(2)
browser.maximize_window()
browser.get('https://alphasaas.commafit.club/#/login')
browser.implicitly_wait(15)

# 登录
def login():
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[1]/div/div[1]/input').send_keys(
        'hexiaohui@likingfit.com')
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[2]/div/div/input').send_keys('123')
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[4]/div/button/span').click()


# 健身课程-课程库
def course():
    time.sleep(2)
    # 健身课程
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul[1]/li/div').click()
    # 课程库
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul[1]/li/ul/li[1]').click()

    # 搜索框
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[1]/div['
                                  '1]/div/div/div/input').send_keys('游')
    # 快速查询
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[1]/div['
                                  '2]/div/button').click()
    time.sleep(2)
    # 高级搜索
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[1]/div['
                                  '2]/div/span').click()

    # 选择健身房


    well = browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[2]/div[''1]/div[1]/div/div/div/div[1]/input')
    #well.send_keys(Keys.ARROW_DOWN)
    well.send_keys(Keys.DOWN)
    time.sleep(2)

    well.send_keys(Keys.ENTER)

    time.sleep(10)
    # s=Select(browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[2]/div[''1]/div[1]/div/div/div/div[1]/input'))
    # #browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[2]/div[''1]/div[1]/div/div/div/div[1]/input').click()
    # # time.sleep(2)
    #
    # # 点击所选项
    # #s1 = Select(browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div/form/div[2]/div[1]/div[1]/div/div/div/div[1]')) # 实例化Select
    # try:
    #     s.select_by_visible_text('有氧舞蹈')
    # except:
    #     s.select_by_index('1')

    #browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
    #browser.find_element_by_link_text('有氧舞蹈').click()


    # 团操课详情
    browser.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/table/tbody/tr[1]/td[8]/div/button').click()
    time.sleep(2)
    # browser.find_element_by_xpath('')
    # browser.close()
    # 课程库标签
    browser.find_element_by_xpath('//*[@id="tab-/course"]').click()
    time.sleep(2)
    # 切换私教课
    browser.find_element_by_xpath('//*[@id="tab-second"]').click()
    time.sleep(2)
    # 私教详情
    browser.find_element_by_xpath('//*[@id="pane-second"]/div/div[3]/table/tbody/tr[1]/td[8]/div/button').click()
    time.sleep(2)
    # 课程库标签
    browser.find_element_by_xpath('//*[@id="tab-/course"]').click()
    time.sleep(2)


# 健身课程-团课排期
def Add():
    time.sleep(2)
    # 健身课程
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul[1]/li/div').click()
    time.sleep(1)
    # 团课排期
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul[1]/li/ul/li[2]').click()
    time.sleep(2)
    # 新增排期
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div[2]/a/button').click()

login()
course()
#Add()
# time.sleep(4)
# browser.quit()
