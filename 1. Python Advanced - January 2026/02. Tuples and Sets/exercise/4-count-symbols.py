occurences = {}

for symbol in input():
    occurences[symbol] = occurences.get(symbol, 0) + 1
    
for symbol, count in sorted(occurences.items()):
    print(f"{symbol}: {count} time/s")