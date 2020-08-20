def predict_Model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    rf = pickle.load(open('my_titanic_Model.sav', 'rb'))  # read binary
    prediction = rf.predict(x)
    if prediction == 1:
        prediction = 'survived'
    elif prediction == 0:
        prediction = 'not survied'
    return prediction
