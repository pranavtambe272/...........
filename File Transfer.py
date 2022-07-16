import dropbox

class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def upload_file(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)

        f=open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)

def main():
    accesstoken='sl.BKgax_sjVQtgcSBSbAvl_OCoyz_fEXg_Q4BTwyeXyKd5NR39_nifj4fV-AgEUS8W0MP54fHe8n2L5d0BmxIsr5sfy7yqiaaD0c2UPioefE66Xax8JI8WIyAlCOISSPvkvFnnIifximQi'
    transferdata=Transferdata(accesstoken)

    filefrom=input("Enter the file path to transfer : ")
    fileto=input("Enter the full path to upload to dropbox : ")

    transferdata.upload_file(filefrom,fileto)
    print("File has been moved.")

main()