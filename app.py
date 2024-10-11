from flask import Flask, request, render_template, redirect
import crawler  # Import your crawler and parser functions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        
        # Load inverted index from JSON file
        results = crawler.process_query(query)  # Now this uses the inverted index from the file
        
        return render_template('results.html', results=results)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for better performance
