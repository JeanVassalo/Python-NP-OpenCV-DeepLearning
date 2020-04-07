import numpy as np


print('\n Array \n')

mylist = [1,2,3]

print('Type:', type(mylist))

print('Content:', mylist)

myarray = np.array(mylist)

print('Type:', type(myarray))

print('Content:', myarray)

print('\n Arange \n')

print(np.arange(0,10))

print(np.arange(0,100,10))

print('\n Matrix \n')

print(np.zeros(shape=(5,5))) #SHAPE=(R,C)

print('\n Random \n')

randArray = np.random.randint(0,100,10)

print(randArray)

print('Max:', randArray.max(), 'Position:', randArray.argmax())

print('Min:', randArray.min(), 'Position:', randArray.argmin())

print('Mean:', randArray.mean())

print('\n Reshape \n')

print(randArray.reshape((2,5)))

mat=np.random.randint(0,1000,(10,10))

print('\n Matrix op \n')

print(mat)

print('Pos[0,0]:', mat[0,0])

print('Row 3:', mat[3,:])

print('Slice:\n', mat[0:4,0:4])

matCut=mat.copy()

matCut[0:4,0:4]=0
print('Cut:\n', matCut)
























