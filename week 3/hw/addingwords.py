
definitions = {}

good = True
while good:
    command = input().strip()
    if not command:
        continue
    if command.startswith('def'):
       _ , var, val = command.split()
       definitions[var] = int(val)

    elif command.startswith('calc'):
        parts = command.split()
        calc_parts = parts[1:-1]
        result = 0
        unknown = False
        current_op = "+"

        for part in calc_parts:
            if part in ["+", "-"]:
                current_op = part
            else:
                if part not in definitions:
                    unknown = True
                    break
                if current_op == "+":
                    result += definitions[part]
                else:
                    result -= definitions[part]

        if unknown:
            print(" ".join(calc_parts) + " = unknown")
        else:
            reverse_lookup = {v: k for k, v in definitions.items()}
            if result in reverse_lookup:
                print(" ".join(calc_parts) + " = " + reverse_lookup[result])
            else:
                print(" ".join(calc_parts) + " = unknown")
    else:
        definitions.clear()
        good = False