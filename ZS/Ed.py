from delin_testcase.ZS import FQ
from delin_testcase.denglu import driver
import time
from selenium.webdriver.common.keys import Keys
# 回到父层
driver.switch_to.parent_frame()
# 进入子层 frame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('iframe37ac3c4c-ac34-4bd2-92a5-0ed286951ad2'))

# 编辑
driver.find_element_by_id('1').click()
time.sleep(1)
driver.find_element_by_id('lr-edit').click()
time.sleep(1)

# 回到父层
driver.switch_to.parent_frame()
time.sleep(1)
# 验证编辑窗口信息
tl = driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[1]').text
# title
if tl == '编辑增补申请':
    print('编辑窗口标题正确')
else:
    print('编辑窗口标题错误')

# 进入子层 frame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('Form'))  #第一层
driver.switch_to.frame(driver.find_element_by_id('formIframe'))  #第二层

# 申请事业部
bjs = driver.find_element_by_id('ApplyOrgId').text
if bjs == '总部职能中心':
    print('申请事业部正确')
else:
    print('申请事业部错误')
time.sleep(1)
# 申请部门
b = driver.find_element_by_id('ApplyDeptId').text
if b == '人力资源':
    print('人力资源正确')
else:
    print('人力资源错误')
time.sleep(1)
# 编辑申请岗位
gw = driver.find_element_by_xpath('//*[@id="ApplyPost"]').text
if gw == '文员':
    print('申请岗位正确')
else:
    print('申请岗位错误')
driver.find_element_by_xpath('//*[@id="ApplyPost"]').click()
driver.find_element_by_xpath('//*[@id="ApplyPost-option"]/div[2]/input').send_keys('行政专员', Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyPost-option"]/div[1]/ul/li[2]').click()
# 编辑申请人数
rs = driver.find_element_by_id('ApplyNumber').get_attribute("value")
if rs == '1':
    print('申请人数正确')
else:
    print('申请人数错误')
driver.find_element_by_xpath('//*[@id="ApplyNumber"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyNumber"]').send_keys('2')
time.sleep(1)
# 编辑申请类型
sqlx = driver.find_element_by_xpath('//*[@id="ApplyType"]/div').text
if sqlx == '岗位新增':
    print('申请类型正确')
else:
    print('申请类型错误')
driver.find_element_by_xpath('//*[@id="ApplyType"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyType-option"]/div/ul/li[3]').click()
time.sleep(1)
# 编辑期望到职时间
dzsj = driver.find_element_by_id('ExpectEntryDate').get_attribute("value")
if dzsj == '2019-09-15':
    print('期望到职时间正确')
else:
    print('期望到职时间错误')
driver.find_element_by_xpath('//*[@id="ExpectEntryDate"]').clear()
driver.find_element_by_xpath('//*[@id="ExpectEntryDate"]').send_keys('2019-09-28')
time.sleep(1)
# 编辑薪酬范围
xcfw = driver.find_element_by_id('SalaryRange').get_attribute("value")
if xcfw == '5000-10000':
    print('薪酬范围正确')
else:
    print('薪酬范围错误')
driver.find_element_by_xpath('//*[@id="SalaryRange"]').clear()
driver.find_element_by_xpath('//*[@id="SalaryRange"]').send_keys('8k-10k')
time.sleep(1)
# 编辑申请理由
sqly = driver.find_element_by_id('ApplyReason').get_attribute("value")
if sqly == '人手不足，急需增派':
    print('申请理由正确')
else:
    print('申请理由错误')
driver.find_element_by_xpath('//*[@id="ApplyReason"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyReason"]').send_keys('离职增补')
time.sleep(1)
# 编辑性别要求
xbyq = driver.find_element_by_xpath('//*[@id="ApplySex"]/div').text
if xbyq == '女':
    print('性别要求正确')
else:
    print('性别要求错误')
driver.find_element_by_xpath('//*[@id="ApplySex"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplySex-option"]/div/ul/li[1]').click()
time.sleep(1)
# 编辑学历要求
xlyq = driver.find_element_by_xpath('//*[@id="ApplyEducation"]/div').text
if xlyq == '大专':
    print('学历要求正确')
else:
    print('学历要求错误')
driver.find_element_by_xpath('//*[@id="ApplyEducation"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyEducation-option"]/div[2]/input').send_keys('本科', Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyEducation-option"]/div[1]/ul/li[2]').click()
time.sleep(1)
# 编辑年龄
nl = driver.find_element_by_id('ApplyAgeExplain').get_attribute("value")
if nl == '25':
    print('年龄要求正确')
else:
    print('年龄要求错误')
driver.find_element_by_xpath('//*[@id="ApplyAgeExplain"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyAgeExplain"]').send_keys('23')
time.sleep(1)
# 编辑专业要求
zy = driver.find_element_by_id('ApplyProfessionalExplain').get_attribute("value")
if zy == '行政相关':
    print('专业要求正确')
else:
    print('专业要求错误')
driver.find_element_by_xpath('//*[@id="ApplyProfessionalExplain"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyProfessionalExplain"]').send_keys('人力资源相关')
time.sleep(1)
# 编辑工作经验要求
gzjy = driver.find_element_by_xpath('//*[@id="ApplyWorkExperience"]').text
if gzjy == '有要求':
    print('工作经验要求正确')
else:
    print('工作经验要求错误')
driver.find_element_by_xpath('//*[@id="ApplyWorkExperience"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyWorkExperience-option"]/div/ul/li[1]').click()
time.sleep(1)
# 编辑职称要求
zc = driver.find_element_by_xpath('//*[@id="ApplyProfessionalTitle"]').text
if zc == '无要求':
    print('职称要求正确')
else:
    print('职称要求错误')
driver.find_element_by_xpath('//*[@id="ApplyProfessionalTitle"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyProfessionalTitle-option"]/div/ul/li[3]').click()
time.sleep(1)
# 编辑职业资格证书要求
zs = driver.find_element_by_id('ApplyProfessionalCertificateExplain').get_attribute("value")
if zs == '秘书证':
    print('证书要求正确')
else:
    print('证书要求错误')
driver.find_element_by_xpath('//*[@id="ApplyProfessionalCertificateExplain"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyProfessionalCertificateExplain"]').send_keys('人力资源相关证书')
time.sleep(1)
# 编辑专业技能要求
zyjn = driver.find_element_by_id('ApplyProfessionalSkillsExplain').get_attribute("value")
if zyjn == '熟悉办公自动化相关软件':
    print('专业技能要求正确')
else:
    print('专业技能要求错误')
driver.find_element_by_xpath('//*[@id="ApplyProfessionalSkillsExplain"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyProfessionalSkillsExplain"]').send_keys('熟悉办公软件')
time.sleep(1)
# 编辑外语要求
wy = driver.find_element_by_id('ApplyForeignLanguageExplain').get_attribute("value")
if wy == '英语四级以上':
    print('外语要求正确')
else:
    print('外语要求错误')
driver.find_element_by_xpath('//*[@id="ApplyForeignLanguageExplain"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyForeignLanguageExplain"]').send_keys('熟悉简单口语即可')
time.sleep(1)
# 编辑计算机要求
jsj = driver.find_element_by_id('ApplyComputerExplain').get_attribute("value")
if jsj == '计算机二级以上':
    print('计算机要求正确')
else:
    print('计算机要求错误')
driver.find_element_by_xpath('//*[@id="ApplyComputerExplain"]').clear()
driver.find_element_by_xpath('//*[@id="ApplyComputerExplain"]').send_keys('熟悉常用办公软件即可')
time.sleep(1)
# 编辑其他要求
qt = driver.find_element_by_id('ApplyOthersExplain').get_attribute("value")
if qt == '形象气质俱佳者优先':
    print('其他要求正确')
else:
    print('其他要求错误')
driver.find_element_by_xpath('//*[@id="ApplyOthers"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ApplyOthers-option"]/div/ul/li[1]').click()
time.sleep(1)

# 修改标题
# 回到父层
driver.switch_to.parent_frame()
time.sleep(1)
# 进入子层 frame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('Form'))  #第一层
time.sleep(1)
bt = driver.find_element_by_id('CustomName').get_attribute("value")
if bt == '人力-文员增补':
    print('标题正确')
else:
    print('标题错误')
driver.find_element_by_xpath('//*[@id="CustomName"]').clear()
driver.find_element_by_xpath('//*[@id="CustomName"]').send_keys('行政专员_离职增补')
time.sleep(1)
# 修改重要等级
driver.find_element_by_xpath('//*[@id="ProcessInfo"]/table/tbody/tr[6]/td/div[2]').click()
time.sleep(1)
# 修改备注
bz = driver.find_element_by_xpath('//*[@id="Description"]').get_attribute("value")
if bz == '这是总部职能中心，人力资源部的文员增补申请。':
    driver.find_element_by_xpath('//*[@id="Description"]').clear()
    driver.find_element_by_xpath('//*[@id="Description"]').send_keys\
        ('这是总部职能中心，人力资源部的行政人员的离职增补申请。')
time.sleep(1)
# 完成提交
driver.find_element_by_xpath('//*[@id="btn_finish"]').click()

# 验证编辑结果
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
time.sleep(1)
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











