import random

low = 1
high = 100
attempts = 0

print("Hãy nghĩ 1 số từ 1 đến 100, tôi sẽ đoán!")

while True:
    guess = (low + high) // 2
    attempts += 1

    print(f"Tôi đoán là: {guess}")
    feedback = input("Đúng (d), Lớn hơn (l), Nhỏ hơn (n): ")

    if feedback == "d":
        print(f"Tôi đã đoán đúng sau {attempts} lần!")
        break
    elif feedback == "l":
        low = guess + 1
    elif feedback == "n":
        high = guess - 1
    else:
        print("Nhập sai rồi!") 