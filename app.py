from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/run-colab')
def run_colab():    
    gdown.download('https://colab.research.google.com/drive/1AnkaT2HS5xfZVcIozbBqqDGSS8gEqOD0', 'colab.ipynb', quiet=False)
    #return jsonify(message='colab notebook ran successfully')
    return "AI was triggered! 2"

if __name__ == '__main__':
    app.run()
