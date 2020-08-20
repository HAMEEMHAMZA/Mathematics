#code written by Hameem C Hamza
#Date 20 August 2020
import numpy as np
import matplotlib.pyplot as plot 
from math import log10, floor 

start = 1
end = 999
len1 = end - start + 1
repitition_matrix = np.zeros([len1,9])
cumulative_repitition_matrix = np.zeros([len1,9])
probability_matrix = np.zeros([len1,9])

#find starting digit
for i in range(len1):
    number = i+start
    significant_digit = floor(number / (10**floor(log10(number))))
    repitition_matrix[i,(significant_digit-1)] = repitition_matrix[i,(significant_digit-1)] + 1
    print(significant_digit)
#calulate cumulative repitition
for i in range(len1):
    for j in range(9):
        cumulative_repitition_matrix[i,j] = np.sum(repitition_matrix[0:i,j]  )
        probability_matrix[i,j] = 100* cumulative_repitition_matrix[i,j] / (i+1)

#plot
for i in range(9):
    plot.plot(probability_matrix[:,i])
    

plot.title('% Probability of a number starting with a PARTICULAR DIGIT Vs PRESET MAX VALUE- ALL NUMBERS HAVE EQUAL probability')
#generate legend array of string
legend_array = ["1"]
for i in range(8):
    legend_array.append( str(i+2) ) 

#calculate average probability
average_probability = np.zeros(9)
for i in range(9):
    average_probability[i] = np.mean(probability_matrix[:,i])

#more plot handles
plot.legend(legend_array)
plot.xlabel("PRESET MAX SET VALUE")
plot.ylabel(" % Probability that any number start with a PARTICULAR DIGIT")
#print average on plot
for i in range(10):
    if i==0:
        str1 = 'AVERAGE OVER ENTIRE RANGE'
    else:
        str1 = str(i) + ' = ' + str( int(average_probability[i-1])  ) + '%'
    x1= int(end*0.7)
    y1= int( np.max(probability_matrix) * 0.9) - i* 3
    plot.text(x1,y1,str1, fontsize = 15)
plot.show()


