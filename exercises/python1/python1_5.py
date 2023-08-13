# Chapter : 1 - item : 5 - vickrey auction
# จงสร้าง vickrey auction แบบจำลอง
# Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

# word
# "Enter All Bid : "
# "not enough bidder"
# "error : have more than one highest bid"
# "winner bid is $ need to pay $"

cnt = 0
bid_list = [int(b) for b in input("Enter All Bid : ").split()] # Input bids
if len(bid_list) <= 1: # Only one bid
    print("not enough bidder")
else:
    for bid in bid_list:
        if bid == max(bid_list) and cnt <= 1: # Find amount of max bid
            cnt += 1
    if cnt > 1: # Amount of max bid more than one
        print("error : have more than one highest bid")
    else:
        win = max(bid_list) # Find max bid winner
        bid_list.remove(win) # Remove max bid from bid list
        pay = max(bid_list) # Find pay bid
        print(f"winner bid is {win} need to pay {pay}")
        