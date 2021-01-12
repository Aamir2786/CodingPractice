"""
@author: aamir
"""
import sys
def printFilteredData(fp_input):
    interval = {"I1":[], "I2":[], "I3":[], "I4":[], "I5":[]}        # Using Dictionary data structures (like map in CPP) to create 5 subset intervals.
    minss = sys.maxsize
    for i in fp_input:      #  We store numbers in its appropriate interval, ex : numbers between 0.2 and 0.4(not included) are placed in second subset interval(I2)
        if 0 <= i < 0.2:
            interval["I1"].append(i)
        elif 0.2 <= i < 0.4:
            interval["I2"].append(i)
        elif 0.4 <= i < 0.6:
            interval["I3"].append(i)
        elif 0.6 <= i < 0.8:
            interval["I4"].append(i)
        elif 0.8 <= i < 1.0:
            interval["I5"].append(i)
    for i in range(1,6):        # Here we find the minimum subset size(minss)
        k = "I" + str(i)
        ilen = len(interval[k])
        if minss > ilen:
            minss = ilen

    print("Output: ", end = "")
    for i in range(1,6):
        k = "I" + str(i)
        subset = interval[k]
        del subset[minss:]      # Now we delete the extra elements from each subsets to make it equal to "minss"
        slen = len(subset)
        for j in range(slen):
            if i == 5:
                if j == slen-1:
                    print(subset[j])
            else:
                print(subset[j], end = ",")

if __name__ == "__main__":
    inp = input()
    print("Input: {}".format(inp))
    fp_input = [float(x) for x in inp.split(",")]
    printFilteredData(fp_input)