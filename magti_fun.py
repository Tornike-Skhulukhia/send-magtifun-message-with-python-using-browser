'''
    About us:
    
        Youtube Channel:  bit.ly/shencshegidzlia
        Facebook Page  :  fb.me/shencshegidzlia
        Email:            info.shencshegidzlia@gmail.com

        შენც შეგიძლია!
        24.05.2018
        
'''




def help_():
    result = '''
	ფუნქცია გვეხმარება მაგთიფანიდან (magtifun.ge) შეტყობინებების გაგზავნაში პროგრამირების ენა პითონის გამოყენებით.
	წინაპირობები:
		Chrome ბრაუზერი
		selenium ბიბლიოთეკა   ( start --> cmd --> pip install selenium )
		chromedriver           ( ლინკი(windows) --> https://chromedriver.storage.googleapis.com/2.38/chromedriver_win32.zip )

	გამოყენების მიზნებიდან გამომდინარე, შესაძლებელია მრავალი ასპექტის დახვეწა და კონკრეტულ საჭიროებებზე მორგება.
	საიტის სტრუქტურაში ცვლილებების შემთხვევაში, შესაძლოა საჭირო გახდეს კოდის მცირედი მოდიფიკაცია.

	ამჟამინდელი მდგომარეობა არ ითვალისწინებს შესაბამისი შეტყობინებების ჩვენებას გაუთვალისწინებელ შემთხვევებში,
	მაგალითად როგორიცაა არარსებული ნომრის მითითება შეტყობინების გასაგზავნად.
	
	პრობლემის შემთხვევაში, შესაძლებელია show_browser არგუმენტის მნიშვნელობის გაჭეშმარიტება
	და პრობლემის ვიზუალური დათვალიერების შემდეგ მის მოგვარებაზე მუშაობა.

	თითოეული შეტყობინების გაგზავნის შემდეგ ხდება დარჩენილი შეტყობინებების რაოდენობის ბეჭდვაც.
	თუ შეტყობინებების რაოდენობა 0-ია, ვიღებთ შესაბამის შეცდომის მაჩვენებელ ტექსტს და მნიშვნელობას მცდარი.

	არგუმენტები: 
		1. username -  ავტორიზაციისთვის საჭირო მომხმარებლის სახელი(ტელეფონის ნომერი)
		2. password - ავტორიზაციისთვის საჭირო პაროლი 
		3. numbers - ნომერი, რომელზეც გვინდა შეტყობინების გაგზავნა(string - ერთი ნომრის შემთხვევაში,
                    ან list - რამდენიმე ნომრის შემთხვევაში).
                    
                    გასათვალისწინებელი ფაქტორი: ნომერზე გაგზავნის მცდელობამდე მოწმდება მასში მხოლოდ რიცხვების შემცველობა,
                    თუ გასაგზავნი ნომრები შეიცავს +, ან სხვა სიმბოლოებს, დაგჭირდებათ მათი ფორმატის შეცვლა, ან ფუნქციის მცირედი მოდიფიკაცია.
                    
		4. messages - შეტყობინება(string - ერთი შეტყობინების  შემთხვევაში, ან list - რამდენიმეს შემთხვევაში).
                    აუცილებელია ნომრებისა და შეტყობინებების რაოდენობები იყოს ერთნაირი.

                    ნომერთა და შეტყობინებათა გამოყენება ხდება თანმიმდევრულად:
                        პირველი შეტყობინება ეგზავნება პირველ ნომერს, მეორე - მეორეს ...
                        
		5. show_browser - სტანდარტულად მნიშვნელობა მცდარია, ჭეშმარიტების შემთხვევაში,
                    გაგზავნის პარალელურად ბრაუზერის ფანჯარა იქნება ხილული.
                    
		6. close_after - სტანდარტულად მნიშვნელობა ჭეშმარიტია, შედეგად შეტყობინებების წარმატებით გაგზავნის შემდეგ
                    ხდება ბრაუზერის ხილული/უხილავი ფანჯრის დახურვა.
		
        '''

def send_message(username, password, numbers, messages, show_browser=False, close_after = True):
    #import
    from selenium import webdriver
    
    ''' define lists using given data, that we will use later '''
    if isinstance(numbers, list) and isinstance(messages,list) and len(numbers) == len(messages): # few at once case
        numbers_to_check, messages_to_check = numbers, messages # use given arguments data
        
    elif isinstance(numbers, str) and isinstance(messages,str): # single number and single message case
        numbers_to_check, messages_to_check = [numbers], [messages] # create lists with one element
        
    else:  # case when something unexpected happens
        print("\n", "| There was a problem, maybe number of messages and numbers are not the same,".center(70),"\n")
        print("or their structure is not correct, check and try again. |".center(70))
        return False # stop process

    ''' simple check for messages and numbers '''
    for individual_message, individual_number in zip(messages_to_check, numbers_to_check):
        #check that message length is within magtifun limit and not 0
        if len(individual_message) == 0 or len(individual_message) > 445:  
            print("\n", "| Sorry, message should be from 1 to 445 characters, not |{}|. |".format(len(individual_message)).center(70, "="), "\n")
            return False # stop process
        
        # message also needs to contain at least one character different from space
        elif len(individual_message.strip()) == 0:  
            print("\n", "| Sorry, message should contain at least one character different from space. |".center(70, "="), "\n")
            return False # stop process

        # check that each number contains only numbers(number itself should has string type) and number of numbers in a number is at least 1
        elif not individual_number.isdigit(): 
            print("\n", "| Sorry, number format |{}| is not valid. |".format(individual_number).center(70, "="), "\n")
            return False # stop process


    ''' work with show_browser argument '''
    if not show_browser:  # do not show browser
        #import options
        from selenium.webdriver.chrome.options import Options
        # add headless option
        options_ = Options(); options_.add_argument("--headless")
        # define browser
        browser = webdriver.Chrome(chrome_options = options_)
    else:  # show browser
        browser = webdriver.Chrome()

    ''' log in and check balance ''' 
    # open page
    browser.get(r"http:/magtifun.ge")
    # get username and password fields
    username_field = browser.find_element_by_xpath(r'//*[@id="user"]')
    password_field = browser.find_element_by_xpath(r'//*[@id="password"]')
    # type user information and log in 
    username_field.send_keys(username); password_field.send_keys(password)
    browser.find_element_by_xpath(r'/html/body/div[1]/center/div[1]/div[2]/div[1]/form/table/tbody/tr/td[2]/input').click()    
    # if log in was completed successfully
    try:
    # check how many free sms we have left
        balance = browser.find_element_by_xpath(r'/html/body/div[1]/center/div[1]/div[2]/div[1]/form/div[2]/span/span').text
    except:  # if log in information is not correct
        print("\n", "| Login failed,change username and/or password and try again. |".center(70, "-"), "\n")
        return False
    # if balance is not enough (more than 0)
    if eval(balance) < 1:
        print("| Sorry, you have not enough balance  |{}| to send a message. |".format(balance).center(70, "="))
        return False # stop process

        ''' start sending messages '''
    else:
        for number_, sms_ in zip(numbers_to_check,messages_to_check):
            # get number and message fields + send button location
            numbers_field = browser.find_element_by_xpath(r'//*[@id="recipient"]')
            message_field = browser.find_element_by_xpath(r'//*[@id="message_body"]')
            send_button = browser.find_element_by_xpath(r'//*[@id="sms_form"]/p[6]/input')
            # type individual number and message
            numbers_field.send_keys(number_); message_field.send_keys(sms_)
            # send and refresh page
            send_button.click(); browser.refresh()
            # print that message was sent
            print("\n","| Your message to {} was successfully sent. |".format(number_).center(70, "*"), "\n")
            # get number of messages left again
            balance_final = browser.find_element_by_xpath(r'/html/body/div[1]/center/div[1]/div[2]/div[1]/form/div[2]/span/span').text
            # print balance
            print("\n", "| You have left {} messages. |".format(balance_final).center(70, "="),"\n"); print("-" * 72, "\n")

            #if balance is 0, print about it and stop process
            if not eval(balance): #if balance is not different from 0
                print("\n", "| Sorry, you have not enough balance |{}| to send other messages. |".format(balance).center(70, "="), "\n")
                return False # stop process

    #close browser if appropriate argument is set to True and return True if everything finished successfully
    if close_after:
        browser.quit()
    # finish
    return True
