import math

def find_kth_permutation(v, k, result):
  if not v:
    return result

  n = len(v)

  selected = (k - 1) // math.factorial(n - 1)
  
  print('v: ', v)
  print('k: ', k)
  print('fact: ', math.factorial(n - 1))
  print('selected: ', selected)
  print('v[selected]: ', v[selected])
  result += str(v[selected])
  del v[selected]

  k = k - math.factorial(n - 1) * selected
  print('result: ', result)

  return find_kth_permutation(v, k, result)

def get_permutation(n, k):
  #TODO: Write - Your - Code

  v = list(range(1, n + 1))

  # print(block_sizes)


  result = find_kth_permutation(v, k, '')

  return result

def main():
    # aaa = not []
    # print('aaa: ', aaa)
    # print("1. 2nd permutation of 12 =", get_permutation(2, 2))
    # print("\n------------------------------------------------------------------------------------------------------\n")
    # print("2. 5th permutation of 123 =", get_permutation(3, 5))
    # print("\n------------------------------------------------------------------------------------------------------\n")
    print("3. 6th permutation of 1234 =", get_permutation(4, 6))


if __name__ == '__main__':
    main()