# Ask the user if they want to create a css file and a js file with the web server
def Css_file():
    print("Css")
def Js_files():
    print("Js")
def Url_creater(Url):
    print("Creating Url")
files = input("If you want to either create a css file or a js file with this web server enter Yes, otherways enter No: ")
if files == "Yes":
    files = input("Do you was to creat a CSS file or a JS file: ")
    if files == "Css":
        Css_file()
    else:
        Js_files()
# Ask the user if they want a custom url
customUrl = input("Do you want a custom url (Yes/No): ")
if customUrl == "Yes":
    customUrl = input("Enter your custom url: ")
    Url_creater(customUrl)
# Enter in the IP address for the web server (click enter for default localhost) & the port for the web server
IPaddress = input("Enter the IP address you wish to use for the web server: ")


