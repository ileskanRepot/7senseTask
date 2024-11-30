# 7senseTask

This is a simple app/function which returns a list of objects that are closer than `objectStreshold` (for example 2 meters) and it prints a warning to stderr if the object closer than `criticalStreshold` (for example 1 meter) is found. The main C++ function has been multithreaded with openMP

## Files

This consist of two main files `app.py` and `main.cpp`. In these the core logic is coded. As the name suggests `tests.py` is for tests. `CMakeLists.txt` is for compiling the application and `Doxyfile` is for compailing the documentation. In `requirements.txt` there is list of requirements for this application. If you have Nix package manager installed, you can just use `nix-shell` to install all of the applications in `shell.nix`.

## Building

To build this app make sure you have `openMP`, `python`, `pybind11`, `numpy`, `cmake` and `gcc` installed. Run the following commands to compile the app

```
mkdir build
touch build/__init__.py
cd build
cmake ..
make
cd ..
```

## Running

To run the app simply run command `python app.py`

## Testing

To test the app simply run command `pytest tests.py`
