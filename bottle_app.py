
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file , template
import json
from bottle import get, post, request, redirect
from hashlib import sha256	
	
	
def create_hash(passw):
	pw_byte = passw.encode()
	return sha256(pw_byte).hexdigest()
	
def htmlify(background_image):
    return 	template('template.tpl' , img_name = background_image , name = 'sfc' , style_hr = 'styles.css')

def index():
    return htmlify(background_image = "./img/start-actiongimpenhanced.png")

#def comment():
	
	


@route('/img/<img_name>')	
def route_img(img_name):
	return static_file(img_name , root = './img')

@route('/styles.css')
def route_style():
	return static_file('/styles.css', root = './')

@route('/comments/wrongpw')
def get_comm():
	with open('comments.json') as file2:
		commdata = json.load(file2) 
	return template('test' , name = 'sfc' , comments = commdata['comments'] , wrongpw = True)

@route('/comments')
def get_comm():
	with open('comments.json') as file2:
		commdata = json.load(file2) 
	return template('test' , name = 'sfc' , comments = commdata['comments'] , wrongpw = False)

route('/index', 'GET', index)
route('/', 'GET', index)



#route('/comments','GET',comment);


@route('/comments', method='POST')
def post_comment():
    author = request.forms.get('author')
    context = request.forms.get('content')
    pw = request.forms.get('password')
    hashedpw = create_hash(pw)
    new_com = { "author" : author, "content" : context}
    flag = 0
    with open("passwords.json",'r') as pws:
		if author in pws:
			if hashedpw != pws[author]:
				flag=1	
		else:	
			with open("passwords.json",'r') as collectpw:
				pws = json.load(collectpw)
				pws[author] = hashedpw
			with open("passwords.json",'w') as dumpfile:
				json.dump(pws , dumpfile)
	if flag == 0:
		with open("comments.json",'r') as collect:
			comments = json.load(collect)
			comments['comments'].append(new_com)
		with open("comments.json",'w') as dumpfile:
			json.dump(comments , dumpfile)
			redirect('/comments')
	else:
		redirect('/comments/wrongpw')












#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run(debug=True,reloader=True)

