for /l %%x in (1, 1, 100) do (
   echo %%x
   tesseract  inputimg\%%x.png outputtxt\output%%x.txt -l sin
)
