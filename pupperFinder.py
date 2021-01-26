import requests
import webbrowser
from bs4 import BeautifulSoup
import smtplib

page = requests.get("https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&gender=A&agegroup=UnderYear&location=&site=&onhold=A&orderby=name&colnum=3&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=io53xfw8b0k2ocet3yb83666507n2168taf513lkxrqe681kf8&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=&wmode=opaque", auth=('user', 'pass'))
soupContent = BeautifulSoup(page.content, 'html.parser')
baseUrl = "https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimalDetails.aspx?id="

newPupperDivs = soupContent.select('div.list-animal-id')

oldPuppersDirty = open("C:/Buildworkspace/apps/pupperFinder/pups.txt", "r").readlines()
oldPuppersClean = []
for oldPupDirty in oldPuppersDirty:
    oldPupClean = oldPupDirty.rstrip('\n')
    oldPuppersClean.append(oldPupClean)

for newPup in newPupperDivs :
    if not (newPup.text in oldPuppersClean) :
        server = smtplib.SMTP("smtp.mail.yahoo.com",587)
        server.ehlo()
        server.starttls()
        server.login('notAndrewPaffel@yahoo.com', 'ugtdnsuczbfkqjsi')
        server.sendmail('notAndrewPaffel@yahoo.com', '6082148036@email.uscc.net', 'Subject: New Pupper. \n\n ' + baseUrl + newPup.text)
        server.quit()
        open("C:/Buildworkspace/apps/pupperFinder/pups.txt","a").write(newPup.text + "\n")
        print (newPup.text + " is new")
