if __name__ == '__main__':
    n = int(input())
    s = (list(set(map(int, input().split())))[:n])
    s.sort(reverse = True) 
    print(s[1])
