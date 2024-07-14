# Installation Guide for ADAPtT POC 1.0.1

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.6 or higher
- `pip` (Python package installer)

### Step 1: Clone the Repository

First, clone the repository containing the package to your local machine. Open a terminal and run the following command:

```bash
git clone https://github.com/BitsGate-Tech-Ventures/adapt.git
```

### Step 2: Navigate to the Project Directory

Change your directory to the project directory:

```bash
cd adapt_model_poc
```

### Step 3: Create and Activate a Virtual Environment (Optional but Recommended)

It is recommended to use a virtual environment to avoid conflicts with other Python packages. Run the following commands to create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, you can activate the virtual environment using:

```
venv\Scripts\activate
```

### Step 4: Install Dependencies

Ensure you have a `requirements.txt` file in the project directory with the following contents:

```
pandas
nltk
scikit-learn
scipy
joblib
```

Install the dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 5: Install the Package

Run the following command to install the package:

```bash
pip install .
```

### Step 6: Verify Installation

After installation, verify that the `run_notebook` command is available. Run the following command:

```bash
run_notebook
```

If you see a message asking for user input, the installation was successful.

### Troubleshooting

### Script Not Found

If you see a warning indicating that the script is installed in a directory not on your `PATH`, add the directory to your `PATH`:

For `bash`:

```bash
echo 'export PATH=$PATH:/home/mint/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

For `zsh`:

```bash
echo 'export PATH=$PATH:/home/mint/.local/bin' >> ~/.zshrc
source ~/.zshrc
```

Alternatively, run the script using the full path:

```bash
/home/mint/.local/bin/run_notebook
```

### FileNotFoundError

If you encounter a `FileNotFoundError` for the `nmap_command_classifier.pkl` or `nmap_commands_updated.json` files, ensure that these files are located in the correct directory within the package. The directory structure should look like this:

```arduino
mypackage/
├── mypackage/
│   ├── __init__.py
│   ├── poc_model_ver_2.py
│   ├── nmap_commands_updated.json
│   ├── nmap_command_classifier.pkl
├── requirements.txt
├── setup.py
```

Ensure that `poc_model_ver_2.py` uses package-relative paths to locate these files.

### Usage

After successful installation, you can run the interactive mode by executing:

```bash
run_notebook
```

Follow the on-screen instructions to enter queries and provide feedback.

### Uninstallation

To uninstall the package, run:

```bash
pip uninstall mypackage
```