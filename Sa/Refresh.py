from delin_testcase.Sa import Zbsq
from delin_testcase.denglu import driver
# 刷新
driver.find_element_by_xpath('//*[@id="lr-replace"]').click()
ts = driver.find_element_by_xpath('//*[@id="loading_manage"]').text
if ts == '拼命加载中…':
    print('刷新中。。。')
else:
    print('未刷新。。。')
