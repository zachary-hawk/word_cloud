 Word Cloud
 ==========

 Word Cloud is a Python script that generates a word cloud from a PDF document. It extracts keywords from the text and visualizes them in a visually appealing word cloud image.

Features
========

- Extract keywords from PDF documents.
- Create a word cloud with customizable parameters such as font, color, and maximum number of words.
- Support for custom font files and logo masking. (Note that a black and white logo/crest works best, and mustn't have a transparent background) 

Installation
============

1. Clone this repository to your local machine:

    git clone https://github.com/zachary-hawk/word_cloud.git

2. Navigate to the project directory:

    cd word_cloud

3. Install the dependencies:

    python setup.py install

Usage
-----

Run the word_cloud script from the command line with the following arguments:

    usage: word_cloud [-h] [-f FONT] [-l LOGO] [-c COLOUR COLOUR] [-m MAX_WORDS] [--dpi DPI] [-o OUTPUT] file_path

    Create word cloud from a pdf document

    positional arguments:
      file_path             Name of the file to process

    optional arguments:
      -h, --help            show this help message and exit
      -f FONT, --font FONT  Specify the .otf font to be used
      -l LOGO, --logo LOGO  Specify the logo to be used to mask
      -c COLOUR COLOUR, --colour COLOUR COLOUR
                            Specify the main colour of the text
      -m MAX_WORDS, --max_words MAX_WORDS
                            Set the number of words allowed in the final output
      --dpi DPI             Set the number of words allowed in the final output
      -o OUTPUT, --output OUTPUT
                            File name for output png

Example usage:

    word_cloud my_document.pdf -f my_font.otf -l logo.png -c purple black -m 5000 --dpi 300 -o output.png

License

This project is licensed under the MIT License - see the LICENSE file for details.
