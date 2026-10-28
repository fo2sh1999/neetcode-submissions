class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = 1 
        while k < len(arr):
            arr[k-1]=max(arr[k:])
            k+=1
        arr[-1]=-1
        return arr