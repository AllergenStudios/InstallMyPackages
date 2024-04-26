# InstallMyPackages
Easy package management from a Github repo instead of dealing with annoying pyproject.toml's and setup.py's

# How do I make my package work with it?

All you need is a github repository and a requirements.txt.
Your main python file for your module should be main.py, if its not then you can do 
```--mainfile <the name of your python file if its not main.py>```
For instance, if your main python file is mymodule.py it would be

```imp https://github.com/YourUser/YourRepo/ --mainfile mymodule.py```

# How do I install it?
- Clone the github repo using ```git clone https://github.com/AllergenStudios/Install-My-Packages```
- Run install.py
- Once it is finished, run these commands

POWERSHELL/WINDOWS:
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
