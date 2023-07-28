import csv

# read the csv file and load the data into a list of dictionaries
with open('file.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# dictionary with categories and corresponding links
category_links = {
    'feature-extraction': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c89a13229be9d530ef79_Feature%20Extraction.svg',
    'text-to-image': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c4d613229be9d52c8185_Text-to-Image.svg',
    'image-to-text': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c67dee42f488ff915465_Image-to-Text.svg',
    'text-to-video': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c634e3959a06df701b41_Text-to-Video.svg',
    'visual-question-answering': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c4f95e63a23d3f26e06e_Visual%20Question%20Answering.svg',
    'document-question-answering': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c7fbd649af0365a4961f_Document_Question_Answering_-_2.svg',
    'graph-machine-learning': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c606b488c9621f5c591c_Graph%20Machine%20Learning.svg',
    'depth-estimation': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c9ca967baeceb7975cf3_Depth_Estimation-2.svg',
    'image-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c062f02b5a28e26197f913_Image%20Classification.svg',
    'object-detection': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c921e73e7b6d3bf06402_Object%20Detection.svg',
    'image-segmentation': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c914a5f52efbcfb97cd1_Image%20Segmentation.svg',
    'image-to-image': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c77cb5f6fb8da5d7c0cb_Image-to-Image.svg',
    'Unconditional Image Generation': '',
    'video-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c8c4b488c9621f5f7af4_Video%20Classification.svg',
    'zero-shot-image-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c6145e63a23d3f282ad5_Zero-Shot%20Image%20Classification.svg',
    'text-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c436ecd77eb47132affa_Text%20Classification.svg',
    'token-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c44113229be9d52beb7b_Token%20Classification.svg',
    'table-question-answering': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c477a4006f982ddfda4a_Table%20Question%20Answering.svg',
    'question-answering': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c8fb967baeceb7967ad1_Question_Answering.svg',
    'zero-shot-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c42cd649af0365a01a1e_Zero-Shot%20Classification.svg',
    'translation': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c35d78b2b6024ba90ddb_Translation.svg',
    'summarization': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c4855e63a23d3f26771a_Summarization.svg',
    'conversational': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c462ee7f35a824dae892_Conversational.svg',
    'text-generation': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c0945c4aa4f4832ec6afd6_Text%20Generation.svg',
    'text2text-generation': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c45a4cdefda2b124a8f8_Text2Text%20Generation.svg',
    'fill-mask': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c063a54aa4f4832e8bcb11_Fill-Mask.svg',
    'sentence-similarity': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c0640e9ca5a179810f728e_Sentence%20Similarity.svg',
    'text-to-speech': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c9511aaa882b322dc3d8_Text-to-Speech.svg',
    'automatic-speech-recognition': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c62056acb71ccf5d18e6_Automatic%20Speech%20Recognition.svg',
    'audio-to-audio': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c9bbee42f488ff959bf7_Audio-to-Audio.svg',
    'audio-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c0941358df9b5cffb0d11b_Audio%20Classification.svg',
    'voice-activity-detection': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c943ee7f35a824e10258_Voice%20Activity%20Detection.svg',
    'tabular-classification': 'https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1c41b3f6ae3d03dc10e54_Tabular%20Classification.svg',
    'Tabular Regression': '',
    'Reinforcement Learning': '',
    'Robotics': ''
}

# function to generate the new value based on the category
def generate_new_value(category):
    # Return the corresponding link for the category
    return category_links.get(category, '') # 'No link' is the default value if category not found

# update each dictionary (row) in the list with the new value
for row in data:
    row['Blog Post - Featured Image (Page)'] = generate_new_value(row['task'])

# write the data back to a csv file
with open('file_with_new_column.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)