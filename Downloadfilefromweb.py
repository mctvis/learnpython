from urllib import request
goog_url="https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/AirPassengers.csv"

def downloaddata(file_url):
    response=request.urlopen(file_url)#open the file ..sortof  ...simlar to opening a file
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest_url=r'goog.csv'
    fx=open(dest_url,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

downloaddata(goog_url)

