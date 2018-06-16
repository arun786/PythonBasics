# to check the number of segments given in ip address and number of
# characters in each segment

ipAddress = input('Enter a number')
if len(ipAddress) != 0:
    if ipAddress[-1] != '.':
        ipAddress += '.'
else:
    ipAddress += '.'

count = 1
countNum = 0
for value in ipAddress:
    if value in '.':
        print('{} segment count is {}'.format(count, countNum))
        count += 1
        countNum = 0
    else:
        countNum += 1
