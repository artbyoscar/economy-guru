import gdown

# URL to the model file with the correct format for gdown
url = 'https://drive.google.com/uc?id=14DeKmI6oIsdQLDeGeXojPS76QG0mOc0k'
output = '/workspace/economy-guru/logistic_model.pkl'  # Adjust this path if necessary

gdown.download(url, output, quiet=False)
