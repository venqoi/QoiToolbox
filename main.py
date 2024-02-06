import os
import requests
import webbrowser

DOWNLOAD_FOLDER = "files"

def post_install_actions():
    print("Performing post-install actions...")

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    files_to_download = [
        "https://github.com/hellzerg/optimizer/releases/download/16.4/Optimizer-16.4.exe",
        "https://github.com/auraside/Hone/releases/download/Hone/Hone.-.Installer.exe"
    ]

    for url in files_to_download:
        filename = os.path.join(DOWNLOAD_FOLDER, os.path.basename(url))
        print(f"Downloading {url} to {filename}")
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url}")

        print("Opening Azurites website")
        webbrowser.open("https://tweakcentral.net/downloads/azurite")

def pre_install_actions():
    print("Performing pre-install actions...")
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    url = "https://github.com/pbatard/rufus/releases/download/v4.4/rufus-4.4.exe"
    filename = os.path.join(DOWNLOAD_FOLDER, os.path.basename(url))
    print(f"Downloading rufus")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded rufus")

    print("Opening NexusLiteOS website")
    webbrowser.open("https://nexusliteos.blogspot.com/")

def main():
    os.system("cls")
    print("1. Pre-install")
    print("2. Post-install")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        pre_install_actions()
    elif choice == '2':
        post_install_actions()
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
