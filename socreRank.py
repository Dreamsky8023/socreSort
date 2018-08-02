#!/usr/bin/env python
#-*- coding:utf-8
import xlrd
import copy
print("开始读取......")
book=xlrd.open_workbook('竞赛成绩排名.xlsx')
sheet=book.sheet_by_name('Sheet1')
print(sheet.ncols)
cols1=sheet.col_values(2)
cols2=sheet.col_values(4)
cols3=sheet.col_values(6)
cols4=sheet.col_values(8)
cols5=sheet.col_values(10)

ls1=[]
for i,ch in enumerate(cols4):
	if(i>1 and ch!=''):
		ls1.append(ch)
		print(i,ch)
ls = copy.deepcopy(ls1)
print("----------")
print(ls1)
for i in range(len(ls1)-1):
	for j in range(len(ls1)-i-1):
		if ls1[j]<ls1[j+1]:
			temp=ls1[j]
			ls1[j]=ls1[j+1]
			ls1[j+1]=temp
print("===============")
print(ls1)
print(ls)
c=[]
cj=[]
m=0
yt=[0 for i in range(len(ls1))]
for i in range(len(ls1)):
	for j in range(len(ls1)):
		if ls1[i]==ls[j]:
			if j not in c:
				c.append(j)
				cj.append(j)
				print(j,ls[j])
				print("haha")
				qq=len(cj)
				print(qq)
				print(cj[qq-1])
				if(qq-2>=0):
					if(ls[cj[qq-1]]==ls[cj[qq-2]]):
						m+=0
						yt[j]=m
					elif ls[cj[qq-1]]!=ls[cj[qq-2]]:
						m+=1
						yt[j]=m
						
print(yt)
mm=[0 for i in range(len(yt))]
for i in range(len(yt)):
	mm[i]=yt[i]+1
print(mm)
a=file('result.txt','w')
for k in mm:
	a.write(str(k)+"\n")
a.close() 
