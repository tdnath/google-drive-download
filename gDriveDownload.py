# import required pkgs
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Create local webserver which automatically handles authentication.
gauth.LocalWebserverAuth()

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

# define the mimeType to which one you want to download
mimetypes = {
    # Drive Document files as MS Word files.
    #'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	
	# Drive video mp4 files as mp4 files.
	".mp4", "video/mp4",
	
	#etc.
}

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

for file1 in file_list:
    download_mimetype = None
    if file1['mimeType'] in mimetypes:
        download_mimetype = mimetypes[file1['mimeType']]
        file1.GetContentFile(file1['title'], mimetype=download_mimetype)
