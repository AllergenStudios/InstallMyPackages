from time import sleep
import colorama
import argparse
import shutil
import os

def main():
    parser = argparse.ArgumentParser(description='Easy package management from a Github repo instead of dealing with annoying pyproject.toml\'s and setup.py\'s')
    parser.add_argument('repo', help='The link to the github repo')
    parser.add_argument('--mainfile', help='If the package has a different name than main.py, you can specify it here.')
    args = parser.parse_args()

    repo_name = str(args.repo[args.repo.rindex('/') + 1:])

    if os.path.exists("venv"):
        print(f"{colorama.Fore.LIGHTGREEN_EX}Installing {repo_name} as a package... {colorama.Fore.LIGHTBLACK_EX} (This might take longer if your pip version is outdated!)")
        os.system("python.exe -m pip install --upgrade pip --quiet")
        os.system(f"git clone {args.repo} --quiet")
        print(f"{colorama.Fore.LIGHTBLACK_EX}Cloned repository{colorama.Fore.RESET}")
        sleep(0.5)
        repo_name_lowered = repo_name.lower()
        os.system(f"pip install -r {repo_name}/requirements.txt --quiet")
        print(f"{colorama.Fore.LIGHTBLACK_EX}Installed requirements{colorama.Fore.RESET}")
        sleep(1)
        os.rename(f"{repo_name}", f"{repo_name_lowered}")
        sleep(0.5)
        if args.mainfile:
            os.rename(f"{repo_name_lowered}/{args.mainfile}", f"{repo_name_lowered}/__init__.py")
            sleep(0.5)
        else:
            os.rename(f"{repo_name_lowered}/main.py", f"{repo_name_lowered}/__init__.py")
            sleep(0.5)
        os.replace(f"{repo_name_lowered}", f"venv/Lib/site-packages/{repo_name_lowered}")
        print(f"{colorama.Fore.LIGHTBLACK_EX}Moved into site-packages{colorama.Fore.RESET}")
        sleep(0.5)
        print(f"{colorama.Fore.LIGHTGREEN_EX}{repo_name} has finished installing!{colorama.Fore.RESET}")
    else:
        print(f"{colorama.Fore.LIGHTRED_EX}This tool only works with a virtualenv.{colorama.Fore.RESET}")

if __name__ == "__main__":
    main()
