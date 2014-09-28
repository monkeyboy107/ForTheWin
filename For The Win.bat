@echo off
mkdir "For The Win"
cd "For The Win"
mkdir "Invintory"
cd Invintory
cls
:no
:No
:nO
:NO
set /p name=What is your name? 
set /p ny=Is your name  yes or no? 
cls
goto %ny%
:yes
:Yes
:yEs
:YEs
:yeS
:YeS
:yES
:YES
echo Your name is %name%, you are on a adventure to the nether,
echo you require 10 square meters obsidian and some flint and steel, or
echo other sources of fire(fire, lava, spontanous conbustion, cheating,
echo fire charge, and/or etc).
pause>nul
cls
echo Stranger: Oh no...
timeout /T 3 >nul
echo Stranger: Are you alright?
timeout /T 3 >nul 
echo %name%: Ugh...
timeout /T 3 >nul 
echo %name%: My head is killing...
timeout /T 3 >nul 
echo (You passout)
pause>nul
cls
echo (You wake up in a bed, the smell of food touches your nose,
echo the stranger from earlier walkesd in.)
timeout /T 3 >nul 
set /p name1=Stranger: Hey your awake you've been out for 3 days now. What is your name? 
timeout /T 3 >nul 
echo %name%: My name is %name1%.
timeout /T 3 >nul 
echo Stranger: Hello %name1%, nice to meet you, my name is John.
timeout /T 3 >nul 
echo %name%: What happended?
timeout /T 3 >nul 
echo John: You fell from somewhere and hit your head preaty hard and you became incompassateted
pause>nul
cls
echo (You leave Johns house.)
:return
:r
:R
set /p place=Where would you like to go. (John's House=JH Battle Field=BF Mineshaft=bf Exit=Exit) 
cls
goto %place%
goto return
:exit
:Exit
:eXit
:EXit
:exIt
:ExIt
:eXIt
:EXIt
:exiT
:ExiT
:eXiT
:EXiT
:exIT
:ExIT
:eXIT
:EXIT
exit
:jh
:Jh
:jH
:JH
echo (You enter John's House)
timeout /T 3 >nul 
set /p Dialog=John:Hey %name1% how have you been? 
timeout /T 3 >nul 
echo %name%:I'm %Dialog%
:HJ
set /p place=What would you like to do? (Sleep=S Leave=L) 
goto %place%
:l
:L
cls
goto return
:s
:S
cls
echo You Rested
timeout /T 3 >nul 
goto return
:bf
:Bf
:bF
:BF
set /a enemy=%RANDOM% * 10 / 32768 + 1
cls
goto bf%enemy%
:bf1
echo There where no enemies.
pause>nul
cls
goto return
:bf2
echo There was a week enemy you kill them easily.
pause>nul
cls
goto return
:bf3
echo The enemies do a bit of damage. You take them out easily.
pause>nul
cls
goto return
:bf4
echo The enemies enemies do little damage. You take them out quickly.
pause>nul
cls
goto return
:bf5
echo The enemies do a normal ammount of damage. You take them out effenintly.
pause>nul
cls
goto return
:bf6
echo The enemies do a lot of damage. You bareilly take them out.
pause>nul
cls
goto return
:bf7
echo The enemies do a ton of damage. You hardly take them out.
pause>nul
cls
goto return
:bf8
echo The enemies do an inordinate amount of damage. You bareilly make it out of there alive.
pause>nul
cls
goto return
:bf9
echo The enemies do too much damage for you to stand for a long time I suggest for you to visit John's House.
pause>nul
cls
goto return
:bf10
echo The enemies knock you out.
timeout /T 3 >nul 
goto Uncon
:ms
:Ms
:mS
:MS
set /a bf=%RANDOM% * 8 / 32768 + 1
goto %bf%
:1
echo you find nothing
pause>nul
cls
goto return
:2
echo You find coal
echo 1 Coal>>coal.txt
pause>nul
cls
goto return
:3
echo You find iron
echo 1 iron>>iron.txt 
pause>nul
cls
goto return
:4
echo You find diamond
echo 1 diamond>>diamond.txt
pause>nul
cls
goto return
:5
echo YOU FIND OBSIDIAN WOOT
echo 1 OBSIDIAN>>OBSIDIAN.txt
pause>nul
cls
goto return
:6
echo You find nothing
pause>nul
cls
goto return
:7
set /p what=You find John say, hey. 
echo %what%
pause>nul
cls
goto return
:8
echo you find a pickaxe.
echo 1 pickaxe>>pickaxe.txt
pause>nul
cls
goto return
pause>nul
cls
goto return
:Uncon
echo You wake up in John's house
pause>nul
goto HJ
:id
set /a id=11975 * 8 / 32768 
goto %id%