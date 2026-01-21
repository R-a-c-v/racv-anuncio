import os 

from  app import create_app 

config_mode = os.getenv("FLASK_CONFIG", "development")
app = create_app(config_mode)

from  app.anuncios.routes.urls  import *

if __name__=='__main__':
     app.run(host="0.0.0.0",port = 5001, debug=True)
#end-if
