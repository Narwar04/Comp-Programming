def solve():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    for _ in range(N):
        M = int(input[idx])
        idx += 1
        distances = list(map(int, input[idx:idx+M]))
        idx += M
        
        total = sum(distances)
        if total % 2 != 0:
            print("IMPOSSIBLE")
            continue
        
        # Initialize DP: each step is a dictionary {height: (max_height, prev_h, direction)}
        dp = [{} for _ in range(M+1)]
        dp[0][0] = (0, None, None)
        
        for step in range(M):
            current_dist = distances[step]
            current_dp = dp[step]
            next_dp = dp[step+1]
            
            for h in current_dp:
                current_max, _, _ = current_dp[h]
                
                # Try 'U' direction
                new_h = h + current_dist
                new_max = max(current_max, new_h)
                if new_h >= 0:
                    if new_h not in next_dp or new_max < next_dp[new_h][0]:
                        next_dp[new_h] = (new_max, h, 'U')
                
                # Try 'D' direction
                new_h = h - current_dist
                new_max = max(current_max, new_h)
                if new_h >= 0:
                    if new_h not in next_dp or new_max < next_dp[new_h][0]:
                        next_dp[new_h] = (new_max, h, 'D')
        
        if 0 not in dp[M]:
            print("IMPOSSIBLE")
        else:
            # Reconstruct path
            path = []
            current_h = 0
            for step in range(M, 0, -1):
                entry = dp[step][current_h]
                direction = entry[2]
                path.append(direction)
                current_h = entry[1]
            path.reverse()
            print(''.join(path))

if __name__ == "__main__":
    solve()