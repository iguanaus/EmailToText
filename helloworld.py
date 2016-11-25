import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail
import smtplib
from datetime import datetime, date , timedelta
from convertCarrier import *
from settings import *

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        #THis gets triggered. So the next thing that I need to be able to do is go pull the right email from bookerville.

        logging.info("Received a message from: " + mail_message.sender)
        plaintext_bodies = mail_message.bodies('text/plain')
        plaintext = ""
        for content_type, body in plaintext_bodies:
            plaintext = body.decode()
            logging.info("Plain text body of length %d.", len(plaintext))
            #plaintext
        #print str(mail_message.body)
        newad = convertMessage(plaintext)
        mail.send_mail(sender=replyToEmail,
              to=ccEmail+","+str(newad),
              subject=mail_message.subject,
              body=mail_message.body)
       	#sendEmail("Hi there",None,False)
       	logging.info("Done")

class MainPage(webapp2.RequestHandler):
    def get(self):
        import requests
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!!!!!!!!!!!!!!!!')
       
        logging.info("Done")


app = webapp2.WSGIApplication([
    LogSenderHandler.mapping(),
    ('/', MainPage),
], debug=True)
