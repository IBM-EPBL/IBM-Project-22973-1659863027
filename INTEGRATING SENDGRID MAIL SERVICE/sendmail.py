import configparser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sendgrid import SendGridAPIClient , Mail
#from Mail.views import sendgrid_mail
from sendgrid.helpers.mail import Mail

config= configparser.Configparser()
config.reac("config.ini")

def sendMailUsingSendGrid(API,from_email,to_emails,subject,html_content):
    if API!=None and from_email!=None and len(to_emails):
        message= Mail(from_email,to_emails,subject,html_content)
        try:
            sg = SendGridAPIClient(API)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

try:
    settings=config["SETTINGS"]
except:
    settings={}
API= settings.get["APIKEY",None]
from_email= settings.get["FROM",None]
to_emails= settings.get["TO",""]

subject="Single Test Message"
html_content="Message Successful send through python"

sendMailUsingSendGrid()