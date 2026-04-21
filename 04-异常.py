# try:
#     x=int(input("what's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")


# try:
#     x=int(input("what's x? "))
# except ValueError:
#     print("x is not an integer")
# print(f"x is {x}")      #输入cat时，报错NameError

# try:
#     x=int(input("what's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# def main():
#     x=get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             pass
# main()

# # 最好选择应用有参函数，实用性强
# def main():
#     x=get_int("what's x? ")
#     print(f"x is {x}")
# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass
# main()

# 错误代码
# def main():
#     x=get_int("what's x? ")
#     print(f"x is {x}")
# def get_int(prompt):
#     while True:
#         user_input=input(prompt)
#         try:
#             return int(user_input)
#         except ValueError:
#             raise ValueError(f"'{user_input}' 不是有效的整数，请输入数字") 
# main()

def main():
    while True:  # 循环直到输入正确
        try:
            x = get_int("what's x? ")
            print(f"x is {x}")
            break  # 输入正确，退出循环
        except ValueError as e:
            print(f"提示：{e}，请重新输入！")

def get_int(prompt):
    user_input = input(prompt)
    try:
        return int(user_input)
    except ValueError:
        raise ValueError(f"'{user_input}' 不是有效的整数，请输入数字")

main()