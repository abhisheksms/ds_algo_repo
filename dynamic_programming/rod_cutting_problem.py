from itertools import product
def rod(price, n):
    """
       m: no. of cuts available
       n: rod length from 0 to n

       Cut a rod of length j using cuts from 0 to i
    """
    m = len(price)
    n = n+1
    dp = [[0]*n for _ in range(m)]

    for i,j in product(range(m), range(1, n)):
        if i == 0:
            # first row, cannot move up, hence we go back
            dp[i][j] = price[i] + dp[i][j-i-1]
        elif j-i-1 < 0 :
            # out of boundary, cannot go back, hence we move up
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], price[i] + dp[i][j-i-1])

        # if dp[i-1][j] <= (price[i] + dp[i][j-i-1]):
        #     # print("*"*100)
        #     # print("There is an update!!!")
        #     # print(f"i value {i} j value {j}")
        #     # print(f"j-i-1 is {j-i-1}, which actually is dp[{i}][{j-i-1}]")
        #     # print(f"j-i could have been {j-i} which would have been dp[{i}][{j-i}]")
        #     # print(f"price[i] is {price[i]}, dp[i][j] is {dp[i][j]}, dp[i-1][j] is {dp[i-1][j]}")

        #     dp[i][j] = price[i] + dp[i][j-i-1]
        #     # print("DP Table is")
        #     # for d in dp:
        #     #     print(d, end = "\n")
        #     # print()
        #     # print("*"*100)
            
        # else:
        #     dp[i][j] = dp[i-1][j]

    for d in dp:
        print(d, end = "\n")
    print()

    return dp[-1][-1]

    # print([d for d in dp], end = "\n")

print(rod([2,5,7,8],5)) #12 = 5(2nd piece) + 7(3rd piece)


# print(rod([1, 2, 5],6))
# print(rod([1, 5, 8, 9, 10, 17, 17, 20],4))