from flask import Flask, request, render_template

app = Flask(__name__, static_folder='.', static_url_path='')
data = []

@app.route('/')
def index():
  #return '<html><body><h1>Hello World</h1></body></html>' 
  return app.send_static_file('templates/index.html')

@app.route('/append', methods=['GET', 'POST'])
def append():
  if request.method == 'POST':
    data.append(request.form['message'])
    print(data)
    #return app.send_static_file('templates/index.html')
    return render_template('index.html', data=data)
  else:
    #return app.send_static_file('templates/index.html')
    return render_template('index.html', data=data)

@app.route('/display', methods=['GET', 'DELETE'])
def display():
  pass
  
"""
def display():
    if request.method == 'GET':
        html = '<html><body>'
        html += '<h1>Data Contents</h1>'
        html += '<form method="POST" action="/delete">'
        html += '<ul>'
        for item in data:
            html += f'<li><input type="checkbox" name="item" value="{item}">{item}</li>'
        html += '</ul>'
        html += '<input type="submit" value="Done">'
        html += '</form>'
        html += '</body></html>'
        return html
    else:
        return 'ERROR'
"""

@app.route('/delete', methods=['POST', 'DELETE'])
def delete():
    print(request.method)
    if request.method == 'POST':
        items_to_delete = request.form.getlist('item')
        print(items_to_delete)
        print(data)

        for item in items_to_delete:
            print(data)
            data.remove(item)
        
        # return display, GET method
        request.method = 'GET'
        return render_template('index.html', data=data)
    else:
        return render_template('index.html', data=data)


app.run(port=8080, debug=True)