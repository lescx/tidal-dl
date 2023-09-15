#!/bin/sh

rm -rf dist build __init__.spec

cd tidal-dl
rm -rf __init__.spec dist build exe MANIFEST.in ./*.egg-info

python3 setup.py sdist bdist_wheel
pyinstaller -F tidal_dl/__init__.py

mkdir exe
mv dist/__init__.exe exe/tidal-dl.exe

pip uninstall -y tidal-dl

cd ..