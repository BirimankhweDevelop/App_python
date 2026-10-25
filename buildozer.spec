[app]

title = Meu Aplicativo
package.name = meuaplicativo
package.domain = org.exemplo

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23

[buildozer]

log_level = 2
warn_on_root = 1
