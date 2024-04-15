# inherit strWithNewLt from str class
class strWithNewLt(str):
  # redefine __lt__, instead of compare "x" and "y", make smaller of "x" + "y" and "y" + "x" in front
  def __lt__(x, y):
    return x + y < y + x

def largest_number(nums):
    # Write your code here
    # map(str, nums): apply str method to each of nums, make each number in nums to a string\
    # make the map object(which contains all strings) to a list
    str_nums = list(map(str, nums))
    #sort str_nums, why use strWithNewLt class as a key, explained at the end
    sorted_list = sorted(str_nums, key=strWithNewLt, reverse=True)

    if sorted_list[0] == "0":
      return "0"
      
    return "".join(sorted_list)

    # Role of __lt__ in sorted():

    # The sorted() function and the sort() method on lists use these comparison methods to determine the order of objects. Specifically:

    # If no key function is provided, sorted() compares the items using their natural ordering, which, for custom objects, will rely on the implemented comparison methods like __lt__.
    # When a key function is used, sorted() doesn't directly compare the elements themselves but instead compares the values returned by the key function for each element.
  
    # Usage of LargerNumKey in sorted():

    # In your example, you are passing the LargerNumKey class itself as the key argument to sorted(). This usage might seem a bit unusual because typically the key function should return a value that helps determine the sort order, not a class. However, what's effectively happening here is that each string (converted from an integer) is being wrapped into a LargerNumKey object. This wrapping allows the sorted() function to use the __lt__ method defined in LargerNumKey for comparisons, which is based on your custom logic for forming the largest number possible by concatenation.

def main():
     # Driver Code
    nums_arr = [[21,35,20], [0, 5, 1, 3, 2, 4], [71, 5, 21, 52], [0, 0, 0], [1]]
    
    for i in range(len(nums_arr)):
        print(str(i+1) + ". The largest possible number obtained by arranging", nums_arr[i], "is: '", end = "")
        print(str(largest_number(nums_arr[i])) + "'")
        print("---------------------------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()