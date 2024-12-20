# Sanger-Plate-Primer-Volume-Counter
Simple tool for calculating volume of primer you need to aliquot for sanger when sending off a plate for sequencing. Useful when using many primer pairs.   

This Python script calculates the total microliters needed for each forward and reverse primer pair based on their usage frequency and a specified minimum allowable volume. It is designed to simplify primer aliquoting calculations for Sanger sequencing.

BAsically you just set the minimum amount, I think Eurofins reccomends 10 or maybe 15ul minimum. Then Go to your Eurofins/other sequencing spread sheet collums which contain your primer pairs and copy/paste them into the script. They will be tallied up


## Features
- Automatically counts the number of times each primer is used.
- Multiplies the count by 5 µL to calculate total volume.
- Allows setting a minimum allowable volume for primers.

## Requirements
- Python 3.x
- No additional dependencies required.

