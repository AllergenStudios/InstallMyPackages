# Install-My-Packages
Easy package management from a Github repo instead of dealing with annoying pyproject.toml's and setup.py's

# How do I install it?
- Clone the github repo using ```git clone https://github.com/AllergenStudios/Install-My-Packages```
- Run install.py
- Once it is finished, run these commands

POWERSHELL:
  ```powershell
  $pythonScriptPath = "$env:USERPROFILE\imp\main.py"
  New-Alias -Name 'imp' -Value $pythonScriptPath
  ```
BASH/LINUX:
  ```bash
  alias imp="$HOME/imp/main.py"
  ```

# How do I use it?

Use ```imp <github repo>``` to install it into your packages.
If the package does not have a main.py and for the main file has a different file name,
you can use ```imp <github repo> --mainfile <the main file name.py>```
