def globalAndLocalVars():
    global g
    g=5
    x=2
g="one"
x="two"
globalAndLocalVars()
print("g: ", g)
print("x: ", x)
