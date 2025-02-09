import sys
import requests

for modul_name, modul_path in sys.modules.items():
    print(modul_name, modul_path)