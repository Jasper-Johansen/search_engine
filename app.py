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
        
        # Load inverted index from JSON file and process the search query
        results = crawler.process_query(query)  # Uses the inverted index from the file

        if not results:
            # Handle the case where no results are found
            return render_template('results.html', results=[], message="No results found.")
        
        return render_template('results.html', results=results)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to True for development purposes
