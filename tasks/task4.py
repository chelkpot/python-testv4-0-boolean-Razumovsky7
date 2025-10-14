# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    D = a + b > c and a + c > b and b + c > a
    print(D)

    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()