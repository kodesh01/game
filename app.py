
# from flask import Flask, render_template, request, jsonify
# import random
# import numpy as np
# from sklearn.linear_model import LogisticRegression

# app = Flask(__name__)

# # AI model to predict player's movement
# player_moves = []  # Store past movements
# ai_model = LogisticRegression()
# def train_ai():
#     if len(player_moves) > 5:  # Train only if enough data
#         X = np.array(player_moves[:-1]).reshape(-1, 1)
#         y = np.array(player_moves[1:])
#         ai_model.fit(X, y)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/move', methods=['POST'])
# def move():
#     data = request.json
#     player_last_move = data['move']
#     player_moves.append(player_last_move)
#     train_ai()
    
#     # Predict the player's next move
#     ai_next_move = random.choice([-1, 1])  # Default: Random choice
#     if len(player_moves) > 5:
#         try:
#             ai_next_move = int(ai_model.predict([[player_last_move]])[0])
#         except:
#             pass
    
#     return jsonify({"ai_move": ai_next_move})

# if __name__ == '__main__':
#     app.run(debug=True)

# HTML, CSS, and JavaScript for the game



from flask import Flask, render_template, request, jsonify ,send_from_directory
import random
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import KBinsDiscretizer

app = Flask(__name__)

# AI model to predict player's movement
player_positions = []  # Store past positions
ai_model = LogisticRegression()

def train_ai():
    if len(player_positions) > 5:  # Train only if enough data
        X = np.array(player_positions[:-1]).reshape(-1, 1)
        y = np.array(player_positions[1:]).reshape(-1, 1)

        # Convert y into discrete classes
        kbins = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
        y_discrete = kbins.fit_transform(y).ravel()

        ai_model.fit(X, y_discrete)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/move', methods=['POST'])
def move():
    data = request.json

    # Ensure 'position' exists in the request
    if 'position' not in data:
        return jsonify({"error": "Missing 'position' field"}), 400
    
    player_position = data['position']
    player_positions.append(player_position)
    train_ai()

    # Predict the player's next position
    ai_next_position = random.randint(0, 500)  # Default random movement
    if len(player_positions) > 5:
        try:
            pred_class = ai_model.predict([[player_position]])[0]
            # Convert class back to a position using bin midpoints
            bin_width = 500 / 5  # Assuming 5 bins between 0-500
            ai_next_position = int(pred_class * bin_width + bin_width / 2)
        except:
            pass
    
    return jsonify({"ai_position": ai_next_position})

if __name__ == '__main__':
    app.run(debug=True)


