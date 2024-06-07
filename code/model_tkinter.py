import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk

window = tk.Tk()
window.title("Secondary Protein Structure Prediction")

my_label = tk.Label(text="Please enter a sequence below:", font=("Arial", 24, "normal"))
my_label.pack()

filename = "Data/natural_proteins.csv"
df = pd.read_csv(filename)

choice = "helices"

def choose_helix():
    choice = "helices"

def choose_sheet():
    choice = "sheets"

helix_button = tk.Button(text="Predict Helix count", command=choose_helix)
sequence_button = tk.Button(text="Predict Sheet count", command=choose_sheet)
helix_button.pack()
sequence_button.pack()



def get_features(file, choice):
    df = pd.read_csv(file)
    features = pd.DataFrame()

    if choice == "helices":
        features["A"] = df["sequences"].str.count("A")
        features["R"] = df["sequences"].str.count("R")
        features["D"] = df["sequences"].str.count("D")
        features["E"] = df["sequences"].str.count("E")
        features["Y"] = df["sequences"].str.count("Y")
        features["M"] = df["sequences"].str.count("M")
        features["F"] = df["sequences"].str.count("F")
        features["L"] = df["sequences"].str.count("L")
        features["I"] = df["sequences"].str.count("I")

    elif choice == "sheets":
        features["P"] = df["sequences"].str.count("P")
        features["S"] = df["sequences"].str.count("S")
        features["G"] = df["sequences"].str.count("G")
        features["T"] = df["sequences"].str.count("T")
        features["V"] = df["sequences"].str.count("V")

    features["Len"] = df["sequences"].str.len()
    features["chains"] = df["chains"]

    return features


def convert_to_features(sequence, choice):
    features = pd.DataFrame()
    if choice == "helices":
        features["A"] = [sequence.count("A")]
        features["R"] = [sequence.count("R")]
        features["D"] = [sequence.count("D")]
        features["E"] = [sequence.count("E")]
        features["Y"] = [sequence.count("Y")]
        features["M"] = [sequence.count("M")]
        features["F"] = [sequence.count("F")]
        features["L"] = [sequence.count("L")]
        features["I"] = [sequence.count("I")]

    elif choice == "sheets":
        features["P"] = [sequence.count("P")]
        features["S"] = [sequence.count("S")]
        features["G"] = [sequence.count("G")]
        features["T"] = [sequence.count("T")]
        features["V"] = [sequence.count("V")]

    features["Len"] = len(sequence)
    split = sequence.split(",")
    features["chains"] = len(split)

    return features


features = get_features(filename, choice)

y = df[choice]

x_train, x_test, y_train, y_test = train_test_split(features, y, test_size=0.2)
reg = LinearRegression().fit(x_train, y_train)
y_pred = reg.predict(x_test)
for i in range(len(y_pred)):
    if y_pred[i] < 0:  # if the algorithm predicts a negative value
        y_pred[i] = 1  # set the value to 1

y_pred_round = [round(elem) for elem in y_pred]


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tk.Button(text="Enter choice", command=button_clicked)
button.pack()


# Entry

sequence = tk.Entry()
sequence.pack()

converted_sequence = convert_to_features(sequence.get(), choice)

output = round(reg.predict(converted_sequence)[0])
if output < 0:
    output = 0

print(output, choice, "predicted for this sequence")


window.mainloop()