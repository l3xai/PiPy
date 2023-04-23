def load_digits(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def verify_digits(digits, user_input, start_index):
    correct_digits = digits[start_index:start_index + len(user_input)]
    errors = 0

    for i, (correct_digit, user_digit) in enumerate(zip(correct_digits, user_input)):
        if correct_digit != user_digit:
            print(f"Erro no dígito {i + 1}: Você digitou {user_digit}, mas o correto é {correct_digit}.")
            errors += 1

    return errors

def practice_pi(digits):
    start_index = 0
    group_size = 5

    while True:
        user_input = input("Digite os próximos 5 dígitos de Pi: ")
        if len(user_input) != group_size:
            print(f"Por favor, insira exatamente {group_size} dígitos.")
            continue

        errors = verify_digits(digits, user_input, start_index)

        if errors == 0:
            print("👍 Parabéns! Todos os dígitos estão corretos.")
            start_index += group_size
        else:
            print(f"{errors} erro(s) encontrado(s). Tente novamente.")

def main():
    file_path = "./pi_digits.txt"  # Insira o caminho para o arquivo de dígitos de Pi que você baixou
    digits = load_digits(file_path)
    practice_pi(digits)


if __name__ == "__main__":
    main()
