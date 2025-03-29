from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
import numpy as np

def generate_random_number(bits=8, shots=1):
    """
    Generate a random number using quantum circuit simulation.
    
    Args:
        bits (int): Number of bits for the random number (default: 8)
        shots (int): Number of times to run the circuit (default: 1)
    
    Returns:
        int: Random number generated using quantum simulation
    """
    # Create quantum and classical registers
    qr = QuantumRegister(bits)
    cr = ClassicalRegister(bits)
    circuit = QuantumCircuit(qr, cr)
    
    # Apply Hadamard gates to create superposition
    for i in range(bits):
        circuit.h(qr[i])
    
    # Measure quantum bits
    circuit.measure(qr, cr)
    
    # Execute the circuit on the QASM simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=shots)
    result = job.result()
    counts = result.get_counts(circuit)
    
    # Convert binary string to decimal
    binary_str = list(counts.keys())[0]  # Get the first (and only) measurement
    return int(binary_str, 2)

def generate_random_sequence(n_numbers, bits=8):
    """
    Generate a sequence of random numbers.
    
    Args:
        n_numbers (int): Number of random numbers to generate
        bits (int): Number of bits for each random number
    
    Returns:
        list: List of random numbers
    """
    return [generate_random_number(bits=bits) for _ in range(n_numbers)]

def generate_lotto_max_numbers():
    """
    Generate 7 unique numbers for Lotto Max (1-50 range).
    
    Returns:
        list: 7 sorted unique numbers between 1 and 50
    """
    numbers = set()
    # We need 6 bits to represent numbers up to 50 (as 2^6 = 64)
    while len(numbers) < 7:
        num = generate_random_number(bits=6)
        # Only accept numbers in the valid range (1-50)
        if 1 <= num <= 50:
            numbers.add(num)
    
    # Convert to sorted list for better readability
    return sorted(list(numbers))

if __name__ == "__main__":
    print("🎰 Quantum Lotto Max Number Generator 🎰\n")
    
    print("Generating Lotto Max numbers (7 unique numbers from 1-50):")
    print("-------------------------------------------------------")
    lotto_numbers = generate_lotto_max_numbers()
    
    # Format numbers with leading zeros for consistent display
    formatted_numbers = [f"{num:02d}" for num in lotto_numbers]
    print(f"Your quantum-generated numbers: {' - '.join(formatted_numbers)}")
    print("\nNote: These numbers are generated using true quantum randomness simulation!")
    print("Good luck! 🍀") 