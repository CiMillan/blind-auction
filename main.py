from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bid_not_finish = True

def find_highest_bid(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while bid_not_finish:
  name = input("What's your name?: ")
  price = int(input("What's your bid?: $"))
  bids[name] = price
 
  bid_cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if bid_cont == "no":
    bid_not_finish = False
    find_highest_bid(bids)
  elif bid_cont == "yes":
    clear()



  




