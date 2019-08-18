## Download All files from Google Drive with a python script 

### Enable *Google Drive API* from Google developers console & set the client key and download client_secrets.json file

**Using Google developers console** 
Steps
1. Go to https://console.developers.google.com/apis/dashboard
2. Search for *Google Drive API* & click *Enable*
3. Click *Create credentials*
4. In *Add credentials to your project*

   Choose 
- *Google Drive API*
- *Web server (e.g. node.js, Tomcat)* or *Other UI (e.g. Windows, CLI tool)*
- *User data* 
- Click *What credentials do I need?*
5. Click *Create OAuth client ID* & *Done*
6. Now Download JSON by clicking small down arrow 



**Using OAuth 2.0 Playground**
Steps
1. Go to https://developers.google.com/oauthplayground/
2. Select *Drive API v3* API and 'https://www.googleapis.com/auth/drive.readonly'
3. Click button *Authorize APIs*
4. Choose Account and click on *Allow* for Playground API
5. Click on *Exchange authorization code for tokens* button
6. Copy the *Access token*
7. Now use the curls in the following way


### CURLs

**DOS/Windows**

Invoke-RestMethod -Uri https://www.googleapis.com/drive/v3/files/<google_drive_file_id>?alt=media -Method Get -Headers @{"Authorization"="Bearer <access_token>"} | Out-File <output_file_name>

**Mac/Linux/Ubuntu**

curl -H "Authorization: Bearer <access_token>" https://www.googleapis.com/drive/v3/files/<google_drive_file_id>?alt=media -o <output_file_name>