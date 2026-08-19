def shipwithInDays( weights , days):
    max_weights = 0
    for i in range(len(weights)):
        max_weights+=weights[i]

    for capacity in range(max(weights) , max_weights+1):
        current_sum = 0
        required_day = 1
        for i in range(len(weights)):
            if current_sum + weights[i] <= capacity :
                current_sum += weights[i]
            else :
                required_day+=1
                current_sum = weights[i] 

        
                
        if required_day <=  days :
            return capacity  
    return -1    
       
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5               
print(shipwithInDays(weights,days))
weights = [3, 2, 2, 4, 1, 4]
days = 3
print(shipwithInDays(weights ,days))

# Optimal Solution :
