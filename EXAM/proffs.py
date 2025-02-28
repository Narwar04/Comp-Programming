def check(n):
    knowledge = set()
    for i in range(n):
        line = input().strip()
        if "->" in line:
            assumptions, conclusion = line.split("->")
            assumptions = assumptions.strip().split() 
            conclusion = conclusion.strip()
            
            if all(assumption in knowledge for assumption in assumptions):
                knowledge.add(conclusion)
            else:
                return i + 1  
        else:
            return i + 1 

    return "correct"

def main():
    print(check(int(input().strip())))

if __name__ == "__main__":
    main()
