def numWaterBottles(numBottles, numExchange):
    total_drunk = numBottles
    empty_bottles = numBottles
    
    while empty_bottles >= numExchange:
        new_bottles = empty_bottles // numExchange
        total_drunk += new_bottles
        empty_bottles = empty_bottles % numExchange + new_bottles
    
    return total_drunk

# Example usage:
numBottles = 9
numExchange = 3
print(numWaterBottles(numBottles, numExchange))  # Output: 13
