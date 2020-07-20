def isPalindrome(x):
    if len(str(x)) == 1:
        return True
    stack = list()
    for i in str(x):
        stack.append(i)
    while len(stack) not in [0, 1]:
        if stack.pop() != stack.pop(0):
            return False
    return True


def isPalindrome2(x: int) -> bool:
    lst = list(str(x))
    head, tail = 0, len(lst) - 1
    while head <= tail:
        if lst[head] != lst[tail]:
            return False
        head += 1
        tail -= 1
    return True


if __name__ == '__main__':

