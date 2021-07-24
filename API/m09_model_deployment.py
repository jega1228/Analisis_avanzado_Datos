#!/usr/bin/python

import pandas as pd
import pickle
import sys
import os

def predict_price(url):

    # clf =  pickle.load(open(os.path.dirname(__file__) + '/phishing_clf.pkl', 'rb'))
    # clf =  pickle.load(open(os.path.dirname(__file__) + '/API' +'/phishing_clf.pkl', 'rb'))
    # clf = pickle.load(open('./phishing_clf.pkl', 'rb'))
    clf = pickle.load(open('phishing_clf.pkl', 'rb'))

    url_ = pd.DataFrame([url], columns=['url'])
  
    # Create features
    """keywords = ['https', 'login', '.php', '.html', '@', 'sign']
    for keyword in keywords:
        url_['keyword_' + keyword] = url_.url.str.contains(keyword).astype(int)

    url_['lenght'] = url_.url.str.len() - 2
    domain = url_.url.str.split('/', expand=True).iloc[:, 2]
    url_['lenght_domain'] = domain.str.len()
    url_['isIP'] = (url_.url.str.replace('.', '') * 1).str.isnumeric().astype(int)
    url_['count_com'] = url_.url.str.count('com')"""

    # Make prediction
    p1 = clf.predict(url_)
    p1 = str(p1)

    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add an URL')
        
    else:

        url = sys.argv[1]

        p1 = predict_price(url)
        
        print(url)
        print('Price of Car: ', p1)
        