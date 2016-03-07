#trexei me python thema4.py
#!/usr/bin/env python
import random
from PIL import Image, ImageDraw
im = Image.new("RGB", (1024, 1024), "white")
x=[]
y=[]
r=[]
a=[]
b=[]
c=[]
d=[]
s=0

# for i in range(0,2):
# 	x.append([i])
# 	y.append([i])
# 	r.append([i])
# 	a.append([i])
# 	b.append([i])
# 	c.append([i])
# 	d.append([i])
for i in range(0,6):
	
	x.append(random.randint(10,1024))
	y.append(random.randint(10,1024))
	r.append(random.randint(10,50))
	#print "ta arxika x y klp gia to " ,i,"antikeimeno", x[i],y[i],r[i]
	t1=x[i]-r[i]
	t2=y[i]-r[i]
	t3=x[i]+r[i]
	t4=y[i]+r[i]
	a.append(t1)
	b.append(t2)
	c.append(t3)
	d.append(t4)
	
	print "ta arxika x y klp gia to ",i,"antikeimeno", x[i],y[i],r[i]
	print "ta arxika shmeia einai: ", a[i],b[i],c[i],d[i]
	draw = ImageDraw.Draw(im)
	c1=random.randint(0,255)
	c2=random.randint(0,255)
	c3=random.randint(0,255)
	while((a[i]<0)or(c[i]>1024)or(b[i]<0)or(d[i]>1024)):
		
		x[i]=random.randint(10,1024)
		y[i]=x[i]
		r[i]=random.randint(10,500)
		a[i]=(x[i]-r[i])
		b[i]=(y[i]-r[i])
		c[i]=(x[i]+r[i])
		d[i]=(y[i]+r[i])
		
	print "ta x y klp", x[i],y[i],r[i]
	print "ta shmeia einai: ","\nto aristero akro: \n" ,a[i],"\nto katw akro: \n",b[i],"\nto deksi akro: \n",c[i], "\nto panw akro: \n", d[i],"\ngia to ",i
	draw.ellipse((a[i], b[i], c[i], d[i]), fill=(c1,c2,c3), outline ='orange')
temp1=0


for i in range(0,6):
	for j in range(i+1,6):
		akt1=(r[i]-r[j])**2
		akt2=(r[i]+r[j])**2	
		stath=(x[i]-x[j])**2+(y[i]-y[j])**2
		if((akt1<=stath)and(stath<=akt2)):
			s=s+1		

if(s==1):
	print "temnetai enas kuklos me enan allon"
else:
	print "temnontai",s,"kukloi"


choice=int(raw_input("pata 1 gia na deis thn eikona h 0 gia na termatisei to programma \n"))
if(choice==1):
	im.show()