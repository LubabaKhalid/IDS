def find_unique_users(transactions):
    
    unique_users = set()  
    for transaction in transactions:
        unique_users.add(transaction[1])  
    return len(unique_users)

def highest_transaction(transactions):
    highest=transactions[0]
    for transcation in transactions:
        if transcation[2]>highest[2]:
            highest=transcation
    return highest
        

def separate_ids(transactions):
   
    transaction_ids = []
    user_ids = []
    
    for transaction in transactions:
        if len(transaction) != 4:
            raise ValueError(f"Inconsistent tuple size: {transaction}")
        transaction_ids.append(transaction[0])  
        user_ids.append(transaction[1])  
    
    return transaction_ids, user_ids

transactions_data = [
    (101, 'user1', 150.75, '2024-10-01 10:23:45'),
    (102, 'user2', 320.60, '2024-10-01 11:12:30'),
    (103, 'user3', 50.25, '2024-10-02 09:50:22'),
    (104, 'user2', 450.00, '2024-10-02 14:15:10'),
    (105, 'user1', 120.00, '2024-10-03 08:05:30')
]
unique_user_count = find_unique_users(transactions_data)
print("Total Unique Users:", unique_user_count)
highest_tx = highest_transaction(transactions_data)
print("Transaction with the Highest Amount:", highest_tx)
transaction_ids, user_ids = separate_ids(transactions_data)
print("Transaction IDs:", transaction_ids)
print("User IDs:", user_ids)
