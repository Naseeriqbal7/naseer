## Email subscribers from two campaigns
campaign_A = {"Anand", "Bharat", "Chaitanya"}
campaign_B = {"Bharat", "Deepak", "Esha"}

# find common subscribers
common_subscribers = campaign_A & campaign_B
print("Common Subscriber(s):", common_subscribers)
# find all unique subscribers
all_subscribers = campaign_A | campaign_B
print("All Unique Subscriber(s):", all_subscribers)