# Installing Nuitka
pip3 install nuitka

# Install some packages for Nuitka..
# for standalone building
sudo apt install patchelf 
# for perfomance building
sudo apt install ccache
# Copy all data sources to build directory
mkdir ../build
cp -r . ../build

# Compiling by Nuitka
cd ../build && python3 -m nuitka --standalone --follow-imports --plugin-enable=pyqt5 --plugin-enable=pylint-warnings --include-data-dir=src=src app.py
