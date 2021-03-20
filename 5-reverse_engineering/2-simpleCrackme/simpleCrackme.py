def crack(a):
    res = 0
    if a <= 96 or a > 122:
        if a <= 64 or a > 90:
            res = a
        else:
            res = (102 * (a - 65) + 3) % 26 + 65
    else:
        res = (102 * (a - 97) + 3) % 26 + 97
    return res

if __name__ == '__main__':
    target = 'zpdt{Pxn_zxndl_tnf_ddzbff!}'
    ans = ''
    for i in range(len(target)):
        for j in range(0,250):
            if chr(crack(j)) == target[i]:
                ans += chr(j)
                break
    print(ans)
