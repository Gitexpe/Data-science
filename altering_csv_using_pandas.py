import pandas as pd
import random

# Function to generate random plausible values for numerical data
def randomize_numeric(data, min_val, max_val):
    return random.randint(min_val, max_val)
def random_yes_no():
    return random.choice(['Yes', 'No'])

# Load the CSV file
zomato_data = pd.read_csv('C:\\Users\\gaura\\Documents\\python\\zomato_data.csv')

# randomizing Yes/No values
zomato_data['online_order'] = zomato_data['online_order'].apply(lambda x: random_yes_no())
zomato_data['book_table'] = zomato_data['book_table'].apply(lambda x: random_yes_no())

# Randomize numerical data
zomato_data['votes'] = zomato_data['votes'].apply(lambda x: randomize_numeric(x, 50, 1000))
zomato_data['approx_cost(for two people)'] = zomato_data['approx_cost(for two people)'].apply(
    lambda x: randomize_numeric(x, 200, 2000))

# Save the modified DataFrame back to the CSV file
zomato_data.to_csv('C:\\Users\\gaura\\Documents\\python\\zomato_data.csv', index=False)

print("Data successfully updated and saved to the CSV file.")
