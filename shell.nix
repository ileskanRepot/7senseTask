{ pkgs ? import <nixpkgs> {}}:
  pkgs.mkShell {
    nativeBuildInputs = let
      env = pyPkgs : with pyPkgs; [
        matplotlib
        pybind11
        numpy
        pytest
      ];
    in with pkgs; [
      (python311.withPackages env)
      gcc
      valgrind
      cmake
    ];
}
