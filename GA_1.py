from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np


df = pd.read_csv('MAGIC Gamma Telescope Data.csv')

shuffle=df.iloc[np.random.permutation(len(df))]
df1=shuffle.reset_index(drop=True)

df1['Class']=df1['Class'].map({'g':0, 'h':1})
df_class = df1['Class'].values

training_indices, validation_indices = training_indices, testing_indices = train_test_split(df1.index,
	stratify= df_class, train_size=0.75, test_size=0.25)

tpot = TPOTClassifier(generations=5, verbosity=2)
tpot.fit(tele.drop('Class', axis=1).loc[training_indices].values,
	df1.loc[training_indicss, 'Class'].values)

tpot.score(df1.drop('Class', axis=1).loc[validation_indices].values,
	df1.loc[validation_indices, 'Class'].values)

tpot.export('pipeline.py')