class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        sum = 0
        result = [[ 0 for col in range(len(other.values[0]))] for row in range(len(self.values))]
        for a_row in range(len(self.values)):
            for b_col in range(len(other.values[0])):
                for b_row in range(len(other.values)):
                    sum += self.values[a_row][b_row] * other.values[b_row][b_col]
                result[a_row][b_col] = sum
                sum = 0
        return Matrix(result)
                
    def __rmatmul__(self, other):
        sum = 0
        result = [[ 0 for col in range(len(self.values[0]))] for row in range(len(other.values))]
        for a_row in range(len(other.values)):
            for b_col in range(len(self.values[0])):
                for b_row in range(len(self.values)):
                    sum += other.values[a_row][b_row] * self.values[b_row][b_col]
                result[a_row][b_col] = sum
                sum = 0
        return Matrix(result)

    def __imatmul__(self, other):
        sum = 0
        result = [[ 0 for col in range(len(other.values[0]))] for row in range(len(self.values))]
        for a_row in range(len(self.values)):
            for b_col in range(len(other.values[0])):
                for b_row in range(len(other.values)):
                    sum += self.values[a_row][b_row] * other.values[b_row][b_col]
                result[a_row][b_col] = sum
                sum = 0
        return Matrix(result)

