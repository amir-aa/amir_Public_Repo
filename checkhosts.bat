@echo off
setlocal

REM Replace these values with the parameters you want to check
set "host1=google.com"
set "host2=example.com"
set "host3=192.168.1.1"

REM Set the interval in seconds (modify this value as needed)
set "interval=10"

:mainLoop
echo Checking connectivity...

REM Function to check connectivity using ping
:pingHost
ping -n 1 %1 > nul
if %errorlevel% equ 0 (
    echo %1 is reachable.
) else (
    echo %1 is unreachable.
)
goto :eof

REM Check connectivity for each parameter
call :pingHost %host1%
call :pingHost %host2%
call :pingHost %host3%

echo Checking complete.

REM Wait for the specified interval before checking again
timeout /t %interval% /nobreak > nul
goto mainLoop
