def minion_game(S):
    S = S.lower()
    kp = 0
    sp = 0
    for i in range(len(S)):
        if S[i] in "aeiou":
            kp += len(S)-i
        else:
            sp += len(S)-i   
    if kp > sp:
        print("Kevin",kp)
    elif sp > kp:
        print("Stuart",sp)
    else:    
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)