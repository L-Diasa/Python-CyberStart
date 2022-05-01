import zipfile

zf = zipfile.ZipFile("alien-sample-42.zip")
for password in possiblePasswordList:
    try:
        zf.extract(member='alien-sample-42.txt',
            path='/tmp/', pwd = str(password).encode())
        print('Password found: %s' % password)
        break
    except:
        pass
else:
    print('No valid password found.')
