# file: "Matricies.py"
def Id(n):
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
        # Pad etra length with 0
        ref = 0
        for x in range(self.crow):
            for y in range(self.ccol):
                self.elements[x][y] = args[ref]
                ref = ref + 1
        self.isReg = (self.det() != 0)
                
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

        #if ( type(other) != Matrix ):
            ## = Matrix(self.crow,self.ccol)
            #for m in range(self.crow):
                #for n in range(self.ccol):
                   # temp.elements[m][n] = other * self.elements[m][n]
           # return temp
        #else:
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
        
    #ELEMENTARY OPERATIONS
    
    def row_multk(self,n,k): #n is row to be multiplied, k is constant to multiply by
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

    def Minor(self,i,j):
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
    def det(self):
        assert self.sq == True, "Matrix must be a square matrix"
        temp = 0
        if self.crow==2:
            return (self.elements[0][0] * self.elements[1][1]) - (self.elements[0][1] * self.elements[1][0])
        else:
            for m in range(self.ccol):
                temp = temp + (((-1)**m) * self.elements[0][m] * self.Minor(0,m).det())
            return temp
    




















        
        

