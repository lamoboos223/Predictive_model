# from __future__ import print_function

import pymysql	
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression



conn = pymysql.connect('localhost', 'root', '', 'People')
conn.autocommit(True)
result = conn.cursor()

#insert to DB
# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('181', '80', '40', 'male') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('177', '70', '43', 'male') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('160','60','38', 'female') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('154', '54', '37', 'female') ;"
# result.execute(query)


# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('159', '50', '37', 'female') ;"
# result.execute(query)


# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('156', '49', '38', 'female') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('158', '50', '38', 'female') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('166', '65', '40' ,'male') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('170', '74', '41' ,'male') ;"
# result.execute(query)

# query = "INSERT INTO Person (Hieght, Wieght, Feet, Gender) VALUES ('177', '81', '44' ,'male') ;"
# result.execute(query)







# Retrieve from DB
query = "Select Hieght, Wieght, Feet from Person;"
result.execute(query)
data = result.fetchone()
People = []   
i=0 
while data is not None:
    # print data[0]
    # print data [1]
    # print data [2]
    People.append([])
    People[i].append(data[0])
    People[i].append(data[1])
    People[i].append(data[2])
    i = i+1
    data = result.fetchone()


print(People)
# for i in range(10): # create a list with nested lists
#     People.append([])
#     People[i].append(data[i]) # fills nested lists with data
# print People


# Retrieve from DB
query2 = "Select Gender from Person;"
result.execute(query2)
data2 = result.fetchone()
Gender = []
while data2 is not None:
    # print data2[0]
    Gender.append(data2[0])
    data2 = result.fetchone()
print(Gender)






print("======================")
print("======================")
print("======================")
print("======================")
print("======================")


New_Person = [[165, 68, 39]]

classifier1 = tree.DecisionTreeClassifier()
classifier1 = classifier1.fit(People, Gender)
prediction1 = classifier1.predict(New_Person)
print("Decision Tree Classifier says:",prediction1)


classifier2 = RandomForestClassifier()
classifier2 = classifier2.fit(People, Gender)
prediction2 = classifier2.predict(New_Person)
print("\n\nRandom Forest Classifier says:",prediction2)


classifier3 = LogisticRegression()
classifier3 = classifier3.fit(People, Gender)
prediction3 = classifier3.predict(New_Person)
print("\n\nLogistic Regression Classifier says:",prediction3)

print("Done.")









# conn.commit()
conn.close()