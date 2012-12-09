##Next steps:
##enhance the image library creation
##enable the mosiac making part of the code
##Think about filtering image search by license
##Prevent the re-upload to items
##Check for file extension and file size when uploading

## Imports
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from random import random, choice, shuffle
from werkzeug import secure_filename
from math import floor
import os, ast
import mosaicModule
from time import time

UPLOAD_FOLDER='data/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

## Application Initialization
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
## This is the bridge between variables in the app.py file and
## variables in the index.html file
def index():
        sampleMosaicPics = sampleMosaicList
        
        randImgList=[]
        for i in range(len(imageUrlArray)):
                index=int(floor(100*random()))
                randImgList.append(imageUrlArray[i][index])

        sampleFile = open("newFile.txt",'a')

        filename=""
        filesource="uploads/NoFileChosen.PNG"
        upload_message="You have not yet uploaded anything"
        if request.method == 'POST':
                file = request.files['file']
                #if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                sampleFile.write(filename+': was added at '+str(time())+'\n')
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filesource=os.path.join("uploads/", filename)
                sampleFile.write(filesource+'\n')
                upload_message="You have just uploaded: "
                #return redirect(url_for('uploaded_file',filename=filename))
                
        sampleFile.close()
                
	return render_template('index.html',
                               sampleMosaicPics=sampleMosaicPics,
                               randomImages=randImgList,
                               filename=filename,
                               filesource=filesource,
                               upload_message=upload_message
                               )

## This gathers a list of sample mosaic pics from a specified dir. 
sampleMosaicList=[]
currentDir=os.getcwd()
sampleMosaicDir=currentDir+"/static/sample_mosaics"
for item in os.listdir(sampleMosaicDir):
        sampleMosaicList.append("/static/sample_mosaics/"+item)

## Get a list of queries (not actually user selected) and return them
def getUserSelectedQueries(fileContents):
        listOfQueries=[]

        for item in fileContents:
                if item[:7]=="Search:":
                        listOfQueries.append(item[8:-1])

        querySelection=(1,2,3,4,5,6,7,8,9)

        userSelectedQueries=[]
        try:
                for item in querySelection:
                        userSelectedQueries.append(listOfQueries[item-1])
        except:
                userSelectedQueries.append(listOfQueries[querySelection-1])

        return userSelectedQueries

## Takes a list of strings that are query terms and the entire
## query file and gives all the urls for each term in a separate tuple?
def getImgUrl(selection, fileContents):
        imageUrlArray=[]
        intermediate=[]
        singleQueryImageList=[]

        for item in selection:
                for i in range(len(fileContents)):
                        if fileContents[i][8:-1]==item:
                                singleQueryImageList=fileContents[i+2]
                                singleQueryImageList=ast.literal_eval(singleQueryImageList[:-1])
                                imageUrlArray.append(singleQueryImageList)

        return imageUrlArray

## Uses the above functions and generates a list of random urls
## (One from each term)
filenameIQ = "data/savedImageQueriesF1.log"
imageQueryData = mosaicModule.getFileContents(filenameIQ)
selection = getUserSelectedQueries(imageQueryData)
imageUrlArray = getImgUrl(selection, imageQueryData)
##randImgList=[]
##for i in range(len(imageUrlArray)):
##        index=int(floor(100*random()))
##        randImgList.append(imageUrlArray[i][index])

##----File Upload----##
def upload_file():
        if request.method == 'POST':
                file = request.files['file']
                if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        return redirect(url_for('uploaded_file',filename=filename))
        
##        return '''
##        <!doctype html>
##        <title>Upload new File</title>
##        <h1>Upload new File</h1>
##        <form action="" method=post enctype=multipart/form-data>
##              <p><input type=file name=file>
##                      <input type=submit value=Upload>
##        </form
##        '''
        

@app.route('/uploads/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],filename)



##---- Just a Test ----##
@app.route('/user', methods=['GET', 'POST'])
def user():
        return render_template('brewSelector.html')

  
## This makes the app run - it goes at the end. 
if __name__ == '__main__':
        port = int(os.environ.get('PORT',5000))

        if port == 5000:
                app.debug = True

        app.run(host='0.0.0.0', port=port)
	
	
