import pandas as pd
import re

def process_mirna_name(name):
    """处理miRNA名称：替换miR为mir并保留前三部分"""
    name = re.sub(r'(?i)-miR-', '-mir-', name)
    parts = name.split('-')
    return '-'.join(parts[:3])

# 读取miRNA数据
df = pd.read_csv('miRNA.RPM.txt', sep='\t', index_col=0)

# 处理miRNA名称并去重
df.index = df.index.map(process_mirna_name)
df = df.loc[~df.index.duplicated(keep='first')]

# 转置数据并处理样本ID
df_transposed = df.T.reset_index().rename(columns={'index': 'original_sample_id'})
df_transposed['sample_id'] = df_transposed['original_sample_id'].apply(lambda x: '-'.join(x.split('-')[:3]))
df_cleaned = df_transposed.drop(columns=['original_sample_id']).drop_duplicates(subset='sample_id', keep='first')

# 读取响应数据并排序
response_df = pd.read_csv('filtered_response.csv')
ordered_samples = response_df['sample_id'].tolist()

# 按响应样本顺序对齐数据
result = df_cleaned.set_index('sample_id').reindex(ordered_samples).reset_index()

# 保存处理结果
result.to_csv('aligned_miRNA.csv', index=False)

print("处理完成，结果已保存为 aligned_miRNA.csv")