@echo off
cd "C:\inetpub\wwwroot\Proyectos\INSPIRE-validator-API"
for %%x IN (0, 1, 10) DO powershell.exe "python ./__main__.py"