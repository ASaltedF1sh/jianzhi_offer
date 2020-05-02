import numpy as np

class Solution:
  def hasPath(matrix, path):

    path = list(path)
    height, width = (4,4)
    result = False

    for h in range(height):
      for w in range(width):
        if matrix[h][w] == path[0]:
          current_matrix =matrix.copy()
          current_matrix[h][w] = '@'
          current_path = path.copy()
          current_path.pop(0)
          result = searchPath(current_matrix, h, w, current_path)
          if result == True:
            return result

    return result

  def searchPath(matrix, rows, cols, path):

    result = False
    if len(path) == 0:
      # print('fsdf',path,len(path))
      return True
    else:
      height, width = (4,4)

      next_point = []
      if rows - 1 >= 0:
        next_point.append([rows - 1, cols])
      if rows + 1 <= height - 1:
        next_point.append([rows + 1, cols])
      if cols - 1 >= 0:
        next_point.append([rows, cols - 1])
      if cols + 1 <= width-1:
        next_point.append([rows, cols + 1])

      if len(next_point) == 0:
        return False
      else:
        for h ,w in next_point:
            if matrix[h][w] == path[0]:
              current_matrix = matrix.copy()
              current_matrix[h][w] = '@'						
              current_path = path.copy()
              current_path.pop(0)
              result = searchPath(current_matrix, h, w, current_path)
              if result:
                return True
        return result



if __name__ == '__main__':

	# mymatrix = 			[['a', 'a', 'a', 'a'],
	# 					 ['a', 'a', 'a', 'a'],
	# 					 ['a', 'a', 'a', 'a'],
	# 					 ['a', 'a', 'a', 'a']]
						
	# print(hasPath(mymatrix,'aaaaaaaaaaaaaa'))
