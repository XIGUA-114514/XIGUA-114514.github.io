import os
from flask import Flask, request, render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return '文件上传成功！<a href="/" class="back-button" style="position: absolute; top: 40px; left: 40px; background-color: #FF6347; color: #fff; padding: 12px 24px; border: 2px solid #FF4500; border-radius: 8px; text-decoration: none; font-family: \'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif; font-size: 16px; font-weight: bold; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); transition: all 0.3s ease;">返回</a>'
    return '未选择文件。<a href="/" class="back-button" style="position: absolute; top: 40px; left: 40px; background-color: #FF6347; color: #fff; padding: 12px 24px; border: 2px solid #FF4500; border-radius: 8px; text-decoration: none; font-family: \'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif; font-size: 16px; font-weight: bold; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); transition: all 0.3s ease;">返回</a>'

if __name__ == '__main__':
    app.run(debug=True)