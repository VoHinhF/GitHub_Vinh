from module import process, Printaccount

def main():
	accounts=['hovinh@gmail.com:1234', 'garchomp@hotmail.com:4321', 'illidant@gmail.com:2345']
	for account in accounts:
		Email_user_name, Password = process(account)
		Printaccount(Email_user_name, Password)

if __name__ == '__main__':
	main()