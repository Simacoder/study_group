string = "abracadabra"
string = string[:5] + "k" + string[6:] 
def mutate_string(string, position, character):
    # Convert string to list of characters
    char_list = list(string)
    
    # Perform the mutation
    char_list[position] = character
    
    # Convert list back to string
    mutated_string = ''.join(char_list)
    
    return mutated_string

# Example usage:
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)