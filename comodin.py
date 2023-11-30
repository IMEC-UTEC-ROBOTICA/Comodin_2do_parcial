import sympy as sp

def Tdh(d, th, a, alpha):
    cth = sp.cos(th); sth = sp.sin(th)
    ca = sp.cos(alpha); sa = sp.sin(alpha)
    Tdh = sp.Matrix([[cth, -ca*sth, sa*sth, a*cth],
                    [sth, ca*cth, -sa*cth, a*sth],
                    [0, sa, ca, d],
                    [0, 0, 0, 1]])
    return Tdh

# Variables simbólicas
q1, q2, d3, q4 = sp.symbols("q1 q2 d3 q4")
l1, l2, l3, l4 = sp.symbols("l1 l2 l3 l4")
# Transformaciones homogéneas
T01 = Tdh(l1, sp.pi+q1, l2, 0)
T12 = Tdh(0,-sp.pi/2+q2, l3, 0)
T23 = Tdh(-l4+d3, 0, 0, 0)
T34 = Tdh(0, sp.pi/2+q4, 0, sp.pi)
Tf = sp.simplify(T01*T12*T23*T34)

def calcular_pos(val_q1,val_q2,val_d3,val_q4):
    # Asignar valores específicos a los parámetros
    Mov=Tf.subs([(q1, val_q1),(q2, val_q2),(d3, val_d3),(q4, val_q4)])
    print("Matriz resultante: ")
    print("[")
    for row in range(0,4):
        for col in range(4):
            el=str(Mov.row(row).col(col)[0])
            espacio=(18-len(el))*" "
            print(f"  {el} {espacio},", end="")
        print()
    print("]")
    coord_x=Mov.row(0).col(-1)[0]
    coord_y=Mov.row(1).col(-1)[0]
    coord_z=Mov.row(2).col(-1)[0]
    print("Cooredenadas del efector")
    print(f"x: {coord_x}")
    print(f"y: {coord_y}")
    print(f"z: {coord_z}")

def rad(angulo):
    return angulo*sp.pi/180

#calcular_pos(rad(180), rad(90), 0.2, rad(45)) #(180º ; 90º ; 0,20m ; 45º) 
#calcular_pos(rad(45),rad(45),0.1,0) #(45º ; 45º; 0,10m ; 0º ) 
#calcular_pos(rad(30),rad(45),0.25,rad(60)) #(30º ; 45º; 0,25m ; 60º )
#calcular_pos(rad(30),rad(60),0.15,0) #(30º ; 60º; 0,15m ; 0º ) 
#calcular_pos(rad(45),rad(90),0.20,rad(180)) #(45º ; 90º; 0,20m ; 180º ) 
#calcular_pos(rad(30),rad(90),0.20,rad(180)) #(30º ; 60º; 0,20m ; 90º )
calcular_pos(rad(30),rad(90),0.20,rad(180)) #(30º ; 60º; 0,20m ; 90º )









