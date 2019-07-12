echo OFF

FOR /F "tokens=2 delims==" %%F IN ('wmic bios get serialnumber /value') DO (
  SET SN=%%F
)

FOR /F "tokens=2 delims=(" %%F IN ('wmic bios get smbiosbiosversion') DO (
  SET BIOSV=%%F
)

echo %SN%
echo %BIOSV%

start iexplore http://localhost:9999/whatever?sn=%SN%^&bios=%BIOSV%
pause