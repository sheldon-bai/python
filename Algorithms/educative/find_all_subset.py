def find_subset_rec(s, subset, res, index):
  res.append(subset[:])

  n = len(s)

  for i in range(index, n):
    subset.append(s[i])
    find_subset_rec(s, subset, res, i + 1)
    subset.pop()

def find_all_subsets(s):
  subset = []
  res = []

  find_subset_rec(s, subset, res, 0)

  return res



def main():
  s = [1, 2, 3]

  res = find_all_subsets(s)

  print(res)

if __name__ == '__main__':
  main()