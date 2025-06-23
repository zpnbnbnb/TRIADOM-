import pandas as pd

# 读取制表符分隔的临床数据
df = pd.read_csv('COAD_clinical.txt', sep='\t', low_memory=False)

# 筛选并保留指定列
df = df[['bcr_patient_barcode', 'person_neoplasm_cancer_status']]

# 创建状态映射字典并转换
status_mapping = {'WITH TUMOR': 1, 'TUMOR FREE': 0}
df['person_neoplasm_cancer_status'] = df['person_neoplasm_cancer_status'].map(status_mapping)

# 过滤无效值并转换为整数类型
df = df.dropna(subset=['person_neoplasm_cancer_status'])
df['person_neoplasm_cancer_status'] = df['person_neoplasm_cancer_status'].astype(int)

# 重命名列
df = df.rename(columns={
    'bcr_patient_barcode': 'sample_id',
    'person_neoplasm_cancer_status': 'response'
})

# 保存处理后的数据
df.to_csv('response_1.csv', index=False)