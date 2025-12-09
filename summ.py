import math


def sum(numbers):
    s=0
    if len(numbers)==0:
        return 0
    for k in numbers:
        s+= k
    return s

def get_estimated_spread(audience_followers):
    num_followers = len(audience_followers)
    if num_followers==0:
        return 0
    sum=0
    for n in audience_followers:
        sum += n
    avg = sum /num_followers
    return avg * (num_followers **1.2)


def influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage*math.log(num_followers, 2)

list = {1,4,2}
average_engagement= float(15)



print("Sum of List:",sum(list))
print ("Estimated Spread:",get_estimated_spread(list))
print ("Influencer Score:",influencer_score(6, average_engagement))

