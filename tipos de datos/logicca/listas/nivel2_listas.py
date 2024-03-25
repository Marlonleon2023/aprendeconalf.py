"""La siguiente es una lista de 10 edades de estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Ordena la lista y encuentra la edad mínima y máxima.
Agregue la edad mínima y la edad máxima nuevamente a la lista.
Encuentre la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
Encuentre la edad promedio (suma de todos los artículos dividida por su número)
Encuentra el rango de edades (máximo menos mínimo)
Compare el valor de (min - promedio) y (max - promedio), use el método abs()"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
edadPromedio=sum(ages)/10
mediana=ages[4:5]
edadMediana=sum(mediana)/2
edadMaxima=max(ages)
edadMinima=min(ages)
print("edad promedio",edadPromedio,"edad mediana",edadMediana,)
print("edad minima",edadMinima)

if abs(edadMinima)<abs(edadPromedio):
    print("el valor absoluto de edad minima es menor que el de edad promedio")
elif abs(edadMinima)>abs(edadPromedio):
    print("el valor absoluto de edad minima es mayor que el de edad promedio")
else:
    print("el valor edad minima es igual que el edad promedio")
  
    # EDAD MAXIMA
    
    print("edad maxima",edadMaxima)
if abs(edadMaxima)<abs(edadPromedio):
    print("el valor absoluto de edad maxima es menor que el de edad promedio")
elif abs(edadMaxima)>abs(edadPromedio):
    print("el valor absoluto de edad maxima es mayor que el de edad promedio")
else:
    print("el valor edad minima es igual que el edad promedio")
    
    
"""Encuentre los países del medio en la lista de países"""
paises=['Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',]

paisesNuevos=[]
mitad=(len(paises))//2

paisMedio1 = paises[mitad - 1]  # Primer país en medio
paisMedio2 = paises[mitad]  # Segundo país en medio


print("los paises del medio en la lista son :",paisMedio1,"y",paisMedio2 )

print(len(paises)//2)
paisesNuevos=paises[:mitad]


print(len(paisesNuevos))




