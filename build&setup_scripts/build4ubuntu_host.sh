# script for ubuntu 18.04 LTS host for first building

# Installing Nuitka
pip3 install nuitka

# Install some packages for Nuitka..
# for standalone building
sudo apt install patchelf 
# for perfomance building
sudo apt install ccache
# Copy all data sources to build directory

python3 -m run_me.py
sudo apt remove python3-pyqt5
sudo apt remove python3-pyaudio
pip3 install pyaudio
pip3 install PyQt5

mkdir ../build
cp -r . ../build

# Compiling by Nuitka
# Standalone + Onefile
#cd ../build && python3 -m nuitka --standalone --onefile --linux-onefile-icon=src/icons/64x64/audio-input-microphone.svg --follow-imports --plugin-enable=pyqt5 --plugin-enable=pylint-warnings --include-data-dir=src=src app.py

# Standalone
cd ../build && python3 -m nuitka --standalone --follow-imports --plugin-enable=pyqt5 --plugin-enable=pylint-warnings --include-data-dir=src=src app.py

#cd ../build && python3 -m nuitka --standalone --follow-imports --plugin-enable=pyqt5 --plugin-enable=pylint-warnings --include-data-dir=src=src app.py
#cd ../build && python3 -m nuitka --standalone --follow-imports --plugin-enable=pyqt5 --include-data-dir=src=src app.py
