import subprocess

x = 5
for i in range(x):
    print(f"Account number:{i+1}/{x}")
    subprocess.run(["python", "main.py", "--LOGIN", "papajauke", "--HASLO", "papajauke2137"])
