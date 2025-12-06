# Setup

## Linux
### Create environment for linux
``` bash
mkdir -p ~/venvs
python3 -m venv ~/venvs/bleuraven_blender_python_library
source ~/venvs/bleuraven_blender_python_library/bin/activate
```

### Install fake bpy module
``` bash
python -m pip install --upgrade pip
python -m pip install fake-bpy-module-latest
```

### Set VSode Python interpreter
In VSCode, press `Ctrl+Shift+P`, then select `Python: Select Interpreter`, 
and choose the interpreter located at `~/venvs/bleuraven_blender_python_library/bin/python`.


## Windows
### Create environment for windows
``` bash
py -m venv C:\venvs\bleuraven_blender_python_library
C:\venvs\bleuraven_blender_python_library\Scripts\Activate.ps1
```

### Install fake bpy module
``` bash
python -m pip install --upgrade pip
python -m pip install fake-bpy-module-latest
```

### Set VSode Python interpreter
In VSCode, press `Ctrl+Shift+P`, then select `Python: Select Interpreter`, 
and choose the interpreter located at `C:\venvs\bleuraven_blender_python_library\Scripts\python.exe`.

# Best Practices
- Follow the official Blender best practices for addon development:
"Blender best_practice": "https://docs.blender.org/api/current/info_best_practice.html"

# Copilot Guidelines
- Always write comments in English
- Follow PEP8
- Follow strict typing
- Prefer Pathlib over os.walk / os.path
- for bpy.types.Object don't check type with `obj.type == 'MESH'` use `isinstance(obj.data, bpy.types.Mesh)`