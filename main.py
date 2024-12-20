from intpl import tools
import argparse




parser = argparse.ArgumentParser(description="Przykładowy skrypt z argumentami LOGIN i HASLO")


parser.add_argument('--LOGIN', type=str, required=True, help="Login użytkownika")
parser.add_argument('--HASLO', type=str, required=True, help="Hasło użytkownika")


args = parser.parse_args()


LOGIN = args.LOGIN
HASLO = args.HASLO


tools.create_account(LOGIN, HASLO)


