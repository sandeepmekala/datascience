from sklearn import tree

X = [	[1,10,120],
		[1,12,150],
		[0,3,100],
		[0,15,150],
		[1,4,90],
		[1,11,130],
		[1,12,160],
		[0,4,100],
		[0,14,140], 
		[1,5,80]
	]

Y = ['yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 
	'yes', 'no']

clf = tree.DecisionTreeClassifier()

clf.fit(X,Y)

prediction = clf.predict([[1,6,70], [0,12,150]])

print (prediction)
