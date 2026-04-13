import pandas as pd

# 1. Ma'lumot yaratish (Extract o'rnida)
data = {
    'Sana': ['2024-03-01', '2024-03-01', '2024-03-02', '2024-03-02', '2024-03-03'],
    'Mahsulot': ['Monitor', 'Klaviatura', 'Monitor', 'Sichqoncha', 'Klaviatura'],
    'Sotuv_Soni': [10, 5, 8, 15, None],  # Bitta ma'lumot yo'q (NaN)
    'Narxi': [150, 50, 150, 25, 50]
}

df = pd.DataFrame(data)

# 2. Ma'lumotlarni tozalash (Transformation)
# Bo'sh (None) qiymatlarni 0 bilan to'ldiramiz
df['Sotuv_Soni'] = df['Sotuv_Soni'].fillna(0)

# Umumiy tushumni hisoblaymiz (Yangi ustun qo'shish)
df['Umumiy_Tushum'] = df['Sotuv_Soni'] * df['Narxi']

# 3. Ma'lumotlarni tahlil qilish (Aggregation)
# Har bir mahsulot bo'yicha jami tushumni hisoblaymiz
hisobot = df.groupby('Mahsulot')['Umumiy_Tushum'].sum().reset_index()

print("Tozalangan va hisoblangan ma'lumotlar:")
print(df)
print("\nMahsulotlar bo'yicha hisobot:")
print(hisobot)

# 4. Saqlash (Load o'rnida)
# Natijani Excel yoki CSV faylga saqlash mumkin
# hisobot.to_excel('hisobot.xlsx', index=False)