from flask import Flask, render_template

app = Flask(__name__)

# Home Page Route
@app.route('/')
def home():
    return render_template('home.html')

# About Page Route  
@app.route('/about')
def about():
    return render_template('about.html')

# Skills Page Route
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Projects Page Route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    