# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets


import pandas as pd
from urllib.parse import urlparse,urlencode
import ipaddress
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime
import requests
import whois
import urllib
import urllib.request
import xlsxwriter
import pickle
from xgboost import XGBClassifier
import xgboost as xg
from itertools import chain
import csv



class Ui_MainDetectPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 700, 81))
        self.label.setStyleSheet("font: 24pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 951, 601))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ss4.png"))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 210, 391, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 175, 131, 21))
        self.label_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 280, 211, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 10pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.UrlfeatureExtraction);
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 400, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 24pt \"Algerian\";")
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "    PHISHING WEBSITE DETECTION"))
        self.pushButton.setText(_translate("MainWindow", "DETECT"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Enter URL"))

    

    # 1.Domain of the URL (Domain)
    def getDomain(self,url):
        domain = urlparse(url).netloc
        if re.match(r"^www.", domain):
            domain = domain.replace("www.", "")
        return domain

    # 2.Checks for IP address in URL (Have_IP)
    def havingIP(self,url):
        try:
            ipaddress.ip_address(url)
            ip = 1
        except:
            ip = 0
        return ip

    # 3.Checks the presence of @ in URL (Have_At)
    def haveAtSign(self,url):
        if "@" in url:
            at = 1
        else:
            at = 0
        return at

    # 4.Finding the length of URL and categorizing (URL_Length)
    def getLength(self,url):
        if len(url) < 54:
            length = 0
        else:
            length = 1
        return length

    # 5.Gives number of '/' in URL (URL_Depth)
    def getDepth(self,url):
        s = urlparse(url).path.split('/')
        depth = 0
        for j in range(len(s)):
            if len(s[j]) != 0:
                depth = depth + 1
        return depth

    # 6.Checking for redirection '//' in the url (Redirection)
    def redirection(self,url):
        pos = url.rfind('//')
        if pos > 6:
            if pos > 7:
                return 1
            else:
                return 0
        else:
            return 0


    # 7.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)
    def httpDomain(self,url):
        domain = urlparse(url).netloc
        if 'https' in domain:
            return 1
        else:
            return 0

    # listing shortening services
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                        r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                        r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                        r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                        r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                        r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                        r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                        r"tr\.im|link\.zip\.net"


    # 8. Checking for Shortening Services in URL (Tiny_URL)
    def tinyURL(self,url):
        match = re.search(self.shortening_services, url)
        if match:
            return 1
        else:
            return 0


    # 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
    def prefixSuffix(self,url):
        if '-' in urlparse(url).netloc:
            return 1  # phishing
        else:
            return 0  # legitimate


    def get_ipython(self):
        pass
        self.get_ipython().system('pip install python-whois')


    # 12.Web traffic (Web_Traffic)
    def web_traffic(self,url):
        try:
            # Filling the whitespaces in the URL if any
            url = urllib.parse.quote(url)
            rank = \
                BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(),
                            "xml").find(
                    "REACH")['RANK']
            rank = int(rank)
        except TypeError:
            return 1
        if rank < 100000:
            return 1
        else:
            return 0

    # 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
    def domainAge(self,domain_name):
        creation_date = domain_name.creation_date
        expiration_date = domain_name.expiration_date
        if (isinstance(creation_date, str) or isinstance(expiration_date, str)):
            try:
                creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
                expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
            except:
                return 1
        if ((expiration_date is None) or (creation_date is None)):
            return 1
        elif ((type(expiration_date) is list) or (type(creation_date) is list)):
            return 1
        else:
            ageofdomain = abs((expiration_date - creation_date).days)
            if ((ageofdomain / 30) < 6):
                age = 1
            else:
                age = 0
        return age

    # 14.End time of domain: The difference between termination time and current time (Domain_End)
    def domainEnd(self,domain_name):
        expiration_date = domain_name.expiration_date
        if isinstance(expiration_date, str):
            try:
                expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
            except:
                return 1
        if (expiration_date is None):
            return 1
        elif (type(expiration_date) is list):
            return 1
        else:
            today = datetime.now()
            end = abs((expiration_date - today).days)
            if ((end / 30) < 6):
                end = 1
            else:
                end = 0
        return end

    # 15. IFrame Redirection (iFrame)
    def iframe(self,response):
        if response == "":
            return 1
        else:
            if re.findall(r"[<iframe>|<frameBorder>]", response.text):
                return 0
            else:
                return 1

    # 16.Checks the effect of mouse over on status bar (Mouse_Over)
    def mouseOver(self,response):
        if response == "":
            return 1
        else:
            if re.findall("<script>.+onmouseover.+</script>", response.text):
                return 1
            else:
                return 0

    # 17.Checks the status of the right click attribute (Right_Click)
    def rightClick(self,response):
        if response == "":
            return 1
        else:
            if re.findall(r"event.button ?== ?2", response.text):
                return 0
            else:
                return 1


    # 18.Checks the number of forwardings (Web_Forwards)
    def forwarding(self,response):
        if response == "":
            return 1
        else:
            if len(response.history) <= 2:
                return 0
            else:
                return 1

    # Function to extract features
    # There are 16 features extracted from the dataset
    def featureExtractions(self,url):
        self.getDomain(url)
        features=[]
        features = [self.havingIP(url), self.haveAtSign(url),self.getLength(url),self.getDepth(url),self.redirection(url),
                    self.httpDomain(url),self.tinyURL(url),self.prefixSuffix(url)]
        # Address bar based features (9)

        # Domain based features (4)
        dns = 0
        try:
            domain_name = whois.whois(urlparse(url).netloc)
        except:
            dns = 1

        features.append(dns)
        features.append(self.web_traffic(url))
        features.append(1 if dns == 1 else self.domainAge(domain_name))
        features.append(1 if dns == 1 else self.domainEnd(domain_name))

        # HTML & Javascript based features (4)
        try:
            response = requests.get(url)
        except:
            response = ""
        features.append(self.iframe(response))
        features.append(self.mouseOver(response))
        features.append(self.rightClick(response))
        features.append(self.forwarding(response))
        # label=0
        # features.append(label)

        book = xlsxwriter.Workbook('Extracted_data.xlsx')     
        sheet1 = book.add_worksheet()
            
        feature_names = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                    'https_Domain', 'TinyURL','Prefix/Suffix', 'DNS_Record','Web_Traffic', 'Domain_Age', 'Domain_End',
                    'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards']
            
        row = 0    
        column = 0 

        for item in feature_names :     
                # write operation perform     
            sheet1.write(row, column, item)      
            # incrementing the value of row by one with each iterations.     
            column += 1

        row = 1    
        column = 0

        for item in features :     
                # write operation perform     
            sheet1.write(row, column, item)      
                # incrementing the value of row by one with each iterations.     
            column += 1

        book.close()
        return features 

    def searchinBacklistCsv(self,url):
        csvdata=[]
        with open("abc.csv") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                csvdata.append(row)
        col=[x[0] for x in csvdata]
        if url in col:
            for x in range(0,len(csvdata)):
                if(url==csvdata[x][0]):
                    return 1;
        else:
            return 0;
    
    def searchinWhitelistCsv(self,url):
        csvdata2=[]
        with open("Legitimatesites.csv") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                csvdata2.append(row)
        col=[x[0] for x in csvdata2]
        if url in col:
            for x in range(0,len(csvdata2)):
                if(url==csvdata2[x][0]):
                    return 1;
        else:
            return 0;
        

    def UrlfeatureExtraction(self):
        url = self.textEdit.toPlainText()
        data=[]
        label=0
        ans=self.searchinBacklistCsv(url);
        ans2=self.searchinWhitelistCsv(url)
        if ans!=1 and ans2!=1:
            data=self.featureExtractions(url)
            # data.pop()
            XGmodel = pickle.load(open('XGBoostClassifiernew.pkl', 'rb'))
            # cols_when_model_builds = XGmodel.get_booster().feature_names
            print(data)
            series = {'Have_IP': [data[0]],
            'Have_At': [data[1]],
            'URL_Length': [data[2]],
            'URL_Depth': [data[3]],
            'Redirection': [data[4]],
            'https_Domain': [data[5]],
            'TinyURL': [data[6]],
            'Prefix/Suffix': [data[7]],
            'DNS_Record': [data[8]],
            'Web_Traffic': [data[9]],
            'Domain_Age': [data[10]],
            'Domain_End': [data[11]],
            'iFrame': [data[12]],
            'Mouse_Over': [data[13]],
            'Right_Click': [data[14]],
            'Web_Forwards': [data[15]]
            }

            dfa=pd.DataFrame(series)
            print(dfa)
            y_pred = XGmodel.predict(dfa.values)
            # predictions = [round(value) for value in y_pred]
            # evaluate predictions
            if y_pred == 0:    
                value = "Legitimate"
                self.label_4.setText(value)
            else:
                value = "Phishing"
                self.label_4.setText(value);
        elif ans==1:
            self.label_4.setText("Phishing")
        elif ans2==1:
            self.label_4.setText("Legitimate")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDetectPage = QtWidgets.QMainWindow()
    ui = Ui_MainDetectPage()
    ui.setupUi(MainDetectPage)
    MainDetectPage.show()
    sys.exit(app.exec_())