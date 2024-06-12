class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_tracker = 0

        def sorter(num_to_sort, array1, index_tracker):
            """
            num_to_sort: number to sort all occurrences
            array1: array to sort
            index_tracker: keeps track of index in array1
            """
            count = array1.count(num_to_sort)

            for i in range(count):
                # Correctly swap the elements to the current index_tracker position
                current_index = array1.index(num_to_sort, index_tracker)
                array1[index_tracker], array1[current_index] = array1[current_index], array1[index_tracker]
                index_tracker += 1
            
            return index_tracker  # Return the updated index_tracker
        
        # Iterate over arr2 and sort arr1 according to arr2's order
        for num in arr2:
            index_tracker = sorter(num, arr1, index_tracker)
        
        # Sort the remaining elements and append them at the end
        if index_tracker < len(arr1):
            remaining_elements = sorted(arr1[index_tracker:])
            arr1[index_tracker:] = remaining_elements
        
        return arr1
