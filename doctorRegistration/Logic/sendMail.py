import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

def send(emailid,name,did,url):
    html="""
    <body style="background-color: #f1f1f1;">
        <section style="min-width: 320px;max-width: 520px;margin: auto; background-color: white;">
            <div style="text-align: center;border: 1px solid #f1f1f1;">
                <img width="100px" src="https://ci6.googleusercontent.com/proxy/DqhPy-zLU7un3Jv5JeiasvpTF8jSvaQbPqEXKulLBQCF-iAtWmcLBriUdhPdBsJea1gk9ZyZPZHb8BCnrOcO0VsqtQMyMr5tV2qV5xwmERNhcvMFg0tnO9vyn0iiihGrHuS0qZlxQJzZMv0gbY9774XJgNN-=s0-d-e1-ft#https://www.zilliondesigns.com/images/portfolio/healthcare-hospital/iStock-471629610-Converted.png" alt="">
                <div style="font-family: sans-serif;color: #236ea0;">
                    <h1>Patient Automation and Security System</h1>
                </div>
                <div style="padding:0px;background-color:transparent">
                    <div style="Margin:0 auto;word-wrap:break-word;word-break:break-word;background-color:#003399">
                    <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
                        <div style="display:table-cell;vertical-align:top">
                        <div style="width:100%!important">
                            <div style="padding:0px;border-top:0px solid transparent;border-left:0px solid transparent;border-right:0px solid transparent;border-bottom:0px solid transparent">
                            <table style="font-family:'Cabin',sans-serif" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td style="word-break:break-word;padding:40px 10px 10px;font-family:'Cabin',sans-serif" align="left">
        
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tbody><tr>
                                        <td style="padding-right:0px;padding-left:0px" align="center">
        
                                        <img align="center" border="0" src="https://ci4.googleusercontent.com/proxy/HSFHzYcQq9U1UQlXLsBgUD-twop5t3KtATKiwljuxdxb3cOgbdYWnjfZbj_5TwW7xc-fvTvnvb5vtXoq5QjGf3jB2R1dY5CV3LGo0potgE1qSKY=s0-d-e1-ft#https://cdn.templates.unlayer.com/assets/1597218650916-xxxxc.png" alt="Image" title="Image" style="outline:none;text-decoration:none;clear:both;display:inline-block!important;border:none;height:auto;float:none;width:26%;max-width:150.8px" width="150.8" class="CToWUd">
        
                                        </td>
                                        </tr>
                                    </tbody></table>
        
                                    </td>
                                </tr>
                                </tbody>
                            </table>
        
                            <table style="font-family:'Cabin',sans-serif" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td style="word-break:break-word;padding:10px;font-family:'Cabin',sans-serif" align="left">
        
                                    <div style="color:#e5eaf5;line-height:140%;text-align:center;word-wrap:break-word">
                                        <p style="font-size:14px;line-height:140%"><strong>T H A N K S&nbsp; &nbsp;F O R&nbsp; &nbsp;R E G I S T E R I N G&nbsp; &nbsp;W I T H&nbsp; &nbsp;U S !</strong></p>
                                    </div>
        
                                    </td>
                                </tr>
                                </tbody>
                            </table>
        
                            <table style="font-family:'Cabin',sans-serif" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td style="word-break:break-word;padding:0px 10px 31px;font-family:'Cabin',sans-serif" align="left">
        
                                    <div style="color:#e5eaf5;line-height:140%;text-align:center;word-wrap:break-word">
                                        <p style="font-size:14px;line-height:140%"><span style="font-size:28px;line-height:39.2px"><strong><span style="line-height:39.2px;font-size:28px">Verify Your E-mail Address </span></strong>
                                        </span>
                                        </p>
                                    </div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
            </div>

            <div style="text-align: center;font-family: sans-serif;padding: 50px 10px;">
                <p style="font-size: 1.5rem;">Hi Dr. """+name+"""</p>
                <p style="font-size: 1.2rem;">Your Unique ID is: """+did+"""</p>
                <p style="font-size: 1.2rem;">You're almost ready to get started, please click below to confirm your account</p>
                <a href="""+url+""">"""+url+"""</a>
            </div>

            <div style="padding:0px;background-color:transparent">
                <div style="Margin:0 auto;word-wrap:break-word;word-break:break-word;background-color:#e5eaf5">
                <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
                    

                    
                    <div style="display:table-cell;vertical-align:top">
                    <div style="width:100%!important">
                        
                        <div style="padding:0px;border-top:0px solid transparent;border-left:0px solid transparent;border-right:0px solid transparent;border-bottom:0px solid transparent">
                        

                        <table style="font-family:'Cabin',sans-serif" cellpadding="0" cellspacing="0" width="100%" border="0">
                            <tbody>
                            <tr>
                                <td style="word-break:break-word;padding:41px 55px 18px;font-family:'Cabin',sans-serif" align="left">

                                <div style="color:#003399;line-height:160%;text-align:center;word-wrap:break-word">
                                    <p style="font-size:14px;line-height:160%"><span style="font-size:20px;line-height:32px"><strong>Get in touch</strong></span></p>
                                    <p style="font-size:14px;line-height:160%"><span style="font-size:16px;line-height:25.6px;color:#000000">+91 111 333 4444</span></p>
                                    <p style="font-size:14px;line-height:160%"><span style="font-size:16px;line-height:25.6px;color:#000000"><a href="mailto:Info@pmass.com" target="_blank">Info@pmass.com</a></span></p>
                                </div>

                                </td>
                            </tr>
                            </tbody>
                        </table>
        
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            <div style="padding:0px;background-color:transparent">
                <div style="Margin:0 auto;word-wrap:break-word;word-break:break-word;background-color:#003399">
                <div style="border-collapse:collapse;display:table;width:100%;background-color:transparent">
                    

                    
                    <div style="display:table-cell;vertical-align:top">
                    <div style="width:100%!important">
                        
                        <div style="padding:0px;border-top:0px solid transparent;border-left:0px solid transparent;border-right:0px solid transparent;border-bottom:0px solid transparent">
                        

                        <table style="font-family:'Cabin',sans-serif" cellpadding="0" cellspacing="0" width="100%" border="0">
                            <tbody>
                            <tr>
                                <td style="word-break:break-word;padding:10px;font-family:'Cabin',sans-serif" align="left">

                                <div style="color:#fafafa;line-height:180%;text-align:center;word-wrap:break-word">
                                    <p style="font-size:14px;line-height:180%"><span style="font-size:16px;line-height:28.8px">Copyrights © Company All Rights Reserved</span></p>
                                </div>

                                </td>
                            </tr>
                            </tbody>
                        </table>

                        
                        </div>
                        
                    </div>
                    </div>
                    
                    
                </div>
                </div>
            </div>
        </section>
    </body>
"""
    print("MAIL HOSPITAL IN")
    email=MIMEMultipart('alternative')
    email['Subject']='Doctor ID '+str(date.today().strftime("%d/%m/%Y"))
    email['From']='doctorgeek1947@gmail.com'
    email['To']=emailid
    mail_string=MIMEText(html,'html')
    email.attach(mail_string)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('doctorgeek1947@gmail.com','Dancebar123')
    server.send_message(email)
