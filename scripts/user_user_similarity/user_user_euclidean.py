import csv
import numpy as np
import math
import random


class user_sim:
	def __init__(self):	
		self.data=np.genfromtxt('refined_all.csv',delimiter=',')
		shp=self.data.shape
		self.length=shp[0]
		self.width=shp[1]
		self.user_rowid={}				#dictionary containing the row number of each user
		self.user_comments={}			#dictionary containing the number of comments of every user above a certain threshold

	def euclidean(self,a,b):
		arr_1=self.data[a][1:]
		arr_2=self.data[b][1:]
		diffx=arr_1-arr_2
		sqrd=diffx*diffx
		sum_sqrd=np.sum(sqrd)
		distx=math.sqrt(sum_sqrd)
		return(distx)

	def num_comments(self,threshold):
		with open("refined_all.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			#row=next(reader)				#first row in the dataset
			for j in range(self.length):
				row=next(reader)
				userid=row[0]
				self.user_rowid[userid]=j
				noc=sum(self.data[j][1:])
				if noc>=threshold:
					self.user_comments[userid]=noc		

	def control(self):
		self.num_comments(5)
		count=0
		ofile=open('lol.txt','w')
		for keyx in self.user_rowid.keys():
			print(keyx,self.user_rowid[keyx])
			extr=self.user_comments.get(keyx,-1)
			if extr==-1:
				print("not available")
			else:
				print(self.user_comments[keyx])
			#print(keyx,)
			ofile.write(keyx)
			count+=1
			if count==10:
				break;

ux=user_sim()
ux.control()
