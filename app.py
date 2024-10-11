from flask import Flask, request, render_template
import crawler  # Import your crawler and parser functions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Create a home page

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = crawler.process_query(query, inverted_index)  # Adjust based on your function
        return render_template('results.html', results=results)  # Render results page
    return redirect('/')  # Redirect if not POST

if __name__ == '__main__':
    app.run(debug=True)
