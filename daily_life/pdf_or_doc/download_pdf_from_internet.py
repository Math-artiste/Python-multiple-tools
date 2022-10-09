from fileinput import filename
import urllib.request
url = input("Enter link to download pdf : ")
name = input("Enter a name for the pdf file : ")
FileName = name+".pdf"
urllib.request.urlretrieve(url,FileName)