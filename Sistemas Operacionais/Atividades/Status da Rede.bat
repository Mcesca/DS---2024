@echo off
chcp 65001 >nul 
:loop
cls
echo Escolha uma opção
echo 1 - IPconfig
echo 2 - Testar ping

set /p opcao="Digite sua opção: "

if "%opcao%"=="1" (
	ipconfig
)
if "%opcao%"=="2" (
	set /p inf="Testar conectividade com: "
	ping %inf%
)
pause
goto loop