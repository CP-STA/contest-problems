import json 
cases = []

with open('manual-cases.txt') as f:
    key = None
    for line in f:
        line = line.strip()
        if line == '@@':
            cases.append({})
        elif line == '>':
            key = 'input'
            cases[-1][key] = ''
        elif line == '>>':
            key = 'output'
            cases[-1][key] = ''
        else:
            cases[-1][key] += ('\n' + line) if cases[-1][key] != '' else line

print(json.dumps(cases, indent=2))