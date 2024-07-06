import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit

import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import pickle

# Load the tokenizer and model
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = tf.keras.models.load_model('my_model.keras')  # Load the downloaded model

def generate_recipe(seed_text, next_words=100):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=149, padding='post')
        predicted = model.predict(token_list, verbose=0)
        next_index = np.argmax(predicted[0])
        next_word = tokenizer.index_word.get(next_index, '')
        if next_word == '':
            break
        seed_text += " " + next_word
        if next_word == 'end':
            break
    return seed_text

def generate_regional_recipe(seed_text, region, method, next_words=100):
    region_specifics = {
        "Northeast India": "using bamboo shoot and fermented fish",
        "South India": "with coconut and curry leaves",
        "North India": "with ghee and dry fruits",
        "West India": "using jaggery and coconut",
        "East India": "with mustard oil and panch phoron"
    }
    method_instructions = {
        "oven": " Bake in an oven preheated to 180°C.",
        "cooker": " Place the cake tin inside a cooker without water, cover it, and cook on a low flame."
    }
    region_text = f"{seed_text} {region_specifics.get(region, '')} {method_instructions.get(method, '')}"
    recipe = generate_recipe(region_text, next_words)
    return recipe

class RecipeGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Indian Recipe Generator')

        layout = QVBoxLayout()

        self.label1 = QLabel('Enter Seed Text:')
        self.seed_text_input = QLineEdit(self)

        self.label2 = QLabel('Select Region:')
        self.region_combo = QComboBox(self)
        self.region_combo.addItems(["Northeast India", "South India", "North India", "West India", "East India"])

        self.label3 = QLabel('Select Method:')
        self.method_combo = QComboBox(self)
        self.method_combo.addItems(["oven", "cooker"])

        self.generate_button = QPushButton('Generate Recipe', self)
        self.generate_button.clicked.connect(self.generate_recipe)

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)

        layout.addWidget(self.label1)
        layout.addWidget(self.seed_text_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.region_combo)
        layout.addWidget(self.label3)
        layout.addWidget(self.method_combo)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def generate_recipe(self):
        seed_text = self.seed_text_input.text()
        region = self.region_combo.currentText()
        method = self.method_combo.currentText()
        recipe = generate_regional_recipe(seed_text, region, method)
        self.result_text.setText(recipe)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipeGeneratorApp()
    ex.show()
    sys.exit(app.exec_())
