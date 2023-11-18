import smtplib
server = smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()
server.login('ishabijlani123@gmail.com', '7354431517')
server.sendmail('ishabijlani123@gmail.com',
                'ashishbijlani35@gmail.com',
                'In science fiction, the "metaverse" is a hypothetical iteration of the Internet as a single, universal, and immersive virtual world that is facilitated by the use of virtual reality (VR) and augmented reality (AR) headsets.[1][2] In colloquial usage, a "metaverse" is a network of 3D virtual worlds focused on social connection.[2][3][4]'
                    )