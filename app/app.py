import os 

from  app import create_app 

config_mode = os.getenv('CONFIG_MODE') or 'development'
app = create_app(config_mode)
#123
#123
#123
#123
#123
#123

from  app.anuncios.routes.urls  import *

if __name__=='__main__':
     app.run(host="0.0.0.0",port = 5002, debug=True)
#end-if