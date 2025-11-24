import argparse
import re


def int_to_twos_complement(n):
    if not (-32768 <= n <= 32767):
        raise ValueError("Number out of range for 16-bit two's complement.")

    return f'{n & 0xFFFF:016b}'  # Convert to 16-bit two's complement binary


def complex_to_32bit(complex_str):
    match = re.fullmatch(r'\s*(-?\d+)\s*([+-])\s*(\d+)j\s*', complex_str)
    if not match:
        raise ValueError("Invalid complex number format. Use 'a + bj' or 'a - bj'")

    a = int(match.group(1))
    b = int(match.group(3))
    if match.group(2) == '-':
        b = -b

    a_bin = int_to_twos_complement(a)
    b_bin = int_to_twos_complement(b)

    combined_bin = b_bin + a_bin  # Swap order: imaginary (b) first, real (a) second
    verilog_format = f"32'h{int(combined_bin, 2):08X}"

    return verilog_format, a, b


def complex_multiply(a, b, c, d):
    real_part = a * c - b * d
    imag_part = a * d + b * c
    return real_part, imag_part


def main():
    parser = argparse.ArgumentParser(
        description="Convert a complex number into 32-bit two's complement")
    parser.add_argument("complex_number", type=str, help="Complex number in the format 'a + bj'")
    args = parser.parse_args()


    comp1 = args.complex_number
    hex1, a, b = complex_to_32bit(comp1.strip())
    print(f"{hex1}; //{a} + {b}j",end="")





if __name__ == "__main__":
    main()