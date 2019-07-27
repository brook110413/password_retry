password = 'a123456'
i = 3
while True:
	password_1 = input('請輸入您的密碼: ')
	if password != password_1:
		i = i - 1
		print('密碼錯誤 還有', i, '次機會 ')
		if i == 0:
			break
	else:
		print('登入成功')
		break



