def swap(input, i, j):
   string_list = list(input)
   string_list[i], string_list[j] = string_list[j], string_list[i]
   return ''.join(string_list)

def permute_string_rec(input, fix_index, result):
   n = len(input)

   if fix_index == n - 1:
      result.append(input)
      return
   
   for i in range(fix_index, n):
      swapped_input = swap(input, fix_index, i)
      permute_string_rec(swapped_input, fix_index + 1, result)

def permute_string(input_string):
    result = []
    # Starts finding permuations from start of string  
    permute_string_rec(input_string, 0, result)
    return result

def main():
  input_list = ["ab", "bad", "abcd"]

  for i in range(0, len(input_list)):
    res = permute_string(input_list[i])
    print(str(i+1) + '. All permutations of ' + input_list[i] + ': [' + ', '.join(res) + ']')
    print('-----------------------------------------')

  print(res)

if __name__ == '__main__':
  main()






