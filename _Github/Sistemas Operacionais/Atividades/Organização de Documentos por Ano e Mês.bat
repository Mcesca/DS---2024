@echo off

chcp 65001 >nul

set /p pastaano="Digite sua opção: "

mkdir %pastaano%

cd %pastaano%

mkdir "01 - janeiro", "02 - fevereiro", "03 - março", "04 - abril", "05 - maio", "06 - junho", "07 - julho", "08 - agosto", "09 - setembro", "10 - outubro", "11 - novembro", "12 - dezembro"