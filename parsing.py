def eval(my_dict,string):
  if len(string) == 1:
    return string
  else:
    for key, value in my_dict.items():
      string = string.replace(key, value)
    return eval(my_dict,string)


my_dict = {'p': '+', 'q': '-', 'r': '-', 's': '+', '-N':'+', '+N':'-', 'rN':'+', 'sN':'-', '--A':'-', '-+A':'-', '+-A':'-', '++A':'+', '--O':'-', '-+O':'+', '+-O':'+', '++O':'+', '--C':'+', '-+C':'+', '+-C':'-', '++C':'+','--B':'+', '-+B':'-', '+-B':'-', '++B':'+'}

string = 'srCpqOANrBNNpsBpsOOrNCO'####input string here!!!

result = eval(my_dict,string)
print(result)
