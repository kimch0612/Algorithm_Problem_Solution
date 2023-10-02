N = input()
NN = int(0)
if N.find('c=') != 0:
    print(N.find('c='))
if N.find('c-') != 0:
    NN += N.find('c-')
if N.find('dz=') != 0:
    NN += N.find('dz=')
if N.find('d-') != 0:
    NN += N.find('d-')
if N.find('lj') != 0:
    NN += N.find('lj')
if N.find('nj') != 0:
    NN += N.find('nj')
if N.find('s=') != 0:
    NN += N.find('s=')
if N.find('z=') != 0:
    NN += N.find('z=')
print(NN)