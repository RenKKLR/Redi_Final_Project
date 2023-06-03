from tkinter import *
import csv

def buy():
  global sName_buy
  global sAmount_buy
  sName_buy = stockname.get()
  sID_buy = stockid.get()
  sPrice_buy = stockprice.get()
  sAmount_buy = stockamount.get()
  sDate_buy = stockdate.get()
  print(sName_buy, sID_buy, sPrice_buy, sAmount_buy, sDate_buy)
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
  
#creating the file buy
  file = open("buy.csv", "a", newline="")
  file.write(sName_buy + ",")
  file.write(sID_buy + ",")
  file.write(sPrice_buy + ",")
  file.write(sAmount_buy + ",")
  file.write(sDate_buy + "\n")
  print("Stock", sName_buy, " has been submitted successfully")

def sell():
  sName_sell = stockname.get()
  sID_sell = stockid.get()
  sPrice_sell = stockprice.get()
  sAmount_sell = stockamount.get()
  sDate_sell = stockdate.get()
  #print(sName_sell, sID_sell, sPrice_sell, sAmount_sell, sDate_sell)
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)
#check if a stock alread has been bought enough before to save the entry sell
  with open('buy.csv') as buyfile:
    buy_reader = csv.reader(buyfile)
    next(buy_reader)
    for row in buy_reader:
      if sName_sell in row[0] and int(sAmount_sell) <= int(row[3]):
        print(sName_sell + " is in the buylist and you have enough to sell!")
        #creating the file sell
        file = open("sell.csv", "a", newline="")
        file.write(sName_sell + ",")
        file.write(sID_sell + ",")
        file.write(sPrice_sell + ",")
        file.write(sAmount_sell + ",")
        file.write(sDate_sell + "\n")
        print("Stock", sName_sell, " has been submitted successfully")
      elif sName_sell in row[0] and int(sAmount_sell) > int(row[3]):
        print("You cannot sell " +sName_sell+" in amount "+ sAmount_sell + ", because you didn't buy that much!")
      #else:
       #print("You cannot sell " + sName_sell +", because you didn't buy it!")

#create a new window to do a single query and display the result
def create_window():
  def submit():
    sName_query = stockname_query.get()
    stockname_query.delete(0, END)
    with open('buy.csv') as buyfile:
      buy_reader = csv.reader(buyfile)
      next(buy_reader)
      for row in buy_reader:
        if sName_query in row[0]:
          print("Buy: " + row[0], row[2], row[3])
          #print("A toal of Buy: " + str(int(row[2])*int(row[3])) + " Euro")
          
          '''
          with open('sell.csv') as sellfile:
            sell_reader = csv.reader(sellfile)
            next(sell_reader)
            for row in sell_reader:
              if sName_query in row[0]:
                print("Sell: " + row[0], row[2], row[3])
                print("A toal of Sell: " + str(int(row[2])*int(row[3])) + " Euro")
              '''    

        
        #else:
          #print("Invalid: You didn't buy Stock "+ sName_query +"!")
    
  
  
  window = Tk()
  window.geometry("500x200")
  window.title("Redi Final Project")
  heading = Label(window, text="Single Query", bg="grey", fg="black", width="500")
  heading.pack()
  
  screen.destroy()
  
  stockname_text = Label(window, text = "Name of Stock *")
  stockname_text.place(x = 15, y = 50)
  stockname_query = Entry(window,)
  stockname_query.place(x = 15, y = 80)

  submit_btn = Button(window,text ="Submit", command=submit, bg="grey")
  submit_btn.place(x=15, y=150)

  
#screen design
screen = Tk()
screen.geometry("500x500")
screen.title("Redi Final Project")
heading = Label(text="Trading Performance Query", bg="grey", fg="black", width="500")
heading.pack()

#label defnition and positon
stockname_text = Label(text = "Name of Stock *")
stockid_text = Label(text = "Stock ID *")
stockprice_text = Label(text = "Price pro Share (in Euro) *")
stockamount_text = Label(text = "Amount *")
stockdate_text = Label(text = "Date of Transaction (DD/MM/YYYY) *")
stockname_text.place(x = 15, y = 70)
stockid_text.place(x = 270, y = 70)
stockprice_text.place(x = 15, y = 140)
stockamount_text.place(x = 270, y = 140)
stockdate_text.place(x = 15, y = 210)

#entry definition and position
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

#place button to buy or sell or do a single query
buy_btn = Button(screen, text ="Buy", command=buy, bg = "grey")
sell_btn = Button(screen, text = "Sell", command=sell, bg ="grey")
query_btn = Button(screen, text="Single Query ", command=create_window, bg="grey")
buy_btn.place(x = 15, y = 290)
sell_btn.place(x = 75, y = 290)
query_btn.place(x=15, y=330)

screen.mainloop()

#calculate the performance
#entry the name of stock
#check if sAmount_sell=buy

 