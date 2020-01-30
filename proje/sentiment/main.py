import sys,os
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from clearAdditional import DataCleaner
from instagram.get import GetComment

def Main():
    try:
        if(len(sys.argv[1])!= 11):
            print( "wrong short code")
            return


        #Veri setinin eklenip basliklarin belirlenmesi
        #column = ['yorum',"Positivity"]
        df = pd.read_csv('/var/www/html/proje/sentiment/yorumlarBirlesik.csv.cleaned',\
                         names=['rown','yorum','Positivity'], encoding ='iso-8859-9', sep=',')
        df = df.dropna()

        # verilerimizi yorum sutununu kullanarak egitim ve test olarak boluyoruz.
        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(df['yorum'], \
                                                            df['Positivity'],\
                                                            random_state = 1)

        #CountVectorizer'i baslatiyoruz ve egitim verilerimize uyguluyoruz.
        from sklearn.feature_extraction.text import CountVectorizer
        n_gram = 3 #veri setimizde bulunan kelimelerin 3'luye kadar gruplandiriyoruz
        vect = CountVectorizer(min_df = 5, ngram_range = (1,n_gram)).fit(X_train)
        X_train_vectorized = vect.transform(X_train)

        #Modelimizi olusturuyoruz
        model = LogisticRegression()
        #Modelimizi egitiyoruz
        model.fit(X_train_vectorized, y_train)
        predictions = model.predict(vect.transform(X_test))
        #print('AUC: ', roc_auc_score(y_test, predictions))

        feature_names = np.array(vect.get_feature_names())
        sorted_coef_index = model.coef_[0].argsort()
        #print('Negatif: \n{}\n'.format(feature_names[sorted_coef_index][:10]))
        #print('Pozitif Coef: \n{}\n'.format(feature_names[sorted_coef_index][:-11:-1]))

        #############
        ## Instagram comment getter
        #############
        #                   Bu parametre instagram gonderisinin shortcode'dudur.
        getter = GetComment(sys.argv[1])
        ############
        ##Data Cleaner
        ############
        cleaner = DataCleaner()

        count = 0
        positiveCount = 0
        while(True):
            comments = getter.getComments()
            if(comments == None):
                break
            for comment in comments:
                cleanedComment = cleaner.Clear(comment["node"]["text"])
                if(len(cleanedComment) == 0):
                        continue
                count += 1
                result = model.predict(vect.transform([cleanedComment]))
                positiveCount += result
        print("{} yorumdan:".format(count))
        if(count == 0):
            return
        print("Yuzde {0:.2f}% oraninda yorum pozitif.".format(float(positiveCount*100/count)))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e)

Main()
