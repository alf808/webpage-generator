import os

"""This app will generate web pages from raw text files"""
# list the files in raw directory
raw_files = os.listdir("raw")

# iterate through and process text files
for rf in raw_files:
    with open(f"raw/{rf}", "r") as fin:
        # assuming first line is title
        title = fin.readline()
        # get rest of text
        content = ""
        for line in fin.readlines()[1:]:  # except for first line
            #  concatenate to empty content
            #
            content += f"<p>{line.rstrip()}</p>"
        webpage = f"""<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {content}
</body>
"""
        #  get the name of original file minus the .txt
        with open(f"raw/{rf[:-4]}.html", "w") as fout:
            fout.write(webpage)
