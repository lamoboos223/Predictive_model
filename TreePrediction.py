from sklearn import tree

x = [[181, 80, 40], [177, 70, 43], [160,60,38], [154, 54, 37], [159, 50, 37], [156, 49, 38], [158, 50, 38], [166, 65, 40], [170, 74, 41], [177, 81, 44]]
y = ["male","male","fmale","fmale","fmale","fmale","fmale","male","male","male"]

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(x, y)


prediction = classifier.predict([[180, 40, 39]])

print prediction