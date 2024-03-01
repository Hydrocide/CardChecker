



def luhnsalgorithm(card: str) -> bool:
    sign = (len(card)-1)%2
    sum = 0
    for i in range(len(card)-2, -1, -1):
        num = int(card[i])
        sum += num if i%2 == sign else (num*2)%10 + (num*2)//10
    newcheck = 10 - (sum%10)
    return card[:-1] + str(newcheck) == card