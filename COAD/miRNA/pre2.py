
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 读取数据，第一列为样本ID
df = pd.read_csv('aligned_miRNA.csv', index_col=0)

# 1. 过滤非KEGG miRNA（假设列名已经是KEGG miRNA）
# （此处需要KEGG miRNA列表，假设数据已预先过滤）

# 2. 对数转换处理（根据论文要求）
# 添加伪计数1避免log(0)，然后进行log2转换
df_log = np.log2(df + 1)

# 3. 归一化到0-1范围
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler.fit_transform(df_log),
    columns=df.columns,
    index=df.index
)

# 保存处理后的数据
df_normalized.to_csv('miRNA.csv')

print("预处理完成，数据已保存为 miRNA.csv")