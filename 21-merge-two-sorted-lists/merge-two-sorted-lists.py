# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(0)
        finalList = mergedList
        while list1 and list2:
            if list2.val < list1.val:
                finalList.next = list2
                list2 = list2.next
            else:
                finalList.next = list1
                list1 = list1.next
            finalList = finalList.next
        if list1:
            finalList.next = list1
        if list2:
            finalList.next = list2
        return mergedList.next


# def mergeTwoLists(list1, list2):
    
#     merged_list = list1 + list2
#     merged_list.sort()

#     return merged_list

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# sorted_list = mergeTwoLists(list1, list2)
# print(sorted_list)
        