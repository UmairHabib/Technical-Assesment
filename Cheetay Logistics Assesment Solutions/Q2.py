def equilibriumPoint(array, n):
    # Time complexity is O(n) due to iteration
    # Space complexity is O(1) because of constant space requirement

    try:
        if n<1 or n>106:
            raise Exception('Size Constraint Error. Size of array mismatch with requirement')
        total = sum(array)
        left = 0

        for index, value in enumerate(array):
            if value < 1 or value > 108:
                raise Exception('Value Constraint Error. value of array mismatch with requirement')

            total -= value
            if total == left:
                return index+1
            left += value
        return -1

    except Exception as e:
        return 'Exception Occured ' + str(e)
