# i=3
# while i!=0:
#     print("meow")
#     i-=1

# for i in [0,1,2]:
#     print("meow")

# def main():
#     number=get_number()
#     meow(3)
# def get_number():
#     while True:
#         n=int(input("what's n? "))
#         if n>0:
#             break
#     return n		
# def meow(n):
#     for _ in range(n):
#         print("meow")
# main()

# students={
#     "Hermione":"G",
# 	"Harry":"G",
# 	"Ron":"G",
# 	"Draco":"S",
# }
# for student in students:
#     print(student,students[student],sep=",")

""""-----------------------------------------------------"""
# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#",end="")
#         print()
# main()

def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#"*size)
main()

# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
# 	    print_row(size)
# def print_row(width):
#     print("#"*width)
# main()