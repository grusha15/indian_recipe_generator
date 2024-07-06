# Indian Recipe Generator

This is a PyQt5 application for generating Indian recipes based on seed text, region, and cooking method. The application uses a deep learning model trained in Google Colab to generate recipes.

## Features

- Generate recipes based on seed text
- Select different regions of India for region-specific recipes
- Choose between oven and cooker methods for cooking instructions

## Requirements

- Python 3.x
- PyQt5
- TensorFlow
- Keras

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/grusha15/indian_recipe_generator.git
    cd indian_recipe_generator
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the model training script to generate the model and tokenizer:
    ```bash
    python model_training.py
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Usage

- Enter seed text for the recipe
- Select the region and method
- Click "Generate Recipe" to get the recipe

## License

This project is licensed under the MIT License.
