#list-example_1.py TLM
file0 = ["IMG03.png", "IMG010.png", "IMG111.png", "IMG222.png"]
file1 = ["IMG-001.png", "IMG-002.png", "IMG-003.png", "IMG-004.png"]
#print(file0)
#print(file1)
for i in range(0,4):
	print ("mv "+file0[i]+" "+file1[i]+";")
