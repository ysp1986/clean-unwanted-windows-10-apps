# clean unwanted windows 10 apps
 useage: Run cmd with administration authority, and enter the code dir, run clean_main.bat

Note:
1. Principle of this code: The code will generate all pachage name in packages.txt, and filter the full name with package names listed in ref_package_name.txt, and delete all the packages found.
2. In ref_package_name.txt, only package names before '_' of each line are used.
