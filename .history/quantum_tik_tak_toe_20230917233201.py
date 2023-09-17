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

