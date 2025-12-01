import os, sys

print("Python:", sys.executable)
THIS = os.path.abspath(__file__)
BASE = os.path.dirname(THIS)
print("WORKING DIR:", os.getcwd())
print("THIS FILE:", THIS)
print("BASE_DIR (project):", BASE)
STATIC = os.path.join(BASE, "static")
TEMPLATES = os.path.join(BASE, "templates")
print("EXPECTED static dir:", STATIC)
print("EXPECTED templates dir:", TEMPLATES)
print("static exists:", os.path.isdir(STATIC))
if os.path.isdir(STATIC):
    print("static files:", os.listdir(STATIC))
else:
    print("static files: (static dir missing)")

print("templates exists:", os.path.isdir(TEMPLATES))
if os.path.isdir(TEMPLATES):
    print("templates files:", os.listdir(TEMPLATES))
else:
    print("templates files: (templates dir missing)")
