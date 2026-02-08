#!/usr/bin/python3
import json, os, platform, time

def get_data_path():
    """Get path to OneShotWME data folder for current OS"""
    os_name = platform.system().lower()
    # Linux path by default
    data_path = os.path.join(os.getenv("HOME"), ".steam/root/steamapps/compatdata/2915460/pfx/drive_c/users/steamuser/Application Data/OneShotWME")
    if os_name == "windows":
        # Windows
        data_path = os.path.join(os.getenv("APPDATA"), "OneShotWME")
    elif os_name == "darwin":
        # MacOS (untested)
        data_path = os.path.join(os.getenv("HOME"), "Library/Application Support/Steam/steamapps/compatdata/2915460/pfx/drive_c/users/steamuser/Application Data/OneShotWME")
    if os.path.isdir(data_path):
        print(f"Data path: {data_path}")
        return data_path
    else:
        print("Data path not found.")

def main():
    """Main script flow"""
    data_path = get_data_path()

    if data_path:
            while True:
                # Open the fs.dat file which is actually a JSON file despite the extension
                f = open(os.path.join(data_path, "fs.dat"), "r")
                if f:   
                    try:
                        # Try to decode the file
                        j = json.loads(f.read())
                        files = j["files"]
                        # Find the document with the safe code
                        document = next((item for item in files if item["name"] == "app_safe_document"), None)
                        if document:
                            if len(document) >= 2:
                                # If found, print the code and exit
                                print(f"Code: {document['argument'][1]}")
                                break
                        else:
                            # If not found, print the error
                            print("Document not found")
                    except Exception as e:
                        print(type(e).__name__, ":", e)
                f.close()
                # Wait 5 seconds before retrying
                time.sleep(5)

if __name__ == "__main__":
    main()
