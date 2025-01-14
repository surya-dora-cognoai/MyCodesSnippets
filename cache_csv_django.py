import csv
from django.conf import settings
from EasyChatApp.models import EasyChatTranslationCache
import os
import sys  
import pandas as pd

def import_csv_to_model(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Excel file successfully read.")
        for _, row in df.iterrows():
            EasyChatTranslationCache.objects.create(
                input_text_hash_data=row['input_text_hash_data'], 
                output_text_hash_data=row['output_text_hash_data'], 
                input_text=row['input_text'], 
                translated_data=row['translated_data'], 
                lang=row['lang'])
        
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
        print("Try using a different encoding, like 'latin-1'.")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"An error occurred: {e} at {exc_tb.tb_lineno}")

file_path = os.path.join(settings.MEDIA_ROOT,'AS_translation_cache.xlsx')
import_csv_to_model(file_path)
