@echo off
setlocal enabledelayedexpansion

:: Capture the input argument
set MODULE_NAME=%1

:: Run the findstr command to search for the specified module
for /f "delims=" %%A in ('findstr /s /n /i /c:"module %MODULE_NAME%(" *.v') do (
    :: Extract the file path and line number from the output
    for /f "tokens=1,2* delims=:" %%B in ("%%A") do (
        set FILE_PATH=%%B
        set LINE_NUMBER=%%C
    )
)
    set FILE_PATH=%CD%\%FILE_PATH%
if not "%FILE_PATH%"=="%CD%\" (
    "C:\Program Files\Notepad++\notepad++.exe" -n%LINE_NUMBER% "%FILE_PATH%"
)
echo NULL
endlocal