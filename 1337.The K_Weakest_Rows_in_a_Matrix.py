class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
                def binarySearch(arr):
                    left, right = 0, len(arr)-1
                    while left<=right:
                        mid =(left+right)//2
                        if arr[mid] == 1:
                            left = mid + 1
                        else:
                            right = mid - 1
                    return left
                
                queue = [(binarySearch(row), idx) for idx, row in enumerate(mat)]
                heapq.heapify(queue)

                return [idx for _, idx in heapq.nsmallest(k, queue)]
        
