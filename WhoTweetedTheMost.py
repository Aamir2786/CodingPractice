def whoTweetedMost(no_of_tw):
    udict = dict()
    for _ in range(no_of_tw):
        user_twid = input().split()
        uname = user_twid[0]
        if uname in udict.keys():
            udict[uname] += 1
        else:
            udict[uname] = 1

    max_count = 0
    for i in udict.values():
        if max_count < i:
            max_count = i
    ulist = []
    for k,v in udict.items():
        if v == max_count:
            ulist.append(k)

    ulist.sort()
    for i in ulist:
        print('{} {}'.format(i, max_count))

if __name__ == "__main__":
    no_of_tc = int(input())

    for _ in range(no_of_tc):
        no_of_tw = int(input())
        whoTweetedMost(no_of_tw)