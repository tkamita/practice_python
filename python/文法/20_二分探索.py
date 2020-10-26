def binary_search(arr, target):  #arr:昇順にソートされた配列　target:配列にある探索したい値
  left = 0  #探索の左はし
  right = len(arr) - 1 #探索の右はし
  for i in range(len(arr)):
    search_idx = (left + right)
    if arr[search_idx] == target:
      return search_idx
    elif arr[search_idx] > target:
      right = search_idx - 1
    elif arr[search_idx] < target:
      left = search_idx + 1
    if left > right:
      return -1


a = [1,2,3,4,5,6]
print(binary_search(a, 1))