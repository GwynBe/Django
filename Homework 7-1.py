# 1.0
color = "black"
# 1.1
pi = 3.14159
diameter = 3
radius = diameter/2
area = pi*(radius**2)
# 1.2
a = [1, 2, 3]
b = [3, 2, 1]
c = a
a = b
b = c
# 1.3a
(5-3)//2
# 1.3b
8 - 3 * (2 - (1 + 1))
# 1.4
alice_candies = 121
bob_candies = 77
carol_candies = 109
total_candies = alice_candies + bob_candies + carol_candies
candies_each = total_candies // 3
to_smash = total_candies % 3


# 2.1
def round_to_two_places(num):
    result = round(num, 2)
    return result
# 2.2
# round(1310.14, -2) = 1300.0
# 2.3
def candies_to_smash(total_candies, total_friends = 3):
    return total_candies % total_friends
# 2.4
# 'ruound_to_two_places' chưa định nghĩa
# abs() chỉ nhận 1 giá trị
# return ở ngoài def()


# 3.1
def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
# 3.2
def candies_to_smash(total_candies):
    if total_candies > 1:
        print("Splitting", total_candies, "candies")
        return total_candies
    else:
        print("Splitting", total_candies, "candy")
        return total_candies
# 3.3
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    if have_umbrella or (rain_level < 5 and have_hood):
        return True
    elif rain_level > 0 and is_workday:
        return False
# 3.4
def concise_is_negative(number):
    return number < 0
# 3.5a
def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion
# 3.5b
def wants_plain_hotdog(ketchup, mustard, onion):
    return not ketchup and not mustard and not onion
# 3.5c
def exactly_one_sauce(ketchup, mustard, onion):
    return (ketchup and not mustard) or (mustard and not ketchup)
# 3.6
def exactly_one_topping(ketchup, mustard, onion):
    return (int(ketchup) + int(mustard) + int(onion)) == 1


# 4.1
def select_second(L):
    if len(L) > 1:
        return L[1]
    else:
        return None
# 4.2
def losing_team_captain(teams):
    return teams[-1][1]
# 4.3
def purple_shell(racers):
    first_place = racers.pop(0)
    last_place = racers.pop(-1)
    racers.insert(0, last_place)
    racers.insert(-1, first_place)
# 4.4
lengths = [3, 2, 0, 2]
# 4.5
def fashionably_late(arrivals, name):
    if len(arrivals) > 2:
        half_arrivals = arrivals[round(len(arrivals)/2)]
        fashion_late = arrivals[half_arrivals:-1]
        if name in fashion_late:
            return True
        else:
            return False
    else:
        return None


# 5.1
def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False
# 5.2
def elementwise_greater_than(L, thresh):
    result = []
    for l in L:
        if l > thresh:
            result.append(True)
        else:
            result.append(False)
    return result
# 5.3
def menu_is_boring(meals):
    for meal in meals:
        if meals.count(meal) > 1:
            return True
    return False
# 5.4
def estimate_average_slot_payout(n_runs):
    payout = []
    for i in range(n_runs):
        payout.append(play_slot_machine())
    print(sum(payout)/n_runs)


# 6.0a
length = 0
# 6.0b
length = 7
# 6.0c
length = 7
# 6.0d
length = 3
# 6.0e
length = 1
# 6.1
def is_valid_zip(zip_code):
    if len(zip_code) == 5 and str(zip_code).isdigit == True:
        return True
    else:
        return False
# 6.2
def word_search(doc_list, keyword):
    result = []
    for doc in doc_list:
        for word in doc:
            if str(word).lower() == str(keyword).lower():
                result.append(doc_list.index(doc))
    return result
# 6.3
def multi_word_search(doc_list, keywords):
    result = {}
    for keyword in keywords:
        word_search(doc_list, keyword)
        result[keyword] = doc_list
    return result
