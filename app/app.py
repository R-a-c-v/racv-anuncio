import os 

from  app import create_app 

config_mode = os.getenv('CONFIG_MODE') or 'development'
app = create_app(config_mode)

from  app.anuncios.routes.urls  import *

if __name__=='__main__':
     app.run(debug=True)
#end-if