# Webinar component

from app import mongo

class Webinar():
    
    @staticmethod
    def view_webinar():
        
        # Webinar list for display
    
        webinar_list =[]
        try: 
        
            webinar_data = list(mongo.db.webinar_data.find({}))
            for webinar in webinar_data:
                webinar_dict ={
        
                "id":webinar["id"],

                "topic":webinar["topic"],
                "industry":webinar["industry"],
                "speaker":webinar["speaker"],
                "date":webinar["date_time"],
                "time":webinar["time"],
                "timeZone":webinar["timeZone"],
                "duration":webinar["duration"],
                "category":webinar["category"],
                
                "sessionLive":webinar["sessionLive"],
                "priceLive":webinar["priceLive"],
                "urlLive":webinar["urlLive"],
                
                "sessionRecording":webinar["sessionRecording"],
                "priceRecording":webinar["priceRecording"],
                "urlRecording":webinar["urlRecording"],

                "sessionDigitalDownload":webinar["sessionDigitalDownload"],
                "priceDigitalDownload":webinar["priceDigitalDownload"],
                "urlDigitalDownload":webinar["urlDigitalDownload"],
                
                "sessionTranscript":webinar["sessionTranscript"],
                "priceTranscript":webinar["priceTranscript"],
                "urlTranscript":webinar["urlTranscript"],

                "status":webinar["status"],
                "webinar_url": webinar["webinar_url"],
                "description":webinar["description"],
                    
                    }
                    
                webinar_list.append(webinar_dict)
        
        except Exception as e:
                webinar_list = []
        
        
        return webinar_list
          
    
    @staticmethod
    def create_webinar(webinar_data):
        
        try:
            mongo.db.webinar_data.insert_one(webinar_data)
            return {"success":True, "message": "webinar created successfully"} 
        
        except Exception as e:
            return {"success":False, "message":str(e)}
    
    @staticmethod
    def data_webinar(w_id):
        
        webinar_info = None
        try: 
            
            webinar_data = list(mongo.db.webinar_data.find({"id":w_id}))
            webinar = webinar_data[0]
               
            webinar_data_dict ={
            
                    "id":webinar ["id"],

                    "topic":webinar ["topic"],
                    "industry":webinar ["industry"],
                    "speaker":webinar ["speaker"],
                    "date":webinar ["date_time"],
                    "time":webinar ["time"],
                    "timeZone":webinar["timeZone"],
                    "duration":webinar["duration"],
                    "category":webinar["category"],
                    
                    "sessionLive":webinar ["sessionLive"],
                    "priceLive":webinar ["priceLive"],
                    "urlLive":webinar ["urlLive"],
                    
                    "sessionRecording":webinar ["sessionRecording"],
                    "priceRecording":webinar ["priceRecording"],
                    "urlRecording":webinar ["urlRecording"],

                    "sessionDigitalDownload":webinar ["sessionDigitalDownload"],
                    "priceDigitalDownload":webinar ["priceDigitalDownload"],
                    "urlDigitalDownload":webinar ["urlDigitalDownload"],
                    
                    "sessionTranscript":webinar ["sessionTranscript"],
                    "priceTranscript":webinar ["priceTranscript"],
                    "urlTranscript":webinar ["urlTranscript"],

                    "status":webinar ["status"],
                    "webinar_url": webinar ["webinar_url"],
                    "description":webinar ["description"],

                    }
            webinar_info = webinar_data_dict
        except Exception as e:
            webinar_info = None
        
        return webinar_info

    @staticmethod
    def update_webinar(w_id, webinar_data):
        
        try:
            
            mongo.db.webinar_data.update_one({"id":w_id},{"$set": webinar_data})
            return {"success":True, "message":"webinar update successfull"}
        
        except Exception as e:
            return {"success": False, "message": str(e)}
        

    @staticmethod
    def edit_webinar(w_id, webinar_status):
        
        try:
            
            mongo.db.webinar_data.update_one({"id":w_id},{"$set": {"status": webinar_status}})
            return {"success":True, "message":"status update successfull"}
        
        except Exception as e:
            return {"success": False, "message": str(e)}

    @staticmethod
    def delete_webinar(w_id):
        
        try: 
            mongo.db.webinar_data.delete_one({"id":w_id})
            return {"success":True,"message": " deleted sucessfully"}
        
        except Exception as e:
            return {"success":False, "message": str(e)}
    
