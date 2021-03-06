# -*- coding: utf-8 -*-
"""project01(shapeai).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s2qYCMwnrwGfIbf-B-6JBexj5LqFDP52
"""



# Import pandas package
import pandas as pd

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj','Ram','Nitika','Ragini','Ruchir','Labhanshi',],
		'Age':[27, 24, 22, 32, 45, 23, 65, 47, 68,],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj','Nagpur','Sagar','Indore','Mumbai','Chenni',],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd','PGDCA','MDSC','DBMC','B.ARCH','M.ARCH'],
    'Employed':['Yes','Yes','Yes','Yes','No','No','Yes','Yes','Yes'],
    'Gender':['Male','Female','Male','Male','Male','Female','Female','Male','Female'],
    'University':['UOD','UOK','DAVV','LPU','JNU','AMITY','VIT','GGSIU','NIRMA'],
    'Covid Tested':['ON MONDAY','ON SATURDAY','STILL NOT TESTED','ON FRIDAY','ON TUESDAY','NO INFORMATION','ON WEDNESDAY','ON 25TH JUNE','ON SUNDAY'],
    'Vaccinated':['Partially vaccinated','Partially vaccinated','Not vaccinated','Partially vaccinated','Fully vaccinated','Fully vaccinated','Fully vaccinated','Fully vaccinated','Fully vaccinated']}

df = pd.DataFrame(data)
print(df[['Name','Age','Address', 'Qualification','Employed','Gender','Covid Tested',]])