from tkinter import *
from test import *

#Main Screen Init
master       = Tk()
master.title = 'Yokio Converter'
if __name__ == "__main__":
    #list of quote currencies
    quotes_lst = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX','USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
    #list of base currencies
    base_lst = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD','UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
    #Functions
    def submit():
        from_currency_text = from_currency.get()
        to_currency_text = to_currency.get()
        amount_value = amount.get()
        if from_currency_text =='Select a currency' or to_currency_text == 'Select a currency' or amount_value == 0 or amount_value=='':
            notif.config(text="You did not complete the form", fg="red")
        else:    
            converted_amt = convert(from_currency_text,to_currency_text,amount_value)
            print(type(amount_value))
            notif.config(text=f'{amount_value} {from_currency_text} in {to_currency_text} is {str(converted_amt)}', fg="green")
            

    def reset():
        from_currency.set("Select a currency")
        to_currency.set("Select a currency")
        amountEntry.delete(0,'end')
    

    #Labels
    Label(master, text="Yokio Converter", font=('Calibri',15)).grid(row=0, sticky=N)
    Label(master, text="Fill the form with the appropriate information", font=('Calibri',11)).grid(row=1, sticky=W, padx=5 ,pady=10)

    Label(master, text="From", font=('Calibri', 11)).grid(row=2,sticky=W, padx=5)
    Label(master, text="To", font=('Calibri', 11)).grid(row=3,sticky=W, padx=5)
    Label(master, text="Amount", font=('Calibri', 11)).grid(row=4,sticky=W, padx=5)
    notif = Label(master, text="", font=('Calibri', 11),fg="red")
    notif.grid(row=7,sticky=S)


    #Storage
    from_currency = StringVar(master)
    to_currency = StringVar(master)
    amount = DoubleVar(master)

    from_currency.set("Select a currency")
    to_currency.set("Select a currency")

    #Entries
    fromEntry = OptionMenu(master,from_currency,*base_lst)
    fromEntry.grid(row=2,column=0)
    toEntry = OptionMenu(master,to_currency,*quotes_lst)
    toEntry.grid(row=3,column=0)
    amountEntry  = Entry(master, textvariable = amount)
    amountEntry.grid(row=4,column=0,padx=50)

    #Buttons
    Button(master, text = "Convert", command = submit).grid(row=7,   sticky=W,  pady=15, padx=5)
    Button(master, text = "Reset", command = reset).grid(row=7,  sticky=W,  padx=85, pady=40)

    #Mainloop
    master.mainloop()
