x = input()
nums = []
for i in x.split():
    nums.append(int(i))
if (nums[0] * nums[1]) % 2 == 0:
    print(int((nums[0]*nums[1]) / 2))
else:
    print(int(((nums[0]*nums[1]) -1)/ 2))