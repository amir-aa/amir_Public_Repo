#written by Amir The scientist
from flask import Flask,request,jsonify,render_template,stream_with_context
import requests,os

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download',methods=['POST'])
def download_url():
    def download():
        url=request.form['url']
        response=requests.get(url,stream=True)
        totalsize=response.headers.get('content-length',0)
        print("Size to be downloaded",totalsize)
        downloaded_size=0
        savepath='downloads'
        os.makedirs(savepath,exist_ok=True)
        savepath= os.path.join(savepath,'file.zip')

        with open(savepath,'wb') as f:
            for data in response.iter_content(chunk_size=4096):
                downloaded_size+=len(data)
                f.write(data)
                yield f"{downloaded_size} Bytes"
        yield f"{downloaded_size} COMPLETED!"
    return stream_with_context(download())
app.run()
