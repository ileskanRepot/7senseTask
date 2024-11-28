{ pkgs ? import <nixpkgs> {}}:
  pkgs.mkShell {
    nativeBuildInputs = let
      env = pyPkgs : with pyPkgs; [
        numpy
      ];
    in with pkgs; [
      (python311.withPackages env)
      gcc
    ];
}
