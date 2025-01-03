num = 0
while True:
    a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
    while True:
        try:
            number = int(a)
            if number in [1, 2, 3]:
                for i in range(1, number + 1):
                    print("playerA:", num + i)
                num += number
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")
    if num >= 31:
        print("playerB win!")
        break


    while True:
        try:
            number = int(a)
            if number in [1, 2, 3]:
                for i in range(1, number + 1):
                    print("playerB:", num + i)
                num += number
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")
    if num >= 31:
        print("playerA win!")
        break