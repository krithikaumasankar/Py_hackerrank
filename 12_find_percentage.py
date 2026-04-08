if __name__ == '__main__':
    n = int(input())
    s = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        s[name] = scores
    qn = input()
    avg = sum(s.get(qn))/len(scores)
    print("{:.2f}".format(avg))
