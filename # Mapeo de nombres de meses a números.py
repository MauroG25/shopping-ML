# Mapeo de nombres de meses a números
month = {"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "Man": 5, "June": 6,
         "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

vtype = {"Returning_Visitor": 1, "New_Visitor": 0}


# Mapeo de verdadero/falso a 1/0
true_false = {"TRUE": 1, "FALSE": 0}

def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    raise NotImplementedError
# Leer datos del archivo
with open("tu_archivo.csv") as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la cabecera

    data = []
    for row in reader:
        # Transformar los datos según tus necesidades
        evidence = [int(row[0]), float(row[1]),int(row[2]),float(row[3]), int(row[4]),float(row[5]),
                     float(row[6]),float(row[7]),float(row[8]),float(row[9]), month[row[10]], int(row[11]),
                     int(row[12]),int(row[13]),int(row[14]), true_false[row[15]]]
        labels = 1 if row[16] == "TRUE" else 0
        data.append({"evidence": evidence, "label": labels})

def train_model(evidence, labels):
   # Separate data into training and testing groups
    evidence = [row["evidence"] for row in data]
    labels = [row["label"] for row in data]

    X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
    )

    # Fit model
    model.fit(X_training, y_training)

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # Make predictions on the testing set
    predictions = model.predict(X_testing)

    # Compute how well we performed
    true_positive = sum((labels == 1) & (predictions == 1))
    false_positive = sum((labels == 0) & (predictions == 1))
    true_negative = sum((labels == 0) & (predictions == 0))
    false_negative = sum((labels == 1) & (predictions == 0))

    # Calculate sensitivity and specificity
    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)