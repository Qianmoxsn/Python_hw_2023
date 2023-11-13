'''
Description:
用字典来模拟一个简单的用户账号注册、登录与退出的程序：
Demo: Login system with User PWD
Registration:
input name&pwd,
Duplicate Checking
Login:
check name&pwd
Quit:
quit
'''

if __name__ == "__main__":
    # answer here
    # Dict
    user = {}
    # Mode Select
    while True:
        mode = input("Please select mode: 1.Register 2.Login 3.Quit")
        if mode == "1":
            # Register
            while True:
                print(">> Welcome to register!")
                name = input("Please input your name:")
                if name in user:
                    print("The name is already exist!\n")
                else:
                    pwd = input("Please input your password:")
                    user[name] = pwd
                    print("Register successfully!\n")
                    break

        elif mode == "2":
            # Login
            while True:
                print(">> Welcome to login!")
                name = input("Please input your name:")
                if name in user:
                    pwd = input("Please input your password:")
                    if user[name] == pwd:
                        print("Login successfully!\n")
                        break
                    else:
                        print("Wrong password!\n")
                else:
                    print("The name is not exist!\n")

        elif mode == "3":
            # Quit
            print("Quit successfully!\n")
        else:
            print("Wrong mode code!\n")
