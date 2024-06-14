def find_pythagorean_triples(arr):
    triples = []
    n = len(arr)
    arr.sort()

    for i in range(0, n):
        if arr[i] == 0:
            continue

        c2 = arr[i] ** 2

        j = 0
        k = n - 1

        while j < k:
            if j == i or arr[j] == 0:
                j += 1
                continue

            if k == i or arr[k] == 0:
                k -= 1
                continue

            a2 = arr[j] ** 2
            b2 = arr[k] ** 2

            sum = a2 + b2

            if sum == c2:
                triples.append([arr[j], arr[k], arr[i]])
                break
            elif sum < c2:
                j += 1
            else:
                k -= 1

    return triples


def main():
    pythagorean_list = [[4,16,1,2,3,5,6,8,25,10], [3,4,5,10,12,13,14,14,15]]

    for i in range(len(pythagorean_list)):
        result = find_pythagorean_triples(pythagorean_list[i])
        print("1.  Original:             ", pythagorean_list[i])
        print("    Pythagorean triples:  ", result)
        print("-"*100)

if __name__ == '__main__':
    main()