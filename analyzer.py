from parser_ import parse
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def main():
    data = parse()
    Spearman(data)
    regression(data)

def Spearman(data):
    ordering = make_ordering(data)
    print(ordering)
    n = len(ordering)
    rs = 1 - 6/(n * (n**2 - 1)) * sum((P-R)**2 for P,R in ordering)
    print(f"statistic: {np.abs(rs)}")
    a = 2.33/np.sqrt(n-1)
    print(f"critical value: {a}")

def regression(data):
    temperatures = []
    temperatures_bias = []
    deaths = []
    for d in data:
        temperatures.append(d[0])
        temperatures_bias.append([d[0], 1])
        deaths.append(d[1])
    model = sm.OLS(deaths, temperatures_bias).fit()
    print(model.summary())
    print("P-value: " + str(model.pvalues[1]))
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_ylabel('deaths')
    ax.set_xlabel('temperature')
    plt.plot(temperatures, deaths, "bo")
    plt.plot(temperatures, model.predict(temperatures_bias), "--r")
    plt.show()


def make_ordering(data):
    ordering =[]
    data.sort()
    for i,d in enumerate(data):
        ordering.append([i+1,d[1]])
    ordering.sort(key=takeSecond)
    for i,o in enumerate(ordering):
        o[1] = i+1
    return ordering

def takeSecond(elem):
    return elem[1]

if __name__ == "__main__":
    main()