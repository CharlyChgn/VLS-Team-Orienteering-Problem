import sys
import math

def checker(instanceName, solutionName):

    # =======================================
    # READ INSTANCE FILE
    # =======================================
    # instanceName="rd400_gen1_m2.txt"
    lines = []
    with open(instanceName) as file:
        lines = [line.rstrip() for line in file]

    # =======================================
    # GET NEEDED INFORMATIONS
    # n : number of points
    # tmax : time limit
    # x-y : coordinates of all vertices
    # profit : profit of all vertices
    # =======================================
    n = 0
    tmax=0
    x=[]
    y=[]
    profit=[]
    for i in range(0,len(lines)) :
        array = lines[i].split(" ")
        if i == 0:
            n = int(array[1])
        if i == 2 :
            tmax = float(array[1])
        if i > 2 :
            x.append(float(array[0]))
            y.append(float(array[1]))
            profit.append(float(array[2]))

    # =======================================
    # READ SOLUTION FILE
    # =======================================
    # solutionName="rd400_gen1_m2_Solution.txt"
    lines = []
    with open(solutionName) as file:
        lines = [line.rstrip() for line in file]

    # =======================================
    # BUILD SOLUTION BASED ON THE GIVEN FILE
    # =======================================
    sol=[]
    for i in range(0,len(lines)) :
        array = lines[i].split(",")
        if i%2 != 0:
            route = []
            for j in range(0,len(array)):
                # first vertice = depot
                if j == 0 :
                    route.append(0)
                # last vertice = depot
                elif j == len(array)-1:
                    route.append(n-1)
                else :
                    route.append(int(array[j]))
            sol.append(route)

    # =======================================
    # New best known solution criteria
    # =======================================

    # =======================================
    # TOTAL PROFIT
    # =======================================
    prof = 0
    totalCostPerVehicle = []
    test = True
    # PROFIT
    for j in range(0,len(sol)):
        for i in range(0,len(sol[j])):
            prof+=profit[sol[j][i]]

    # =======================================
    # COST PER VEHICLE
    # =======================================
    for j in range(0,len(sol)):
        totalCostPerVehicle.append(0)
        for i in range(0,len(sol[j])-1):
            totalCostPerVehicle[j]+=math.sqrt(pow((x[sol[j][i]]-x[sol[j][i+1]]),2)+pow((y[sol[j][i]]-y[sol[j][i+1]]),2))
        if totalCostPerVehicle[j]>tmax:
            test=False

    # =======================================
    # DISPLAY
    # =======================================
    print("Solution's profit : ",prof)
    print("Cost of every builded route : \n",totalCostPerVehicle)
    # check time limit
    if test:
        print("The solution respect the time limit of ", tmax)
    else:
        print("The solution is not feasible with respect to the time limit of ",tmax)


def main():
    instanceName=""
    solutionName=""
    if len(sys.argv) == 5:
        for i in range(0,len(sys.argv)):
            if sys.argv[i] == '-i':
                instanceName=sys.argv[i+1]
            elif sys.argv[i] == '-s':
                solutionName=sys.argv[i+1]

    else:
        print("INVALID NUMBER OF ARGUMENTS : ONLY NEED THE INSTANCE FILE (-i 'name') AND THE SOLUTION FILE (-s 'name')")

    print("Instance file : ", instanceName)
    print("Solution file : ", solutionName)

    checker(instanceName,solutionName)


if __name__ == '__main__':
    main()
