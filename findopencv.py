import sys
import os

def find_opencv_3_0_path():
    # Get the system's PATH environment variable
    path_env = os.environ.get('PATH', '')

    # Split the PATH variable into individual directories
    paths = path_env.split(';')

    # Search for the OpenCV 3.0 binaries in the directories
    for path in paths:
        opencv_bin_path = os.path.join(path, 'opencv_world300.dll')
        if os.path.exists(opencv_bin_path):
            return os.path.dirname(opencv_bin_path)

    return None

# Usage example
opencv_3_0_path = find_opencv_3_0_path()

if opencv_3_0_path:
    print("OpenCV 3.0 binaries path:", opencv_3_0_path)
else:
    print("OpenCV 3.0 binaries path not found.")
