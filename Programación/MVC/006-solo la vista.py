import subprocess

resultado = subprocess.run(
            ['./controlador.out',str(25)],
            capture_output=True,
            text=True,
            check=True
)

print(resultado.stdout.strip())