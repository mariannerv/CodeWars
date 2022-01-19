#[7, 1]  =>  [1, 7]
#[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True) #organiza a lista de odds
  return [x if x%2==0 else odds.pop() for x in arr]
