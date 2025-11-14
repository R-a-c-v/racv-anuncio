import os 

from flask import  request ,jsonify

from  app import create_app 
from  app.listing.services.create  import create 
from  app.listing.services.list  import list

config_mode = os.getenv('CONFIG_MODE') or 'development'
app = create_app(config_mode)

from  app.listing.routes.urls  import *

if __name__=='__main__':
     app.run(debug=True)
#end-if