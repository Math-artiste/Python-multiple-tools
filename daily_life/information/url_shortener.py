import pyshorteners
long_url = input("Enter the url to shorten : ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The shortened url is : " + short_url)