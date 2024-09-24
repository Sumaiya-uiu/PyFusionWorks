import json
import math
import os


def split_geojson(input_file, num_chunks=12):
    # Read the input GeoJSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    features = data['features']
    total_features = len(features)

    # Calculate features per chunk
    features_per_chunk = math.ceil(total_features / num_chunks)

    print(f"Total features: {total_features}")
    print(f"Features per chunk: {features_per_chunk}")

    # Split features into chunks
    for i in range(num_chunks):
        start = i * features_per_chunk
        end = min((i + 1) * features_per_chunk, total_features)

        chunk_data = {
            "type": "FeatureCollection",
            "features": features[start:end]
        }

        # Write chunk to file
        output_file = f"{os.path.splitext(input_file)[0]}_chunk_{i + 1}.geojson"
        with open(output_file, 'w') as f:
            json.dump(chunk_data, f)

        print(f"Created {output_file} with {len(chunk_data['features'])} features")


# Usage
input_file = "uk_postcode.geojson"
split_geojson(input_file)