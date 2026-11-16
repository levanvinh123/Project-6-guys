# Defines functions for project
# Cole Jansma, Vihn Le, Noah Tarver, Bennet Kruse, Connor Schultz, Matthew Spalla
# 11/12/2026

# This part defines a function "cls" (for clearing the Windows Terminal)
import os
import subprocess
def cls():
    subprocess.run('cls' if os.name=='nt' else 'clear', shell=True)

