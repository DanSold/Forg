sub1 = int(1)
sub2 = float(2.3)
sub3 = str('abc')
sub4 = [1, 2, 'WW']
sub5 = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
sub6 = False
sub7 = True
sub8 = ('a', 'b', 'c', 'd',)

total_list = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8]
for item in total_list:
    print(type(item))
