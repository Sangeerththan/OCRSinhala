for /l %%x in (1, 1, 100) do (
   echo %%x
   tesseract  %%x.jpg output%%x.txt
)