# Ask the user if they want to create a css file and a js file with the web server

def create_css_file():
    print('Css')

def create_js_file():
    print('Js')

def generate_custom_url(custom_url):
    print('Creating Url')

create_optional_files = input('If you want to either create a css file or a js file with this web server enter Yes, otherwise enter No: ')

if create_optional_files == 'yes'.lower():
    
    choose_from_fileOptions = input('Do you was to creat a CSS file or a JS file: ')
    if choose_from_fileOptions == 'css'.lower():
        create_css_file()
    else:
        create_js_file()


# Enter in the IP address for the web server (click enter for default localhost) & the port for the web server
ip_address = int(input('Enter the IP address you wish to use for the web server: '))
port_number = int(input('Enter in a port number for the Web Server (Defaulted to port 80 if no entry)'))
if (port_number < 65536 and port_number > 0):
    print()

# Ask the user if they want a custom url

create_custom_url = input('Do you want a custom url (Yes/No): ')
if create_custom_url == 'yes'.lower():
    enter_custom_url = input('Enter your custom url: ')
    generate_custom_url(enter_custom_url)