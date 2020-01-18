from flask import Flask, render_template, request
import os
import json
        
def server():
    
    FOLDER = os.path.join('static', 'photo')
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = FOLDER

    # root      
    @app.route("/up", methods=['POST','GET'])
    def up():
        print('up') 
        return 's'  
    
    @app.route("/down", methods=['POST','GET'])
    def down():
        print('down')
        return 'ss'
        
    @app.route("/display")
    def index():
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'map_final.png')
        return render_template("index.html", user_image = full_filename)

    @app.route('/start', methods=['POST','GET'])
    def jsonreq():
        global data
        data = request.get_json('msg')
        print (data)
        execfile('modules/start.py')
        return data['msg']
    
    # running web app in local machine
    if __name__ != '__main__':
        app.run(host='0.0.0.0', port=5000)
    return data

