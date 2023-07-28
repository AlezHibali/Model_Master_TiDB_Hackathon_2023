import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd

def crawl(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # Find and print all links
    for link in soup.find_all('a'):
        print(link.get('href'))

class model_info:
    def __init__(self, name=None, task=None, lib=[], language=[], license=None, paper=[], like=None, dataset=[], download=None, size=None, usage=None, link=None, abstract=[]):
        self.model_name = name
        self.task = task
        self.libraries = lib
        self.language = language
        self.license = license
        self.paper = paper
        self.likes = like
        self.datasets = dataset
        self.downloads_last_month = download
        self.model_size = size
        self.model_usage = usage
        self.huggingface_link = link
        self.abstract = abstract

# class import hugging face
class spider: 
    def __init__(self, page):
        self.URL = "https://huggingface.co/models"
        self.startnum = []
        for num in range (0, page): # max 8855
            self.startnum.append(num)
        self.header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        self.models_info = []

    def check_task(self, string):
        tasks = ['Feature Extraction','Text-to-Image','Image-to-Text','Text-to-Video','Visual Question Answering','Document Question Answering','Graph Machine Learning','Depth Estimation','Image Classification','Object Detection','Image Segmentation','Image-to-Image','Unconditional Image Generation','Video Classification','Zero-Shot Image Classification','Text Classification','Token Classification','Table Question Answering','Question Answering','Zero-Shot Classification','Translation','Summarization','Conversational','Text Generation','Text2Text Generation','Fill-Mask','Sentence Similarity','Text-to-Speech','Automatic Speech Recognition','Audio-to-Audio','Audio Classification','Voice Activity Detection','Tabular Classification','Tabular Regression','Reinforcement Learning','Robotics']
        for task in tasks:
            if (string == task):
                return True
        return False

    def convert_to_bytes(self, size):
        units = {
            'Bytes': 1,
            'kB': 2**10,
            'MB': 2**20,
            'GB': 2**30,
            'TB': 2**40,
            'PB': 2**50,
            'EB': 2**60,
            'ZB': 2**70,
            'YB': 2**80,
        }
        s = size.strip()
        s = s.split('\n')[0]
        number, unit = s.split()
        try:
            return float(float(number) * units[unit])
        except KeyError:
            raise ValueError(f"Invalid unit '{unit}'. Expected one of: {', '.join(units.keys())}")
    
    def crawl_model(self, link):
        model = model_info(name=None, task=None, lib=[], language=[], license=None, paper=[], like=None, dataset=[], download=None, size=None, usage=None, link=None, abstract=[])

        model_response = requests.get(link)
        model_soup = BeautifulSoup(model_response.text, 'html.parser')
        
        # name
        name_tag = model_soup.find_all('a', class_= 'break-words font-mono font-semibold hover:text-blue-600')
        for tag in name_tag:
            model.model_name = tag.text

        # task and lib
        task_lib_tag = model_soup.find_all('a', class_='tag tag-white')
        task_tag = True
        for tag in task_lib_tag:
            task_lib_info = tag.find_all('span')
            for task_or_lib in task_lib_info:
                if (task_tag and self.check_task(task_or_lib.text)):
                    model.task = task_or_lib.text
                else:
                    model.libraries.append(task_or_lib.text)
            task_tag = False
        
        # language
        lan_tag = model_soup.find_all('a', class_='tag tag-green')
        for tag in lan_tag:
            lan_info = tag.find_all('span')
            for lan in lan_info:
                model.language.append(lan.text)

        # license
        license_tag = model_soup.select('body > div > main > div.SVELTE_HYDRATER.contents > header > div > div.mb-3.flex.flex-wrap.md\:mb-4 > a.tag.tag-white.rounded-full > span:nth-child(3)')
        for tag in license_tag: 
            model.license = tag.text
        if (model.license == None):
            license_select = model_soup.select('body > div > main > div.SVELTE_HYDRATER.contents > header > div > div.mb-3.flex.flex-wrap.md\:mb-4 > div.relative.inline-block.mr-1.mb-1.md\:mr-1\.5.md\:mb-1\.5.w-72 > button > a > span:nth-child(3)')
            for ss in license_select: 
                model.license = ss.text

        # paper and license
        paper_license_tag = model_soup.find_all('a', class_='tag mr-0 mb-0 md:mr-0 md:mb-0 tag-white rounded-full')
        for tag in paper_license_tag:
            paper_license_info = tag.find_all('span')
            is_paper = False
            is_license = False
            for paper_or_license in paper_license_info:
                if (paper_or_license.text == 'arxiv:'):
                    is_paper = True
                    continue
                if (paper_or_license.text == 'License:'):
                    is_license = True
                    continue
                if (is_paper):
                    #print(paper_or_license.text)
                    paper_link = f'https://arxiv.org/pdf/{paper_or_license.text}.pdf'
                    model.paper.append(paper_link)
                    is_paper = False
                if (is_license):
                    if (model.license == None):
                        model.license = paper_or_license.text
                        is_license = False

        # likes
        likes_tag = model_soup.find('button', {'class' : 'flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800'})
        model.likes = likes_tag.text

        # datasets
        data_tag = model_soup.find_all('a', class_='tag mr-0 mb-0 md:mr-0 md:mb-0 tag-indigo')
        for tag in data_tag:
            data_info = tag.find_all('span')
            for data in data_info:
                model.datasets.append(data.text)

        # downloads_last_month
        downloads = model_soup.find('dd', {'class' : 'font-semibold'})
        model.downloads_last_month = downloads.text

        # model_size
        file_link = f'{link}/tree/main'
        file_response = requests.get(file_link)
        file_soup = BeautifulSoup(file_response.text, 'html.parser')
        file_sizes = file_soup.find_all('a', class_='group col-span-4 flex items-center justify-self-end truncate text-right font-mono text-[0.8rem] leading-6 text-gray-400 md:col-span-2 xl:pr-10')
        total_size = 0
        for file_size in file_sizes:
            try:
                total_size += self.convert_to_bytes(file_size.text)
                print(total_size)
            except ValueError as e:
                #print(f"Error: {e}")
                continue
        total_size = total_size/(2**20)
        model.model_size = total_size

        # model_usage
        usage_tag = model_soup.find('span', {'class' : 'ml-3 font-normal text-gray-400'})
        if (usage_tag != None):
            model.model_usage = usage_tag.text

        # huggingface_link
        model.huggingface_link = link

        # abstract
        h_tags = model_soup.find_all('p')
        for h_tag in h_tags[:5]:
            abs = h_tag.get_text()
            #print(abs)
            model.abstract.append(abs)

        # add to models_info
        self.models_info.append(model)
    
    def get_models(self):
        for start in self.startnum:
            start = str(start)
            html = requests.get(self.URL, params={'p' : start}, headers=self.header)
            
            soup = BeautifulSoup(html.text, "html.parser")
            links = soup.find_all('a', class_='block p-2')
            count = 1
            for link in links: 
                href = link.get('href')
                if href: 
                    full_link = f'https://huggingface.co{href}'
                    self.crawl_model(full_link)
                    print('Page: ', start, '/8855;  Progress: ',count,'/30')
                    count += 1
            print('*****************Page: ',start,'/8855 DONE*****************')
    
    def export_models(self):
        # Convert each model_info object to a dictionary
        dicts = []
        for model in self.models_info:
            model_dict = vars(model).copy()  # Convert to dictionary and create a copy
            for key, value in model_dict.items():  # Iterate through each attribute
                if isinstance(value, list):  # If attribute is a list
                    model_dict[key] = '; '.join(value)  # Convert list to a string
            dicts.append(model_dict)
        
        # Convert list of dictionaries to a DataFrame
        df = pd.DataFrame(dicts)

        # Write DataFrame to CSV
        df.to_csv('models_info.csv', index=False, encoding='utf_8_sig')


if __name__ == '__main__':
    cls = spider(1)
    cls.get_models()
    cls.export_models()
