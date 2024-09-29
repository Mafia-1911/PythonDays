print("Welcome to our Secret Auction")
auctioneers={"name":[],"Bids":[]}
next="yes";
while(next=="yes"):
    print(chr(27) + "[2J");                 #It clears the terminal
    name=input("What is your name?");
 auctioneers["name"].append(name);
    bid=int(input("What's your bid?"));
    auctioneers["Bids"].append(bid);
    print("Please type 'yes' if there are any otherwise type 'no'")
    next=input("Are there any other bidders?").lower()  #tackling the case-sensitivity

#now we need to find the largest value along with the index
arr1=auctioneers["Bids"];
large=-1;
for i in range(len(arr1)):
        if arr1[i] > large:
            large = arr1[i]
winner=auctioneers["name"][i];
print(f"The winner is {winner} with a bid of ${large}")
