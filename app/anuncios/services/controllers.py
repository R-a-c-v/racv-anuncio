from datetime import datetime

from flask import request 
from flask import jsonify


from app import  dbt 
from  app.listing.models.anuncio import Anuncio

def delete(listing_id):
    try:
        Anuncio.query.filter_by( id_ad=listing_id).delete()
        dbt.session.commit()  
        return jsonify({'Response': "DONE "})
    except AttributeError as e:
        return jsonify({'Respose':"DATA NOT FOUND FOR DELETE"})
    #end-try
#end-def
         
def retrieve_listing(listing_id):
    try:
            response= Listing.query.get(listing_id).to_dict()
            return jsonify (response)
    except AttributeError  as e :
            return jsonify ({"Response": "DATA NOT FOUND"})
    #end-try
#end-def