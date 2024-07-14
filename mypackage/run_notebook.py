import subprocess

def main():
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "poc_model_ver_2.ipynb"])

if __name__ == "__main__":
    main()