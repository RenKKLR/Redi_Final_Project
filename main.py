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





  
  #
    #check if B>=S
#elif selType == "I" or "i":
  #print("inquiry!")
#else:
  #print("Your entry is invalid, please try again.")
 