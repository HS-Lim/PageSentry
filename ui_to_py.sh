#!/bin/bash

echo "Generating .py files from .ui files using pyuic5"

pyuic5 ./UIFiles/MainWindow.ui -o ui_main_window.py
pyuic5 ./UIFiles/EditWindow.ui -o ui_edit_window.py
pyuic5 ./UIFiles/AboutWindow.ui -o ui_about_window.py
pyuic5 ./UIFiles/OptionsWindow.ui -o ui_options_window.py

echo "Done!"
