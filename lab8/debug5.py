# Program to remove any scores from a list that are below 50.
 
scores = [60, 45, 30, 85, 10, 90] 

return_score = scores.copy()
for score in scores: 
    if score < 50: 
        return_score.remove(score)
print(return_score) 
