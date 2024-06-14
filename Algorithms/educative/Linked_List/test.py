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

        # print('i: ', i)

        while j < k:
            b2 = arr[j] ** 2
            c2 = arr[k] ** 2

            print('i: ', i)
            print('j: ', j)
            print('k: ', k)

            sum = a2 + b2

            if sum == c2:
                result.append([arr[i], arr[j], arr[k]])
                break
            elif sum < c2:
                k -= 1
            else:
                j += 1

            print()

    return result

def main():
    arr = [4,16,1,2,3,5,6,8,25,10]
    result = find_pythagorean_triples(arr)
    print(result)

if __name__ == '__main__':
    main()
