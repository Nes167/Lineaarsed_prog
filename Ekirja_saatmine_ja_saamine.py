#https://myaccount.google.com/apppasswords Rakenduste paroolid
import smtplib,ssl
from email.message import EmailMessage
def saada_kiri():
    kellele=input("Kellele: ")
    kiri="""<!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<h2>Sending an HTML email from Python</h2>
<p>Hello there,</p>
<a href="https://inspirezone.tech/">Here's a link to an awesome dev
community!</a>
</body>
</html>"""
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="anastassiamayba@gmail.com"
    parool=input("Rakenduste parool") #gjfk fbvi nfjk hoyu
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    with open("FELV-cat.jpg","rb") as f:
        pilt=f.read()
    msg.add_attachment(pilt,maintype="image",subtype="png",filename="FELV-cat.jpg")
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print('Kiri saadetud')
    except Exception as e:
        print("Viga: ", e)


