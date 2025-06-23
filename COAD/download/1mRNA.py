import csv

# 读取response.csv中的样本ID
response_samples = {}
with open('response_1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过标题行
    for row in reader:
        sample_id = row[0]
        response_samples[sample_id] = row

# 处理miRNA文件，截断样本ID并去重
miRNA_data = {}
with open('samples_miRNA.txt', 'r') as f:
    lines = f.readlines()
    header = lines[0]  # 保留标题行
    for line in lines[1:]:
        parts = line.strip().split('\t')
        original_id = parts[0]
        truncated_id = '-'.join(original_id.split('-')[:3])
        if truncated_id not in miRNA_data:
            miRNA_data[truncated_id] = line

# 处理mRNA文件，截断样本ID并去重
mRNA_data = {}
with open('samples_mRNA.txt', 'r') as f:
    lines = f.readlines()
    header_mrna = lines[0]  # 保留标题行
    for line in lines[1:]:
        parts = line.strip().split('\t')
        original_id = parts[0]
        truncated_id = '-'.join(original_id.split('-')[:3])
        if truncated_id not in mRNA_data:
            mRNA_data[truncated_id] = line

# 获取三个数据集的公共样本ID
common_ids = set(response_samples.keys()) & set(miRNA_data.keys()) & set(mRNA_data.keys())

# 生成新的response.csv
with open('filtered_response.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sample_id', 'response'])  # 标题行
    for sid in common_ids:
        writer.writerow(response_samples[sid])

# 生成新的miRNA文件
with open('filtered_miRNA.txt', 'w') as f:
    f.write(header)  # 写入标题行
    for sid in common_ids:
        f.write(miRNA_data[sid])

# 生成新的mRNA文件
with open('filtered_mRNA.txt', 'w') as f:
    f.write(header_mrna)  # 写入标题行
    for sid in common_ids:
        f.write(mRNA_data[sid])

print(f"生成完成，公共样本数量：{len(common_ids)}")