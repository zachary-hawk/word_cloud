import os
import string
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud,STOPWORDS
import PyPDF2
import textract
import numpy as np
import matplotlib.colors
from PIL import Image
import argparse

    
def main():    
    parser = argparse.ArgumentParser(description="Create word cloud from a pdf document")
        
    parser.add_argument("file_path", help="Name of the file to process")
    parser.add_argument("-f", "--font", help="Specify the .otf font to be used")
    parser.add_argument("-l", "--logo", help="Specify the logo to be used to mask")
    parser.add_argument("-c", "--colour", help="Specify the main colour of the text",nargs=2,default=['purple','black'])
    parser.add_argument("-m", "--max_words", help="Set the number of words allowed in the final output",default=3500)
    parser.add_argument("--dpi", help="Set the DPI of the final output",default=200)
    parser.add_argument("-o", "--output", help="File name for output png",default='word_cloud.png')
    
    
    args = parser.parse_args()
    
    # Accessing the values of arguments
    file_path = args.file_path
    font_path = args.font
    logo = args.logo
    colour = args.colour
    max_words = args.max_words
    dpi=args.dpi
    output = args.output
        
    def read_file_textract(filepath):
        text = textract.process(filepath)
        return text.decode("utf-8") 
    
    
    def read_file_pypdf(filepath):
        pdfFileObj = open(filepath,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages
        text = ""
        # Read all the pages
        for pg in range(num_pages):
            page = pdfReader.getPage(pg)
            text += page.extractText()
        return text
    def read_file(filepath, use_method = 'textract'):
        
        text = ""
        if not os.path.isfile(filepath):
            print(f'Invalid file:{filepath}')
        else:
            if use_method == 'textract':
                return read_file_textract(filepath)
            elif use_method == 'pypdf':
                return read_file_pypdf(filepath)
            else:
                print('Invalid method to read file. Supported formats: "textract" or "pypdf".')
        
        return text
    
    def extract_keywords(text, ignore_words = [],
                         min_word_length = 3,
                         ignore_numbers = True,
                         ignore_case = False):
        # Remove words with special characters
        filtered_text = ''.join(filter(lambda x:x in string.printable, text))
        
        # Create word tokens from the text string
        tokens = word_tokenize(filtered_text)
        
        # List of punctuations to be ignored 
        punctuations = ['(',')',';',':','[',']',',','.','--','-','#','!','*','"','%','/']
        
        # Get the stopwords list to be ignored
        stop_words = stopwords.words('english')
    
        # Convert ignore words from user to lower case
        if ignore_words is not None:
            ignore_words_lower = [x.lower() for x in ignore_words]
            # Combine all the words to be ignored
            all_ignored_words = punctuations + stop_words + ignore_words_lower
        else:
            all_ignored_words = punctuations + stop_words
            
        # Get the keywords list
        keywords = [word for word in tokens \
                        if  word.lower() not in all_ignored_words
                        and len(word) >= min_word_length]    
    
        # Remove keywords with only digits
        if ignore_numbers:
            keywords = [keyword for keyword in keywords if not keyword.isdigit()]
        
    
        # Return all keywords in lower case if case is not of significance
        if ignore_case:
            keywords = [keyword.lower() for keyword in keywords]
        
        return keywords
    
    
    def create_word_cloud(keywords, maximum_words = 100, bg = 'white', cmap='Dark2',
                          maximum_font_size = 190, width = 1308, height = 1505,
                          random_state = 42, fig_w = 8, fig_h = 8, font_path=None,output_filepath = None):
        
        # Convert keywords to dictionary with values and its occurences
        word_could_dict=Counter(keywords)
    

        if logo is not None:
            mask = np.array(Image.open(logo))
        else:
            mask =None
        wordcloud = WordCloud(background_color=bg, max_words=maximum_words, colormap=cmap,mask=mask, 
                              stopwords=STOPWORDS, max_font_size=maximum_font_size,contour_width=0.,contour_color='gray',
                              random_state=random_state,font_path=font_path, relative_scaling=0.2,
                              width=width, height=height).generate_from_frequencies(word_could_dict)
        
        plt.figure(figsize=(fig_w,fig_h))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        if output_filepath:
            plt.savefig(output_filepath, bbox_inches='tight')
        plt.tight_layout()
        plt.savefig(output,dpi=dpi)
        plt.close()
    
    #ignore=['cr1/3','1.0','1.5','nbs2','cu2','tsa2','0.5','gav4','oseo3','clo4','fig','chapter','tas2','al.','jeff','2.5','Se8','S8','0.0','Ti2','Dy2','Phys','Rev','pyz','gly','Figure','eects','SkL']
    #print(ignore)
    try:
        ignore = np.loadtxt('exclude.txt',dtype=str)
    except:
        ignore=None
    
    file_text = read_file(file_path)
    keywords = extract_keywords(file_text, min_word_length = 3,ignore_words=ignore)
    
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [colour[0],colour[1]])
    create_word_cloud(keywords,maximum_words=max_words,cmap=cmap,bg='white',font_path=font_path)
    
    
if __name__ == "__main__":
    main()
