# Lesson 5
#input

start_money = float(input()) #float() helps to cast its argument to a real number
cookies_sold =  input()

#processing 

big_cookies = 0
normal_cookies = 0 

for current_cookie in cookies_sold:
#print(current_cookie)
    if current_cookie == "c":
        normal_cookies += 1
    elif current_cookies == "b":
        big_cookies += 1
    else:
        print (f"{current_cookie} is not a valid item")

total_cookies = big_cookies+normal_cookies
profit = (big_cookies * 1.25) + (normal_cookies*0.75)
end_day = (profit + start_money)

print(f"at the end of the day we sold {total_cookies} and made a total of ${end_day}")
  

