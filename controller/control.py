from mechanize import Browser

input_data = input("Enter product name / description: ").replace(" ", "+")
urlLink = "{}?q=({})&oq={}".format("https://patents.google.com/", input_data, input_data)
products = Browser(urlLink)
print(urlLink)