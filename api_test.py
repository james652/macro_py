import requests

uploadUrl = 'https://nidvia.co.kr/api/qr/upload'        # Server
# uploadUrl = 'http://localhost:3000/api/qr/upload'     # TEST Local
qrImageFileName = 'nvidia_signin_with_qr.png'
qrCaptureImageFile = open(qrImageFileName, 'rb')
uploadFiles = {'file': (qrImageFileName, qrCaptureImageFile, 'image/png')}
# headers = {'Content-Type' : 'image/jpeg'}

print(uploadFiles)
res = requests.post(uploadUrl, files=uploadFiles)

print(res)

