name = input("Please tell me your name: ")
stocks_purchased = int(input("Enter the number of shares purchased: "))
purchase_price = float(input("Enter the purchase price per share: "))
selling_price = float(input("Enter the stock's selling price per share: "))

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

purchase_total = stocks_purchased * purchase_price
buying_commission = purchase_total * 0.03
purchase_value = purchase_total - buying_commission
selling_total = stocks_purchased * selling_price
selling_commission = selling_total * 0.02
total_commission = buying_commission + selling_commission
profit_loss = selling_total - purchase_total - total_commission


print(" ")
print("Investor Name:", name)
print("")
("")
print("Money spent for stocks:", locale.currency(purchase_total))
print("Buying Commission:", locale.currency(buying_commission))
print("Money earned selling shares:", locale.currency(selling_total))
print("Selling Commission:",locale.currency(selling_commission))
print("Total Commission:", locale.currency(total_commission))
print("Profit/Loss:", f"-{locale.currency(abs(profit_loss))}" if profit_loss < 0 else locale.currency(profit_loss))
