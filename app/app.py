import os 

from  app import create_app 

 
#123
#123
from  app.anuncios.routes.urls  import *

if __name__=='__main__':
     config_mode = os.getenv("FLASK_CONFIG", "development")
     app = create_app(config_mode)
     app.run()
#end-if
