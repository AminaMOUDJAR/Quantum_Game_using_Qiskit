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

    """By default player1 tiles are initilized to \0> state
# Player2 tiles initialized |1> state
    """
    
l_player_1 = [0]
l_player_2     