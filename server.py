from flask import Flask, render_template, url_for,request, redirect
import csv
app = Flask(__name__)
print(__name__)
# Routing 
@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

# write to file 
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		#write contents extracted from data
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')
	
# here function to call it to database,
def write_to_csv(data):
	
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		# we are writing to database, with the given options
		# each item in row seperated with comma from database
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # each item in row seperated with comma from database
		csv_writer.writerow([email,subject,message])


#  A post request from the contact form

@app.route('/submit_form', methods=['POST', 'GET'])

def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		# once user fills contact form and submits
		return redirect('/thankyou.html')
	else:
		return 'Something went wrong, Try again'
	

'''
@app.route('/components.html')
def components():
	return render_template('components.html')
'''
