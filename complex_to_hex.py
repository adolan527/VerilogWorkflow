import re
import sys

def hex_to_bin(hex_num):
    bin_str = f"{int(hex_num, 16):016b}"  # Convert to 16-bit binary
    return " ".join([bin_str[i:i+4] for i in range(0, 16, 4)])  # Group into 4-bit chunks

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py '<input_string>'")
        sys.exit(1)
    input_str = sys.argv[1]

    print('[',hex_to_bin(input_str),']')
