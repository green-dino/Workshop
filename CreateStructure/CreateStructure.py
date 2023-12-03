import os

def create_directory_structure():
    base_dir = "myapp"
    
    # Main application directory
    os.makedirs(base_dir, exist_ok=True)
    
    # Subdirectories within the main application directory
    subdirectories = [
        "myapp",
        "myapp/module1",
        "myapp/module2",
        "myapp/utils",
        "tests",
        "docs",
    ]
    
    for subdirectory in subdirectories:
        os.makedirs(os.path.join(base_dir, subdirectory), exist_ok=True)
    
    # Files within the directories
    files = [
        "myapp/__init__.py",
        "myapp/main.py",
        "myapp/module1/__init__.py",
        "myapp/module1/module1_file1.py",
        "myapp/module1/module1_file2.py",
        "myapp/module2/__init__.py",
        "myapp/module2/module2_file1.py",
        "myapp/module2/module2_file2.py",
        "myapp/utils/__init__.py",
        "myapp/utils/helper_functions.py",
        "myapp/utils/constants.py",
        "tests/__init__.py",
        "tests/test_module1.py",
        "tests/test_module2.py",
        "docs/conf.py",
        "docs/index.rst",
        "docs/module1.rst",
        "requirements.txt",
        "README.md",
        ".gitignore",
        "setup.py",
        ".flake8",
    ]
    
    for file in files:
        with open(os.path.join(base_dir, file), 'w') as f:
            pass  # Create an empty file

    print("Directory structure created successfully.")

if __name__ == "__main__":
    create_directory_structure()
