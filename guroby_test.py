from gurobipy import Model, GRB

# Crea un modello
model = Model("test")

# Aggiungi variabili
x1 = model.addVar(name="x1")
x2 = model.addVar(name="x2")

# Imposta la funzione obiettivo
model.setObjective(x1 + x2, GRB.MAXIMIZE)

# Aggiungi vincoli
model.addConstr(x1 + 2 * x2 <= 10, "c0")

# Ottimizza il modello
model.optimize()

# Stampa i risultati
for v in model.getVars():
    print(f'{v.varName} {v.x}')

print(f'Obj: {model.objVal}')