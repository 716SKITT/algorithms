def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el
    return min_number
nums1 = [1.2, 2, 3, 6, 1]
min1= minimal(nums1)
nums2 = [1, 2, 3, 4, 56]
min2 = minimal(nums2)

if nums1 > nums2:
    print(min1)
else:
    print(min2)

list = ("дАША","сЕВЫЧ", "юСУПОВ")
