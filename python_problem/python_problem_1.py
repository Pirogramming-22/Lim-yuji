num = 0
def brGame(player):
    global num
    while True:
        a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        try:
            number = int(a)
            if number in [1, 2, 3]:
                for i in range(1, number + 1):
                    print(player,":", num + i)
                num += number
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")

while True:
    brGame("playerA")
    if num >= 31:
        print("playerB win!")
        break


    brGame("playerB")
    if num >= 31:
        print("playerA win!")
        break