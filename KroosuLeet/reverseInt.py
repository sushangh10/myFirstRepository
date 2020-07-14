def reverse(x):
    if -9 < x < 9:
        return x
    x_str = str(x)
    while True:
        if x_str[-1] == '0':
            x_str = x_str[:-1]
        else:
            break
    prefix = '-' if x_str[0] == '-' else ''
    x_list = list()
    for i in x_str:
        if i != '-':
            x_list.append(i)
    y_str = prefix
    while x_list:
        j = x_list.pop()
        y_str += j
    if - (1 << 31) <= int(y_str) <= (1 << 31) -1:
        return int(y_str)
    else:
        return 0



if __name__ == '__main__':
    a = reverse(901000)
    print('a %d' % a)