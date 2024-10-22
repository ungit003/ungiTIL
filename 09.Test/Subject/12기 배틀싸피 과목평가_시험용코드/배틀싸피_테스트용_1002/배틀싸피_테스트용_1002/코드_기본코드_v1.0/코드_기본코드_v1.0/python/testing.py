def finder(x):
    askii_list = []
    for elem in x:
        if elem.isdecimal:
            askii_num = ord(elem) + 9
            if askii_num > 90:
                askii_list.append(chr(askii_num-26))
            else:
                askii_list.append(chr(askii_num))
        else:
            askii_list.append(elem)
    ans = ''.join(askii_list)
    print('G', ans)


finder(input())