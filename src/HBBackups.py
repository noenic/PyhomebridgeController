import os
class HBBackups:
    def __init__(self,HBController) -> None:
        self.HBController = HBController


    def download_backup(self,filename:str="Backup",dir:str=".")-> str:
        """Download a .tar.gz of the Homebridge instance.


        returns:
            str: path to the backup file"""
             #Remove the .tar.gz extension if it's present
        if filename.endswith(".tar.gz"):
            filename = filename[:-7]
            
        response = self.HBController.send_request("GET","backup/download").content
        #We save the file in the dir directory
        path = os.path.join(dir,filename+".tar.gz")
        with open(path,"wb") as f:
            f.write(response)
        return path

    def get_next_scheduled_backup(self)-> dict:
        """Return the date and time of the next scheduled backup.

        Returns:
            dict: a dict with the next scheduled backup
        """
        return self.HBController.send_request("GET","backup/scheduled-backups/next").json()
    
    def get_generated_backups(self)-> dict:
        """Return the generated backups from the system.

        Returns:
            dict: a dict with the generated backups 
        """
        return self.HBController.send_request("GET","backup/scheduled-backups").json()

    def download_specific_backup(self,id:str,filename:str="Backup",dir:str=".")-> str:
        """Download a system generated instance backup.

        Args:
            id (str): the id of the backup

        Returns:
            str: path to the backup file
        """
        #Remove the .tar.gz extension if it's present
        if filename.endswith(".tar.gz"):
            filename = filename[:-7]

        response = self.HBController.send_request("GET","backup/scheduled-backups/"+id).content
        #We save the file in the dir directory
        path = os.path.join(dir,filename+".tar.gz")
        with open(path,"wb") as f:
            f.write(response)
        return path
    

    def upload_backup(self,path:str)-> dict:
        """Upload a .tar.gz of the Homebridge instance.

        Args:
            path (str): path to the backup file

        Returns:
            dict: a dict with the status of the upload
        """
        # f = {'upload_file': open(path,"rb")}
        # response = self.HBController.send_request("POST","backup/restore",files=f)
        # return response
        raise Exception("Not implemented yet, API not responding")

    
    def trigger_backup_restore(self)-> dict:
        """Triggers a headless restore process from the last uploaded backup file.

        Returns:
            dict: a dict with the status of the backup
        """
        return self.HBController.send_request("PUT","backup/restore/trigger").json()

    def restore_from_hbfx(self,path:str)-> dict:
        """Upload a .hbfx backup file created by third party apps.

        Returns:
            dict: a dict with the status of the backup
        """
        f = {'upload_file': open(path,"rb")}
        response = self.HBController.send_request("POST","backup/restore/hbfx",files=f)
        return response

    def hard_restart_after_restore(self)-> bool:
        """Trigger a hard restart of Homebridge (use after restoring backup).

        Returns:
            bool: True if the restart was successful
        """
        return self.HBController.send_request("PUT","backup/restart").json()['status']==0
