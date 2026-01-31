[app]

title = A_project
package.name = aproject
package.domain = org.joyserver

source.dir = .
source.include_exts = py,png,txt,json
source.include_patterns = con.txt,regles.txt,memoire.json,t.png

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Affichage au démarrage
presplash_image = t.png
presplash_color = #000000


[buildozer]

log_level = 2
warn_on_root = 0


[android]

minapi = 21
target = 33
ndk_api = 21
use_androidx = True

android.add_src = .