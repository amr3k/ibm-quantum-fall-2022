import qiskit as qi
from dotenv import load_dotenv
from os import environ

load_dotenv()

IBMId: str = environ.get("IBMId")

# qi.IBMQ.save_account(IBMId)

qr = qi.QuantumRegister(2)
cr = qi.QuantumRegister(2)

circ = qi.QuantumCircuit(qr, cr)

results = circ.draw()

print(results)
