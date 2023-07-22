cnt = 0
bid_list = [int(b) for b in input("Enter All Bid : ").split()]
if len(bid_list) <= 1:
    print("not enough bidder")
else:
    for bid in bid_list:
        if bid == max(bid_list) and cnt <= 1:
            cnt += 1
    if cnt > 1:
        print("error : have more than one highest bid")
    else:
        win = max(bid_list)
        bid_list.remove(win)
        pay = max(bid_list)
        print(f"winner bid is {win} need to pay {pay}")
        