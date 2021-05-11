import os

from flask import Flask, render_template, send_file
import markdown as md

app = Flask(__name__)

@app.route('/')
def route_index():
    files = os.listdir('markr/documents')
    documents = []
    for filename in files:
        document = {}
        document["filename"] = filename
        with open(f'markr/documents/{filename}','r') as f:

            # try to find the title from the file
            try:
                for line in f:
                    title = line 
                    if len(title) != 1:
                        break

                #expect an _italic_ for the description, if there is none, ignore it.
                description = f.readline()
                if description[0] != '_':
                    description = ''
                else:
                    #get rid of the markdown underscores
                    description = description.rstrip()
                    description = description[1:-1]


            except (IndexError, UnicodeDecodeError):
                #something went wrong while parsing the file, just set the title to the filename to be safe
                title = filename
                description = ''
            
            #limit length of description to a preview of 100 chars
            limit = 100

            if len(description) > limit:
                description = description[:limit] 
                description += '...'

            #get rid of h1 hashtag
            title = title.replace('#','')
            if title[0] == " ":
                title = title[1:]
        document["title"] = title
        document["description"] = description 
        documents += [document]

    return render_template('home.html',documents=documents)

@app.route('/document/<name>')
def route_document(name):
    if not safety(name):
        return render_template('document.html',document='<h1>:(</h1><p>bad file name</p>')

    with open(f'markr/documents/{name}','r') as f:
        content = f.read()
    html = md.markdown(content, extensions=['tables'])        

    print(html)
    return render_template('document.html',document=html,filename=name)


@app.route('/raw/<name>')
def route_raw(name):
    filepath = f'documents/{name}'
    return send_file(filepath)

def safety(filename):
    #some defense against file inclusion, because I am paranoid
    safe_characters= 'abcdefghijklmnopqrstuvwxyz._-0123456789'
    for i in range(len(filename)):
        if filename[i].lower() not in safe_characters:
            return False
    return True

if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0',port=5000)
