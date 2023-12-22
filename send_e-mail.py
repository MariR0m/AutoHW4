import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "r.m.u@bk.ru"
toaddr = "r.m.u@bk.ru"
mypass = "uU7eLTRNfGRVqVgTNCuk"
reportname = "report.xml"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name = basename((reportname)))
    part['Content - Desposition'] = 'attachment; filename = "%s"' % basename((reportname))
    msg.attach(part)

body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smpt.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()