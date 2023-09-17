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
    circuit.x(l_entangled[inx][1]) #x gate
    circuit.cx(l_entangled[inx][0], l_entangled[inx][1]) #controled-x gate

circuit.measure(list(range(9)), list(range(9)))

print("this is the corresponding quantum circuit from the user\'s input")

circuit.draw(output ="mpl", filename= "circuit.png")       
    
    
# Check winner
def check_winner(board,mark):
    return(((board[0]==mark) and (board[1]== mark) and (board[2]==mark) )or #for row1 

            ((board[3]==mark) and (board[4]==mark) and (board[5]==mark) )or #for row2

            ((board[6]==mark) and (board[7]==mark) and (board[8]==mark) )or #for row3

            ((board[0]==mark) and (board[3]==mark) and (board[6]== mark) )or#for Colm1 

            ((board[1]==mark) and (board[4]==mark) and (board[7]==mark) )or #for Colm 2

            ((board[2]==mark) and (board[5]==mark) and (board[8]==mark) )or #for colm 3

            ((board[0]==mark) and (board[4]==mark) and (board[8]==mark) )or #diagonal 1

            ((board[2]==mark) and (board[4]==mark) and (board[6]==mark) )) #diagonal 2


flag_p1=1 
flag_p2=0

while (flag_p1 or flag_p2) and not(flag_p1 and flag_p2):
    print('Running the quantum circuit...')
    flag_p1=0 
    flag_p2=0
    job = execute(circuit, BasicAer.get_backend('qasm_simulator'), shots=1)
    result = job.result()
    l_final_ordered=list(map(lambda x: int(x),list(list(result.get_counts().keys())[0][::-1])))
    print(l_final_ordered)
    #list with ordered cells
    print('The colapsed state is:')
    print('-----\n'+str(l_final_ordered[6])+'|'+str(l_final_ordered[7])+'|'+str(l_final_ordered[8]))
    print('-----\n'+str(l_final_ordered[3])+'|'+str(l_final_ordered[4])+'|'+str(l_final_ordered[5]))
    print('-----\n'+str(l_final_ordered[0])+'|'+str(l_final_ordered[1])+'|'+str(l_final_ordered[2]))
    print('-----')

    if (check_winner(l_final_ordered,0) ):## to check if player 1 won
        print('Player 1 won!')
        flag_p1 = 1
    else:
        flag_p1 = 0

    if (check_winner(l_final_ordered,1)): ## to check if player 2 won
        print('Player 2 won!')
        flag_p2 = 1
    else:
        flag_p2 = 0

    if (flag_p1 or flag_p2) and not(flag_p1 and flag_p2):
        break

    if flag_p1 and flag_p2:
        print('The game will repeat until one one player wins')

    if not(flag_p1 and flag_p2):
        print('No winners,\nThe game will repeat until one one player wins')    