
import math

classes = input("How many classes?\n")
while type(classes)== str:
    try:
        classes = int(classes)
    except:
        print("Must be an integer.\n")
        classes = input("How many classes?\n")

# 5,24,23,10,21,29,0,21,2,22,25,12,26,17,24,2,19,0,12,2

# Assumes the list is of integers
data = input("Input your list, separated by commas.\n")
data = data.split(',')
# Casts to int from string, could be float or else
data = [int (m) for m in data]
# Sorts by size small to large
data.sort()

entries = len(data)
if entries % 2 == 1:
    median = data[int((entries+1)/2)]
else:
    mm = int(entries / 2)
    mp = mm + 1
    median = (data[mm] + data[mp]) / 2

md = {}
mn = 0
for c in data:
    if c not in md:
        md.update({c:[data.index(c)]})
    else:
        md[c].append(data.index(c))
    
for b in md:
    i = len(md[b])
    if i > mn:
        mode = b
        mn = i



frequency = entries / classes

s = int(data[0])
g = int(data[-1])
r = g - s
w = math.ceil(r / classes)
m = 0
for d in data:
    m = float(d)+ m
m = m / entries

minusmean = []
minusmeansquared = []
for q in data:
    minusmean.append(q - m)
    minusmeansquared.append((q - m) ** 2)

summinusmeansquared = 0 
for k in minusmeansquared:
    summinusmeansquared = k + summinusmeansquared

pop_variance = summinusmeansquared / entries
pop_std_deviation = math.sqrt(pop_variance)

sample_variance = summinusmeansquared / (entries - 1)
sample_std_deviation = math.sqrt(sample_variance)



print("\nMinimum:",s,'\nMaximum:',g,'\nMean:',m,"\nRange:",r,'\nMedian:',median,'\nMode:',mode,'\nClass Width:',w)
print("Population Variance:",pop_variance,"\nPopulation Standard Deviation:",pop_std_deviation,"\nSample Variance:",sample_variance,"\nSample Standared Deviation:",sample_std_deviation)



# print("\nFrequency Distribution:\n")
cumulative_frequency = 0
for v in range(classes):
    low = s + (v * w) 
    up = s + (v * w) + (w - 1)
    mid = (up + low) / 2
    freq = 0
    
    for q in data:
        if q >= low and q <= up:
            freq += 1
    relative_frequency = freq / entries
    cumulative_frequency = freq + cumulative_frequency
    # print("Lower limit:",low,'\nUpper Limit:',up,'\nFrequency:',freq,'\nMidpoint:',mid,'\nRelative Frequency:',relative_frequency,'\nCumulative Frequency:',cumulative_frequency,'\n\n')


print(classes,
data,
)
# 47,35,44,46,44,44,44,39,40,47,44,47,47,40