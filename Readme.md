EmailToText
==========
API that allows you to seemlessly convert emails to text messages and send them.

To use:
----
  * Send an email to the server name (eg: admin@main-duality-117002.appspotmail.com)
  * Make sure to sign the email with 'Thanks', and put the phone number two lines before the thanks. 
  * Then this will pull the correct email to send the document to someone's phone. 

Local Setup
------
```
    git clone
    pip install -r requirements.txt
    dev_appserver.py helloworld/
```
Then setup the settings.py file (copy the settings_template file and fill in the proper fields).


This will start a local server on http://localhost:54005.
The debugging for this will be at: http://localhost:8000.

You should verify that the main page is working, to ensure that the library dependencies were dealt with properly.
Goto https://[project-id].appspot.com/

To upload this to google's servers, you need to configure and set up a google cloud project https://console.cloud.google.com/home/.
Make sure you note the project-id.


To upload the file to the server, go to the directory that the project is in and enter:
```
  appcfg.py -A [project-id] update helloworld/
```
