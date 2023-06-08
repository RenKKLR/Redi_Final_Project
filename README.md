# Trading Performance Query (TPQ) - ReDi Final Project 

Why this project:
* to deal with data (numbers);
* to use programming language python;
* to practice the functions which were learned during the courses: loops, decision-making, def, arithmetic operations and object oriented programming;
* to do something realistic

What does Trading Performance Query (TRQ) do:
* to save buy transactions in a csv file: buy.csv;
* to check a sell transaction if there are enought stocks bought already first, then save the sell transaction in a csv file: sell.csv if there is enough;
* to do single stock performance query:
  * firstly, check whether the queried stock was already bought;
  * secondly, list all the historical transaction of this already bought queried stock with all its inforamtion, including name, id, price per share, amount and date of the transaction;
  * lastly, if the account of this queried stock was balanced, then calculate the performance (win/loss) in percentage directly; and if the account was not balanced, a current sell price would be asked in order to calculate the current performance of this queried stock

What functions could be upgraded in the future:
* to do the stock query for the whole portfolio performance;
* to do the stock query for a selected portfolio performance by selecting the single stocks;
* to show the results on a GUI window;
* to use a GUI window to input the current sell price;
* to warn the user if the mandatory fields are not (correctly) filled in;
* to warn the user if the stock name and stock id don't match (stock id (WKN / ISIN) is a digit alphanumeric code that uniquely identifies a specific stock).