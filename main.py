from tkinter import *

def buy():
  sName = stockname.get()
  sID = stockid.get()
  sPrice = stockprice.get()
  sAmount = stockamount.get()
  sDate = stockdate.get()
  print(sName, sID, sPrice, sAmount, sDate)
  stockname.delete(0, END)
  stockid.delete(0, END)
  stockprice.delete(0, END)
  stockamount.delete(0, END)
  stockdate.delete(0, END)

#creating the file buy
  file = open("buy.txt", "a")
  file.write(sName)
  file.write(sID)
  file.write(sPrice)
  file.write(sAmount)
  file.write(sDate)
  print("Stock", sName, " has been submitted successfully")

#screen design
screen = Tk()
screen.geometry("500x500")
screen.title("Redi Final Project")
heading = Label(text="Trading Performance Inquiry", bg="grey", fg="black", width="500")
heading.pack()

#label defnition and positon
stockname_text = Label(text = "Name of Stock *")
stockid_text = Label(text = "Stock ID *")
stockprice_text = Label(text = "Price pro Stock *")
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

#place button to buy or sell
buy = Button(screen, text ="Buy", command=buy, bg = "grey")
sell = Button(screen, text = "Sell", bg ="grey")
buy.place(x = 15, y = 290)
sell.place(x = 75, y = 290)


print("Welcome to Trading Performance Inquiry!")

selType = input("For a new entry of a transaction, please type E; to make an inquiry, please type I:\n")

if selType == "E" or selType == "e":
  
  transType = input("For making an entry of a new Buy, please type B; of a new Sell, please type S:\n")
  if transType == "B" or transType == "b":
      stockName = input("What is the name of the stock?\n")
      stockID = input("What is the ID of the stock?\n")
      stockPrice = input("What is the single traded price of the stock in Euro?\n")
      stockAmountBuy = input("What are the amounts of your traded stocks in piece?\n")
      stockDate = input("What is the date of your transaction (DD/MM/YY)?\n")
  elif transType == "S" or transType == "s":
      print("Sell")
  else:
      print("Your entry is invalid, please try again!")


else:
  print("Your entry is invalid, please try again!")





  
 