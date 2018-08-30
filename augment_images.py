# imports
import os
import shutil as sh


# Define directory for images
source_directory = 'C:/Users/batemant1/PycharmProjects/AugmentImages/source_files'
processed_ok_directory = 'C:/Users/batemant1/PycharmProjects/AugmentImages/processed_ok_files'
processed_nok_directory = 'C:/Users/batemant1/PycharmProjects/AugmentImages/processed_nok_files'

# Loop through images
for filename in os.listdir(source_directory):
    source_file = source_directory + '/' + filename
    destination_file = processed_ok_directory + '/' + filename

    sh.copyfile(source_file, destination_file)


