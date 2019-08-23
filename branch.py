username = input('请输入用户名：')
password = input('请输入口令：')

#getpass
#import getpass
#password = getpass.getpass('请输入口令：')


if username == 'admin' and password == '123456':
    print('身份验证通过！')
else:
    print('身份验证失败！')