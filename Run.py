import subprocess

scripts = ["combine.py", "compile.py", "prep.py", "format.py", "calc.py"]

for script in scripts:
    print("Running: ", script)
    try:
        subprocess.run(["python", script])
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script}: {e}")