def calculate_weightage(number_of_users):
    amounts = []  # Initialize an empty list to store user-input amounts

    # Input amounts for all users
    for i in range(number_of_users):
        while True:
            try:
                # amounts = [random.uniform(1, 10000) for _ in range(number_of_users)]
                amount = float(input(f"Enter dollar amount for person {i + 1}: ")) # dollar amount = A51 token quantity or NFT
                break  # Exit the loop if a valid float is entered
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        amounts.append(amount)  # Add the user-input amount to the list

    # Calculate the sum of all amounts
    total_amount = sum(amounts)

    # Calculate the weightage for each person
    weightage = [amount / total_amount for amount in amounts]

    return amounts, weightage

def calculate_reward_rate(total_reward_to_be_distributed, days_in_which_reward_will_be_distributed):
    # Calculate the reward rate for given time period
    blocks_in_a_day = 7144 # This should not be constant
    
    reward_rate = total_reward_to_be_distributed / (blocks_in_a_day * days_in_which_reward_will_be_distributed)  # Can assuming 30 days in a month
    
    return reward_rate

# 1. User stakes A51 tokens, is eligible for ETH rewards
def for_A51_token_staked():
    number_of_users = int(input("\nEnter the number of users: "))
    number_of_days_user_staked = []  # Initialize a list to store staked days for each user

    for i in range(number_of_users):
        while True:
            try:
                days_staked = int(input(f"Enter the number of days staked for User {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        number_of_days_user_staked.append(days_staked)

    random_amounts, weightage_values = calculate_weightage(number_of_users)

    print("\nUser-Input A51 Token Amounts: ")
    for amount in random_amounts:
        print(amount)

    print("\nWeightage values: ")
    for value in weightage_values:
        print(value)

    total_ETH_reward_to_be_distributed = float(input("\nEnter the total ETH reward to be distributed: "))
    days_in_which_reward_will_be_distributed = int(input("\nEnter the number of days in for total reward distribution: "))

    # Calculate the ETH reward rate
    eth_reward_rate = calculate_reward_rate(total_ETH_reward_to_be_distributed, days_in_which_reward_will_be_distributed)

    # Print the result
    print("\nA51 Token Reward Rate:", eth_reward_rate)

    final_rewards = []  # Initialize a list to store final rewards for each user

    # Calculate final_rewards for each user based on weightage, reward rate, and days staked
    for i in range(number_of_users):
        user_final_reward = weightage_values[i] * eth_reward_rate * number_of_days_user_staked[i] * 7144
           
        # Print information about each user's calculation
        print(f"For user {i + 1}:")
        print(f"- Weightage: {weightage_values[i]}")
        print(f"- Number of days staked: {number_of_days_user_staked[i]}")
        print(f"- Final Reward: {user_final_reward}\n")
        final_rewards.append(user_final_reward)

    return final_rewards

# 3. User stakes A51 tokens and whitelisted NFT (ERC721), is eligible for veA51 token, ETH rewards (token A), A51 rewards (token B)
def for_anyNFT_and_A51_token_staked():
    days_in_which_reward_will_be_distributed = int(input("\nEnter the number of days in which total rewards (both A51 and ETH) will be distributed: "))
    number_of_users = int(input("\nEnter the number of users: "))
    number_of_days_user_staked = []  # Initialize a list to store staked days for each user

    for i in range(number_of_users):
        while True:
            try:
                days_staked = int(input(f"Enter the number of days staked for User {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        number_of_days_user_staked.append(days_staked)


#TOKEN A (staked A51 and will recieve ETH as rewards)
    print("\nFor A51: ")
    random_amounts_A, weightage_values_A = calculate_weightage(number_of_users)

    print("\nUser-Input A51 Token Amounts: ")
    for amount in random_amounts_A:
        print(amount)

    print("\nWeightage values: ")
    for value in weightage_values_A:
        print(value)

    total_ETH_reward_to_be_distributed = float(input("\nEnter the total ETH rewards to be distributed: "))
    
    # Calculate the ETH reward rate
    eth_reward_rate = calculate_reward_rate(total_ETH_reward_to_be_distributed, days_in_which_reward_will_be_distributed)

    # Print the result
    print("\nETH Token Reward Rate:", eth_reward_rate)

#TOKEN B (staked NFT and will recieve A51 as rewards)
    print("\nFor ETH: ")
    random_amounts_B, weightage_values_B = calculate_weightage(number_of_users)

    print("\nUser-Input NFT dollar value Token Amounts: ")
    for amount in random_amounts_B:
        print(amount)

    print("\nWeightage values: ")
    for value in weightage_values_B:
        print(value)

    total_A51_reward_to_be_distributed = float(input("\nEnter the total A51 rewards to be distributed: "))
    
    # Calculate the A51 reward rate
    a51_reward_rate = calculate_reward_rate(total_A51_reward_to_be_distributed, days_in_which_reward_will_be_distributed)

    # Print the result
    print("\nA51 Token Reward Rate:", a51_reward_rate)


    rewards_A_weightage_factor = []  # Initialize a list to store weightage factor for each user for Token A
    rewards_B_weightage_factor = []  # Initialize a list to store weightage factor for each user for Token B

    print("\n")
    # Calculate final weightage factor for each user based on weightage and days staked for Token A
    for i in range(number_of_users):
        user_reward_A_weightage_factor = (weightage_values_A[i]) * 0.6
        print(f"User {i + 1} reward A weightage_factor: ", user_reward_A_weightage_factor) 
        rewards_A_weightage_factor.append(user_reward_A_weightage_factor)
    print("\n")
    # Calculate final weightage factor for each user based on weightage and days staked for Token A
    for i in range(number_of_users):
        user_reward_B_weightage_factor = (weightage_values_B[i]) * 0.4
        print(f"User {i + 1} reward B weightage_factor: ", user_reward_B_weightage_factor)
        rewards_B_weightage_factor.append(user_reward_B_weightage_factor)

    # Calculate final rewards for each user
    final_A51_rewards = [] 
    final_ETH_rewards = []

    for i in range(number_of_users):
        user_final_reward = (rewards_A_weightage_factor[i] + rewards_B_weightage_factor[i]) * a51_reward_rate * number_of_days_user_staked[i] * 7144
        final_A51_rewards.append(user_final_reward)

    for i in range(number_of_users):
        user_final_reward = weightage_values_A[i] * eth_reward_rate * number_of_days_user_staked[i] * 7144
        final_ETH_rewards.append(user_final_reward)

    return final_A51_rewards, final_ETH_rewards

# 2. User stakes A51/ETH pair NFT, is eligible for veA51 token, ETH rewards (token A), A51 rewards (token B)

def for_a51ethNFT_token_staked():
    number_of_users = int(input("\nEnter the number of users: "))
    number_of_days_user_staked = []  # Initialize a list to store staked days for each user

    for i in range(number_of_users):
        while True:
            try:
                days_staked = int(input(f"Enter the number of days staked for User {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        number_of_days_user_staked.append(days_staked)

    days_in_which_reward_will_be_distributed = int(input("\nEnter the number of days in which total rewards (both A51 and ETH) will be distributed: "))
    total_ETH_reward_to_be_distributed = float(input("\nEnter the total ETH rewards to be distributed: ")) 
    # Calculate the ETH reward rate
    eth_reward_rate = calculate_reward_rate(total_ETH_reward_to_be_distributed, days_in_which_reward_will_be_distributed)
    # Print the result
    print("\nETH Token Reward Rate:", eth_reward_rate)

    total_A51_reward_to_be_distributed = float(input("\nEnter the total A51 rewards to be distributed: "))
    # Calculate the A51 reward rate
    a51_reward_rate = calculate_reward_rate(total_A51_reward_to_be_distributed, days_in_which_reward_will_be_distributed)
    # Print the result
    print("\nA51 Token Reward Rate:", a51_reward_rate)

#TOKEN B (staked A5I/ETH NFT and will recieve both A51 and ETH as rewards)
    print("\nFor ETH: ")
    random_amounts_B, weightage_values_B = calculate_weightage(number_of_users)

    print("\nUser-Input NFT dollar value Token Amounts: ")
    for amount in random_amounts_B:
        print(amount)
    print("\nWeightage values: ")
    for value in weightage_values_B:
        print(value)


    rewards_A_weightage_factor = []  # Initialize a list to store weightage factor for each user for Token A
    rewards_B_weightage_factor = []  # Initialize a list to store weightage factor for each user for Token B

    print("\n")
    # Calculate final weightage factor for each user based on amount staked and days staked, for Token reward A (A51)
    for i in range(number_of_users):
        user_reward_A_weightage_factor = (weightage_values_B[i]) * 0.3
        print(f"User {i + 1} reward A weightage_factor: ", user_reward_A_weightage_factor) 
        rewards_A_weightage_factor.append(user_reward_A_weightage_factor)
    print("\n")
    # Calculate final weightage factor for each user based on amount staked and days staked, for Token reward A (A51)
    for i in range(number_of_users):
        user_reward_B_weightage_factor = (weightage_values_B[i]) * 0.7
        print(f"User {i + 1} reward B weightage_factor: ", user_reward_B_weightage_factor)
        rewards_B_weightage_factor.append(user_reward_B_weightage_factor)

    # Calculate final rewards for each user
    final_A51_rewards = [] 
    final_ETH_rewards = []

    for i in range(number_of_users):
        user_final_reward = rewards_B_weightage_factor[i] * a51_reward_rate * number_of_days_user_staked[i] * 7144
        final_A51_rewards.append(user_final_reward)

    for i in range(number_of_users):
        user_final_reward = rewards_A_weightage_factor[i] * eth_reward_rate * number_of_days_user_staked[i] * 7144
        final_ETH_rewards.append(user_final_reward)

    return final_A51_rewards, final_ETH_rewards

# 4. Combine function  
def combine_rewards_distribution():
    days_in_which_reward_will_be_distributed = int(input("\nEnter the number of days in which total rewards (both A51 and ETH) will be distributed: "))
    
    total_ETH_reward_to_be_distributed = float(input("\nEnter the total ETH rewards to be distributed: ")) 
    
    # Calculate the ETH reward rate
    eth_reward_rate = calculate_reward_rate(total_ETH_reward_to_be_distributed, days_in_which_reward_will_be_distributed)
    # Print the result
    print("\nETH Token Reward Rate:", eth_reward_rate)
    total_A51_reward_to_be_distributed = float(input("\nEnter the total A51 rewards to be distributed: "))

    # Calculate the A51 reward rate
    a51_reward_rate = calculate_reward_rate(total_A51_reward_to_be_distributed, days_in_which_reward_will_be_distributed)
    # Print the result
    print("\nA51 Token Reward Rate:", a51_reward_rate)
    
    number_of_users = int(input("\nEnter the number of users: "))
    
    # Initialize lists to store user data
    user_staking_choices = []
    user_days_staked = []
    user_nft_dollar_amounts = []
    user_a51_dollar_amounts = []

    for i in range(number_of_users):
        # Choose "O" for original NFT and "W" for whitelisted NFT
        while True:
            choice = input(f"User {i + 1}, choose 'O' for original NFT or 'W' for whitelisted NFT: ").strip().upper()
            if choice in ('O', 'W'):
                user_staking_choices.append(choice)
                break
            else:
                print("Invalid choice. Please enter 'O' for original NFT or 'W' for whitelisted NFT.")
        
        # Initialize variables to collect NFT and A51 dollar amounts
        nft_dollar_amount = 0.0
        a51_dollar_amount = 0.0

        # If the user chose "O" for original NFT, collect additional information
        if user_staking_choices[i] == 'O':
            days_staked = int(input(f"Enter the number of days for the token to be staked, for User {i + 1}: "))
            user_days_staked.append(days_staked)
            
            nft_dollar_amount = float(input(f"Enter the NFT dollar amount to be staked for User {i + 1}: "))

            # Append the collected NFT dollar amounts 
            user_nft_dollar_amounts.append(nft_dollar_amount)

        # If the user chose "W" for whitelisted NFT, collect additional information
        elif user_staking_choices[i] == 'W':
            days_staked = int(input(f"Enter the number of days for the token to be staked, for User {i + 1}: "))
            user_days_staked.append(days_staked)
            
            nft_dollar_amount = float(input(f"Enter the NFT dollar amount to be staked for User {i + 1}: "))
            a51_dollar_amount = float(input(f"Enter the A51 dollar amount to be staked for User {i + 1}: "))
            
            # Append the collected NFT and A51 dollar amounts    
            user_nft_dollar_amounts.append(nft_dollar_amount)
            user_a51_dollar_amounts.append(a51_dollar_amount)

    # Calculate sum of NFT and A51 dollar amounts
    total_nft_dollar_amounts = sum(user_nft_dollar_amounts)
    total_a51_dollar_amounts = sum(user_a51_dollar_amounts)
    
    # Calculate weightage for each user
    weightage_nft = [amount / total_nft_dollar_amounts for amount in user_nft_dollar_amounts]
    weightage_a51 = [amount / total_a51_dollar_amounts for amount in user_a51_dollar_amounts]

    # Initialize lists to store user rewards
    user_final_a51_rewards = []
    user_final_eth_rewards = []

    # Calculate rewards for each user based on staking choice
    for i in range(number_of_users):
        if user_staking_choices[i] == 'O':
            final_a51_rewards = (weightage_nft[i] * 0.7) * eth_reward_rate * user_days_staked[i] * 7144
            final_eth_rewards = (weightage_nft[i] * 0.3) * a51_reward_rate * user_days_staked[i] * 7144
        elif user_staking_choices[i] == 'W':
            weightageA = weightage_a51[i] * 0.6
            weightageB = weightage_nft[i] * 0.4
            final_a51_rewards = (weightageA + weightageB) * a51_reward_rate * user_days_staked[i] * 7144
            final_eth_rewards = (weightage_a51[i]) * eth_reward_rate * user_days_staked[i] * 7144

        user_final_a51_rewards.append(final_a51_rewards)
        user_final_eth_rewards.append(final_eth_rewards)
    
    '''
    # Print the collected NFT dollar amounts and A51 dollar amounts 
    print("\nUser NFT Dollar Amounts:") 
    for i, amount in enumerate(user_nft_dollar_amounts):
        print(f"User {i + 1} NFT staked:", amount)

    print("\nUser A51 Dollar Amounts:")
    for i, amount in enumerate(user_a51_dollar_amounts):
        print(f"User {i + 1} A51 staked:", amount)

    # Print the calculated weightage for each user
    print("\nWeightage for NFT:")
    for i, w in enumerate(weightage_nft):
        print(f"User {i + 1} weightage:", w)

    print("\nWeightage for A51:")
    for i, w in enumerate(weightage_a51):
        print(f"User {i + 1} weightage:", w)
    '''

    return user_final_a51_rewards, user_final_eth_rewards

            

'''
print("\n**************************************************************************************************************************************")

print("\n1. Final Rewards for users who staked A51 tokens and received ETH as rewards")
final_rewards = for_A51_token_staked()

# Print the final rewards for each user
for i, reward in enumerate(final_rewards):
    print(f"User {i + 1} Final Reward:", reward)

print("\n**************************************************************************************************************************************")

print("\n3. Final Rewards for users who staked both A51 tokens and whitelisted NFT ERC721 tokens, and received veA51 token ID, ETH rewards (token A), A51 rewards (token B)")
final_A51_rewards, final_ETH_rewards = for_anyNFT_and_A51_token_staked()

# Print the final rewards for each user
print("\n")
for i, reward in enumerate(final_A51_rewards):
    print(f"User {i + 1} Final A51 Reward:", reward)
print("\n")
for i, reward in enumerate(final_ETH_rewards):
    print(f"User {i + 1} Final ETH Reward:", reward)

print("\n**************************************************************************************************************************************")

print("\n2. Final Rewards for users who staked A51/ETH pair NFT, and received veA51 token ID, ETH rewards (token A), A51 rewards (token B)")
final_A51_rewards, final_ETH_rewards = for_a51ethNFT_token_staked() 

# Print the final rewards for each user
print("\n")
for i, reward in enumerate(final_A51_rewards):
    print(f"User {i + 1} Final A51 Reward:", reward)
print("\n")
for i, reward in enumerate(final_ETH_rewards):
    print(f"User {i + 1} Final ETH Reward:", reward)

print("\n**************************************************************************************************************************************")
'''
# Call the function to start the process
print("\n4. Users can either stake A51/ETH pair NFT or any other whitelisted NFT. ")
user_final_a51_rewards, user_final_eth_rewards = combine_rewards_distribution()

# Print the calculated rewards for each user
print("\nUser Final A51 Rewards:")
for i, reward in enumerate(user_final_a51_rewards):
    print(f"User {i + 1} final A51 claimable rewards:", reward)

print("\nUser Final ETH Rewards:")
for i, reward in enumerate(user_final_eth_rewards):
    print(f"User {i + 1} final ETH claimable rewards:", reward)