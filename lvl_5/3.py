import zipfile

zf = zipfile.ZipFile("alien-zip-2092.zip")
for password in range(100,1000):
    try:
        zf.extract(member='alien-zip-2092.txt',
            path='/tmp/', pwd = str(password).encode())
        print('Password found: %s' % password)
        break
    except:
        pass
else:
    print('No valid password found.')

