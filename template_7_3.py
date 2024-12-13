
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###

        if not isinstance(arr, list) or not all(isinstance(row, list) for row in arr):
            raise not2DError()

        length = [len(row) for row in arr]
        if len(set(length)) != 1:
            raise unevenListError()

        self.rows = len(arr)
        self.cols = length[0]
    
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        return f'list_2D: {self.rows}*{self.cols}'

        ######

    def transpose(self):

        ### YOUR CODE HERE ###

        transposed = [[self[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return list_D2(transposed)
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###

        if not isinstance(others, list_D2) or self.cols != others.rows:
            raise improperMatrixError()

        result = [[mul1d(self[i], [others[j][k] for j in range(others.rows)]) for k in range(others.cols)] for i in
                  range(self.rows)]
        return list_D2(result)

        ######

    def avg(self):

        ### YOUR CODE HERE ###

        total_sum = sum(sum(row) for row in self)
        total_element = self.rows * self.cols
        return total_sum / total_element

        ######
