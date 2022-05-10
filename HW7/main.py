def partC(skiers, skis):
    if len(skiers) != len(skis):
        raise Exception('Invalid inputs: the number of skiers and skis are not equal!')
    length = len(skiers)
    disparity = 0
    for i in range(length):
        disparity += abs(skiers[i] - skis[i])
    return disparity


def recurDisparity(skiers, skis):
    n = len(skiers)
    m = len(skis)
    if n == 0:
        return 0
    elif n == m:
        return partC(skiers, skis)
    else:
        choice1 = abs(skiers[n - 1] - skis[m - 1]) + recurDisparity(skiers[0:n - 1], skis[0:m - 1])
        choice2 = recurDisparity(skiers, skis[0:m - 1])
        return min(choice1, choice2)


def getDisparity(skiers, skis):
    n = len(skiers)
    m = len(skis)
    # if n > m:
    #     raise Exception('Invalid inputs: more skiers than skis')
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 0
    for i in range(1, n + 1):
        dp[i][i] = partC(skiers[0:i], skis[0:i])
    for i in range(1, n + 1):
        for j in range(i + 1, m - n + i + 1):
            choice1 = dp[i][j - 1]
            choice2 = dp[i - 1][j - 1] + abs(skiers[i - 1] - skis[j - 1])
            dp[i][j] = min(choice1, choice2)
    print('DP table:')
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end=' ')
        print('\n', end='')
    print()

    ans = []
    i = n
    j = m
    while i != 0 and j != 0:
        if i == 0:
            j -= 1
        elif i == j:
            ans.append(j)
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i][j - 1]:
                j -= 1
            else:
                ans.append(j)
                i -= 1
                j -= 1
    ans.reverse()
    print(ans)
    return dp[n][m]


if __name__ == '__main__':
    skiers_list = [64, 68, 69]
    skis_list = [62, 65, 66, 68, 72]
    disparity_recur = recurDisparity(skiers_list, skis_list)
    print(disparity_recur, '\n')
    disparity_dp = getDisparity(skiers_list, skis_list)
    print(disparity_dp, '\n')
