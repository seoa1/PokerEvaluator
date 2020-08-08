# gives max value of a 7 card hand
def getHandVal7(hand):
    hands = handPerms(hand)
    max_hand_val = 0
    # hand format: suit / value ex. h13
    for hand in hands:
        hand_val = getHandVal5(hand, max_hand_val)
        max_hand_val = max(hand_val, max_hand_val)
    return max_hand_val

# returns all 5 card hands possible from 7 card hand
def handPerms(hand):
    perms = []
    for i in range(len(hand) - 1):
        for j in range(i + 1, len(hand)):
            hand_copy = hand.copy()
            del hand_copy[j]
            del hand_copy[i]
            perms.append(hand_copy)
    return perms

# gives value of a 5 card hand.
# return vals:
# high card: sum(vals)
# pair: 1000000 + 100 * pair_val + sum(kickers)
# two pair: 2000000 + 10000 * pair_val + 100 * sec_pair_val + kicker
# trips: 3000000 + 100 * trip_val + sum(kickers)
# straight: 4000000 + max(vals). if low A straight, max is 3
# flush: 5000000 + max(vals)
# full house: 6000000 + 100 * trip_val + pair_val
# quads: 7000000 + 100 * quad_val + kicker
# straight flusH; 8000000 + max(vals). if low A straight, max is 3
# royal flush: 9000000
def getHandVal5(hand, prev_max):
    suits = []
    vals = []
    #suits, vals set
    for card in hand:
        suits.append(card[0])
        vals.append(int(card[1:-1]))
    #flush
    check_suit = suits[0]
    flush = True
    for suit in suits:
        if suit != check_suit:
            flush = False
            break
    #sort vals
    min_val = 100
    for i in range(len(vals) - 1):
        for j in range(i + 1, len(vals)):
            min_val = min(min_val, vals[j])
        vals[i] = min_val
        min_val = 100
    #straight
    straight = True
    for i in range(len(vals) - 1):
        if vals[i] + 1 != vals[i + 1]:
            straight = False
            break
    #check for low straight
    if vals[-1] == 12:
        straight = vals[:-1] == [0,1,2,3]
    #straight flush
    if straight and flush:
        #royal flush
        if vals[-1] == 12 and vals[0] == 8:
            return 9000000 
        if vals[-1] == 12:
            return 8000000 + 3
        return 8000000 + max(vals)
    #check for prev. max
    if prev_max >= 8000000:
        return 0
    #check for duplicate vals:
    counts = collections.Counter(vals)
    quads = False
    f_house = False
    trips = False
    two_pair = False
    pair = False
    #find val
    for val, num in counts.items():
        if num > 3:
            quads = True
            break
        if num == 3 and pair == True:
            f_house = True
            break
        if num == 3:
            trips = True
            break
        if num == 2:
            if trips == True:
                f_house = True
                break
            if pair == True:
                two_pair = True
            else:
                pair = True
            break

    tot_val = 0
    if quads:
        tot_val = 7000000
        for val, num in counts.items():
            if num == 1:
                tot_val += val
            else:
                tot_val += 100 * val
        return tot_val
    if prev_max > 7000000:
        return 0
    
    if f_house:
        tot_val = 6000000
        for val, num in counts.items():
            if num == 3:
                tot_val += 


