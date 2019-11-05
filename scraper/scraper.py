from bs4 import BeautifulSoup
from urllib import request
pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/science.shtml").read())
pageContent = BeautifulSoup(pageContent,"html.parser")

with open("science.txt","w") as f:
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/astronomy.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
        
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/sciences.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
        
    
    
        
        
with open("sports.txt", "w") as f:
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/sports.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
        
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/baseball.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
        
    pageContent = str(request.urlopen("https://footballdatabase.com/ranking/world/1").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".limittext"):
        f.write(item.get_text()+"\n")
        

with open("politics.txt","a") as f:
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/election.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
            

with open("food.txt" ,"w") as f:
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/cooking.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
        
    pageContent = str(request.urlopen("https://www.enchantedlearning.com/wordlist/cookingtools.shtml").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select(".wordlist-item"):
        f.write(item.get_text()+"\n")
        
    pageContent = str(request.urlopen("https://www.speaklanguages.com/english/vocab/foods").read())
    pageContent = BeautifulSoup(pageContent,"html.parser")
    for item in pageContent.select("div a"):
        f.write(item.get_text()+"\n")
    

        

    
    


