from tkinter import *
from tkinter import messagebox
import csv
from transaction import Transaction

print("Welcom to Trading Performance Query!")

#save the entries in csv file buy.csv after click button Buy
def buy():
  #get entries from input box
  name = stockname.get().title()
  id = stockid.get()
  price = stockprice.get()
  amount = stockamount.get()
  date = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  #save the entry in the file buy.csv
  transaction = Transaction(name,id,price,amount,date)
  file = open("buy.csv", "a", newline="")
  file.write(transaction.name + ";")
  file.write(transaction.id + ";")
  file.write(transaction.price + ";")
  file.write(transaction.amount + ";")
  file.write(transaction.date + "\n")
  print("Stock", transaction.name, "in amount", transaction.amount,  "share(s) has been saved in buy.csv successfully!")

#count total single stock bought or sold
def single_stock_count(filename, stock_name):
  single_stock_count = 0
  with open(filename) as transaction_file:
    transactions = csv.reader(transaction_file, delimiter=";")
    next(transactions)
    for transaction in transactions:
      if stock_name == transaction[0]: 
        single_stock_count += int(transaction[3])
  return single_stock_count

def sell():
  #get entries from input box
  name = stockname.get().title()
  id = stockid.get()
  price = stockprice.get()
  amount = stockamount.get()
  date = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  
  #check if a stock alread has been bought enough before saving
  buy_single_stock_count = single_stock_count("buy.csv", name)
  print("Bought: " + str(buy_single_stock_count) + " share(s)")
  sell_single_stock_count = single_stock_count("sell.csv", name) 
  print("Sold: " + str(sell_single_stock_count) + " share(s)")
  
  can_be_sold = buy_single_stock_count - sell_single_stock_count
  transaction = Transaction(name,id,price,amount,date)
  if can_be_sold >= int(amount):
    #save the entry in the file sell.csv
    file = open("sell.csv", "a", newline="")
    file.write(transaction.name + ";")
    file.write(transaction.id + ";")
    file.write(transaction.price + ";")
    file.write(transaction.amount + ";")
    file.write(transaction.date + "\n")
    print("Stock", transaction.name, "in amount", transaction.amount, "share(s) has been saved in sell.csv successfully!")
  else:
    print("You can't sell " + transaction.name +" in amount "+ transaction.amount + " share(s), because you don't have (enough of) this stock!")
    messagebox.showwarning("WARNING", "You can't sell it! You don't have (enough of) this stock!")

#calculate total buy or total sell of one single stock
def total_single_sum(filename, stock_name):
  total_single_sum = 0
  with open(filename) as transaction_file:
    transactions = csv.reader(transaction_file, delimiter=";")
    next(transactions)
    for transaction in transactions:
      if stock_name == transaction[0]: 
        total_single_sum += int(transaction[3])*float(transaction[2])
  return total_single_sum

#create a new window to do a single query
def create_window():
  
  def submit():    
    sName_query = stockname_query.get().title()
    stockname_query.delete(0, END)
  
    def performance(sell_sum, buy_sum):
      return (sell_sum - buy_sum) / buy_sum  * 100
    
    #open file buy.csv and print all buy transactions
    with open('buy.csv') as buy_file:
      buy_transactions = csv.reader(buy_file, delimiter=";")
      for buy_transaction in buy_transactions:
        if sName_query == buy_transaction[0]:
          print("Buy: ", buy_transaction)        
      #open file sell.csv and print all sell transactions       
      with open('sell.csv') as sell_file:
        sell_transactions = csv.reader(sell_file, delimiter=";")
        for sell_transaction in sell_transactions:
          if sName_query == sell_transaction[0]:
            print("Sell: ", sell_transaction)  
      #check if bought=sold and do the calculation 
        buy_single_stock_count = single_stock_count("buy.csv", sName_query)
        sell_single_stock_count = single_stock_count("sell.csv", sName_query)
        is_stock_balanced = buy_single_stock_count - sell_single_stock_count == 0
        if buy_single_stock_count == 0:
          print("You didn't buy stock " + sName_query + "!")
          messagebox.showwarning("WARNING", "You didn't buy this stock! Please buy it first!")             
        else: 
          print(f"Bought: {buy_single_stock_count} share(s)")
          print(f"Sold: {sell_single_stock_count} share(s)")
          buy_total_single_sum = total_single_sum('buy.csv', sName_query)
          sell_total_single_sum = total_single_sum('sell.csv', sName_query)
          print(f"Total Bought: €{buy_total_single_sum:.2f}")
          print(f"Total Sold: €{sell_total_single_sum:.2f}")
          if is_stock_balanced:
            performance_single = performance(sell_total_single_sum, buy_total_single_sum)
            print(f"Performance of Stock {sName_query}: {performance_single:+.2f}%")         
          else: 
            #calculate single stock current performance by inputting current sell price
            remaining_stock_count = buy_single_stock_count - sell_single_stock_count
            current_sell_price = float(input(f"Please enter the current selling price of stock {sName_query} (in Euro): "))
            current_sell_sum = current_sell_price * remaining_stock_count
            performance_single_current = performance(current_sell_sum + sell_total_single_sum, buy_total_single_sum)
          
            print(f"Current total sell €{current_sell_sum:.2f}")
            print(f"Current Performance of Stock {sName_query}: {performance_single_current:+.2f}%")  
          
  #window design 
  window = Tk()
  window.geometry("500x400")
  window.title("Redi Final Project")
  heading = Label(window, text="Single Stock Query", bg="grey", fg="black", width="500")
  heading.pack()
  
  #could close the main screen when the query window is opened
  #screen.destroy() 
  
  #window definition and position of label, entry and button
  stockname_text = Label(window, text = "Name of Stock *")
  stockname_text.place(x = 15, y = 50)
  stockname_query = Entry(window)
  stockname_query.place(x = 15, y = 80)

  submit_btn = Button(window,text ="Submit", command=submit, bg="grey")
  submit_btn.place(x=15, y=150)

  window.mainloop()
  
#screen design
screen = Tk()
screen.geometry("500x500")
screen.title("ReDi Final Project")
heading = Label(text="Trading Performance Query", bg="grey", fg="black", width="500")
heading.pack()

#screen label definition and positon
stockname_text = Label(text = "Name of Stock *")
stockid_text = Label(text = "Stock ID (WKN / ISIN) ")
stockprice_text = Label(text = "Price per Share (in Euro) *")
stockamount_text = Label(text = "Amount *")
stockdate_text = Label(text = "Date of Transaction (DD/MM/YYYY) *")
stockname_text.place(x = 15, y = 70)
stockid_text.place(x = 270, y = 70)
stockprice_text.place(x = 15, y = 140)
stockamount_text.place(x = 270, y = 140)
stockdate_text.place(x = 15, y = 210)

#screen entry definition and position
stockname = Entry()
stockid = Entry()
stockprice = Entry()
stockamount = Entry()
stockdate = Entry()
stockname.place(x = 15, y = 100)
stockid.place(x = 270, y = 100)
stockprice.place(x = 15, y = 170)
stockamount.place(x = 270, y = 170)
stockdate.place(x = 15, y = 240)

#screen button to buy or sell or do a single stock query
buy_btn = Button(screen, text ="Buy", command=buy, bg = "grey")
sell_btn = Button(screen, text = "Sell", command=sell, bg ="grey")
query_btn = Button(screen, text="Single Stock Query", command=create_window, bg="grey")
buy_btn.place(x = 15, y = 290)
sell_btn.place(x = 85, y = 290)
query_btn.place(x=15, y=333)

screen.mainloop()
