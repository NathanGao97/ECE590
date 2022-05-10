def dict(target):
    for i in range(0, 3):
        if target == words[i]:
            return True
    return False


def testcheck(string, front=0, back=1):
    if back == len(string):
        return dict(string[front:back])
    elif dict(string[front:back]):
        return testcheck(string, front, back + 1) or testcheck(string, back, back + 1)
    else:
        return testcheck(string, front, back + 1)


def getdp(string):
    length = len(string)
    dp = [[None for j in range(length + 1)] for i in range(length)]
    for j in range(1, length + 1):
        dp[0][j] = dict(string[0:j])
    for i in range(1, length):
        for j in range(i + 1, length + 1):
            if dict(string[i:j]):
                dp[i][j] = dp[i - 1][j] or dp[i - 1][i]
            else:
                dp[i][j] = dp[i - 1][j]

    print('DP table:')
    for i in range(length):
        for j in range(length + 1):
            print(dp[i][j], end=' ')
        print('\n', end='')
    print()

    ans = []
    pivot = length
    while pivot > 0:
        valid = False
        for i in range(length):
            if dp[i][pivot]:
                valid = True
                pivot = i
                ans.append(i)
                break
        if not valid:
            raise Exception('Invalid!')
    print(ans)


if __name__ == '__main__':
    words = ['of', 'the', 'year']
    string = "oftheyear"
    if testcheck(string):
        print('Valid!\n')
    else:
        print('Invalid!')
    getdp(string)
