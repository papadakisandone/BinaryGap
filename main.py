N = 6291457

def solution(N):
    binary = []
    positionofOne = []
    gap = []
    run = True
    # convert to binary
    while run:
        d = N // 2
        r = N % 2
        N = d
        binary.append(r)
        if d == 0:
            run = False
    binary.reverse()
    #print(binary)

    # find the 1s
    for index in range(0, len(binary)):
        if binary[index] == 1:
            positionofOne.append(index)
    #print(f"1 are at :  {positionofOne}")

    # find the gaps
    for i in range(len(positionofOne)):  # loop the list of 1s
        if len(positionofOne) > 1:  # have more than one , 1
            if i != len(positionofOne) - 1:  # as u are not in last index
                result = positionofOne[i + 1] - positionofOne[i]
                if result > 1:  # have at least one zero between of 1s
                    gap.append(result - 1)

    #print(f"Gaps: {gap}")

    return max(gap) if len(gap) else 0


answer = solution(N)
if answer > 0:
    print(f"The Maximum gap of zero is : {answer}")
else:
    print(f"You dont have any gap")
