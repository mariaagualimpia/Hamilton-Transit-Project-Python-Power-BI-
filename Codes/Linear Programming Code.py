import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp
# Define the solver

solver = pywraplp.Solver.CreateSolver('SCIP')
#Assign Indices

I = 3 #Route i
J = 2 #1 Weekend or 0 weekday j
K = 4 #Season k
B = 2 #Type of bus b

#Parameters


Demand = [[[76,143,353,156],[163,306,756,335]],
          [[249,465,1151,510],[533,998,2467,1093]],
          [[83,156,386,171],[179,335,827,366]]] #Dijk / 4k,
Co2_Emission = [1.4,1.45] #COb
RouteDistance = [46,46,82] #Li #Kilograms of CO2 per km
BusCapacity = [70, 120] #Kb
MaxRoute = [24,21,13] #MaxR i

Seasons = ['Winter', 'Spring', 'Summer', 'Fall']
#Variables

X= {}

for i in range(I):
  for j in range(J):
    for k in range(K):
      for b in range(B):
          X[i,j,k,b] = solver.IntVar(0, solver.infinity(), f'X{i},{j},{k},{b}')

#Objective Function
objective = solver.Objective()
for i in range(I):
  for j in range(J):
    for k in range(K):
      for b in range(B):
        objective.SetCoefficient(X[i,j,k,b], RouteDistance[i]*Co2_Emission[b])


objective.SetMinimization()

#Constraints

#Demand
for i in range(I):
  for j in range(J):
    for k in range(K):
      solver.Add(Demand[i][j][k] <= sum(X[i,j,k,b]*BusCapacity[b] for b in range(B)))

#Frequency of routes
for i in range(I):
  for j in range(J):
    for k in range(K):
      solver.Add(sum(X[i,j,k,b] for b in range(B)) <= MaxRoute[i])


  # Solve the problem
  status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
  print('Optimal solution found!')
  print(f'Total KG of CO2 Emissions = {format(solver.Objective().Value(), ",")}')
  print(f'\n\nTrips Assigned')
  for j in range (J):
    if j == 0:
      print(f"\n Weekdays:\n")
      text = '\t\t'
      for b in range(B):
        text = text + f'| Bus type {b+1} \t\t\t\t\t\t'
      print(text)
      text = ''
      for i in range(I):
        text = text + f'| Route {i + 1}\t'
      print('\t\t'+text+text)
      for k in range(K):
        text = f' {Seasons[k]}\t'
        for b in range (B):
          for i in range(I):
            text = text + f'| {X[i, j, k, b].solution_value()}\t\t'
        print(text)
    else:
      print(f"\n Weekends:\n")
      text = '\t\t'
      for b in range(B):
        text = text + f'| Bus type {b+1} \t\t\t\t\t\t'
      print(text)
      text = ''
      for i in range(I):
        text = text + f'| Route {i + 1}\t'
      print('\t\t'+text+text)
      for k in range(K):
        text = f' {Seasons[k]}\t'
        for b in range (B):
          for i in range(I):
            text = text + f'| {X[i, j, k, b].solution_value()}\t\t'
        print(text)