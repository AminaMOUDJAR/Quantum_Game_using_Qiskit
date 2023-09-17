from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister 
from qiskit import execute, assemble , BasicAer
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor

### tic toc toe ###

######################################
#           #             #          #   
#     6     #     7       #    8     # 
#           #             #          # 
######################################
#           #             #          # 
#     3     #     4       #    5     # 
#           #             #          # 
######################################
#           #             #          #  
#     0     #     1       #     2    #   
#           #             #          # 
######################################

"""
    By default player1 tiles are initilized 
    to 0 state
# Player2 tiles initialized |1> state
"""
    
l_player_1 = [0]
l_player_2 = [2,3]
l_entangled = [(1,6),(7,8),(4,5)]


#translate from lists to initial state matrix
l_initial_ordered = [0,0,0,0,0,0,0,0,0]
for inx in range(len(l_player_1)):
    l_initial_ordered[l_player_1[inx]]=0
for inx in range(len(l_player_2)):
    l_initial_ordered[l_player_2[inx]]=1  
entg_num = 1  
for inx in range(len(l_entangled)):
    l_initial_ordered[l_entangled[inx][0]]='e'+str(entg_num )   
    l_initial_ordered[l_entangled[inx][1]]='e'+str(entg_num  )
    entg_num +=1

print('This the initial table state inputed by the user:\n0 corresponds to player 1, 1 corresponds to player 2,\n e1,e2,e3... corresponds to entangled tiles')
print('-----\n'+str(l_initial_ordered[6])+'|'+str(l_initial_ordered[7])+'|'+str(l_initial_ordered[8]))
print('-----\n'+str(l_initial_ordered[3])+'|'+str(l_initial_ordered[4])+'|'+str(l_initial_ordered[5]))
print('-----\n'+str(l_initial_ordered[0])+'|'+str(l_initial_ordered[1])+'|'+str(l_initial_ordered[2]))
print('-----')

circuit = QuantumCircuit(9,9)
circuit.name = "tik tak toe"
for inx in range(len(l_player_2)):
    circuit.x(l_player_2[inx])
for inx in range(len(l_entangled)):
    circuit.h(l_entangled[inx][0]) #hardamard gate
    circuit.x(l_entangled[inx][])    
    