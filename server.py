from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/displayImage/')
def displayImage():
	import subprocess
	#subprocess.call(['/home/robotic/app/imgCapture.sh'])
	ans1 = subprocess.check_output(['/home/wiki/ab/app/imgCapture.sh'])
	return render_template('template.html',src=ans1)
@app.route('/list_of_errors', methods=['POST'])
def list_of_errors():
	import subprocess
	#import subprocess
	errors = subprocess.check_output(['/home/wiki/ab/app/black.sh'])
	var =  subprocess.check_output(['/home/wiki/ab/app/black.sh']).split('\n')
	return render_template('template.html', errors=errors , var=var)

	
	

	"""import glob, os
	os.chdir("/home/robotic/app/static")
	took = glob.glob("*.jpeg")
	
	for file in took:
    		answer=format(file)
		
	return render_template('mongoose.html',took=took,answer=answer)"""
	




	                                                                                                                                 	 
if __name__ == '__main__':
  app.run(host='0.0.0.0')
