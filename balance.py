def solution(A, D):
    transactions = {}
    total_income = 0
    total_expenses = 0
    
    for amount, date in zip(A, D):
        year, month, _ = date.split('-')
        key = f"{year}-{month}"
        
        transactions[key] = transactions.get(key, 0) + amount
        
        if amount >= 0:
            total_income += amount
        else:
            total_expenses += amount
    
    total_fee = sum(5 for amount in transactions.values() if amount < -5)
    
    final_balance = total_income + total_expenses - total_fee
    return final_balance

# Example usage:
A1 = [100, 100, 100, -10]
D1 = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]
print(solution(A1, D1))  

A2 = [180, -50, -25, -25]
D2 = ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]
print(solution(A2, D2))  

A3 = [-1, -1, 0, -105, 1]
D3 = ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]
print(solution(A3, D3))  

A4 = [100, 100, -10, -20, -30]
D4 = ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]
print(solution(A4, D4))  

A5 = [60, 60, -40, -20]
D5 = ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]
print(solution(A5, D5))  
