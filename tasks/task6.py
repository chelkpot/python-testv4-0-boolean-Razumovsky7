# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a= float(input("введите первую сторону: "))
    b= float(input("введите вторую сторону: "))
    c= float(input("введите третью сторону: "))
    sides= sorted([a, b, c])
    h = sides[2]
    s = sides[0]
    t = sides[1]
    d = h**2 == s**2 + t**2
    print(d)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()