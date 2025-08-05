from PyInstaller.utils.hooks import collect_submodules

# Forces CLI imports, since dynamic imports don't work with PyInstaller by default.
hiddenimports = collect_submodules('inductiva._cli')
