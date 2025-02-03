def calculate_scores(log):
    sub = {}
    for e in log:
        time, problem, result = e
        if problem not in sub:
            sub[problem] = []
        sub[problem].append((time, result))
    
    ps = 0
    tt = 0
    
    for problem, entries in sub.items():
        pet = 0
        st = None
        
        for time, result in entries:
            if result == "right":
                st = time
                break  
            elif st is None: 
                pet += 20
        
        if st: 
            ps += 1
            tt += st + pet  
    
    return ps, tt

log = list(map(int, input().strip().split()))

# Filter out the terminator entry
log = [entry for entry in log if entry[0] != 0]

# Calculate and Print Results
solved, time_score = calculate_scores(log)
print(f"{solved} {time_score}")
