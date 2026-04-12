n = int(input())

for _ in range(n):
    s = input().strip()

    # Rule 1: must start with 4, 5, or 6
    if not s or s[0] not in "456":
        print("Invalid")
        continue

    # Rule 2: handle hyphen format
    if '-' in s:
        parts = s.split('-')
        if len(parts) != 4 or not all(len(p) == 4 for p in parts):
            print("Invalid")
            continue
        s = ''.join(parts)

    # Rule 3: digits + length check
    if not s.isdigit() or len(s) != 16:
        print("Invalid")
        continue

    # Rule 4: no 4 consecutive same digits
    if any(s[i] == s[i+1] == s[i+2] == s[i+3] for i in range(len(s)-3)):
        print("Invalid")
        continue

    print("Valid")
