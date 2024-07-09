import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def process_data(data):
    df = pd.DataFrame(data)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(scaled_data)
    
    return clusters
