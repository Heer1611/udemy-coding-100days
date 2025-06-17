import random
from game_data import data
from art import logo_2, vs

# Print the game logo
print(logo_2)

player_score = 0
game_over = False

# Function to get a random entity from the data
def get_random_entity():
    return random.choice(data)

# Function to format the entity's data for display
def format_entity(entity):
    name = entity['name']
    description = entity['description']
    country = entity['country']
    return f"{name}, a {description}, from {country}"

# Function to compare follower counts
def compare_followers(entity_a, entity_b):
    return entity_a['follower_count'] > entity_b['follower_count']

while not game_over:
    # Get two random entities
    entity_a = get_random_entity()
    entity_b = get_random_entity()
    
    # Ensure the entities are not the same
    while entity_a == entity_b:
        entity_b = get_random_entity()
    
    # Display the entities
    print(f"Compare A: {format_entity(entity_a)}")
    print(vs)
    print(f"Against B: {format_entity(entity_b)}")
    
    # Ask the player to make a choice
    choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    
    # Determine the correct answer
    correct_answer = 'A' if compare_followers(entity_a, entity_b) else 'B'
    
    # Check if the player's choice is correct
    if choice == correct_answer:
        player_score += 1
        print(f"You're right! Current score: {player_score}")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {player_score}")
