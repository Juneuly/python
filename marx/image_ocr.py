from aip import AipOcr

APP_ID = '11123355'
API_KEY = 'fYa3mQynKxYF3acsb3CaYZtk'
SECRET_KEY = '5Uov4KXkOW4Lv9WiagMn0pq69tlwuBv2'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('test.jpeg')

res = client.general(image)
for item in res['words_result']:
    print(item['words'])
