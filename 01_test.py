import datetime
f = open('42_container.txt', 'w')
f.write(str(datetime.datetime.now()) + '\n')
f.close()
# print('I wrote a line to 42_container.txt')
