import random
# 1. User stakes A51 tokens, is eligible for ETH rewards

def calculate_weightage():
    """
    Input amounts for 9 people and calculate their weightage.

    Returns:
    list of float: A list of user-input amounts for each person.
    list of float: A list of weightage values for each person.
    """
    amounts = []  # Initialize an empty list to store user-input amounts

    # Input amounts for 9 people
    for i in range(9):
        while True:
            try:
#                amount = float(input(f"Enter amount for person {i + 1}: "))  # amounts = [random.uniform(1, 10000) for _ in range(9)]
                amount = float(input(f"Enter A51 token quantity for person {i + 1}: "))
                break  # Exit the loop if a valid float is entered
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        amounts.append(amount)  # Add the user-input amount to the list

    # Calculate the sum of all amounts
    total_amount = sum(amounts)

    # Calculate the weightage for each person
    weightage = [amount / total_amount for amount in amounts]

    return amounts, weightage

def calculate_weightage_sum(weightage_values):
    """
    Calculate the sum of weightage values.

    Args:
    weightage_values (list of float): A list of weightage values for each person.

    Returns:
    float: The sum of the weightage values.
    """
    # Calculate the sum of weightage values
    weightage_sum = sum(weightage_values)

    return weightage_sum

def calculate_reward_rate(reward_in_month, blocks_in_a_day):
    """
    Calculate the reward rate.

    Args:
    reward_in_month (float): The total reward in a month.
    blocks_in_a_day (int): The total number of blocks in a day.

    Returns:
    float: The calculated reward rate.
    """
    # Calculate the reward rate for a month
    reward_rate = reward_in_month / (blocks_in_a_day * 30)  # Assuming 30 days in a month
    print("\nblocks_in_a_month:", blocks_in_a_day * 30)
    return reward_rate

"""
def calculate_reward_rate(reward_in_month, blocks_in_a_day, days_in_a_month): # When reward period is not defined 
    
    Calculate the reward rate.

    Args:
    reward_in_month (float): The total reward in a month.
    blocks_in_a_day (int): The total number of blocks in a day.
    days_in_a_month (int): The number of days in a month.

    Returns:
    float: The calculated reward rate.
    
    # Calculate the reward rate for a month
    reward_rate = reward_in_month / (blocks_in_a_day * days_in_a_month)
    print("\nblocks_in_a_month:", blocks_in_a_day * days_in_a_month)
    return reward_rate
"""

#  Usage:
random_amounts, weightage_values = calculate_weightage()

print("\nUser-Input A51 Token Amounts:")
for amount in random_amounts:
    print(amount)

print("\nWeightage values:")
for value in weightage_values:
    print(value)

# Calculate and print the sum of weightage values
weightage_sum = calculate_weightage_sum(weightage_values)
print("\nSum of Weightage values:", weightage_sum)

# Constants
blocks_in_a_day = 7144  # Number of blocks in a day
reward_in_a_month = 7000.0  # Total ETH reward in a month

# Calculate the A51 reward rate
a51_reward_rate = calculate_reward_rate(reward_in_a_month, blocks_in_a_day)

# Print the result
print("\nA51 Token Reward Rate:", a51_reward_rate)

# Calculate the ETH reward rate
eth_reward_rate = calculate_reward_rate(reward_in_a_month, blocks_in_a_day)

# Print the result
print("\nA51 Token Reward Rate:", eth_reward_rate)

# 2. User providing liquidity to our protocol, in A51/ETH pool, and then stakes that ERC721 tokens, is eligible for both ETH & A51 rewards

calculate_weightage()

def calculate_rewards(weightage, eth_reward_per_block, a51_reward_per_block, number_of_block_elapsed_since_staked):
    """
    Calculate tokenA and tokenB rewards based on weightage, reward rates, and time elapsed.

    Args:
    weightage (float): Weightage of the staked amount.
    eth_reward_per_block (float): ETH reward per block.
    a51_reward_per_block (float): A51 reward per block.
    time_elapsed_since_staked (float): Time elapsed since staked (in blocks or any suitable unit).

    Returns:
    float: tokenA reward.
    float: tokenB reward.
    """
    # Calculate tokenA reward using the provided formula
    tokenA_reward = (weightage * 0.3) * eth_reward_per_block * number_of_block_elapsed_since_staked

    # Calculate tokenB reward using the provided formula
    tokenB_reward = (weightage * 0.7) * a51_reward_per_block * number_of_block_elapsed_since_staked

    return tokenA_reward, tokenB_reward

# Example usage
weightage = calculate_weightage()
eth_reward_per_block = a51_reward_rate
a51_reward_per_block = eth_reward_rate
number_of_block_elapsed_since_staked = 7 * blocks_in_a_day  # Replace with the actual blocks elapsed in a day

tokenA_reward, tokenB_reward = calculate_rewards(weightage, eth_reward_per_block, a51_reward_per_block, number_of_block_elapsed_since_staked)

print("TokenA Reward:", tokenA_reward)
print("TokenB Reward:", tokenB_reward)


'''def for_A51_token_staked(number_of_days_user_staked, number_of_users, total_reward_to_be_distributed, days_in_which_reward_will_be_distributed):
    
    random_amounts, weightage_values = calculate_weightage(number_of_users)

    print("\nUser-Input A51 Token Amounts:")
    for amount in random_amounts:
        print(amount)

    print("\nWeightage values:")
    for value in weightage_values:
        print(value)

    # Calculate the A51 reward rate
    a51_reward_rate = calculate_reward_rate(total_reward_to_be_distributed, days_in_which_reward_will_be_distributed)

    # Print the result
    print("\nA51 Token Reward Rate:", a51_reward_rate)


    final_rewards = []  # Initialize a list to store final rewards for each user

    # Calculate final_rewards for each user based on weightage, reward rate, and days staked
    for i in range(number_of_users):
        user_final_reward = a51_reward_rate * weightage_values[i] * number_of_days_user_staked
        final_rewards.append(user_final_reward)

    return final_rewards

# Example usage:
number_of_users = 3  # Replace with the desired number of users
number_of_days_user_staked = 30  # Replace with the actual number of days staked
reward_to_be_distributed = 1000.0  # Replace with the total reward to be distributed
days_in_which_reward_will_be_distributed = 30  # Replace with the actual number of days for reward distribution

final_rewards = for_A51_token_staked(number_of_days_user_staked, number_of_users, reward_to_be_distributed, days_in_which_reward_will_be_distributed)

# Print the final rewards for each user
for i, reward in enumerate(final_rewards):
    print(f"User {i + 1} Final Reward:", reward)
'''