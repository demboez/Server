from ftplib import FTP

def check_ftp_server_status(host):
    try:
        ftp = FTP(host)
        ftp.login()
        ftp.quit()
        return f"FTP server {host} is up"
    except Exception as e:
        return f"Failed to connect to FTP server: {e}"

host = "ftp.scene.org"
status = check_ftp_server_status(host)
print(status)
