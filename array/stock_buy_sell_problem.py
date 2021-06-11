# Incorrect
def stock_buy_sell(a):
    local_minima = profit = 0
    n = len(a)

    for i in range(n-1):

        if i+1 == n-1:
            # last day force sell
            if local_minima > 0:
                profit += a[i+1] - local_minima
        elif a[i] < a[i+1]:
            # buy else hodl
            if local_minima == 0:
                local_minima = a[i]
        else:
            # sell and buy next
            if local_minima > 0:
                profit += a[i] - local_minima

    return profit



print(stock_buy_sell([98,178,250,300,40,540,690]))

print(stock_buy_sell([7,1,5,3,6,4]))

print(stock_buy_sell([5,4,3,2,1]))
