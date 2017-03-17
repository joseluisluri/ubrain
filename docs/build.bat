;; Construccion
del /Q .\_autodoc\*
sphinx-apidoc -o .\_autodoc ..\ubrain
call make clean
call make html
