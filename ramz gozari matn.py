user = input('Enter your string: ')

num = int(input('Enter your number: '))

nums = []

for cher in user:
    nums.append(str(ord(cher)+ num))

print(','.join(nums))

input('bray khroj (E) type konid: ')
