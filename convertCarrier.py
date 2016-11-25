from settings import *
#This takes in the message and parses it for the phone number, then returns the emailaddress to send it to.
def convertMessage(message):
    mylines = message.splitlines()
    val = 0
    emailnum = ""
    for line in mylines:
        print "line: " , line
        val += 1
        if line == "Thanks":
            print "I FOUND IT!"
            emailnum = mylines[val-3]
    print "Cellphone number: " , emailnum

    number=emailnum
    addr="http://www.carrierlookup.com/index.php/api/lookup?key="+carrierLookupKey+"&number="+str(number)
    import requests
    r = requests.get(addr)
    #r.json()
    carrier = str(r.json()['Response']['carrier'])
    #This is something like 'Sprint'
    emailAd = str(number)+"@"+convertCarrier(carrier)
    return emailAd

#This takes in the name of the character and returns the email hostname for the associated carrier.
def convertCarrier(carrier):
    if (carrier==''): carString = ''
    if (carrier=='TracFone (Cingular Orange)') :carString = 'mmst5.tracfone.com'
    if (carrier=='Boost-CDMA') :carString ='myboostmobile.com'
    if (carrier=='3 River Wireless'): carString = 'sms.3rivers.net'
    if (carrier=='ACS Wireless'): carString = 'paging.acswireless.com'
    if (carrier=='Alltel'): carString = 'message.alltel.com'
    if (carrier=='AT&T'): carString = 'txt.att.net'
    if (carrier=='Bell Canada'): carString = 'txt.bellmobility.ca'
    if (carrier=='Bell Mobility'): carString = 'txt.bell.ca'
    if (carrier=='Blue Sky Frog'): carString = 'blueskyfrog.com'
    if (carrier=='Bluegrass Cellular'): carString = 'sms.bluecell.com'
    if (carrier=='Boost Mobile'): carString = 'myboostmobile.com'
    if (carrier=='BPL Mobile'): carString = 'bplmobile.com'
    if (carrier=='Carolina West Wireless'): carString = 'cwwsms.com'
    if (carrier=='Cellular One'): carString = 'mobile.celloneusa.com'
    if (carrier=='Cellular South'): carString = 'csouth1.com'
    if (carrier=='Centennial Wireless'): carString = 'cwemail.com'
    if (carrier=='CenturyTel'): carString = 'messaging.centurytel.net'
    if (carrier=='Cingular (Now AT&T)'): carString = 'txt.att.net'
    if (carrier=='Clearnet'): carString = 'msg.clearnet.com'
    if (carrier=='Comcast'): carString = 'comcastpcs.textmsg.com'
    if (carrier=='Corr Wireless Communications'): carString = 'corrwireless.net'
    if (carrier=='Dobson'): carString = 'mobile.dobson.net'
    if (carrier=='Edge Wireless'): carString = 'sms.edgewireless.com'
    if (carrier=='Fido'): carString = 'fido.ca'
    if (carrier=='Golden Telecom'): carString = 'sms.goldentele.com'
    if (carrier=='Helio'): carString = 'messaging.sprintpcs.com'
    if (carrier=='Houston Cellular'): carString = 'text.houstoncellular.net'
    if (carrier=='Idea Cellular'): carString = 'ideacellular.net'
    if (carrier=='Illinois Valley Cellular'): carString = 'ivctext.com'
    if (carrier=='Inland Cellular Telephone'): carString = 'inlandlink.com'
    if (carrier=='MCI'): carString = 'pagemci.com'
    if (carrier=='Metrocall'): carString = 'page.metrocall.com'
    if (carrier=='Metrocall 2-way'): carString = 'my2way.com'
    if ("MetroPCS" in carrier) :carString = 'mymetropcs.com'
    if (carrier=='Metro PCS'): carString = 'mymetropcs.com'
    if (carrier=='Microcell'): carString = 'fido.ca'
    if (carrier=='Midwest Wireless'): carString = 'clearlydigital.com'
    if (carrier=='Mobilcomm'): carString = 'mobilecomm.net'
    if (carrier=='MTS'): carString = 'text.mtsmobility.com'
    if (carrier=='Nextel'): carString = 'messaging.nextel.com'
    if (carrier=='OnlineBeep'): carString = 'onlinebeep.net'
    if (carrier=='PCS One'): carString = 'pcsone.net'
    if (carrier=='Public Service Cellular'): carString = 'sms.pscel.com'
    if (carrier=='Qwest'): carString = 'qwestmp.com'
    if (carrier=='Rogers AT&T Wireless'): carString = 'pcs.rogers.com'
    if (carrier=='Rogers Canada'): carString = 'pcs.rogers.com'
    if (carrier=='Satellink'): carString = 'satellink.net'
    if (carrier=='Southwestern Bell'): carString = 'email.swbw.com'
    if (carrier=='Sprint'): carString = 'messaging.sprintpcs.com'
    if (carrier=='Sumcom'): carString = 'tms.suncom.com'
    if (carrier=='Surewest Communicaitons'): carString = 'mobile.surewest.com'
    if (carrier=='T-Mobile'): carString = 'tmomail.net'
    if (carrier=='Telus'): carString = 'msg.telus.com'
    if (carrier=='Tracfone'): carString = 'txt.att.net'
    if (carrier=='Triton'): carString = 'tms.suncom.com'
    if (carrier=='Unicel'): carString = 'utext.com'
    if (carrier=='US Cellular'): carString = 'email.uscc.net'
    if (carrier=='Solo Mobile'): carString = 'txt.bell.ca'
    if (carrier=='Sprint'): carString = 'messaging.sprintpcs.com'
    if (carrier=='Sumcom'): carString = 'tms.suncom.com'
    if (carrier=='Surewest Communicaitons'): carString = 'mobile.surewest.com'
    if (carrier=='T-Mobile'): carString = 'tmomail.net'
    if (carrier=='Telus'): carString = 'msg.telus.com'
    if (carrier=='Triton'): carString = 'tms.suncom.com'
    if (carrier=='Unicel'): carString = 'utext.com'
    if (carrier=='US Cellular'): carString = 'email.uscc.net'
    if (carrier=='US West'): carString = 'uswestdatamail.com'
    if (carrier=='Verizon'): carString = 'vtext.com'
    if (carrier=='Virgin Mobile'): carString = 'vmobl.com'
    if (carrier=='Virgin Mobile Canada'): carString = 'vmobile.ca'
    if (carrier=='West Central Wireless'): carString = 'sms.wcc.net'
    if (carrier=='Western Wireless'): carString = 'cellularonewest.com'
    if (carrier=='Chennai RPG Cellular'): carString = 'rpgmail.net'
    if (carrier=='Chennai Skycell / Airtel'): carString = 'airtelchennai.com'
    if (carrier=='Comviq'): carString = 'sms.comviq.se'
    if (carrier=='Delhi Aritel'): carString = 'airtelmail.com'
    if (carrier=='Delhi Hutch'): carString = 'delhi.hutch.co.in'
    if (carrier=='DT T-Mobile'): carString = 't-mobile-sms.de'
    if (carrier=='Dutchtone / Orange-NL'): carString = 'sms.orange.nl'
    if (carrier=='EMT'): carString = 'sms.emt.ee'
    if (carrier=='Escotel'): carString = 'escotelmobile.com'
    if (carrier=='German T-Mobile'): carString = 't-mobile-sms.de'
    if (carrier=='Goa BPLMobil'): carString = 'bplmobile.com'
    if (carrier=='Golden Telecom'): carString = 'sms.goldentele.com'
    if (carrier=='Gujarat Celforce'): carString = 'celforce.com'
    if (carrier=='JSM Tele-Page'): carString = 'pinjsmtel.com'
    if (carrier=='Kerala Escotel'): carString = 'escotelmobile.com'
    if (carrier=='Kolkata Airtel'): carString = 'airtelkol.com'
    if (carrier=='Kyivstar'): carString = 'smsmail.lmt.lv'
    if (carrier=='Lauttamus Communication'): carString = 'pagere-page.net'
    if (carrier=='LMT'): carString = 'smsmail.lmt.lv'
    if (carrier=='Maharashtra BPL Mobile'): carString = 'bplmobile.com'
    if (carrier=='Maharashtra Idea Cellular'): carString = 'ideacellular.net'
    if (carrier=='Manitoba Telecom Systems'): carString = 'text.mtsmobility.com'
    if (carrier=='Meteor'): carString = 'mymeteor.ie'
    if (carrier=='MiWorld'): carString = 'm1.com.sg'
    if (carrier=='Mobileone'): carString = 'm1.com.sg'
    if (carrier=='Mobilfone'): carString = 'page.mobilfone.com'
    if (carrier=='Mobility Bermuda'): carString = 'ml.bm'
    if (carrier=='Mobistar Belgium'): carString = 'mobistar.be'
    if (carrier=='Mobitel Tanzania'): carString = 'sms.co.tz'
    if (carrier=='Mobtel Srbija'): carString = 'mobtel.co.yu'
    if (carrier=='Movistar'): carString = 'correo.movistar.net'
    if (carrier=='Mumbai BPL Mobile'): carString = 'bplmobile.com'
    if (carrier=='Netcom'): carString = 'sms.netcom.no'
    if (carrier=='Ntelos'): carString = 'pcs.ntelos.com'
    if (carrier=='O2'): carString = 'o2.co.uk'
    if (carrier=='O2'): carString = 'o2imail.co.uk'
    if (carrier=='O2 (M-mail)'): carString = 'mmail.co.uk'
    if (carrier=='One Connect Austria'): carString = 'onemail.at'
    if (carrier=='OnlineBeep'): carString = 'onlinebeep.net'
    if (carrier=='Optus Mobile'): carString = 'optusmobile.com.au'
    if (carrier=='Orange'): carString = 'orange.net'
    if (carrier=='Orange Mumbai'): carString = 'orangemail.co.in'
    if (carrier=='Orange NL / Dutchtone'): carString = 'sms.orange.nl'
    if (carrier=='Oskar'): carString = 'mujoskar.cz'
    if (carrier=='P&T Luxembourg'): carString = 'sms.luxgsm.lu'
    if (carrier=='Personal Communication'): carString = 'pcom.ru'
    if (carrier=='Pondicherry BPL Mobile'): carString = 'bplmobile.com'
    if (carrier=='Primtel'): carString = 'sms.primtel.ru'
    if (carrier=='Safaricom'): carString = 'safaricomsms.com'
    if (carrier=='Satelindo GSM'): carString = 'satelindogsm.com'
    if (carrier=='SCS-900'): carString = 'scs-900.ru'
    if (carrier=='SFR France'): carString = 'sfr.fr'
    if (carrier=='Simple Freedom'): carString = 'text.simplefreedom.net'
    if (carrier=='Smart Telecom'): carString = 'mysmart.mymobile.ph'
    if (carrier=='Southern LINC'): carString = 'page.southernlinc.com'
    if (carrier=='Sunrise Mobile'): carString = 'mysunrise.ch'
    if (carrier=='Sunrise Mobile'): carString = 'swmsg.com'
    if (carrier=='Surewest Communications'): carString = 'freesurf.ch'
    if (carrier=='Swisscom'): carString = 'bluewin.ch'
    if (carrier=='T-Mobile Austria'): carString = 'sms.t-mobile.at'
    if (carrier=='T-Mobile Germany'): carString = 't-d1-sms.de'
    if (carrier=='T-Mobile UK'): carString = 't-mobile.uk.net'
    if (carrier=='Tamil Nadu BPL Mobile'): carString = 'bplmobile.com'
    if (carrier=='Tele2 Latvia'): carString = 'sms.tele2.lv'
    if (carrier=='Telefonica Movistar'): carString = 'movistar.net'
    if (carrier=='Telenor'): carString = 'mobilpost.no'
    if (carrier=='Teletouch'): carString = 'pageme.teletouch.com'
    if (carrier=='Telia Denmark'): carString = 'gsm1800.telia.dk'
    if (carrier=='TIM'): carString = 'timnet.com'
    if (carrier=='TSR Wireless'): carString = 'pageralphame.com'
    if (carrier=='UMC'): carString = 'sms.umc.com.ua'
    if (carrier=='Uraltel'): carString = 'sms.uraltel.ru'
    if (carrier=='Uttar Pradesh Escotel'): carString = 'escotelmobile.com'
    if (carrier=='Vessotel'): carString = 'pager.irkutsk.ru'
    if (carrier=='Vodafone Italy'): carString = 'sms.vodafone.it'
    if (carrier=='Vodafone Japan'): carString = 'c.vodafone.ne.jp'
    if (carrier=='Vodafone Japan'): carString = 'h.vodafone.ne.jp'
    if (carrier=='Vodafone Japan'): carString = 't.vodafone.ne.jp'
    if (carrier=='Vodafone UK'): carString = 'vodafone.net'
    if (carrier=='Wyndtell'): carString = 'wyndtell.com'
    if (carString == "") : print "I cannot find the carrier: " + str(carrier)
    return carString