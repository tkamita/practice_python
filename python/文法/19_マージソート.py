def merge_sort(arr):
  if len(arr) > 1:
    res = []    #返り値の配列
    mid = len(arr)    #配列の真ん中の値
    L = arr[:mid]   #配列の真ん中より左の値   [1,2,3,4,] => [1,2]
    R = arr[mid:]   #配列の真ん中より右の値   [1,2,3,4,] => [3,4]
    L = merge_sort(L)   #並び替え   [3,1] => [1,3]
    R = merge_sort(R)   
    i = j = 0       #iはLを探索するインデックス、jはRを探索すインデックス
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        res.append(L[i])
        i += 1
      elif L[i] > R[j]:
        res.append(R[j])
        j += 1
      else:
        res.append(L[i])
        i += 1
    while i < len(L):
      res.append(L[i])
      i += 1
    while j < len(R):
      res.append(R[j])
      j += 1
    return res
  else:
    return arr


list_a = [5,2,6,3,1,7,4,9,8]
print(merge_sort(list_a))