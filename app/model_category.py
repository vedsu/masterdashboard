# Category Component

from app import mongo

class Category():

    @staticmethod
    def industry():
        industry_data = []

        try:
            industry_data = list(mongo.db.category_data.find({}))
        except Exception as e:
            industry_data = []
        return industry_data
    
    @staticmethod
    def categories(industry, category):

        try:
            mongo.db.category_data.update_one(
                {"industry":industry},
                {"$addToSet": {"categories": category}})
            return {"success":True, "message": "category added successfully"}
        
        except Exception as e:
            return {"success": False, "message":str(e)}
            
