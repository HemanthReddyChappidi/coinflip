import random
doublets = ['HH', 'HT', 'TH', 'TT']
num_simulations = 1000 
results = {'HH': 0, 'HT': 0, 'TH': 0, 'TT': 0}
for _ in range(num_simulations):
    doublet_result = random.choice(doublets)
    results[doublet_result] += 1
total_simulations = float(num_simulations)
percentages = {doublet: count / total_simulations * 100 for doublet, count in results.items()}
for doublet, percentage in percentages.items():
    print(f"{doublet}: {percentage:.2f}%")

