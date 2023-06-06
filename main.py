from tkinter import *
from tkinter import messagebox
import csv


#save the entries in csv file buy after click button Buy
def buy():
  global sName_buy
  global sAmount_buy
  global sPrice_buy
  #get entries from input box
  sName_buy = stockname.get().title()
  sID_buy = stockid.get()
  sPrice_buy = stockprice.get()
  sAmount_buy = stockamount.get()
  sDate_buy = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  #save the entry in the file buy.csv
  file = open("buy.csv", "a", newline="")
  file.write(sName_buy + ";")
  file.write(sID_buy + ";")
  file.write(sPrice_buy + ";")
  file.write(sAmount_buy + ";")
  file.write(sDate_buy + "\n")
  print("Stock", sName_buy, " has been saved in buy.csv successfully!")

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
  global sName_sell
  global sPrice_sell
  global sAmount_sell
  #get entries from input box
  sName_sell = stockname.get().title()
  sID_sell = stockid.get()
  sPrice_sell = stockprice.get()
  sAmount_sell = stockamount.get()
  sDate_sell = stockdate.get()
  #delete entries after submit
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  
  #check if a stock alread has been bought enough before saving
  buy_single_stock_count = single_stock_count("buy.csv", sName_sell)
  print("Bought: " + str(buy_single_stock_count) + " share(s)")
  sell_single_stock_count = single_stock_count("sell.csv", sName_sell) 
  print("Sold: " + str(sell_single_stock_count) + " share(s)")
  
  can_be_sold = buy_single_stock_count - sell_single_stock_count

  if can_be_sold >= int(sAmount_sell):
    #save the entry in the file sell.csv
    file = open("sell.csv", "a", newline="")
    file.write(sName_sell + ";")
    file.write(sID_sell + ";")
    file.write(sPrice_sell + ";")
    file.write(sAmount_sell + ";")
    file.write(sDate_sell + "\n")
    print("Stock", sName_sell, " has been saved in sell.csv successfully!")
  else:
    print("You can't sell " +sName_sell+" in amount "+ sAmount_sell + " share(s), because you don't have (enough) of this stock!")
    messagebox.showwarning("WARNING", "You can't sell it! You don't have (enough) of this stock!")

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
    #open file buy.csv and print all buy transactions
    with open('buy.csv') as buy_file:
      buy_transactions = csv.reader(buy_file, delimiter=";")
      next(buy_transactions)
      for buy_transaction in buy_transactions:
        if sName_query == buy_transaction[0]:
          print("Buy: ", buy_transaction)        
      #open file sell.csv and print all sell transactions       
      with open('sell.csv') as sell_file:
        sell_transactions = csv.reader(sell_file, delimiter=";")
        next(sell_transactions)
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
          print(f"Total Bought €{buy_total_single_sum:.2f}")
          print(f"Total Sold €{sell_total_single_sum:.2f}")
          if is_stock_balanced:
            #print("bought=sold")
            performance_single = performance(sell_total_single_sum, buy_total_single_sum)
            print(f"Performance of Stock {sName_query}: {performance_single:+.2f}%")
        
          
          else: 
            #print("bought>sold")
            #calculate single stock performance using current sell price
            remaining_stock_count = buy_single_stock_count - sell_single_stock_count
            current_sell_price = float(input(f"Please enter the current sell price of stock {sName_query} (in Euro): "))
            current_sell_sum = current_sell_price * remaining_stock_count
            performance_single_current = performance(current_sell_sum + sell_total_single_sum, buy_total_single_sum)
            
            
            print(f"Current total sell €{current_sell_sum:.2f}")
            print(f"Current Performance of Stock {sName_query}: {performance_single_current:+.2f}%")

  def performance(sell_sum, buy_sum):
    (sell_sum - buy_sum) / buy_sum * 100
  
          
 #windwo design 
  window = Tk()
  window.geometry("500x400")
  window.title("Redi Final Project")
  heading = Label(window, text="Single Stock Query", bg="grey", fg="black", width="500")
  heading.pack()
  
  #screen.destroy()
  #windwo label, entry and button
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
screen.title("Redi Final Project")
heading = Label(text="Trading Performance Query", bg="grey", fg="black", width="500")
heading.pack()

#screen label defnition and positon
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
