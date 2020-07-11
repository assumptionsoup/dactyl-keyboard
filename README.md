# dactyl-keyboard
Remake of [dactyl-keyboard](https://github.com/adereth/dactyl-keyboard) in SolidPython with Ergodox key caps compatibility.

DSA key caps are generated using [KeyV2](https://github.com/rsheldiii/KeyV2) and imported.

## Getting Started
Install [pipenv](https://github.com/pypa/pipenv) if you haven't already.
```
    pip install pipenv
```

Navigate to the root of the project and initialize your pipenv environment.
```
    pipenv install
```

Start the pipenv environment
```
    pipenv shell
```

Execute the hot-reloading runner:
```
    cd src
    python run.py
```

This will monitor for changes to the src directory and re-run dactyl every time a change is detected.
Open things/dactyl.scad in [openSCAD](https://www.openscad.org/downloads.html) and see your changes reflected in near-realtime!
> If you don't care for hot-reloading, you can execute the dactyl script directly `python dactyl.py`.





