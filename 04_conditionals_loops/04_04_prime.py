'''
Print out every prime number between 1 and 100.

'''

num = int(input("Please enter input range for prime #: "))
for cur_num in range(1, num):
    for i in range(2, cur_num):
        if cur_num % i == 0:
            print("our current number is divisible by")
            print(i)
            break
        print("nothing is divisible by this! this number is prime")
        print(cur_num)
