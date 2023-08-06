# abstract summarization
# model master project
# doing summarization using BART-Large-CNN

# from transformers import BartTokenizer, BartForConditionalGeneration, pipeline
# import torch
# import re

# # GPU
# device = 0 if torch.cuda.is_available() else -1

# # Load the model and tokenizer
# model_name = "com3dian/Bart-large-paper2slides-summarizer"
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

# # Generate summary from input text
# input_text = "BlueMethod is a bit of a convoluted experiment in tiered merging. Furthering the experimental nature of the merge, the models combined were done so with a custom script that randomized the percent of each layer merged from one model to the next. This is a warmup for a larger project. [Tier One and Two Merges not released; internal naming convention]; Tier One Merges:; 13B-Metharme+13B-Nous-Hermes=13B-Methermes; 13B-Vicuna-cocktail+13B-Manticore=13B-Vicortia; 13B-HyperMantis+13B-Alpacino=13B-PsychoMantis"
# input_text_2 = "锟斤拷锟斤拷锟斤拷写锟斤拷锟斤拷模锟斤拷V1锟角伙拷锟斤拷LLaMa锟斤拷130锟节诧拷锟斤拷锟斤拷指锟斤拷微锟斤拷模锟酵ｏ拷锟斤拷写锟斤拷锟斤拷锟斤拷锟较斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷强锟斤拷锟斤拷专注锟斤拷写锟斤拷锟侥达拷模锟酵★拷锟斤拷锟斤拷锟斤拷写锟斤拷模锟酵匡拷锟斤拷锟斤拷晒锟斤拷谋锟斤拷妗拷锟斤拷锟斤拷锟斤拷拧锟斤拷锟斤拷锟斤拷陌锟斤拷榷锟斤拷锟斤拷写锟斤拷锟斤拷锟斤拷; Ziya-Writing-LLaMa-13B-v1 is a 13-billion parameter instruction fine-tuned model based on LLaMa, which has been enhanced for better performance in writing tasks. It is a large model that focuses on writing. Ziya-Writing-LLaMa-13B-v1 can handle several types of writing tasks, including official reports, speeches, creative copywriting, and more.; 锟斤拷锟斤拷细锟节匡拷锟皆参匡拷锟斤拷锟角的癸拷锟节猴拷锟斤拷锟铰ｏ拷; 锟斤拷锟斤拷锟斤拷锟斤拷模锟斤拷系锟斤拷 | 写锟斤拷模锟斤拷ziya-writing锟斤拷源锟斤拷锟斤拷锟戒即锟矫ｏ拷锟斤拷锟斤拷锟斤拷锟斤拷专锟斤拷锟斤拷锟叫达拷锟叫★拷锟斤拷职锟? 锟斤拷锟角达拷锟斤拷锟斤拷锟斤拷锟秸硷拷锟斤拷锟斤拷洗锟剿达拷锟斤拷锟斤拷实锟斤拷锟斤拷锟斤拷写锟斤拷锟斤拷锟捷ｏ拷锟斤拷锟斤拷GPT-3.5锟斤拷锟缴讹拷应锟斤拷写锟斤拷指锟筋，锟斤拷锟斤拷锟斤拷锟剿硷拷为锟较革拷锟斤拷斯锟叫ｏ拷椤?,natural-language-processing,text-generation,Chinese; English,PyTorch; Transformers,https://huggingface.co/IDEA-CCNL/Ziya-Writing-LLaMa-13B-v1,,License: gpl-3.0,,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb0992d4b3151602bc1c_64c04e110d6b76f9eed4a03b_heart-icon%2520(1).svg,likes 6,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb0992d4b3151602bc20_64c05fbd8519be7a7b8243bb_download_icon.svg,downloads 11,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb09f28c42e30cf7d869_64c05fc92b95cbe3c8785fb1_size_icon.svg,model size 52.0GB,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb09f28c42e30cf7d86f_64c05fce61bda9e68fed4508_usage_icon.svg,usage 0 zodiac_eclipse_DAY1,zodiac-eclipse-day1,64bcb453e3df2ded5d02d923,64c201f2d77b82ddfe7a2117,Thu Jul 27 2023 05:34:42 GMT+0000 (Coordinated Universal Time),Thu Jul 27 2023 05:34:42 GMT+0000 (Coordinated Universal Time),Thu Jul 27 2023 05:36:55 GMT+0000 (Coordinated Universal Time),https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb09d98897490e096b87_64c1c4d613229be9d52c8185_Text-to-Image.svg,,Model info :; https://civitai.com/models/108417/zodiac-eclipse-day1; Sample image I made thru Huggingface's API :; ; Original Author's DEMO images :,multimodel,text-to-image,,Diffusers,https://huggingface.co/digiplay/zodiac_eclipse_DAY1,,License: other,,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb0992d4b3151602bc1c_64c04e110d6b76f9eed4a03b_heart-icon%2520(1).svg,likes 3,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb0992d4b3151602bc20_64c05fbd8519be7a7b8243bb_download_icon.svg,downloads 620,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb09f28c42e30cf7d869_64c05fc92b95cbe3c8785fb1_size_icon.svg,model size 3.0GB,https://uploads-ssl.webflow.com/64bcb453e3df2ded5d02d93f/64c1eb09f28c42e30cf7d86f_64c05fce61bda9e68fed4508_usage_icon.svg,usage 3"
# clean_text = re.sub('[^a-zA-Z0-9 \n\. : /]', '', input_text_2)
# print(clean_text)

# # Or using the pipeline API
# summarizer = pipeline("summarization", model=model_name, device=device)
# summary = summarizer(clean_text, max_length=50, min_length=30, do_sample=False)
# print(summary[0]['summary_text'])


from transformers import BartTokenizer, BartForConditionalGeneration, pipeline
import torch
import re
import csv

# GPU
device = 0 if torch.cuda.is_available() else -1

# define Bart large cnn model
model_name = "com3dian/Bart-large-paper2slides-summarizer"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
summarizer = pipeline("summarization", model=model_name, device=device)

csv_list = []

def process_data(data):
    # Put your data processing logic here
    processed_data = data  # This is just a placeholder
    clean_text = re.sub('[^a-zA-Z0-9 \n\. : /]', '', processed_data)
    summary = summarizer(clean_text, max_length=50, min_length=30, do_sample=False)
    return_sen = summary[0]['summary_text']
    return return_sen

# Open the CSV file
with open('abstract.csv', 'r', encoding='ISO-8859-1') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)

# Add the new column
i = 1
for item in data:
    if item:
        clean_text = re.sub('[^a-zA-Z0-9 \n\. : /]', '', item[0]).strip()
        clean_text = clean_text.replace('\\xa0', ' ')
        if len(clean_text) < 50:
            csv_list.append([clean_text])
        else:
            summary = process_data(clean_text)
            summary = re.sub('[^a-zA-Z0-9 \n\. : /]', '', summary)
            csv_list.append([summary])
    else:
        csv_list.append([])
    print(i, "/1448")
    i+=1

# Write the new data to a new CSV file
with open('new_file.csv', 'w', newline='', encoding='utf-8') as new_csv_file:
    writer = csv.writer(new_csv_file)
    writer.writerows(csv_list)