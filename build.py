import os
import subprocess
import sys

def build_executable():
    """Build the executable using PyInstaller."""
    print("Building SimpleTxtReader executable...")
    
    # Ensure PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller==6.4.0"])
    
    # Build the executable
    subprocess.check_call([
        "pyinstaller",
        "--clean",
        "--noconfirm",
        "simple_txt_reader.spec"
    ])
    
    print("\nBuild completed successfully!")
    print("The executable can be found in the 'dist' directory.")
    print("To run the application, execute 'dist/SimpleTxtReader.exe'")

if __name__ == "__main__":
    build_executable() 