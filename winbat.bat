:: Batch scripting task runner

:: Using SET similar used EXPORTS on Unix, 
:: call the SETLOCAL command to make variables local to the scope of your script.

@ECHO OFF

SETLOCAL 
test=book
ENDLOCAL

REM python --version

:: not working
python -m unittest test -s %CD%\tests -p "*_test.py"

echo %CD%\tests

REM EXIT
REM echo %test%: SDHFKJ
REM echo %DATE%
REM echo %CD%
REM echo %PATH%