from sympy import *

# ERO 실습용 행렬
A = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
pprint(A)

# 두 번째 행과 세 번째 행 교환
A1 = A.elementary_row_op(op= "n<->m",row=0, row1=1)
pprint(A1)
A2 = A.elementary_row_op(op= 'n->kn', row=0, k=2)
pprint(A2)
A3 = A.elementary_row_op(op='n->n+km', row=1, row2=0, k = -4)
pprint(A3)
