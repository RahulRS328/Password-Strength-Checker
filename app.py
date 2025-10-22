from flask import Flask, render_template, request, redirect, url_for

# ---
# --- STEP 1: Import all your functions from analysis.py ---
# ---
from analysis import analyze_password, suggest_stronger_password, check_pwned


# Create the Flask app
app = Flask(__name__)

# ---
# --- Routes ---
# ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # You can add real login logic here later
        username = request.form['username']
        # For now, just redirect to the index
        return redirect(url_for('index'))
        
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    # Set default values for a GET request
    username_to_show = "Guest" 
    result = None
    suggestion = None
    breached = None

    if request.method == 'POST':
        # ---
        # --- STEP 2: Call your real functions ---
        # ---
        
        # 1. Get the password from the form
        password = request.form['password']
        
        # 2. Call each of your analysis functions
        result = analyze_password(password)
        suggestion = suggest_stronger_password(password)
        breached = check_pwned(password)

        # 3. Render the template with the REAL data
        return render_template('index.html', 
                               username=username_to_show, 
                               result=result, 
                               suggestion=suggestion, 
                               breached=breached)

    # For a GET request, just show the page without results
    return render_template('index.html', username=username_to_show)


# ---
# --- Run the app ---
# ---
if __name__ == "__main__":
    app.run(debug=True)