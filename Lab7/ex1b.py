for num in range(1,51): 
    value = 2* num - 1 # anything time 2 = even # -1 will be an odd #
    if value < 50: # bc multiplying by 2 will make results greater than 50
        break
    else:
        print(value)

# cons is that after the value 25, the value will exceed  50 which is unnecessary
# solution = use a break to stop the loop value exceeds 50 OR simply change the range from 51 to 26