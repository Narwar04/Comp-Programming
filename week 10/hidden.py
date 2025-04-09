password, message = input().split()
n = len(password)
msg_ptr = 0

for i in range(n):
    target = password[i]
    allowed_set = set(password[i:])  # Characters allowed at this step
    
    found = False
    for j in range(msg_ptr, len(message)):
        c = message[j]
        if c == target:
            msg_ptr = j + 1
            found = True
            break
        elif c in allowed_set:
            # Encountered an allowed character that's not the target
            print("FAIL")
            exit()
    
    if not found:
        print("FAIL")
        exit()

print("PASS")
