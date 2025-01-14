import os
import pandas as pd
from django.conf import settings
from EasyChatApp.models import EasyChatTranslationCache

def export_filtered_data_to_excel():
    print("inside funct")
    try:
        filtered_queryset = EasyChatTranslationCache.objects.filter(lang='te')
        data = list(filtered_queryset.values())
        if not data:
            print("No data found for the given filter.")
            return
        df = pd.DataFrame(data)
        file_path = os.path.join(settings.MEDIA_ROOT,'TE_translation_cache.xlsx')

        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"Data exported successfully to {file_path}")
    except Exception as e:
        print("Exception at "+str(e))

export_filtered_data_to_excel()

