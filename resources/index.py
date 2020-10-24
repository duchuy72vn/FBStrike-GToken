import hashlib, requests, argparse, json

def GToken(data):
    r = requests.get('https://api.facebook.com/restserver.php',params=data)
    a = json.loads(r.text)
    print(a)
    print(a['access_token'])

parser = argparse.ArgumentParser()
parser.add_argument("--username")
parser.add_argument("--password")
args = parser.parse_args()

username = args.username
password = args.password

username = username.replace("-", " ")

try:
    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":username,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":password,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+username+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+password+'return_ssl_resources=0v=1.0'+API_SECRET
    x = hashlib.new('md5')
    x.update(sig)

    data.update({'sig':x.hexdigest()})
    GToken(data)
except NameError:
    print(NameError + " : Error")