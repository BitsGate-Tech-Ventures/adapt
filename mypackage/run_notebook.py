import subprocess

def main():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "poc_model_ver_2.ipynb"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the notebook: {e}")

if __name__ == "__main__":
    main()
