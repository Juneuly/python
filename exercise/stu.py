stu=[]

info=[]
n=0
while True:
	print("1.Insert 2.List 3.Change 4.Delete 5.Quit 6.sort")
	q = input()
	if q=='1':
		n=len(info)
		info.append({'num':'0','name':'0','sex':'0','English':'0','Math':'0','Chinese':'0'})
		print('please input student\'s number:')
		info[n]['num']=input()
		print('please input student\'s name:')
		info[n]['name']=input()
		print('please input student\'s sex:')
		info[n]['sex']=input()
		print('please input student\'s English:')
		info[n]['English']=input()
		print('please input student\'s Math:')
		info[n]['Math']=input()
		print('please input student\'s Chinese:')
		info[n]['Chinese']=input()
		stu_temp=[]
		stu_temp.append(info[n])
		stu=stu+stu_temp
	if q=='2':
		for i in range(0,len(stu)):
			print(stu[i]['num'],end = ' ')
			print(stu[i]['name'],end = ' ')
			print(stu[i]['sex'],end = ' ')
			print(stu[i]['English'],end = ' ')
			print(stu[i]['Math'],end = ' ')
			print(stu[i]['Chinese'])
	if q=='3':
		print('please input the student\'s num you wannna change:')
		num_temp = input()
		i=0
		for i in range(0,len(stu)):
			if stu[i]['num']==num_temp:
				break
		stu_temp=[]
		stu_temp.append({'num':'0','name':'0','sex':'0','English':'0','Math':'0','Chinese':'0'})
		print('please input student\'s number:')
		stu_temp[0]['num']=input()
		print('please input student\'s name:')
		stu_temp[0]['name']=input()
		print('please input student\'s sex:')
		stu_temp[0]['sex']=input()
		print('please input student\'s English Grade:')
		stu_temp[0]['English']=input()
		print('please input student\'s Math Grade:')
		stu_temp[0]['Math']=input()
		print('please input student\'s Chinese Grade:')
		stu_temp[0]['Chinese']=input()
		stu[i]=stu_temp[0]
	if q=='4':
		print('please input the student\'s num you wanna delete:')
		num_temp = input() 
		i=0
		for i in range(0,len(stu)):
			if stu[i]['num']==num_temp:
				break
		del stu[i]
	if q=='5':
		break
	if q=='6':
		print('please input the item you wanna sort:1.number 2.name 3.sex 4.English Grade 5.Math Grade 6.Chinese Grade')
		item_temp=input()
		if item_temp=='1':
			stu.sort(key=lambda x:(x['num']))
		if item_temp=='2':
			stu.sort(key=lambda x:(x['name']))
		if item_temp=='3':
			stu.sort(key=lambda x:(x['sex']))
		if item_temp=='4':
			stu.sort(key=lambda x:(x['English']))
		if item_temp=='5':
			stu.sort(key=lambda x:(x['Math']))
		if item_temp=='6':
			stu.sort(key=lambda x:(x['Chinese']))

