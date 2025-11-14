from flask import  request
 
from  ...app import app
from app.listing.services.controllers import delete
from app.listing.services.controllers import retrieve_listing
from app.listing.services.create import create
from app.listing.services.list import list
from app.listing.services.update import update

@app.route("/anuncio", methods=['GET', 'POST'])
def create_list_listings():
    if request.method == 'GET': return list()
    if request.method == 'POST': return create()    
#end-def

@app.route("/listings/<listing_id>", methods=['GET', 'DELETE', 'PUT'])
def retreive_upadate_destroy_accounts(listing_id):
    
    if request.method == 'GET': return retrieve_listing(listing_id) 
    elif request.method == 'DELETE': return delete(listing_id)
    elif  request.method == 'PUT': return update(listing_id)
#end-def