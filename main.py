from art import logo
print(logo)
data_dict={} #empty dictionary
bid_list=[]
condition=True
while condition==True:
  
  name=input("What is your name? :")
  print(f"The bids previouslytaken are {bid_list}")
  bid=int(input("what is your Bid?:$"))
  bid_list.append(bid)
  data_dict[name]=bid                      #adding key:value pair in the empty dictionary
  choice= input("Are there any other bidder, Yes or No :").lower()
  if choice=="no":
    condition=False
   

for key in data_dict:
  value=0
  if data_dict[key] >value:
    value = data_dict[key]
print(f"The winner is {key} with a bid of {value}")    