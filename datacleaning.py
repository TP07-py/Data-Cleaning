import pandas as pd


file_path = "covid_19_set_2 (1).csv"
df = pd.read_csv(file_path)

df["Country/Region"] = df["Country/Region"].str.strip().str.lower()
df["WHO Region"] = df["WHO Region"].str.strip().str.lower()

# All the correct spellings of 'WHO region' and 'Country/Region'
valid_spellings = {
'eastern mediterranean',
        'europe',
        'africa',
        'americas',
        'western pacific',
        'south-east asia','afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda',
        'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh',
        'barbados', 'belarus', 'belgium', 'burma', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina',
        'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', 'cabo verde', 'cambodia', 'cameroon',
        'canada', 'central african republic', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo', 'costa rica',
        "cote d'ivoire", 'croatia', 'cuba', 'cyprus', 'czechia', 'democratic republic of the congo', 'denmark', 'djibouti',
        'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia',
        'eswatini', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece',
        'greenland', 'grenada', 'guatemala', 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'holy see', 'honduras', 'hungary',
        'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan',
        'kenya', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein',
        'lithuania', 'luxembourg', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'mauritania', 'mauritius', 'mexico',
        'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'namibia', 'nepal', 'netherlands', 'new zealand', 'nicaragua',
        'niger', 'nigeria', 'north korea', 'north macedonia', 'norway', 'oman', 'pakistan', 'palestine', 'panama', 'papua new guinea', 'paraguay',
        'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saint kitts and nevis', 'saint lucia',
        'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles',
        'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan', 'spain', 'sri lanka',
        'sudan', 'suriname', 'sweden', 'switzerland', 'syria', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'trinidad and tobago', 'tunisia',
        'turkey', 'turkmenistan', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states', 'uruguay', 'uzbekistan', 'venezuela', 'vietnam',
        'west bank and gaza', 'yemen', 'zambia', 'zimbabwe'
}

issues_found = []

for index, row in df.iterrows():
    if row.drop(["ID", "Province/State"], errors='ignore').isnull().all():
        issues_found.append([row["ID"], "", "All values are missing form the rows."])

for index, row in df.iterrows():
    country = row["Country/Region"]
    region = row["WHO Region"]


    if pd.notna(country) and country not in valid_spellings:
        issues_found.append([row["ID"], "Country/Region", f"Wrong spelling: {country}"])
    elif pd.isna(country):
        issues_found.append([row["ID"], "Country/Region", "Data missing"])


    if pd.notna(region) and region not in valid_spellings:
        issues_found.append([row["ID"], "WHO Region", f"Wrong spelling: {region}"])
    elif pd.isna(region):
        issues_found.append([row["ID"], "WHO Region", "Data missing"])


# Numeric Value
def check_numeric(val):
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False


quantitative_columns = ["Lat", "Long", "Confirmed", "Deaths", "Recovered", "Active"]
for col in quantitative_columns:
    for index, val in df[col].items():
        if not check_numeric(val):
            issues_found.append([df.loc[index, "ID"], col, "Non-numeric entry."])

df[quantitative_columns] = df[quantitative_columns].apply(pd.to_numeric, errors="coerce")

for index, row in df.iterrows():
    expected_value = row["Confirmed"] - row["Deaths"] - row["Recovered"]
    if row["Active"] != expected_value:
        issues_found.append([row["ID"], "Active", "Inconsistent active cases."])

output_df = pd.DataFrame(issues_found, columns=["ID", "Column", "Issue Description"])
output_df.to_csv("validation_results.csv", index=False)