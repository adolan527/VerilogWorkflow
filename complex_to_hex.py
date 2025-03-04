import argparse
import re


def int_to_signed_magnitude(n):
    if not (-32767 <= n <= 32767):
        raise ValueError("Number out of range for 16-bit signed magnitude.")

    sign_bit = '0' if n >= 0 else '1'
    magnitude = abs(n)
    magnitude_bits = f'{magnitude:015b}'  # Convert to 15-bit binary (excluding sign bit)

    return sign_bit + magnitude_bits


def complex_to_32bit(complex_str):
    match = re.fullmatch(r'\s*(-?\d+)\s*([+-])\s*(\d+)j\s*', complex_str)
    if not match:
        raise ValueError("Invalid complex number format. Use 'a + bj' or 'a - bj'")

    a = int(match.group(1))
    b = int(match.group(3))
    if match.group(2) == '-':
        b = -b

    a_bin = int_to_signed_magnitude(a)
    b_bin = int_to_signed_magnitude(b)

    combined_bin = b_bin + a_bin  # Swap order: imaginary (b) first, real (a) second
    verilog_format = f"32'h{int(combined_bin, 2):08X}"

    return verilog_format


def main():
    parser = argparse.ArgumentParser(
        description="Convert a complex number (a + bj) into a 32-bit signed magnitude representation.")
    parser.add_argument("complex_number", type=str, help="Complex number in the format 'a + bj' or 'a - bj'")
    args = parser.parse_args()

    try:
        result = complex_to_32bit(args.complex_number)
        # print(f"32-bit Signed Magnitude: {result}")
        print(result)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
