som = 0;
for x in range(0,1000,1):
    if (x%3 == 0 or x%5==0):
        som += x;
print(som)