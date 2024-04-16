def min_sub_array_len(target, nums):
    # TODO: Write - Your - Code
	if not nums:
		return None
	
	length = len(nums)
	
	left = 0
	sum = 0
	# At the end, when min_length equal to length, we cannot tell total sum is equal or smaller than target,
	# so when make min_length greater than length initially, if at the end, min_length is smaller or equal to
	# lenght, we will know total sum was greater than target during the middle
	min_length = length + 1

	for right in range(length):
		sum += nums[right]

		while sum >= target:
			min_length = min(right - left + 1, min_length)
			sum -= nums[left]
			left += 1

	if min_length <= length:
		return min_length
	return 0

def main():
    s_list = [7, 4, 11, 1, 1]
    nums_list = [[2,3,1,2,4,3], [1,4,4], [1,1,1,1,1,1,1,1], None, [0]]
    for i in range(len(nums_list)):
        result = min_sub_array_len(s_list[i], nums_list[i])
        print(str(i+1) + ". min_sub_array_len(" + str(s_list[i]) + ", " + str(nums_list[i]) + "): " + str(result))
        print("-------------------------------------------------------------------------------------------------\n");

if __name__ == "__main__":
    main()