# Recipe Formatting
This is a program for standardizing recipe formatting. This includes
 - assigning categories based on recipe contents
 - bolding ingredients
 - spliting instructions into one sentance per line

with the goal of making recipes easier to follow and more ADHD-friendly.

## Steps

## Known issues
 - Although this was built with Google Drive in mind, the tag format depends on exact searches which Drive no longer supports (in early 2024). Recipes must be mirrored elsewhere to leverage tags (e.g using rclone).
 - Titles with apostrophies capitalize overzealously (e.g Za'Atar instead of the correct Za'atar)
 - Removes correct capitalization from ingredients list (e.g converts "Japanese mayonnaise" to all lowercase)

## Possible Improvements
 - Better method to input recipe (currently XML...)
 - Reduce steps (automatically upload to google drive and run drive formatting script)
 - Automatically add flour, sugar and butter weight given volume in ingredients
 - Mathematical conversion between units instead of hard-coded string replacements
 - Automatically bold descriptors for an instruction if it is followed by a colon (e.g "**Prepare the chicken**:")
 - Automatically strip out step numbering from the recipe body
 - Have an easy way to automatically format incredient subdivisions (e.g ingredients split into "cake" and "icing")
 - Batch file conversion
 - Recipe extraction from webpage
 - Add more robust testing (more unit tests, adding end-to-end test, etc)