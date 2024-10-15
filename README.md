# CoolingAssemblyAtTIF
Small python script to rename pictures after thermal paste deposition, after tray assembly and after retightening during the cooling tray assembly procedure.

## Steps for a correct working
1. Copy the 6 pictures into the `inputs/` folder. Make sure there are only those 6 pictures, no more files or other previous pictures.
2. Run `python3 rename_cooling_trays_pictures.py`.
3. Type the image type:
    * `TIM`: for pictures after thermal paste deposition.
    * Just press return key for pictures after the assembly was finished.
    * `RTG`: for pictures after retightening.
4. Write the pipe number (in a 2-digit format, just the number).
5. Enter the cooling plate codes (format: CP2_043 (BN2) CP3_107 (BN2) ). Just copy and paste the 6 cells from the excel sheet.
6. Type the date in DD-MM-YY format.
7. Type `inlet` if you started taking the pictures from the inlet side (plate with code `CP2_XXX`), or `outlet` if you started from the outlet side (plate with code `CP1_XXX`). **This may not work correctly, and you might have to enter the opposite. It depends on how your phone names the photos as it takes them.**
8. After this, you will have the pictures with the modify names in the `output/` directory. Remember to clean the `input/` folder before starting with a new renaming.


**ATTENTION: please verify that the images have been renamed correctly before uploading them to the CERNbox repository.**
