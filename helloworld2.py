import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail
import smtplib
from datetime import datetime, date , timedelta


class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        #THis gets triggered. So the next thing that I need to be able to do is go pull the right email from bookerville.
        
        logging.info("Received a message from: " + mail_message.sender)
        mail.send_mail(sender="John Peurifoy <peurifoyjohn@gmail.com>",
              to="peurifoyjohn@gmail.com",
              subject="TESTING FINAL GUY Your account has been approved",
              body="""
				Dear Albert:

				Your example.com account has been approved.  You can now visit
				http://www.example.com/ and sign in using your Google Account to
				access new features.

				Please let us know if you have any questions.

				The example.com Team
				""")
       	#sendEmail("Hi there",None,False)
       	logging.info("Done")

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!!!!!!!!!!!!!!!!')
        # mail.send_mail(sender="Example.com Support <support@example.com>",
        #       to="peurifoyjohn@gmail.com",
        #       subject="Your account has been approved",
        #       body="""
        # Dear Albert:

        # Your example.com account has been approved.  You can now visit
        # http://www.example.com/ and sign in using your Google Account to
        # access new features.

        # Please let us know if you have any questions.

        # The example.com Team
        # """)
        #sendEmail("Hi there",None,False)
        logging.info("Done")


app = webapp2.WSGIApplication([
    LogSenderHandler.mapping(),
    ('/', MainPage),
], debug=True)
