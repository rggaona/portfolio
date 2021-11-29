from replit import clear
from art import logo


new_bidder = {}
loop = True

def find_highest(max_bidding):
  highest_bid = 0
  winner = ""
  for bidder in max_bidding:
    bid_amount = max_bidding[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"the greatest bid was {winner} with a bid of {highest_bid}")

while loop == True:
  print(logo)
  name = input("What's yopur name?: ").lower()
  bid = int(input("What's your bid?: $"))
  new_bidder[name] = bid
  more = input("Are there any other bidders? Type 'yes' or 'no': \n")
  if more == "no":
    loop = False
  clear()
find_highest(new_bidder)
