import sys
cnt, err_cnt = 0, 0


def userlogin(input_user, input_pwd):
    global err_cnt
    user = "Kate"
    pwd = "666666"
    if input_user == user and input_pwd == pwd:
        print("登录成功！")
        sys.exit()
    else:
        err_cnt += 1
        if err_cnt == 3:
            print("3次用户名或者密码均有误！退出程序。")
            sys.exit()


def main():
    # global cnt
    while True:                         # or [while cnt < 3:]
        input_user = input()
        input_pwd = input()
        userlogin(input_user, input_pwd)
        # cnt += 1


main()
