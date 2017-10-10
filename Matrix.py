# file: "Matricies.py"
from fractions import Fraction

def Id(n): #returns Identity matrix of size n
    A = Matrix(n,n)
    # loop through and make diagnals 1s
    for x in range(A.crow):
        A.setElement(x,x,1)
    return A

class Matrix:
    #BASE
    def __init__(self, n, m):
        self.crow = n
        self.ccol = m
        self.elements = list()
        self.sq = (self.crow == self.ccol)
        self.isRef = False
        for x in range(n):
            self.elements.append(list(range(m)))
            for y in range(m):
                self.elements[x][y] = 0
                    
    def define(self, *args):
        #assert len(args) == self.crow * self.ccol, "Please enter the approopareateareate amount of elements
        #could Pad etra length with 0/ignore extra arguments
        ref = 0
        for x in range(self.crow):
            for y in range(self.ccol):
                self.elements[x][y] = args[ref]
                ref = ref + 1
                
    def display(self):
        for i in range(self.crow):
            print "[",
            for j in range(self.ccol):
                print self.elements[i][j],
            print "]"
    #HELPER FUNCTIONS
    def getElement(self, x, y):
        return self.elements[x][y]

    def setElement(self, x, y, n):
        self.elements[x][y] = n
        return None

    #OPERATORS
    def __mul__(self, other):
        assert self.ccol == other.crow, "for A(nxm)*B(pxq), m must equal p"
        temp = Matrix(self.crow, other.ccol)
        ref = 0
        for m in range(self.crow):
            for n in range(other.ccol):
                temp_sum = 0
                ref = 0
                for x in range(self.ccol):
                    temp_sum = temp_sum + self.elements[m][ref]*other.elements[ref][n]
                    ref = ref + 1
                temp.elements[m][n] = temp_sum
        return temp
    
    def __rmul__(self, k):
        temp = Matrix(self.crow,self.ccol)
        for m in range(self.crow):
            for n in range(self.ccol):
                temp.elements[m][n] = k * self.elements[m][n]
        return temp
                
        
    def __add__(self, other):
        assert self.ccol == other.ccol and self.crow == other.crow, "The matricies are not the same size"
        temp = Matrix(self.crow, self.ccol)
        for m in range(self.crow):
            for n in range(self.ccol):
                temp.elements[m][n] = self.elements[m][n] + other.elements[m][n]
        return temp

    def __pow__(self, k):
        temp = self
        if k < 0:
            return temp.inverse()**(-k)
        if k == 1:
            return temp
        if k%2 == 0:
            temp = temp * temp
            return temp**(k/2)
        if k%2 == 1:
            temp = temp * temp
            return self * temp**((k-1)/2)

        
    #ELEMENTARY OPERATIONS
    
    def row_multk(self,n,k): #multiply row n by k
        temp = Id(self.crow)
        temp.setElement(n,n,k)
        return temp * self
    def row_swap(self,n,m): #n and m are swapped rows
        temp = Id(self.crow)
        temp.setElement(n,m,1)
        temp.setElement(m,n,1)
        temp.setElement(n,n,0)
        temp.setElement(m,m,0)
        return temp * self
    def row_addk(self,n,m,k): #multiply row n by k and add it to m
        temp = Id(self.crow)
        temp.setElement(m,n,k)
        return temp * self

    #MATRIX OPERATIONS

    def minor(self,i,j): #finds minor of matrix
        assert self.sq == True, "Matrix must be a square matrix"
        temp = Matrix(self.crow - 1 , self.ccol - 1)
        x = 0
        y = 0
        for m in range(self.crow):
            for n in range(self.ccol):
                if x < i:
                    if y < j:
                        temp.setElement(m,n,self.elements[x][y])
                    if y > j:
                        temp.setElement(m,n-1,self.elements[x][y])
                if x > i:
                    if y < j:
                        temp.setElement(m-1,n,self.elements[x][y])
                    if y > j:
                        temp.setElement(m-1,n-1,self.elements[x][y])
                y = y + 1
            x = x + 1
            y = 0
        return temp
    
    def det(self): #Finds determinant of matrix using Cofactors
        assert self.sq == True, "Matrix must be a square matrix"
        temp = 0
        if self.crow==2:
            return (self.elements[0][0] * self.elements[1][1]) - (self.elements[0][1] * self.elements[1][0])
        else:
            for m in range(self.ccol):
                temp = temp + (((-1)**m) * self.elements[0][m] * self.minor(0,m).det())
            return temp

    def diagDet(self): #uses list of row operations to find diagonal
        alist = self.getRREF()
        det = 1
        for op in alist:
            if op[0] == 0:
                det = Fraction(det, op[2])
        return det
    
    def getRREF(self): #Gets list of operations needed to get from this matrix to the Identity
        assert self.sq == True, "Matrix must be square"
        temp = self
        algorithm = list()
        for m in range(self.ccol):
            for n in range(self.ccol):
                if m != n:
                    nfact = temp.elements[n][m]
                    algorithm.append([0,n,temp.elements[m][m]])
                    temp = temp.row_multk(n,temp.elements[m][m])
                    algorithm.append([1,m,n,-nfact])
                    temp = temp.row_addk(m,n,-nfact)
        for p in range(self.ccol):
            algorithm.append([0,p,Fraction(1,temp.elements[p][p])])
            temp = temp.row_multk(p,Fraction(1,temp.elements[p][p]))
        return algorithm

    #could move solve code into inverse function and multiply other by inverse to solve
    def solve(self, other): #returns x for. Ax=b for matrix A=self and b=other
        alist = self.getRREF()
        temp = other
        for op in alist:
            if op[0] == 0:
                temp = temp.row_multk(op[1], op[2])
            if op[0] == 1:
                temp = temp.row_addk(op[1],op[2],op[3])
        return temp;

    def inverse(self): #returns inverse of self matrix
        return self.solve(Id(self.ccol))
            




















        
        

