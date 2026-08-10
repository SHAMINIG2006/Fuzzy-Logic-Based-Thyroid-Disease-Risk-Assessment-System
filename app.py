from flask import Flask, render_template, request

app = Flask(__name__)

# ===== ECHRS LOGIC FUNCTION =====
def calculate_risk(T3, TT4, T4U, FTI, nitrate, pollution):

    # Clinical Score
    if TT4 < 85 or T3 < 0.9:
        clinical_score = 85
        class_label = "High Risk"
    elif TT4 < 100 or T3 < 1.1:
        clinical_score = 60
        class_label = "Moderate Risk"
    else:
        clinical_score = 30
        class_label = "Low Risk"

    # Environmental Score
    env_score = (nitrate / 80) * 50 + (pollution / 100) * 50

    # Final Score
    final_score = (0.5 * clinical_score) + (0.5 * env_score)

    # Explanation
    if final_score < 35:
        explanation = "Low Risk – Safe condition"
    elif final_score < 65:
        explanation = "Moderate Risk – Environmental influence detected"
    else:
        explanation = "High Risk – Early warning for thyroid disorder"

    return class_label, round(final_score, 2), explanation


# ===== ROUTES =====

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    T3 = float(request.form['T3'])
    TT4 = float(request.form['TT4'])
    T4U = float(request.form['T4U'])
    FTI = float(request.form['FTI'])
    nitrate = float(request.form['nitrate'])
    pollution = float(request.form['pollution'])

    result, score, explanation = calculate_risk(T3, TT4, T4U, FTI, nitrate, pollution)

    return render_template('result.html',
                           result=result,
                           score=score,
                           explanation=explanation)


if __name__ == '__main__':
    app.run(debug=True)