from bs4 import BeautifulSoup
import os

# Add the path to your files (the directory you're working in)
working_directory = '/Users/shikha/Desktop/Sarvangi/Sarvangi'
os.chdir(working_directory)  # Ensure you're in the correct directory
print(f"Current Working Directory: {os.getcwd()}")  # Print the current directory

new_header_content = """
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>The Sarvāṅgī of Gopāldās</title>
      <editor role="Digital Editor">
        <persName>Shikha Thakur</persName>
      </editor>
    </titleStmt>
  </fileDesc>
  <sourceDesc>
    <p>Gopāladāsa, Sarvāṅgī (abbrev. GopS)</p>
    <p>Source: Winand Callewaert, The Sarvāṅgī of Gopāldās, New Delhi, Manohar Book Publications, 1993; 520pp.; text pp. 119-521.</p>
    <p>The text below of The Sarvāṅgī of Gopāldās is a revised version of the printed text referred to above. Working on the Dictionary of Bhakti and checking the manuscript once more has yielded some useful corrections which in the text below are highlighted in yellow.</p>
  </sourceDesc>
</teiHeader>
"""

# Start the TEI XML structure
tei = """<?xml version="1.0" encoding="utf-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">"""
tei += new_header_content
tei += "<text><body>"

# Process each file
for i in range(1, 127):
    file_path = f"section{i}.xml"
    if os.path.exists(file_path):
        print(f"Processing file: {file_path}")  
        with open(file_path, "r", encoding="utf-8") as file:
            section_content = file.read()
            soup = BeautifulSoup(section_content, "xml")
            tei += soup.div.prettify()
    else:
        print(f"File not found: {file_path}")  
tei += "</text></body>"    
tei += "</TEI>"

# Parse the complete XML and write to a new file
soup = BeautifulSoup(tei, "xml")
with open("sarvangi_of_gopaldaS.xml", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
    print("Completed writing to sarvangi_of_gopaldaS.xml")  

