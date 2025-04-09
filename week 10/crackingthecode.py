import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M = [input().strip() for _ in range(int(input()))]
    
    S = input().strip()
    D = input().strip()
    
    N = len(S)
    T = len(D)
    
    z = ['?'] * T

    M = [word for word in M if len(word) == N]
    
    can = False
    
    W = {chr(i + 97): set() for i in range(26)}

    for m in M:
        a, r = {}, {}
        ok = True
        
        for i in range(N):
            if m[i] not in a:
                a[m[i]] = S[i]
            if S[i] not in r:
                r[S[i]] = m[i]
            if a[m[i]] != S[i] or r[S[i]] != m[i]:
                ok = False
                break
        
        if ok:
            can = True
            for c in S:
                W[c].add(r[c])

    if not can:
        print('IMPOSSIBLE')
        continue

    if all(len(v) < 2 for v in W.values()) and sum(len(v) for v in W.values()) == 25:
        for c in W:
            if not W[c]:
                all_chars = {chr(i) for i in range(97, 123)}
                used = set()
                for j in W:
                    used |= W[j]
                W[c] = all_chars - used
                break

    K = {chr(i + 97): set() for i in range(26)}
    for src in W:
        for dst in W[src]:
            K[dst].add(src)

    for i in range(T):
        possible_sources = K[D[i]]
        if len(possible_sources) == 1:
            src = next(iter(possible_sources))
            if len(W[src]) == 1:
                z[i] = src

    print(''.join(z))
