def readLine(name, line=0):
  x = open(name, 'r')
  x.readlines()[line]
  return x
        
    
def modLine(text, line=0):
  with open(name, 'r') as code:
    lines = code.readlines()
        
  if 0 <= line_num < len(lines):
    lines[line_num] = new_text + '\n'
        
    with open('code', 'w') as code:
      code.writelines(lines)
  else: print("Invalid line space")
