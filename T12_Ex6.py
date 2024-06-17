import subprocess

def pex6():
    try:
        subprocess.run(["python3", "./serverprojecte/manage.py", "runserver", "9090"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al iniciar el servidor Django:", e)

