lut = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
string="MCMXCIV"
sum=0
for i in range(len(string)):
    if i+1<len(string) and lut[string[i]]<lut[string[i+1]]:
        sum-=lut[string[i]]
    else:
        sum+=lut[string[i]]

print(sum)