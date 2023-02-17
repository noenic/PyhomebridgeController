
class HBChildBridge:
    def __init__(self,HBController) -> None:
        self.HBController = HBController


    def restart_child(self,childID:str)-> bool:
        """Restart a child bridge

        **This method is only available when running hb-service.**

        Args:
            childID (str): The child bridge ID

        Returns:
            bool: True if the child bridge is restarted"""
        response= self.HBController.send_request("PUT","server/restart/"+childID).json()
        if "ok" in response:
            return True
        else:
            raise Exception(response['message'])
    
    def stop_child(self,childID:str)-> bool:
        """Stop a child bridge

        **This method is only available when running hb-service.**

        Args:
            childID (str): The child bridge ID

        Returns:
            bool: True if the child bridge is stopped"""
        response= self.HBController.send_request("PUT","server/stop/"+childID).json()
        if "ok" in response:
            return True
        else:
            raise Exception(response['message'])

        
    def start_child(self,childID:str)-> bool:
        """Start a child bridge

        **This method is only available when running hb-service.**

        Args:
            childID (str): The child bridge ID

        Returns:
            bool: True if the child bridge is started"""
        response= self.HBController.send_request("PUT","server/start/"+childID).json()
        if "ok" in response:
            return True
        else:
            raise Exception(response['message'])




    
    def get_status_child_bridges(self)-> list:
        """Return an list of the active child bridges and their status (dict)


        Returns:
            list: a list of dict with the child bridges info"""
        return self.HBController.send_request("GET","status/homebridge/child-bridges").json()
