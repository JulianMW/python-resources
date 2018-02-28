import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib import cm as cm
#import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
import random
from sklearn.metrics import mean_squared_error

pd.set_option('max_columns', 1000) # forces pandas to display up to 100 columns in df.head()
pd.set_option('display.max_rows', 1000)


# Set up our search pattern
processorsIn = -1
nestt_list=[30,90]
maxff_list = [10,20]
maxdd_list = [10,55,75,95,105]
#minss = 4000
minss_list = [25,50,200,500,1000]
excelNm_list = ['ForestReg_1.xlsx','ForestReg_2.xlsx','ForestReg_3.xlsx']
samples_list = ['dev_Samples1.csv','dev_Samples2.csv','dev_Samples3.csv']





ii=0
for sample in samples_list:
        excelNm = excelNm_list[ii]   
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(excelNm, engine='xlsxwriter')    
        df = pd.read_csv(sample)
    df.drop(['id_var1','id_var2','month'], axis=1, inplace=True)    
    #replace missing values
    #df=df.replace({'var1': np.nan}, 'X')
        #create dummy variables
    #df = pd.concat([df, pd.get_dummies(df['GENDER']).rename(columns=lambda x: 'GEND_' + str(x))], axis=1)            #drop dummy originals
    #df.drop(['GENDER'], axis=1, inplace=True)            #df = df.fillna(df.mean())
    print("pre-drop length = " +str(len(df)))    
    #DROP NA ROWS
    df=df.dropna()
    print("post-drop length = " +str(len(df)))
    #df['TARGET'] = df['TARGET'] < 0  #convert to binary target
    xy_train, xy_test = train_test_split(df, test_size=0.30, random_state=42)
    x_train = xy_train.drop('TARGET', 1)
    x_test = xy_test.drop('TARGET', 1)
    y_train = xy_train['TARGET'].astype(int)   # keep only the target variable
    y_test = xy_test['TARGET'].astype(int)   # keep only the target variable

    scores_list = []
    indx=1
    for nestt in nestt_list:
        for maxff in maxff_list:
            for maxdd in maxdd_list:
                for minss in minss_list:
                    # Build a forest and compute the feature importances                    
                    forest = ExtraTreesRegressor(n_estimators=nestt,                                                  
                                                 max_features = maxff,                                                  
                                                 max_depth = maxdd,                                                  
                                                 min_samples_leaf = minss,                                                  
                                                 n_jobs = processorsIn,                                                  
                                                 random_state=int(random.random()*200))
                    forest.fit(x_train, y_train)

                    importances = forest.feature_importances_
                    indices = np.argsort(importances)[::-1]
                    #featureNames
                    feat_df = pd.DataFrame({'FeatureNm':x_train.columns})
                    feat_df['Importance'] = forest.feature_importances_
                    feat_df = pd.DataFrame(feat_df.sort_values(by='Importance', ascending=False))
                    print(feat_df[:20])
                    scoress = forest.score(x_test,y_test)
                    shtname = 'F' +str(indx) + 'e' +str(nestt) + '_' +str(maxff)+ '_' +str(maxdd) + '_' +str(minss) + '_' + str(len(x_train)) + '_' + str(int(scoress*1000))
                    print('Runparams:' + str(shtname))
                    print('Number of observations in set:' + str(len(x_train)))
                    print("Score: ", int(scoress*1000))

                    scores_list.append([indx,nestt,maxff,maxdd,minss,len(x_train),int(scoress*1000),mean_squared_error(y_test,forest.predict(x_test)),sample])
                    print('----------------------')
                    print('----------------------')
                    # Convert the dataframe to an XlsxWriter Excel object.
                    feat_df.to_excel(writer, sheet_name=shtname)

                    indx += 1
    score_df = pd.DataFrame(scores_list, columns = ['index','nest','maxfeatures','maxdepth','minss','obs','scores','rsqr','tableName'])    
    score_df.to_excel(writer, sheet_name='overview')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    ii+=1
