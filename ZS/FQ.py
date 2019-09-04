from selenium import webdriver
from delin_testcase import denglu
import time
from delin_testcase.denglu import driver
# 定位到增补申请模块
driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[5]/a/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[5]/ul/li[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[5]/ul/li[1]/ul/li[1]/a').click()
time.sleep(3)

# 进入子层 frame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('iframe37ac3c4c-ac34-4bd2-92a5-0ed286951ad2'))

# 发起
driver.find_element_by_id('lr-add').click()
# 回到父层
driver.switch_to.parent_frame()
time.sleep(2)

# 进入子层 frame，增补申请表单
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('FlowProcessBuider'))  # 第一层
driver.switch_to.frame(driver.find_element_by_id('formIframe'))  # 第二层

# 验证部门，验证是否为申请人所在部门
s = driver.find_element_by_id('ApplyOrgId').text
if s == '总部职能中心':
    print('申请事业部正确')
else:
    print('申请事业部错误')
b = driver.find_element_by_id('ApplyDeptId').text
if b == '人力资源':
    print('人力资源正确')
else:
    print('人力资源错误')
time.sleep(2)

# 申请岗位
driver.find_element_by_id('ApplyPost').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyPost-option"]/div[1]/ul/li[54]').click()
time.sleep(1)
# 申请人数
driver.find_element_by_xpath('//*[@id="ApplyNumber"]').send_keys('1')
time.sleep(1)
# 申请类型
driver.find_element_by_id('ApplyType').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyType-option"]/div/ul/li[1]').click()
time.sleep(1)
# 期望到职时间
driver.find_element_by_xpath('//*[@id="ExpectEntryDate"]').clear()
driver.find_element_by_xpath('//*[@id="ExpectEntryDate"]').send_keys('2019-09-15')
time.sleep(1)
# 薪酬范围
driver.find_element_by_xpath('//*[@id="SalaryRange"]').send_keys('5000-10000')
time.sleep(1)
# 申请理由
driver.find_element_by_xpath('//*[@id="ApplyReason"]').send_keys('人手不足，急需增派')
time.sleep(1)
# 性别要求
driver.find_element_by_xpath('//*[@id="ApplySex"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplySex-option"]/div/ul/li[3]').click()
time.sleep(1)
# 学历要求
driver.find_element_by_xpath('//*[@id="ApplyEducation"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyEducation-option"]/div[1]/ul/li[6]').click()
# 年龄要求
driver.find_element_by_xpath('//*[@id="ApplyAge"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyAge-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyAgeExplain"]').send_keys('25')
time.sleep(1)
# 专业要求
driver.find_element_by_xpath('//*[@id="ApplyProfessional"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyProfessional-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyProfessionalExplain"]').send_keys('行政相关')
time.sleep(1)
# 工作经验要求
driver.find_element_by_xpath('//*[@id="ApplyWorkExperience"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyWorkExperience-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyWorkExperienceExplain"]').send_keys('至少1年')
time.sleep(1)
# 职称要求
driver.find_element_by_xpath('//*[@id="ApplyProfessionalTitle"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyProfessionalTitle-option"]/div/ul/li[1]').click()
time.sleep(1)
# 职业资格证书要求
driver.find_element_by_xpath('//*[@id="ApplyProfessionalCertificate"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyProfessionalCertificate-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyProfessionalCertificateExplain"]').send_keys('秘书证')
time.sleep(1)
# 专业技能要求
driver.find_element_by_xpath('//*[@id="ApplyProfessionalSkills"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyProfessionalSkills-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyProfessionalSkillsExplain"]').send_keys('熟悉办公自动化相关软件')
time.sleep(1)
# 外语要求
driver.find_element_by_xpath('//*[@id="ApplyForeignLanguage"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyForeignLanguage-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyForeignLanguageExplain"]').send_keys('英语四级以上')
time.sleep(1)
# 计算机要求
driver.find_element_by_xpath('//*[@id="ApplyComputer"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyComputer-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyComputerExplain"]').send_keys('计算机二级以上')
time.sleep(1)
# 其他要求
driver.find_element_by_xpath('//*[@id="ApplyOthers"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyOthers-option"]/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="ApplyOthersExplain"]').send_keys('形象气质俱佳者优先')
time.sleep(1)

# 回到父层
driver.switch_to.parent_frame()
# 进入子层 frame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('FlowProcessBuider'))
time.sleep(2)
# 标题
driver.find_element_by_xpath('//*[@id="CustomName"]').send_keys('人力-文员增补')
time.sleep(1)
# 重要等级
driver.find_element_by_xpath('//*[@id="ProcessInfo"]/table/tbody/tr[6]/td/div[3]').click()
time.sleep(1)
# 备注
driver.find_element_by_xpath('//*[@id="Description"]').send_keys('这是总部职能中心，人力资源部的文员增补申请。')
time.sleep(1)
# 保存草稿
driver.find_element_by_xpath('//*[@id="btn_finish"]').click()
time.sleep(1)

# 回到父层
driver.switch_to.parent_frame()
# 进入子层 frame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('iframe37ac3c4c-ac34-4bd2-92a5-0ed286951ad2'))
# 验证表格信息
# 归属事业部
bm = driver.find_element_by_xpath('//*[@id="1"]/td[3]').text
if bm == '总部职能中心':
    print('归属事业部正确')
else:
    print('归属事业部错误')
time.sleep(1)
# 申请部门
sqbm = driver.find_element_by_xpath('//*[@id="1"]/td[4]').text
if sqbm == '人力资源':
    print('申请部门正确')
else:
    print('申请部门错误')
time.sleep(1)
# 申请岗位
sqgw = driver.find_element_by_xpath('//*[@id="1"]/td[5]').text
if sqgw == '文员':
    print('申请岗位正确')
else:
    print('申请岗位错误')
time.sleep(1)
# 申请人数
sqrs = driver.find_element_by_xpath('//*[@id="1"]/td[6]').text
if sqrs == '1':
    print('申请人数正确')
else:
    print('申请人数错误')
time.sleep(1)
# 申请类型
sqlx = driver.find_element_by_xpath('//*[@id="1"]/td[7]').text
if sqlx == '岗位新增':
    print('申请类型正确')
else:
    print('申请类型错误')
time.sleep(1)
# 期望到职时间
sqdz = driver.find_element_by_xpath('//*[@id="1"]/td[8]').text
if sqdz == '2019-09-15':
    print('期望到职时间正确')
else:
    print('期望到职时间错误')
time.sleep(1)
# 薪酬范围
sqdz = driver.find_element_by_xpath('//*[@id="1"]/td[9]').text
if sqdz == '5000-10000':
    print('薪酬范围正确')
else:
    print('薪酬范围错误')
time.sleep(1)
# 申请理由
sqly = driver.find_element_by_xpath('//*[@id="1"]/td[10]').text
if sqly == '人手不足，急需增派':
    print('申请理由正确')
else:
    print('申请理由错误')
time.sleep(1)
# 审批状态
spzt = driver.find_element_by_xpath('//*[@id="1"]/td[11]/span').text
if spzt == '草稿':
    print('审批状态正确')
else:
    print('审批状态错误')
time.sleep(1)
# 招聘状态
zpzt = driver.find_element_by_xpath('//*[@id="1"]/td[12]/span').text
if zpzt == '未启动':
    print('招聘状态正确')
else:
    print('招聘状态错误')
time.sleep(1)
# 申请人
sqr = driver.find_element_by_xpath('//*[@id="1"]/td[13]').text
if sqr == '倪菲':
    print('申请人正确')
else:
    print('申请人错误')
time.sleep(1)
# 创建时间
today_timestamp = time.time()
today_time = time.strftime('%Y-%m-%d',time.localtime(today_timestamp))
cjsj = driver.find_element_by_xpath('//*[@id="1"]/td[14]').text
if cjsj == today_time:
    print('创建时间正确')
else:
    print('创建时间错误')
time.sleep(1)

# 刷新
driver.find_element_by_xpath('//*[@id="lr-replace"]').click()
time.sleep(5)