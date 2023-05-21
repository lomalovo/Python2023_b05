def RLE(s: str) -> str:
    length = len(s)
    i = 0
    answer = []
    count = 0
    while i < length:
        if i < length - 1 and s[i] == s[i + 1]:
            count += 1
            i += 1
        else:
            count += 1
            lastElem = s[i]
            if count == 1:
                answer.append(lastElem)
            else:
                answer.append(lastElem)
                answer.append(str(count))
            count = 0
            i += 1
    return "".join(answer)


print(RLE(input()))