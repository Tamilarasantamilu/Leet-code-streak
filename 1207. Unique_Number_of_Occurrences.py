class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    dict_occur, list_unique = {}, []
    for a in arr:
      if a not in dict_occur.keys():
        dict_occur[a] = 1
      else:
        dict_occur[a] += 1
    
    for key, val in dict_occur.items():
      if val not in list_unique:
        list_unique.append(val)
    
    return True if (len(dict_occur.values()) == len(list_unique)) else False
