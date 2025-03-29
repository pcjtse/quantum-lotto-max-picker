# Quantum Random Number Generator

This project implements a quantum random number generator using Qiskit, IBM's quantum computing framework. The program simulates quantum circuits to generate truly random numbers based on quantum mechanical principles.

## Requirements

- Python 3.7 or higher
- Qiskit
- NumPy

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the program using:
```bash
python quantum_random.py
```

### Features

The program generates Lotto Max numbers using quantum randomness:
- Generates 7 unique numbers between 1 and 50
- Uses quantum circuit simulation for true randomness
- Numbers are sorted and formatted for easy reading

### Sample Output

```
🎰 Quantum Lotto Max Number Generator 🎰

Generating Lotto Max numbers (7 unique numbers from 1-50):
-------------------------------------------------------
Your quantum-generated numbers: 03 - 17 - 25 - 31 - 42 - 45 - 49

Note: These numbers are generated using true quantum randomness simulation!
Good luck! 🍀
```

### How it Works

The program uses quantum superposition to generate random numbers:

1. Creates a quantum circuit with 6 qubits (needed to represent numbers up to 50)
2. Applies Hadamard gates to put each qubit in superposition
3. Measures the qubits, causing them to collapse to either 0 or 1
4. Converts the resulting binary string to a decimal number
5. Ensures numbers are within the valid range (1-50) and unique
6. Sorts the numbers for consistent display

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments

This project uses the following open-source packages:
- [Qiskit](https://qiskit.org/) - Apache 2.0 License
- [NumPy](https://numpy.org/) - BSD License 