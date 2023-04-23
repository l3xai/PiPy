from mpmath import mp

def generate_pi_digits(digits_count):
    mp.dps = digits_count + 1
    pi = mp.nstr(mp.pi, mp.dps)
    return pi[0] + pi[2:]

def save_digits_to_file(digits, file_path):
    with open(file_path, "w") as file:
        file.write(digits)

def main():
    digits_count = 1000000
    pi_digits = generate_pi_digits(digits_count)
    file_path = "pi_digits.txt"

    save_digits_to_file(pi_digits, file_path)
    print(f"Os primeiros {digits_count} dígitos de Pi foram salvos em {file_path}.")


if __name__ == "__main__":
    main()
