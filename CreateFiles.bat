@echo off
set x=1
:loop
rem Pad x value, store it in padded
   set A=0%x%
   set A=%A:~-2%
rem Show padded value
   echo %A%

rem create directories and files
      MKDIR Day%A%
   echo.>".\Day%A%\Day%A%IN.txt"
   echo.>".\Day%A%\Day%A%INtest.txt"
   echo.>".\Day%A%\Day%A%P1.py"
   echo.>".\Day%A%\Day%A%P2.py"

   set /A x+=1
if %x% leq 25 goto loop
pause