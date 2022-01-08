import pandas as pd
from itertools import combinations

def ord_comb(l,n):
    return list(combinations(l,n))

#####Read the 12 specified attributes from the csv file####
csv = pd.read_csv('ticdata.csv',usecols=[46,47,48,0,1,2,3,4,5,6,7,8],header = None)

min_support = float(input("Enter support : "))
min_conf = float(input("Enter confidence : "))
print ("")

input_firstitemset = []
support = {}
desc = {}
count = []

for i in range(12):
    input_firstitemset.append([])

for i in range(12):
    count.append([])

data=[[0 for x in range(12)] for y in range(5822)]

####Replacing Xno.colno.Y with it's name to be displayed in the association rule####
for i in range (12):
	for j in range (5822):
		data[j][i] = str(csv.values[j,i]) + 'col' + str(i+1)

		if (i == 0):
			if (csv.values[j,i] == 1):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(High Income, expensive child)"
			elif (csv.values[j,i] == 2):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Very Important Provincials)"
			elif (csv.values[j,i] == 3):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(High status seniors)"
			elif (csv.values[j,i] == 4):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Affluent senior apartments)"
			elif (csv.values[j,i] == 5):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Mixed seniors)"
			elif (csv.values[j,i] == 6):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Career and childcare)"
			elif (csv.values[j,i] == 7):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Dinki's (double income no kids))"
			elif (csv.values[j,i] == 8):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Middle class families)"
			elif (csv.values[j,i] == 9):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Modern, complete families)"
			elif (csv.values[j,i] == 10):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Stable family)"
			elif (csv.values[j,i] == 11):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Family starters)"
			elif (csv.values[j,i] == 12):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Affluent young families)"
			elif (csv.values[j,i] == 13):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Young all american family)"
			elif (csv.values[j,i] == 14):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Junior cosmopolitan)"
			elif (csv.values[j,i] == 15):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Senior cosmopolitans)"
			elif (csv.values[j,i] == 16):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Students in apartments)"
			elif (csv.values[j,i] == 17):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Fresh masters in the city)"
			elif (csv.values[j,i] == 18):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Single youth)"
			elif (csv.values[j,i] == 19):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Suburban youth)"
			elif (csv.values[j,i] == 20):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Etnically diverse)"
			elif (csv.values[j,i] == 21):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Young urban have-nots)"
			elif (csv.values[j,i] == 22):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Mixed apartment dwellers)"
			elif (csv.values[j,i] == 23):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Young and rising)"
			elif (csv.values[j,i] == 24):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Young, low educated)"
			elif (csv.values[j,i] == 25):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Young seniors in the city)"
			elif (csv.values[j,i] == 26):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Own home elderly)"
			elif (csv.values[j,i] == 27):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Seniors in apartments)"
			elif (csv.values[j,i] == 28):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Residential elderly)"
			elif (csv.values[j,i] == 29):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Porchless seniors: no front yard)"
			elif (csv.values[j,i] == 30):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Religious elderly singles)"
			elif (csv.values[j,i] == 31):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Low income catholics)"
			elif (csv.values[j,i] == 32):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Mixed seniors)"
			elif (csv.values[j,i] == 33):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Lower class large families)"
			elif (csv.values[j,i] == 34):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Large family, employed child)"
			elif (csv.values[j,i] == 35):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Village families)"
			elif (csv.values[j,i] == 36):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Couples with teens 'Married with children')"
			elif (csv.values[j,i] == 37):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Mixed small town dwellers)"
			elif (csv.values[j,i] == 38):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Traditional families)"
			elif (csv.values[j,i] == 39):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Large religous families)"
			elif (csv.values[j,i] == 40):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Large family farms)"
			elif (csv.values[j,i] == 41):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSTYPE Customer Subtype(Mixed rurals)"

		elif (i == 1):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MAANTHUI Number of houses " + str(csv.values[j,i])

		elif (i == 2):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMOMV Avg size household " + str(csv.values[j,i])

		elif (i == 3):
			if (csv.values[j,i] == 1):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMLEEF Avg age (20-30 years)"
			elif (csv.values[j,i] == 2):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMLEEF Avg age (30-40 years)"
			elif (csv.values[j,i] == 3):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMLEEF Avg age (40-50 years)"
			elif (csv.values[j,i] == 4):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMLEEF Avg age (50-60 years)"
			elif (csv.values[j,i] == 5):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMLEEF Avg age (60-70 years)"
			elif (csv.values[j,i] == 6):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGEMLEEF Avg age (70-80 years)"

		elif (i == 4):
			if (csv.values[j,i] == 1):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Successful hedonists)"
			elif (csv.values[j,i] == 2):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Driven Growers)"
			elif (csv.values[j,i] == 3):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Average Family)"
			elif (csv.values[j,i] == 4):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Career Loners)"
			elif (csv.values[j,i] == 5):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Living well)"
			elif (csv.values[j,i] == 6):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Cruising Seniors)"
			elif (csv.values[j,i] == 7):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Retired and Religeous)"
			elif (csv.values[j,i] == 8):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Family with grown ups)"
			elif (csv.values[j,i] == 9):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Conservative families)"
			elif (csv.values[j,i] == 10):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MOSHOOFD Customer main type(Farmers)"

		elif (i == 5):
			if (csv.values[j,i] == 0):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (0%)"
			elif (csv.values[j,i] == 1):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (1 - 10%)"
			elif (csv.values[j,i] == 2):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (11 - 23%)"
			elif (csv.values[j,i] == 3):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (24 - 36%)"
			elif (csv.values[j,i] == 4):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (37 - 49%)"
			elif (csv.values[j,i] == 5):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (50 - 62%)"
			elif (csv.values[j,i] == 6):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (63 - 75%)"
			elif (csv.values[j,i] == 7):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (76 - 88%)"
			elif (csv.values[j,i] == 8):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (89 - 99%)"
			elif (csv.values[j,i] == 9):
				desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODRK Roman catholic (100%)"

		elif (i == 6):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODPR Protestant " + str(csv.values[j,i]) 

		elif (i == 7):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODOV Other religion " + str(csv.values[j,i])

		elif (i == 8):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="MGODGE No religion " + str(csv.values[j,i])

		elif (i == 9):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="AWAPART Number of private third party insurance " + str(csv.values[j,i])

		elif (i == 10):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="APERSAUT Number of car policies " + str(csv.values[j,i])

		elif (i == 11):
			desc[str(csv.values[j,i]) + 'col' + str(i+1)]="ABRAND Number of fire policies " + str(csv.values[j,i])


notrepeated_item = 0
csv = 0
m = 0

###Generating first itemset by finding the unique numbers in each column and considering them an independant item then counting each item's no. of occurences to get support(occurences/5822)###
###If support of any item is equal to greater than min. support then append it to "firstitems" list 
#"count" list contains the number of occurences of each item
#item format example: '2col3' where 2 is a number in the 3rd col.
firstitems = []
for j in range (12):
	for i in range (5822):
		for x in range(len(input_firstitemset[j])):
			if data[i][j] == input_firstitemset[j][x]:
				notrepeated_item = 1
				m = x

		if notrepeated_item == 0:
			input_firstitemset[j].append(data[i][j])
			count[j].append(1)
		else :
			count[j][m]=count[j][m] + 1 
			notrepeated_item = 0

	if j != 0:
		for v in range(len(input_firstitemset[j-1])):
			if ((count[j-1][v]/5822) >=min_support):
				support["('"+str(input_firstitemset[j-1][v])+"')"]=count[j-1][v]
				firstitems.append(input_firstitemset[j-1][v])

for v in range(len(input_firstitemset[11])):
				if ((count[11][v]/5822)>=min_support):
					firstitems.append(input_firstitemset[11][v])
					support["('"+str(input_firstitemset[11][v])+"')"]=count[11][v]

stop=0
it=2
newitemsets2_old = firstitems
count_it = 0
repeated_no_of_col = 1

####Generating nth-itemsets where n>=2; each (n+1)itemset is generated from what is left from the (n)itemset#### 
while (stop == 0 ):
	#ord_comb: generate all possible combinations from the first itemset list of length "it"
	itemsets=ord_comb(firstitems,it)
	repeated_no_of_col = 1
	newitemsets = []
	newitemsets2 = []
	Count_item = 0

	for x in range(len(itemsets)):
		repeated_no_of_col = 1
		for y1 in range(len(itemsets[x])-1):
		    for y2 in range(y1 + 1,len(itemsets[x])):
		    	if (itemsets[x][y1][-1]==itemsets[x][y2][-1] and itemsets[x][y1][-2]==itemsets[x][y2][-2]):
		    		repeated_no_of_col = 0
		    		break

		    if repeated_no_of_col == 0:
		    	break

		if repeated_no_of_col == 1:
			newitemsets.append(itemsets[x])
			first_item = newitemsets[len(newitemsets)-1][0]
			index = first_item.find('l')
			col_num = first_item[index + 1 :: ]
			found = 1
			found2 = 0
			Count_item = 0

			for r in range (5822):
				index = first_item.find('l')
				col_num = first_item[index + 1 :: ]
				if (data[r][int(col_num)-1] == first_item):
					found2 = 1

					for y2 in range(1,len(newitemsets[len(newitemsets)-1])):
						next_item = newitemsets[len(newitemsets)-1][y2]
						index = next_item.find('l')
						col_num = next_item[index + 1 :: ]
						if not(data[r][int(col_num)-1] == next_item):
							found = 0
							break

				if found == 1 and found2 == 1:
					Count_item = Count_item + 1
				else:
					found = 1
				found2 = 0

			####Stoping condition: if the current itemset is empty(all its elements' supports are less than the min.) 
			#then the newitemsets2 will contain the elements of the previous itemset from which we will generate 
			#the rules and break from the while loop####
			if ((Count_item/5822) >= min_support):
				support[str(newitemsets[len(newitemsets)-1])]=Count_item
				newitemsets2.append(newitemsets[len(newitemsets)-1])

	if (len(newitemsets2) == 0):
		stop = 1
		newitemsets2 = newitemsets2_old
	else:
		newitemsets2_old = newitemsets2
		it = it + 1
		count_it = 1

rules = []
left = []
new = []
repeated_item = 0
flag = 0

####Association rules generation: if conf. of rule> min. conf. then calculate it's lift and leverage and print them####
if count_it != 0:
	rule_number = 1
	for g in range(len(newitemsets2)):
		rules=[]
		left = []
		for x in range (1,len(newitemsets2[g])):
			rules=ord_comb(newitemsets2[g],x)
			left.append(rules)
		for i in range(len(left)):
			for j in range(len(left)):  
				for k in range(len(left[i])):
					for m in range (len(left[j])):
						repeated_item = 0
						flag = 0
						if (len(left[i][k])+len(left[j][m]))==len(newitemsets2[g]):
							flag = 1
							for n in range (len(left[i][k])):
								if repeated_item == 1:
									break
								for x in range (len(left[j][m])):
									if (left[i][k][n]==left[j][m][x]):
										repeated_item = 1
										break

						if repeated_item == 0 and flag == 1:
							leftt = str(left[i][k])
							rightt = str(left[j][m])

							if (len(left[i][k]))==1:
								first_item=str(left[i][k])
								index = first_item.find(',')
								leftt = first_item[0 : index ] + first_item[index + 1 :: ]
								key = left[i][k][0]

							if (len(left[j][m]))==1:
								first_item=str(left[j][m])
								index = first_item.find(',')
								rightt = first_item[0 : index ] + first_item[index + 1 :: ]
								
							if ((support[str(newitemsets2[g])]/support[leftt]) >= min_conf):
								print ("-------" + str(rule_number) + "-------")
								rule_number = rule_number + 1
								print(leftt+"=>"+rightt) 
								
								left_rule ="{"
								for z in range (len(left[i][k])):
									left_rule = left_rule + desc[str(left[i][k][z])]
									if len(left[i][k]) - z != 1:
										left_rule = left_rule + ', '

								left_rule = left_rule + "} => {"

								for v in range (len(left[j][m])):
									left_rule = left_rule + desc[str(left[j][m][v])]
									if len(left[j][m]) - v != 1:
										left_rule = left_rule + ', '

								left_rule = left_rule + "}"
								print (left_rule)
								print ('Lift :' , (support[str(newitemsets2[g])]/5822)/((support[leftt]/5822) * (support[rightt]/5822)))
								print ('Leverage :' , (support[str(newitemsets2[g])]/5822) - ((support[leftt]/5822) * (support[rightt]/5822)))
								print ("")
else:
	print("")
	print ("No rules found")