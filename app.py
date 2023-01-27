from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def run_colab():    
    success = gdown.download('https://colab.research.google.com/drive/1AnkaT2HS5xfZVcIozbBqqDGSS8gEqOD0', 'colab.ipynb', quiet=False)
    if success:
        return jsonify(message='colab notebook downloaded successfully')
    else:
        return jsonify(message='error while downloading colab notebook')

if __name__ == '__main__':
    app.run()
