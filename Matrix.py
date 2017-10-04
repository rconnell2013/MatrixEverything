# file: "Matricies.py"
def Id(n):
    A = Matrix(n,n)
    # loop through and make diagnals 1s
    for x in range(A.crow):
        A.setElement(x,x,1)
    return A

class Matrix:
    def __init__(self, n, m):
        self.crow = n
        self.ccol = m
        self.elements = list()
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
                
    def display(self):
        for i in range(self.crow):
            print "[",
            for j in range(self.ccol):
                print self.elements[i][j],
            print "]"

    def getElement(self, x, y):
        return self.elements[x][y]

    def setElement(self, x, y, n):
        self.elements[x][y] = n
        return None

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
        temp = Id(self.ccol)
        temp.setElement(n,n,k)
        return temp * self
    #def row_swap(self,n,m) #n and m are swapped rows
    #def row_addk(self,n,m,k) #multiply row n by k and add it to m

