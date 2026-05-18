t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    if k == 1:
        print("YES")
        continue

    diffs = [s[i] - s[i - 1] for i in range(1, k)]

    ok = all(diffs[i] >= diffs[i - 1] for i in range(1, len(diffs)))

    if ok and s[0] <= (n - k + 1) * diffs[0]:
        print("YES")
    else:
        print("NO")
