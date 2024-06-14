# def find_pythagorean_triples(arr):
#   triples = []
#   #TODO: Write - Your - Code
#   arr.sort()
#   n = len(arr)

#   for i in range(n):
#     j = i + 1
#     k = n - 1
#     a2 = arr[i] ** 2

#     while j < k:
#       b2 = arr[j] ** 2
#       c2 = arr[k] ** 2
#       sum = a2 + b2
#       print('i: ', i)
#       print('j: ', j)
#       print('k: ', k)

#       if sum == c2:
#         triples.append([arr[i], arr[j], arr[k]])
#         break
#       elif sum < c2:
#         k -= 1
#       else:
#         j += 1

#     return triples

# def find_pythagorean_triples(arr):
#     n = len(arr)
#     result = []

#     arr.sort()

#     for i in range(n):
#         if arr[i] == 0:
#             continue

#         a2 = arr[i] ** 2

#         j = i + 1
#         k = n - 1

#         # print('i: ', i)

#         while j < k:
#             b2 = arr[j] ** 2
#             c2 = arr[k] ** 2

#             print('i: ', i)
#             print('j: ', j)
#             print('k: ', k)

#             sum = a2 + b2

#             if sum == c2:
#                 result.append([arr[i], arr[j], arr[k]])
#                 k -= 1
#                 j += 1
#             elif sum < c2:
#                 k -= 1
#             else:
#                 j += 1

#             print()

#     return result

def find_pythagorean_triples(arr):
    n = len(arr)
    result = []

    arr.sort()

    for i in range(n):
        if arr[i] == 0:
            continue

        a2 = arr[i] ** 2

        j = i + 1
        k = n - 1

        while j < k:
            b2 = arr[j] ** 2
            c2 = arr[k] ** 2

            sum = a2 + b2

            if sum == c2:
                result.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1  # Update both pointers to find other potential triples
            elif sum < c2:
                k -= 1
            else:
                j += 1

    return result

# Example usage
input_arr = [3, 4, 5, 10, 12, 13, 14, 14, 15]
print(find_pythagorean_triples(input_arr))


# def find_pythagorean_triples(arr):
#   n = len(arr)  
#   triples = []

#   # Sorting array
#   arr.sort()

#   # Iterating array from start to end
#   for i in range(0, n):
#     if arr[i] == 0:
#       continue
  
#     # Calculating square of current number
#     c2 = arr[i] ** 2

#     j = 0
    
#     # Decrementing length to traverse array
#     k = n - 1
    
#     # Iterates till j becomes less than length of array
#     while j < k:
#       print('i: ', i)
#       print('j: ', j)
#       print('k: ', k)
#       print('ai, aj, ak', arr[i], arr[j], arr[k])
#       print(' ')
#       # If j become equal to i or value of j is equal to 0,
#       # increment j and continue 
#       if j == i or arr[j] == 0:
#         j += 1
#         continue
      
#       # If k become equal to i or value of k is equal to 0,
#       # decrement k and continue 
#       if k == i or arr[k] == 0:
#         k -= 1
#         continue
      
#       a2 = arr[j] ** 2
#       b2 = arr[k] ** 2

#       # Check triples
#       if a2 + b2 == c2:
#         triples.append([arr[j], arr[k], arr[i]])
      
#       # If a2 + b2 + (-c2) > 0, decrement the end iterator
#       # to hit the target sum.      
#       if  a2 + b2 +(-c2) > 0:
#         k -= 1
      
#       # If a2 + b2 + (-c2) < 0, increment the end iterator
#       # to hit the target sum.      
#       else:
#         j += 1
        
#   return triples

# Driver code
def main():
#   pythagorean_list = [[4,16,1,2,3,5,6,8,25,10], [3,4,5,10,12,13,14,14,15], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 4, 5, 10, 12, 13, 14, 14, 15]]
  pythagorean_list = [[3, 4, 5, 10, 12, 13, 14, 14, 15]]
  for i in range(len(pythagorean_list)):
    result = find_pythagorean_triples(pythagorean_list[i])
    print("1.  Original:             ", pythagorean_list[i])
    print("    Pythagorean triples:  ", result)
    print("-"*100)

if __name__ == '__main__':
    main()