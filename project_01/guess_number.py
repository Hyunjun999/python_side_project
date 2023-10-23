import random

answer = random.randint(1, 100)
cnt = 1
while True:
    try:  # check that the input number is an integer or not
        guess = int(input("Enter the number btw 1 and 100: "))
        if guess > answer:
            print("Down")
        elif guess < answer:
            print("Up")
        else:
            print(f"Congrats! You get the answer in {cnt} times!")
            break
        cnt += 1
    except:
        print("Enter the integer.")
