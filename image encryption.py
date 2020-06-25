from PIL import Image
import numpy,random,sys
img=Image.open(r'C:\Users\Home\Pictures\gtaversion.jpg')
#img.show()
arr=numpy.asarray(img)
arr1=arr.copy()
x,y,z=arr.shape
n=y-(random.randint(y//4,y//2))
n1=x-(random.randint(x//4,x//2))
m,m1=random.randint(1,10),random.randint(1,10)
b,c=random.randint(1,10),random.randint(1,10)
it=random.randint(50,200)
def flip():
	global x,b,n1
	for i in range(b,x-1,n1*2):
		arr1[i:i+n1]=numpy.fliplr(arr1[i:i+n1])
def yflip():
	global y,n,b
	for i in range(b,y-1,n*2):
		arr1[:,i:i+n]=numpy.fliplr(arr1[:,i:i+n])
print('')
for i in range(it):#encryption
	flip()
	c+=m
	yflip()
	b+=m1
	print ('\r{}done'.format((i/it)*100),end='',flush=True)
	sys.stdout.flush()
print('')
#text encryption
li= [n,n1,m,m1,b,c,it]
print('your key',' '.join(str(e) for e in li))


enimg = Image.fromarray(numpy.uint8(arr1)).convert('RGB')
enimg.show()
enimg.save(r'C:\Users\Home\Pictures\New folder\sampleencrypt.jpg')
