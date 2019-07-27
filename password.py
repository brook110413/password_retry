password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	password_1 = input('請輸入您的密碼: ')
	if password != password_1:
		print('密碼錯誤')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('嘗試3次錯誤 帳號已被鎖')
	else:
		print('登入成功')
		break