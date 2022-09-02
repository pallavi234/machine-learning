#!/usr/bin/env python
# coding: utf-8

# In[1]:


#statistics module. It provides some functions for calculating basic statistics on data like mean, median
import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort() function to sort the list and min(),max() to find minimum and maximum values of list respectively.
ages.sort()
print("Sorted ages: ", ages)
print("Minimum value of ages: ", min(ages))
print("Maximum value of ages: ", max(ages))
# insert(position, value) - inserts the value in list at specified position
ages.insert(0,min(ages))
# append(value) - appends the value at the end of list
ages.append(max(ages))
print("List after update: ", ages)
#The biggest advantage of using median() function is that the data-list does not need to be sorted 
#before being sent as parameter to the median() function using statistice module
print("Median of ages: ", statistics.median(ages))
print("Average of ages: ", statistics.mean(ages))
print("Range of ages: ", max(ages)-min(ages))

# we can also use below code to find median and average of listed data
# ages_length = len(ages)
# if ages_length/2 != 0:
#     print('Median of ages: ', ages[int(ages_length/2)])
# else:
#     print('Median of ages: ', ages[ages_length-1/2]+ages[ages_length+1/2])   
# print('Average of ages: ', sum(ages)/ages_length)


# In[2]:


dog= dict()
#update() method inserts the specified dictionary  or any key-value pairs to the resp. dictionary
dog.update({"name":"Pinky", "color":"White", "breed":"Pug", "legs":4, "age":1})
print("Added key-value pair to dog: ",dog)

#used  dict() function which creates a empty dictionary
student_dict = dict()
keyList = ["first_name", "last_name", "gender","age","marital status","skills","country","city","address"]
#added only keys to the dictionary with None value using update method
student_dict.update({key: None for key in keyList})
print("\nStudent_Dictionary after adding keys: ",student_dict)

#utilised len(dictionary) function to calculate lenght
print("Length of Student_Dictionary: ", len(student_dict))
#updated student_dict with sample values
student_dict.update({"first_name": "Pallavi", "last_name": "Meher", "gender": "Female", "age": "21", "marital status": "Single", "skills": ["C++","Python"], "country": "India", "city": "Nagpur",
  "address": "2w Broad Street"})
print("\nStudent_dict ", student_dict)
#accessing paritcular value of key in dict: dict["key"]
print("\nAccessing Skills value in dictionary: ",student_dict["skills"])
#type(value) - function gives the datatype of provided values
print("Data Type of Skills in Student Dict: ", type(student_dict["skills"]))

#The extend() adds all the elements of an iterable (list, tuple, string etc.) to the end of the list
student_dict["skills"].extend(["Apex", "JavaScript"])
print("Updated Skills list after adding new values: ", student_dict["skills"])

# dict.keys() and values() gives the list of keys and values as a list respectively
print("\n",student_dict.keys())
print(student_dict.values())


# In[3]:


sisters = ("Priyanka","Ruchita")
print("Sisters: ", sisters,)
brothers = ("Ritesh","Reyansh","Jevan")
print("Brothers: ", brothers)
siblings = sisters+brothers
print("siblings: ",siblings)
print("Number of Siblings:", len(siblings))
family_members = siblings+("Sushant","Sujatha")
print("family_members: ", family_members)


# In[4]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
a = len(it_companies)
print(a)
#2
it_companies.add('Twitter')
print(it_companies)
#3.
new_companies = ['wipro','Panasonic','Intel']
it_companies.update(new_companies)
print(new_companies)

#4.
it_companies.remove('Facebook')
print(it_companies)

#5.The discard() method removes the specified item from the set. This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

#6.
c=B.union(A)
print(c)

#7.
d=A.intersection(B)
print(d)

#8
print(A.issubset(B))

#9.
print(A.isdisjoint(B))

#10.
joined_1 = A.union(B)
joined_2 = B.union(A)

#11.
sym_diff = A.symmetric_difference(B)

#12.
A.clear()
B.clear()

#13.
Ages_Set = set(age)


# In[5]:


from math import pi
radius_of_circle = 30
_area_of_circle_ = pi * radius_of_circle **2
print("Area of a circle = ",_area_of_circle_," meters square")
_circum_of_circle_ = 2 * pi * radius_of_circle
print("Circumference of a circle = ",_circum_of_circle_, ' meters')

_radius_of_circle_ = float(input("Enter radius of circle: "))
_area_of_circle_ = pi * _radius_of_circle_ **2
print("Area of a circle = ",_area_of_circle_," meters square")


# In[6]:


print("I am a teacher and I love to inspire and teach people")
set_words = set(("I am a teacher and I love to inspire and teach people".split(" ")))
print("Number of Unique words: ",len(set_words), set_words)


# In[7]:


text = "\033[1m Name \t  Age \tCountry City\n Asabench 250 \tFinland Helsinki\033[0m"
print(text)


# In[8]:


radius = 10 
area = 3.14 * radius ** 2 
# using 'f' we can format the data. %.0f will give data without any decimals, %.2f displays until 2 decimals
print("The area of a circle with radius",radius,"is %.0f" %area, "meters square.")


# In[9]:


#1lb = 0.453592kg
no_of_students = int(input("Enter number of students: "))
weight_of_students_lbs = list() #to store weights in lbs
weight_of_students_kgs = list() # to store weights in kgs

for each in range(no_of_students):
    weight_lb = int(input("Enter weight of {} student in lbs: ".format(each+1)))
    weight_of_students_lbs.insert(each, weight_lb)
    #converting lbs to kg and adding to seperate list
    weight_kg = float("%.2f" %(weight_lb*0.453592))
    weight_of_students_kgs.insert(each, weight_kg)
    
print("weight of students in lbs: ",weight_of_students_lbs)
print("weight of students in kgs: ",weight_of_students_kgs)


# 

# In[10]:


import numpy as nm   
import pandas as pd 
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix 

X= nm.array([[1,0],[2,0],[3,0],[6,0],[6,0],[7,0],[10,0],[11,0]])
print("Dataset with total 8 points: \n",X,"\n Size: ",len(X))
y = nm.array([0,0,1,1,1,0,0,0])
print("\nClass label for the datasetX  Y:",y)
x_train, x_test, y_train, y_test= train_test_split(X, y, test_size= 0.50, random_state=0,shuffle=False ) 
print("\nTraining Data X: \n", x_train)
print("\nTraining Data label Y:", y_train)

#feature Scaling-used to normalize the range of independent variables or features of data. .
#i.e.to standardize the data prior to performing classification 
stand_scalar= StandardScaler()    
x_train= stand_scalar.fit_transform(x_train)    
x_test= stand_scalar.transform(x_test) 

#Initialising KNN Classifier with value 3
classifier= KNeighborsClassifier(n_neighbors=3)  
#Fitting the data to classifier
classifier.fit(x_train, y_train)
#Predict Labels for x-test data
y_pred= classifier.predict(x_test) 
print('\nPredicted Classs labels for testing data Y:',y_pred)
     
#Confusion matrix with tested data
confusion_matrix_result = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix\n",confusion_matrix_result)

#total P+N can be calculated using sum(sum(conf_matrix))
total_value = sum(sum(confusion_matrix_result))
#Accuracy TN+TP / P+N
accuracy=(confusion_matrix_result[0,0]+confusion_matrix_result[1,1])/total_value
print ('\nAccuracy : ', accuracy)

#Sensitivity TP/(TP+FN)
sensitivity = confusion_matrix_result[1,1]/(confusion_matrix_result[1,0]+confusion_matrix_result[1,1])
print('Sensitivity : ', sensitivity )

#Specificity TN/(TN+FP)
specificity = confusion_matrix_result[0,0]/(confusion_matrix_result[0,0]+confusion_matrix_result[0,1])
print('Specificity : ', specificity)


# In[ ]:




