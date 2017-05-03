import csv


class prep:
	def __init__(self):
		self.fname="refinedDataToFindSimilarity-csv.csv"
		self.arr=[]
		self.k=0

	def column_map(self,arx):
		print(arx)
		self.dx={}
		for j in range(len(arx)):
			self.dx[arx[j]]=j
		
		for key in self.dx.keys():
			print(key,self.dx[key])

	def writeit(self,usrx,dictx):
		arx=[0]*24
		ary=[usrx]
		ary.extend(arx)
		for key in dictx.keys():
			ary[key]=dictx[key]
		self.arr.append(ary)
		print(self.k,ary)
		self.k+=1

	def mergeit(self):
		with open(self.fname,"r") as f:
			reader = csv.reader(f)
			count=0
			prev=None
			tempdx={}
			#for row in reader:
			for j in range(10):
				row=next(reader)
				#print(row[0])
				
				if count==0:
					self.column_map(row)
					count+=1
				else:
					#print("Reached here!")
					if row[0]==prev:
						indx=self.dx[row[1]]
						tempdx[indx]=row[indx]
					else:
						self.writeit(prev,tempdx)
						tempdx.clear()
						prev=row[0]
						indx=self.dx[row[1]]
						tempdx[indx]=row[indx]
					count+=1
					if count==10:
						break;


p1=prep()
p1.mergeit()

