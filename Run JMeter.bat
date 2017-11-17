REM ----- Set patch to JMeter -----
cd /d "C:\Development\Tools & Scripts\Apache JMeter 3.3\bin"
REM ----- Run JMeter -----
"jmeter.bat"
REM ----- Run JMeter with proxy settings (Uncomment below to run JMeter with proxy) -----
REM ----- "jmeter.bat" -H proxybcw -P 8080 -u USERNAME -a PASSWORD -N localhost