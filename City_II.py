cities_list = ['Aalborg / Denmark', 'Aarhus / Denmark', 'Abidjan / Ivory Coast', 'Abu Dhabi / United Arab Emirates',
               'Abuja / Nigeria', 'Abéché / Chad', 'Accra / Ghana', 'Aconibe / Equatorial Guinea', 'Acquaviva / San Marino',
               'Addis Ababa / Ethiopia', 'Addu City / Maldives', 'Adelaide / Australia', 'Aden / Yemen', 'Agadez / Niger',
               'Ahuachapán / El Salvador', 'Ahvaz / Iran', 'Aimeliik / Palau', 'Aiwo / Nauru', 'Ajman / United Arab Emirates',
               'Aktobe / Kazakhstan', 'Akureyri / Iceland', 'Al Ahmadi / Kuwait', 'Al Khor / Qatar', 'Al Rayyan / Qatar',
               'Alajuela / Costa Rica', 'Albina / Suriname', 'Aleppo / Syria', 'Alexandria / Egypt', 'Algiers / Algeria',
               'Ali Sabieh / Djibouti', 'All Saints / Antigua and Barbuda', 'Almaty / Kazakhstan', 'Amadora / Portugal',
               'Ambato / Ecuador', 'Amman / Jordan', 'Amsterdam / Netherlands', 'Anabar / Nauru', 'Andijan / Uzbekistan',
               'Andorra la Vella / Andorra', 'Angaur / Palau', 'Ankara / Turkey', 'Anna Regina / Guyana', 'Annaba / Algeria',
               'Anse Royale / Seychelles', 'Antalya / Turkey', 'Antananarivo / Madagascar', 'Antigua Guatemala / Guatemala',
               'Antofagasta / Chile', 'Antsiranana / Madagascar', 'Antwerp / Belgium', 'Apia / Samoa', 'Aqaba / Jordan',
               'Arequipa / Peru', 'Arima / Trinidad and Tobago', 'Arusha / Tanzania', 'Ashaiman / Ghana', 'Ashgabat / Turkmenistan',
               'Asmara / Eritrea', 'Assab / Eritrea', 'Astana / Kazakhstan', 'Asunción / Paraguay', 'Atakpamé / Togo',
               'Atar / Mauritania', 'Athens / Greece', 'Auckland / New Zealand', 'Auki / Solomon Islands', 'Aur / Marshall Islands',
               'Aweil / South Sudan', 'Bafatá / Guinea-Bissau', 'Baghdad / Iraq', 'Bahir Dar / Ethiopia', 'Bahla / Oman',
               'Bairiki / Kiribati', 'Baku / Azerbaijan', 'Balkanabat / Turkmenistan', 'Balzers / Liechtenstein', 'Bamako / Mali',
               'Bamyan / Afghanistan', 'Bandar Seri Begawan / Brunei', 'Bandung / Indonesia', 'Banfora / Burkina Faso', 'Bangalore / India',
               'Bangar / Brunei', 'Bangkok / Thailand', 'Bangui / Central African Republic', 'Banja Luka / Bosnia and Herzegovina',
               'Banjul / Gambia', 'Barcelona / Spain', 'Bariloche / Argentina', 'Barquisimeto / Venezuela', 'Barranquilla / Colombia',
               'Barrouallie / Saint Vincent and the Grenadines', 'Bartica / Guyana', 'Basel / Switzerland', 'Basra / Iraq',
               'Basse Santa Su / Gambia', 'Basseterre / Saint Kitts and Nevis', 'Bata / Equatorial Guinea', 'Bathsheba / Barbados',
               'Battambang / Cambodia', 'Batumi / Georgia', 'Baucau / Timor-Leste', 'Beau Bassin / Mauritius', 'Beer Sheva / Israel',
               'Beijing / China', 'Beira / Mozambique', 'Beirut / Lebanon', 'Bel Ombre / Seychelles', 'Belgrade / Serbia',
               'Belize City / Belize', 'Belmopan / Belize', 'Bender / Moldova', 'Benghazi / Libya', 'Benguela / Angola',
               'Bequia / Saint Vincent and the Grenadines', 'Berberati / Central African Republic', 'Bergen / Norway', 'Berlin / Germany',
               'Bern / Switzerland', 'Bertoua / Cameroon', 'Betio / Kiribati', 'Bhaktapur / Nepal', 'Big Bend / Eswatini',
               'Bijelo Polje / Montenegro', 'Birao / Central African Republic', 'Biratnagar / Nepal', 'Birkirkara / Malta',
               'Birmingham / United Kingdom', 'Bishkek / Kyrgyzstan', 'Bissau / Guinea-Bissau', 'Bissora / Guinea-Bissau',
               'Bitola / North Macedonia', 'Bizerte / Tunisia', 'Blantyre / Malawi', 'Blida / Algeria', 'Bluefields / Nicaragua',
               'Bo / Sierra Leone', 'Bobo-Dioulasso / Burkina Faso', 'Boe / Nauru', 'Bogotá / Colombia', 'Bohicon / Benin',
               'Bolands / Antigua and Barbuda', 'Bor / South Sudan', 'Borgo Maggiore / San Marino', 'Bosaso / Somalia',
               'Bouaké / Ivory Coast', 'Braga / Portugal', 'Brasília / Brazil', 'Bratislava / Slovakia',
               'Brazzaville / Congo (Congo-Brazzaville)', 'Briceni / Moldova', 'Bridgetown / Barbados', 'Brikama / Gambia',
               'Brisbane / Australia', 'Brno / Czech Republic', 'Bruges / Belgium', 'Brussels / Belgium', 'Buchanan / Liberia',
               'Bucharest / Romania', 'Budapest / Hungary', 'Buenos Aires / Argentina', 'Bujumbura / Burundi', 'Bukhara / Uzbekistan',
               'Bukit Timah / Singapore', 'Bulawayo / Zimbabwe', 'Buota / Kiribati', 'Burgas / Bulgaria', 'Bursa / Turkey',
               'Busan / South Korea', 'Butare / Rwanda', 'Bălți / Moldova', 'Cacheu / Guinea-Bissau', 'Cairo / Egypt', 'Calgary / Canada',
               'Cali / Colombia', 'Calliaqua / Saint Vincent and the Grenadines', 'Camagüey / Cuba', 'Can Tho / Vietnam', 'Cancún / Mexico',
               'Cap-Haïtien / Haiti', 'Cape Town / South Africa', 'Caracas / Venezuela', 'Carnot / Central African Republic',
               'Carriacou / Grenada', 'Cartagena / Colombia', 'Cartago / Costa Rica', 'Casablanca / Morocco', 'Castries / Saint Lucia',
               'Cebu City / Philippines', 'Celje / Slovenia', 'Chaguanas / Trinidad and Tobago', 'Changi / Singapore',
               'Charlestown / Saint Kitts and Nevis', 'Chennai / India', 'Chiang Mai / Thailand', 'Chicago / United States',
               'Chiclayo / Peru', 'Chimoio / Mozambique', 'Chingola / Zambia', 'Chitre / Panama', 'Chittagong / Bangladesh',
               'Chișinău / Moldova', 'Choibalsan / Mongolia', 'Choloma / Honduras', 'Chongjin / North Korea', 'Christchurch / New Zealand',
               'Cienfuegos / Cuba', 'City of San Marino / San Marino', 'Ciudad del Este / Paraguay', 'Cluj-Napoca / Romania',
               'Cobán / Guatemala', 'Cochabamba / Bolivia', 'Coimbra / Portugal', 'Cologne / Germany', 'Colombo / Sri Lanka',
               'Colón / Panama', 'Conakry / Guinea', 'Concepción / Chile', 'Constantine / Algeria', 'Constanța / Romania',
               'Copenhagen / Denmark', 'Cordoba / Argentina', 'Cork / Ireland', 'Corozal Town / Belize', 'Cotonou / Benin',
               'Cuenca / Ecuador', 'Curepipe / Mauritius', 'Cusco / Peru', 'Da Nang / Vietnam', 'Daegu / South Korea',
               'Daejeon / South Korea', 'Dakar / Senegal', 'Daloa / Ivory Coast', 'Damascus / Syria', 'Dammam / Saudi Arabia',
               'Dangriga / Belize', 'Dar es Salaam / Tanzania', 'Darkhan / Mongolia', 'Dashoguz / Turkmenistan', 'Daugavpils / Latvia',
               'Davao City / Philippines', 'David / Panama', 'Debrecen / Hungary', 'Dhaka / Bangladesh', 'Differdange / Luxembourg',
               'Dikhil / Djibouti', 'Dili / Timor-Leste', 'Dire Dawa / Ethiopia', 'Djibouti / Djibouti', 'Djougou / Benin',
               'Dnipro / Ukraine', 'Dodoma / Tanzania', 'Doha / Qatar', 'Dolisie / Congo (Congo-Brazzaville)', 'Domagnano / San Marino',
               'Domoni / Comoros', 'Douala / Cameroon', 'Drammen / Norway', 'Dubai / United Arab Emirates', 'Dublin / Ireland',
               'Dubrovnik / Croatia', 'Dunedin / New Zealand', 'Durban / South Africa', 'Durrës / Albania', 'Dushanbe / Tajikistan',
               'Ebebiyin / Equatorial Guinea', 'Ebeye / Marshall Islands', 'Edinburgh / United Kingdom', 'Eilat / Israel',
               'Eindhoven / Netherlands', 'El Progreso / Honduras', 'Elbasan / Albania', 'Eldoret / Kenya', 'Encamp / Andorra',
               'Encarnación / Paraguay', 'Entebbe / Uganda', 'Erbil / Iraq', 'Erdenet / Mongolia', 'Esbjerg / Denmark',
               'Escaldes-Engordany / Andorra', 'Esch-sur-Alzette / Luxembourg', 'Eschen / Liechtenstein', 'Escuintla / Guatemala',
               'Espargos / Cabo Verde', 'Espiritu Santo / Vanuatu', 'Espoo / Finland', 'Ettelbruck / Luxembourg', 'Eua / Tonga',
               'Ewa / Nauru', 'Faisalabad / Pakistan', 'Faleasiu / Samoa', 'Famagusta / Cyprus', 'Faranah / Guinea', 'Farwaniya / Kuwait',
               'Fes / Morocco', 'Fianarantsoa / Madagascar', 'Florence / Italy', 'Fomboni / Comoros', 'Fongafale / Tuvalu',
               'Fontvieille / Monaco', 'Fortaleza / Brazil', 'Franceville / Gabon', 'Francistown / Botswana', 'Frankfurt / Germany',
               'Freeport / Bahamas', 'Freetown / Antigua and Barbuda', 'Freetown / Sierra Leone', 'Fujairah / United Arab Emirates',
               'Fukuoka / Japan', 'Funafuti / Tuvalu', 'Fuvahmulah / Maldives', 'Gaborone / Botswana', 'Gabú / Guinea-Bissau',
               'Galle / Sri Lanka', 'Galway / Ireland', 'Ganja / Azerbaijan', 'Garoua / Cameroon', 'Gbarnga / Liberia',
               'Geneva / Switzerland', 'Georgetown / Guyana', 'Ghent / Belgium', 'Gisenyi / Rwanda', 'Gitega / Burundi',
               'Giza / Egypt', 'Gizo / Solomon Islands', 'Gjakova / Kosovo', 'Glen / Saint Vincent and the Grenadines',
               'Gomel / Belarus', 'Gonaïves / Haiti', 'Gondar / Ethiopia', 'Gothenburg / Sweden', 'Gouyave / Grenada',
               "Governor's Harbour / Bahamas", 'Granada / Nicaragua', 'Graz / Austria', 'Grenville / Grenada', 'Grodno / Belarus',
               'Gros Islet / Saint Lucia', 'Guadalajara / Mexico', 'Guangzhou / China', 'Guatemala City / Guatemala',
               'Guayaquil / Ecuador', 'Gulu / Uganda', 'Gweru / Zimbabwe', 'Gyumri / Armenia', "Ha'apai / Tonga",
               'Hafnarfjordur / Iceland', 'Hai Phong / Vietnam', 'Haifa / Israel', 'Hamburg / Germany', 'Hamhung / North Korea',
               'Hamilton / New Zealand', 'Hanoi / Vietnam', 'Harare / Zimbabwe', 'Hargeisa / Somalia', 'Harper / Liberia',
               'Havana / Cuba', 'Hawalli / Kuwait', 'Helsinki / Finland', 'Heraklion / Greece', 'Herat / Afghanistan',
               'Herceg Novi / Montenegro', 'Hithadhoo / Maldives', 'Ho Chi Minh City / Vietnam', 'Hodeidah / Yemen',
               'Hokkaido / Japan', 'Holetown / Barbados', 'Holguín / Cuba', 'Homs / Syria', 'Hong Kong / China',
               'Honiara / Solomon Islands', 'Houston / United States', 'Hua Hin / Thailand', 'Huambo / Angola',
               'Iași / Romania', 'Ibadan / Nigeria', 'Ibb / Yemen', 'Incheon / South Korea', 'Innsbruck / Austria',
               'Irbid / Jordan', 'Isa Town / Bahrain', 'Isfahan / Iran', 'Isfara / Tajikistan', 'Islamabad / Pakistan',
               'Istanbul / Turkey', 'Izmir / Turkey', 'Jacmel / Haiti', 'Jaffna / Sri Lanka', 'Jakar / Bhutan',
               'Jakarta / Indonesia', 'Jalal-Abad / Kyrgyzstan', 'Jalalabad / Afghanistan', 'Jeddah / Saudi Arabia',
               'Jelgava / Latvia', 'Jerusalem / Israel', 'Johannesburg / South Africa', 'Johor Bahru / Malaysia',
               'Juba / South Sudan', 'Jurmala / Latvia', 'Jurong / Singapore', 'Kabul / Afghanistan',
               'Kaga Bandoro / Central African Republic', 'Kailahun / Sierra Leone', 'Kairouan / Tunisia', 'Kampala / Uganda',
               'Kandahar / Afghanistan', 'Kandy / Sri Lanka', 'Kano / Nigeria', 'Kaohsiung / Taiwan', 'Kapan / Armenia',
               'Kara / Togo', 'Karachi / Pakistan', 'Karaganda / Kazakhstan', 'Karakol / Kyrgyzstan', 'Kasungu / Malawi',
               'Kathmandu / Nepal', 'Kaunas / Lithuania', 'Kaya / Burkina Faso', 'Kayes / Mali', 'Keelung / Taiwan',
               'Kelo / Chad', 'Kenema / Sierra Leone', 'Keren / Eritrea', 'Kharkiv / Ukraine', 'Khartoum / Sudan',
               'Khujand / Tajikistan', 'Khulna / Bangladesh', 'Kiffa / Mauritania', 'Kigali / Rwanda', 'Kindia / Guinea',
               'Kingston / Jamaica', 'Kingstown / Saint Vincent and the Grenadines', 'Kira Kira / Solomon Islands',
               'Kirakira / Solomon Islands', 'Kirkuk / Iraq', 'Kismayo / Somalia', 'Kisumu / Kenya', 'Kitwe / Zambia',
               'Klaipeda / Lithuania', 'Kohtla-Järve / Estonia', 'Kolkata / India', 'Kolonia / Micronesia', 'Kopavogur / Iceland',
               'Koper / Slovenia', 'Koror / Palau', 'Kota Kinabalu / Malaysia', 'Koudougou / Burkina Faso', 'Košice / Slovakia',
               'Kragujevac / Serbia', 'Kraków / Poland', 'Kranj / Slovenia', 'Kuala Belait / Brunei', 'Kuala Lumpur / Malaysia',
               'Kulhudhuffushi / Maldives', 'Kulob / Tajikistan', 'Kumanovo / North Macedonia', 'Kumasi / Ghana',
               'Kurgan-Tyube / Tajikistan', 'Kutaisi / Georgia', 'Kuwait City / Kuwait', 'Kwajalein / Marshall Islands',
               'Kwekwe / Zimbabwe', 'Kyiv / Ukraine', 'Kyoto / Japan', 'La Ceiba / Honduras', 'La Chorrera / Panama',
               'La Condamine / Monaco', 'La Digue / Seychelles', 'La Massana / Andorra', 'La Paz / Bolivia', 'La Plaine / Dominica',
               'La Romana / Dominican Republic', 'La Serena / Chile', 'Labasa / Fiji', 'Labe / Guinea', 'Lae / Papua New Guinea',
               'Lagos / Nigeria', 'Lahore / Pakistan', 'Lalitpur / Nepal', 'Lalomanu / Samoa', 'Lankaran / Azerbaijan', 'Larissa / Greece',
               'Larnaca / Cyprus', 'Latakia / Syria', 'Lautoka / Fiji', 'Lelu / Micronesia', 'Lelydorp / Suriname', 'Leon / Nicaragua',
               'Les Cayes / Haiti', 'Liberec / Czech Republic', 'Liberia / Costa Rica', 'Liberta / Antigua and Barbuda',
               'Libreville / Gabon', 'Liege / Belgium', 'Liepaja / Latvia', 'Lilongwe / Malawi', 'Lima / Peru', 'Limassol / Cyprus',
               'Limerick / Ireland', 'Linden / Guyana', 'Linz / Austria', 'Lisbon / Portugal', 'Liverpool / United Kingdom',
               'Livingstone / Zambia', 'Ljubljana / Slovenia', 'Lobamba / Eswatini', 'Lomé / Togo', 'London / United Kingdom',
               'Los Angeles / United States', 'Luanda / Angola', 'Luang Prabang / Laos', 'Luba / Equatorial Guinea', 'Lubango / Angola',
               'Lucerne / Switzerland', 'Luganville / Vanuatu', 'Lusaka / Zambia', 'Luxembourg City / Luxembourg', 'Luxor / Egypt',
               'Lviv / Ukraine', 'Lyon / France', 'Machala / Ecuador', 'Madang / Papua New Guinea', 'Madrid / Spain', 'Mafraq / Jordan',
               'Mahajanga / Madagascar', 'Majuro / Marshall Islands', 'Makeni / Sierra Leone', 'Malabo / Equatorial Guinea',
               'Malaga / Spain', 'Malakal / South Sudan', 'Maldonado / Uruguay', 'Malekula / Vanuatu', 'Maliana / Timor-Leste',
               'Malmö / Sweden', 'Malé / Maldives', 'Managua / Nicaragua', 'Manama / Bahrain', 'Manchester / United Kingdom',
               'Mandalay / Myanmar', 'Mandeville / Jamaica', 'Manila / Philippines', 'Mansakonko / Gambia', 'Manzini / Eswatini',
               'Maputo / Mozambique', 'Maputsoe / Lesotho', 'Maracaibo / Venezuela', 'Maradi / Niger', 'Margarita Island / Venezuela',
               'Maribor / Slovenia', 'Marigot / Dominica', 'Maroua / Cameroon', 'Marrakech / Morocco', 'Marseille / France',
               'Marsh Harbour / Bahamas', 'Mary / Turkmenistan', 'Masaya / Nicaragua', 'Maseru / Lesotho', 'Massawa / Eritrea',
               'Matola / Mozambique', 'Maun / Botswana', 'Mawlamyine / Myanmar', 'Mazar-i-Sharif / Afghanistan', 'Mbabane / Eswatini',
               'Mbale / Uganda', 'Mbarara / Uganda', 'Mbeya / Tanzania', 'Mecca / Saudi Arabia', 'Medan / Indonesia', 'Medellín / Colombia',
               'Medina / Saudi Arabia', 'Mekelle / Ethiopia', 'Melaka / Malaysia', 'Melbourne / Australia', 'Melekeok / Palau',
               'Mellieha / Malta', 'Mendefera / Eritrea', 'Mendoza / Argentina', 'Merca / Somalia', 'Mesaieed / Qatar',
               'Mexico City / Mexico', 'Milan / Italy', 'Mindelo / Cabo Verde', 'Mingachevir / Azerbaijan', 'Minsk / Belarus',
               'Miskolc / Hungary', 'Misrata / Libya', 'Mitrovica / Kosovo', 'Moanda / Gabon', 'Moengo / Suriname', 'Mogadishu / Somalia',
               'Mogilev / Belarus', "Mohale's Hoek / Lesotho", 'Molepolole / Botswana', 'Mombasa / Kenya', 'Monaco / Monaco',
               'Moneghetti / Monaco', 'Monrovia / Liberia', 'Monte Carlo / Monaco', 'Montego Bay / Jamaica', 'Monterrey / Mexico',
               'Montevideo / Uruguay', 'Montreal / Canada', 'Mopti / Mali', 'Moroni / Comoros', 'Moscow / Russia', 'Moshi / Tanzania',
               'Mosta / Malta', 'Mostar / Bosnia and Herzegovina', 'Mosul / Iraq', 'Moundou / Chad', 'Mount Hagen / Papua New Guinea',
               'Muharraq / Bahrain', 'Mulifanua / Samoa', 'Mumbai / India', 'Munich / Germany', 'Musanze / Rwanda', 'Muscat / Oman',
               'Mutare / Zimbabwe', 'Mutsamudu / Comoros', 'Muyinga / Burundi', 'Mzuzu / Malawi', 'Mörön / Mongolia', "N'Djamena / Chad",
               "N'dalatando / Angola", 'Nadi / Fiji', 'Nairobi / Kenya', 'Nakuru / Kenya', 'Namangan / Uzbekistan', 'Nampo / North Korea',
               'Nampula / Mozambique', 'Nanumea / Tuvalu', 'Naples / Italy', 'Narva / Estonia', 'Nassau / Bahamas', 'Naypyidaw / Myanmar',
               'Ndola / Zambia', 'Negombo / Sri Lanka', 'Neiafu / Tonga', 'Neves / São Tomé and Príncipe', 'Nevis / Saint Kitts and Nevis',
               'New Amsterdam / Guyana', 'New Delhi / India', 'New York / United States', 'Ngerulmud / Palau', 'Ngozi / Burundi',
               'Nhlangano / Eswatini', 'Niamey / Niger', 'Nice / France', 'Nicosia / Cyprus', 'Nieuw Nickerie / Suriname',
               'Nikšić / Montenegro', 'Nis / Kosovo', 'Nitra / Slovakia', 'Nizhny Novgorod / Russia', 'Nizwa / Oman', 'Niš / Serbia',
               'Nkayi / Congo (Congo-Brazzaville)', 'Nouadhibou / Mauritania', 'Nouakchott / Mauritania', 'Novi Sad / Serbia',
               'Novosibirsk / Russia', "Nuku'alofa / Tonga", 'Nukufetau / Tuvalu', 'Nyala / Sudan', 'Nzérékoré / Guinea', 'Obock / Djibouti',
               'Ocho Rios / Jamaica', 'Odense / Denmark', 'Odessa / Ukraine', 'Oe-cusse / Timor-Leste', 'Ohrid / North Macedonia',
               'Oichili / Comoros', 'Oistins / Barbados', 'Omdurman / Sudan', 'Oran / Algeria', 'Oruro / Bolivia', 'Osaka / Japan',
               'Osh / Kyrgyzstan', 'Oshakati / Namibia', 'Osijek / Croatia', 'Oslo / Norway', 'Ostrava / Czech Republic', 'Ottawa / Canada',
               'Ouagadougou / Burkina Faso', 'Oulu / Finland', 'Oyem / Gabon', 'Oyo / Congo (Congo-Brazzaville)', 'Pakse / Laos',
               'Palikir / Micronesia', 'Panama City / Panama', 'Panevėžys / Lithuania', 'Paphos / Cyprus', 'Parakou / Benin',
               'Paramaribo / Suriname', 'Paris / France', 'Paro / Bhutan', 'Patras / Greece', 'Pattaya / Thailand', 'Paysandú / Uruguay',
               'Pec / Kosovo', 'Pedro Juan Caballero / Paraguay', 'Penang / Malaysia', 'Perth / Australia', 'Phnom Penh / Cambodia',
               'Phuentsholing / Bhutan', 'Phuket / Thailand', 'Pljevlja / Montenegro', 'Plovdiv / Bulgaria', 'Plzeň / Czech Republic',
               'Podgorica / Montenegro', 'Pointe-Noire / Congo (Congo-Brazzaville)', 'Poipet / Cambodia', 'Pokhara / Nepal',
               'Port Elizabeth / South Africa', 'Port Harcourt / Nigeria', 'Port Louis / Mauritius', 'Port Moresby / Papua New Guinea',
               'Port Sudan / Sudan', 'Port Vila / Vanuatu', 'Port of Spain / Trinidad and Tobago', 'Port-Gentil / Gabon',
               'Port-au-Prince / Haiti', 'Porto / Portugal', 'Porto Novo / Cabo Verde', 'Porto-Novo / Benin', 'Portsmouth / Dominica',
               'Poznań / Poland', 'Prague / Czech Republic', 'Praia / Cabo Verde', 'Praslin / Seychelles', 'Pretoria / South Africa',
               'Prešov / Slovakia', 'Prilep / North Macedonia', 'Principe / São Tomé and Príncipe', 'Pristina / Kosovo',
               'Puerto Plata / Dominican Republic', 'Punakha / Bhutan', 'Punta del Este / Uruguay', 'Puntarenas / Costa Rica',
               'Pyongyang / North Korea', 'Pärnu / Estonia', 'Pécs / Hungary', 'Quatre Bornes / Mauritius', 'Quetzaltenango / Guatemala',
               'Quezon City / Philippines', 'Quito / Ecuador', 'Quthing / Lesotho', 'Rabat / Morocco', 'Rabaul / Papua New Guinea',
               'Rajshahi / Bangladesh', 'Rawalpindi / Pakistan', 'Remich / Luxembourg', 'Reykjanesbær / Iceland', 'Reykjavik / Iceland',
               'Riffa / Bahrain', 'Riga / Latvia', 'Rijeka / Croatia', 'Rio de Janeiro / Brazil', 'Riyadh / Saudi Arabia',
               'Rodney Bay / Saint Lucia', 'Rome / Italy', 'Rosario / Argentina', 'Roseau / Dominica', 'Rosso / Mauritania',
               'Rotterdam / Netherlands', 'Rubavu / Rwanda', 'Rundu / Namibia', 'Ruse / Bulgaria', 'Rustavi / Georgia', 'Ruyigi / Burundi',
               'Saint Petersburg / Russia', 'Saint-Louis / Senegal', 'Salalah / Oman', 'Salmiya / Kuwait', 'Salto / Uruguay',
               'Salvador / Brazil', 'Salzburg / Austria', 'Samarkand / Uzbekistan', 'Same / Timor-Leste', 'San Fernando / Trinidad and Tobago',
               'San Ignacio / Belize', 'San José / Costa Rica', 'San Lorenzo / Paraguay', 'San Miguel / El Salvador', 'San Pedro / Ivory Coast',
               'San Pedro Sula / Honduras', 'San Pedro de Macorís / Dominican Republic', 'San Salvador / El Salvador', "Sana'a / Yemen",
               'Sant Julià de Lòria / Andorra', 'Santa Ana / El Salvador', 'Santa Cruz de la Sierra / Bolivia', 'Santa Maria / Cabo Verde',
               'Santana / São Tomé and Príncipe', 'Santiago / Chile', 'Santiago de Cuba / Cuba', 'Santiago de los Caballeros / Dominican Republic',
               'Santo Domingo / Dominican Republic', 'Sarajevo / Bosnia and Herzegovina', 'Sarh / Chad', "Savai'i / Samoa",
               'Savannakhet / Laos', 'Scarborough / Trinidad and Tobago', 'Schaan / Liechtenstein', 'Sebha / Libya', 'Segou / Mali',
               'Selebi-Phikwe / Botswana', 'Sentosa / Singapore', 'Seoul / South Korea', 'Seria / Brunei', 'Serravalle / San Marino',
               'Serrekunda / Gambia', 'Seville / Spain', 'Sfax / Tunisia', 'Shanghai / China', 'Sharjah / United Arab Emirates',
               'Sharm El Sheikh / Egypt', 'Shenzhen / China', 'Shiraz / Iran', 'Shkodër / Albania', 'Shymkent / Kazakhstan', 'Sidon / Lebanon',
               'Siem Reap / Cambodia', 'Sigatoka / Fiji', 'Sihanoukville / Cambodia', 'Sikasso / Mali', 'Singapore / Singapore',
               'Sitra / Bahrain', 'Skopje / North Macedonia', 'Sliema / Malta', 'Sofia / Bulgaria', 'Sohar / Oman', 'Sokodé / Togo',
               'Sonsonate / El Salvador', 'Soufrière / Dominica', 'Soufrière / Saint Lucia', 'Sousse / Tunisia', 'South Tarawa / Kiribati',
               'Spanish Town / Jamaica', 'Speightstown / Barbados', 'Split / Croatia', "St. George's / Grenada",
               "St. John's / Antigua and Barbuda", 'Stavanger / Norway', 'Stockholm / Sweden', 'Subotica / Serbia',
               'Sucre / Bolivia', 'Sumqayit / Azerbaijan', 'Surabaya / Indonesia', 'Suva / Fiji', 'Swakopmund / Namibia',
               'Sydney / Australia', 'Sylhet / Bangladesh', 'Szeged / Hungary', 'São Paulo / Brazil', 'São Tomé / São Tomé and Príncipe',
               'Tabernacle / Saint Kitts and Nevis', 'Tabiteuea / Kiribati', 'Tabriz / Iran', 'Tadjoura / Djibouti', 'Taguig / Philippines',
               'Tahoua / Niger', 'Taichung / Taiwan', 'Tainan / Taiwan', 'Taipei / Taiwan', 'Taiz / Yemen', 'Takoradi / Ghana',
               'Tallinn / Estonia', 'Tamale / Ghana', 'Tampere / Finland', 'Tangier / Morocco', 'Tanna / Vanuatu', 'Tartu / Estonia',
               'Tartus / Syria', 'Tashkent / Uzbekistan', 'Taunggyi / Myanmar', 'Tbilisi / Georgia', 'Tegucigalpa / Honduras',
               'Tehran / Iran', 'Tel Aviv / Israel', 'Teyateyaneng / Lesotho', 'The Hague / Netherlands', 'Thessaloniki / Greece',
               'Thimphu / Bhutan', 'Thiès / Senegal', 'Tijuana / Mexico', 'Timișoara / Romania', 'Tirana / Albania', 'Tiraspol / Moldova',
               'Toamasina / Madagascar', 'Tofol / Micronesia', 'Tokmok / Kyrgyzstan', 'Tokyo / Japan', 'Toronto / Canada', 'Touba / Senegal',
               'Toulouse / France', 'Trindade / São Tomé and Príncipe', 'Tripoli / Libya', 'Trnava / Slovakia', 'Trondheim / Norway',
               'Trujillo / Peru', 'Tsevie / Togo', 'Tunis / Tunisia', 'Turin / Italy', 'Turkmenabat / Turkmenistan', 'Tutong / Brunei',
               'Tuzla / Bosnia and Herzegovina', 'Tyre / Lebanon', 'Ulaanbaatar / Mongolia', 'Umm Salal / Qatar', 'Uppsala / Sweden',
               'Utrecht / Netherlands', 'Vacoas / Mauritius', 'Vaduz / Liechtenstein', 'Vagharshapat / Armenia', 'Vaiaku / Tuvalu',
               'Valencia / Spain', 'Valencia / Venezuela', 'Valletta / Malta', 'Valparaíso / Chile', 'Vanadzor / Armenia',
               'Vancouver / Canada', 'Vantaa / Finland', 'Varna / Bulgaria', 'Vatican City / Vatican City', "Vava'u / Tonga",
               'Victoria / Grenada', 'Victoria / Seychelles', 'Vienna / Austria', 'Vientiane / Laos', 'Vieux Fort / Saint Lucia',
               'Vilnius / Lithuania', 'Vitebsk / Belarus', 'Vlorë / Albania', 'Västerås / Sweden', 'Wad Madani / Sudan',
               'Walvis Bay / Namibia', 'Warsaw / Poland', 'Washington, D.C. / United States', 'Waterford / Ireland', 'Wau / South Sudan',
               'Wellington / New Zealand', 'Weno / Micronesia', 'West End / Bahamas', 'Windhoek / Namibia', 'Wonsan / North Korea',
               'Wotje / Marshall Islands', 'Wrocław / Poland', 'Xieng Khouang / Laos', 'Yamoussoukro / Ivory Coast', 'Yangon / Myanmar',
               'Yaoundé / Cameroon', 'Yaren / Nauru', 'Yekaterinburg / Russia', 'Yerevan / Armenia', 'Yogyakarta / Indonesia',
               'Zagreb / Croatia', 'Zahle / Lebanon', 'Zarqa / Jordan', 'Zenica / Bosnia and Herzegovina', 'Ziguinchor / Senegal',
               'Zinder / Niger', 'Zomba / Malawi', 'Zugdidi / Georgia', 'Zurich / Switzerland', 'Zuwara / Libya', 'Zwedru / Liberia',
               'Łódź / Poland', 'Šiauliai / Lithuania']



coordinate_map = {
    # Afghanistan
    "Kabul / Afghanistan": (34.5553, 69.2075),
    "Herat / Afghanistan": (34.3529, 62.2041),
    "Kandahar / Afghanistan": (31.6289, 65.7372),
    "Mazar-i-Sharif / Afghanistan": (36.7080, 67.1109),
    "Jalalabad / Afghanistan": (34.4342, 70.4475),
    "Bamyan / Afghanistan": (34.8216, 67.8213),

    # Albania
    "Tirana / Albania": (41.3275, 19.8189),
    "Durrës / Albania": (41.3135, 19.4448),
    "Vlorë / Albania": (40.4672, 19.4897),
    "Shkodër / Albania": (42.0683, 19.5119),
    "Elbasan / Albania": (41.1125, 20.0850),

    # Algeria
    "Algiers / Algeria": (36.7538, 3.0588),
    "Oran / Algeria": (35.6915, -0.6349),
    "Constantine / Algeria": (36.3650, 6.6142),
    "Annaba / Algeria": (36.8663, 7.7661),
    "Blida / Algeria": (36.4795, 2.8341),

    # Andorra
    "Andorra la Vella / Andorra": (42.5078, 1.5211),
    "Escaldes-Engordany / Andorra": (42.5072, 1.5345),
    "Encamp / Andorra": (42.5333, 1.5833),
    "Sant Julià de Lòria / Andorra": (42.4617, 1.4897),
    "La Massana / Andorra": (42.5158, 1.4850),

    # Angola
    "Luanda / Angola": (-8.8390, 13.2894),
    "N'dalatando / Angola": (-9.2436, 14.1919),
    "Lubango / Angola": (-14.9174, 13.4936),
    "Benguela / Angola": (-12.5882, 13.4061),
    "Huambo / Angola": (-12.7600, 15.7370),

    # Antigua and Barbuda
    "St. John's / Antigua and Barbuda": (17.1212, -61.8468),
    "All Saints / Antigua and Barbuda": (17.0833, -61.8500),
    "Liberta / Antigua and Barbuda": (17.0333, -61.8000),
    "Bolands / Antigua and Barbuda": (17.0000, -61.8500),
    "Freetown / Antigua and Barbuda": (17.1000, -61.8500),

    # Argentina
    "Buenos Aires / Argentina": (-34.6037, -58.3816),
    "Cordoba / Argentina": (-31.4201, -64.1888),
    "Rosario / Argentina": (-32.9397, -60.9783),
    "Mendoza / Argentina": (-32.8894, -68.8440),
    "Bariloche / Argentina": (-41.1349, -71.3082),

    # Armenia
    "Yerevan / Armenia": (40.1792, 44.4991),
    "Gyumri / Armenia": (49.6647, 40.1509),
    "Vanadzor / Armenia": (40.8232, 42.4769),
    "Vagharshapat / Armenia": (40.1553, 44.2956),
    "Kapan / Armenia": (39.2260, 46.4020),

    # Australia
    "Sydney / Australia": (-33.8688, 151.2093),
    "Melbourne / Australia": (-37.8136, 144.9631),
    "Brisbane / Australia": (-27.4698, 153.0251),
    "Perth / Australia": (-31.9505, 115.8605),
    "Adelaide / Australia": (-34.9285, 138.6007),

    # Austria
    "Vienna / Austria": (48.2082, 16.3738),
    "Graz / Austria": (47.0707, 15.4395),
    "Linz / Austria": (48.3064, 14.2861),
    "Salzburg / Austria": (47.8095, 13.0550),
    "Innsbruck / Austria": (47.2692, 11.4041),

    # Azerbaijan
    "Baku / Azerbaijan": (40.4093, 49.8671),
    "Ganja / Azerbaijan": (40.6823, 46.3600),
    "Mingachevir / Azerbaijan": (40.7597, 47.0500),
    "Sumqayit / Azerbaijan": (40.5890, 49.6600),
    "Lankaran / Azerbaijan": (38.7533, 48.6111),

    # Bahamas
    "Nassau / Bahamas": (25.0343, -77.3963),
    "Freeport / Bahamas": (26.5352, -78.7245),
    "West End / Bahamas": (25.8167, -78.1167),
    "Marsh Harbour / Bahamas": (25.5547, -77.0601),
    "Governor's Harbour / Bahamas": (25.2175, -76.6887),

    # Bahrain
    "Manama / Bahrain": (26.2235, 50.5876),
    "Riffa / Bahrain": (26.1797, 50.5822),
    "Muharraq / Bahrain": (26.2482, 50.6119),
    "Sitra / Bahrain": (26.1514, 50.5669),
    "Isa Town / Bahrain": (26.2289, 50.5358),

    # Bangladesh
    "Dhaka / Bangladesh": (23.8103, 90.4125),
    "Chittagong / Bangladesh": (22.3569, 91.7832),
    "Khulna / Bangladesh": (22.8456, 89.5403),
    "Rajshahi / Bangladesh": (24.3633, 88.6241),
    "Sylhet / Bangladesh": (24.8949, 91.8687),

    # Barbados
    "Bridgetown / Barbados": (13.1, -59.6167),
    "Speightstown / Barbados": (13.2390, -59.6378),
    "Oistins / Barbados": (13.0724, -59.5350),
    "Holetown / Barbados": (13.1913, -59.6349),
    "Bathsheba / Barbados": (13.2077, -59.4605),

    # Belarus
    "Minsk / Belarus": (53.9, 27.5667),
    "Gomel / Belarus": (52.4419, 30.9754),
    "Mogilev / Belarus": (53.9, 30.3642),
    "Vitebsk / Belarus": (55.1894, 30.2016),
    "Grodno / Belarus": (53.6667, 23.8),

    # Belgium
    "Brussels / Belgium": (50.8503, 4.3517),
    "Antwerp / Belgium": (51.2194, 4.4025),
    "Ghent / Belgium": (51.0543, 3.7174),
    "Bruges / Belgium": (51.2093, 3.2247),
    "Liege / Belgium": (50.6402, 5.5702),

    # Belize
    "Belmopan / Belize": (17.25, -88.7667),
    "Belize City / Belize": (17.5046, -88.1963),
    "San Ignacio / Belize": (17.1500, -89.0700),
    "Corozal Town / Belize": (18.3891, -88.3917),
    "Dangriga / Belize": (16.9657, -88.2323),

    # Benin
    "Cotonou / Benin": (6.3667, 2.4417),
    "Porto-Novo / Benin": (6.4969, 2.6289),
    "Parakou / Benin": (9.3406, 2.6172),
    "Djougou / Benin": (9.7000, 1.8000),
    "Bohicon / Benin": (7.1833, 2.0833),

    # Bhutan
    "Thimphu / Bhutan": (27.4715, 89.6391),
    "Phuentsholing / Bhutan": (26.8501, 89.4274),
    "Paro / Bhutan": (27.4231, 89.4095),
    "Punakha / Bhutan": (27.5705, 89.7130),
    "Jakar / Bhutan": (27.6333, 90.7500),

    # Bolivia
    "La Paz / Bolivia": (-16.5000, -68.1193),
    "Santa Cruz de la Sierra / Bolivia": (-17.7833, -63.1811),
    "Cochabamba / Bolivia": (-17.3939, -66.1578),
    "Sucre / Bolivia": (-19.0333, -65.2628),
    "Oruro / Bolivia": (-17.9833, -68.0994),

    # Bosnia and Herzegovina
    "Sarajevo / Bosnia and Herzegovina": (43.8486, 18.3564),
    "Banja Luka / Bosnia and Herzegovina": (44.7772, 17.1897),
    "Mostar / Bosnia and Herzegovina": (43.3433, 17.8075),
    "Zenica / Bosnia and Herzegovina": (44.2014, 17.9047),
    "Tuzla / Bosnia and Herzegovina": (44.5375, 18.6764),

    # Botswana
    "Gaborone / Botswana": (-24.6282, 25.9231),
    "Francistown / Botswana": (-21.1695, 27.5101),
    "Molepolole / Botswana": (-24.5914, 25.2722),
    "Maun / Botswana": (-19.9833, 23.4167),
    "Selebi-Phikwe / Botswana": (-22.0000, 27.8000),

    # Brazil
    "Brasília / Brazil": (-15.7801, -47.9292),
    "São Paulo / Brazil": (-23.5505, -46.6333),
    "Rio de Janeiro / Brazil": (-22.9068, -43.1729),
    "Salvador / Brazil": (-12.9714, -38.5014),
    "Fortaleza / Brazil": (-3.7172, -38.5437),

    # Brunei
    "Bandar Seri Begawan / Brunei": (4.9031, 114.9398),
    "Kuala Belait / Brunei": (4.5645, 114.1907),
    "Seria / Brunei": (4.5833, 114.6167),
    "Tutong / Brunei": (4.6167, 114.6167),
    "Bangar / Brunei": (4.5389, 115.0428),

    # Bulgaria
    "Sofia / Bulgaria": (42.6977, 23.3219),
    "Plovdiv / Bulgaria": (42.1354, 24.7450),
    "Varna / Bulgaria": (43.2140, 27.9147),
    "Burgas / Bulgaria": (42.5048, 27.4626),
    "Ruse / Bulgaria": (43.8493, 25.9670),

    # Burkina Faso
    "Ouagadougou / Burkina Faso": (12.6392, -1.5333),
    "Bobo-Dioulasso / Burkina Faso": (11.1786, -4.2897),
    "Koudougou / Burkina Faso": (12.2500, -3.5667),
    "Banfora / Burkina Faso": (10.6333, -4.7667),
    "Kaya / Burkina Faso": (12.1262, -1.0724),

    # Burundi
    "Bujumbura / Burundi": (-3.3614, 29.3594),
    "Gitega / Burundi": (-3.4269, 29.9300),
    "Muyinga / Burundi": (-2.9311, 30.4533),
    "Ngozi / Burundi": (-2.8986, 30.3944),
    "Ruyigi / Burundi": (-3.4333, 30.3833),

    # Cabo Verde
    "Praia / Cabo Verde": (14.9333, -23.5133),
    "Mindelo / Cabo Verde": (16.8900, -24.9800),
    "Santa Maria / Cabo Verde": (16.6064, -22.9147),
    "Espargos / Cabo Verde": (16.6347, -22.9164),
    "Porto Novo / Cabo Verde": (17.0900, -25.0600),

    # Cambodia
    "Phnom Penh / Cambodia": (11.5564, 104.9282),
    "Siem Reap / Cambodia": (13.4100, 103.8597),
    "Battambang / Cambodia": (13.0950, 103.2112),
    "Sihanoukville / Cambodia": (10.6250, 103.5236),
    "Poipet / Cambodia": (13.6520, 102.6174),

    # Cameroon
    "Yaoundé / Cameroon": (3.8480, 11.5021),
    "Douala / Cameroon": (4.0511, 9.7075),
    "Bertoua / Cameroon": (4.5833, 13.6833),
    "Garoua / Cameroon": (9.3100, 13.3920),
    "Maroua / Cameroon": (10.5957, 14.3199),

    # Canada
    "Ottawa / Canada": (45.4215, -75.6992),
    "Toronto / Canada": (43.6510, -79.3470),
    "Vancouver / Canada": (49.2827, -123.1207),
    "Montreal / Canada": (45.5017, -73.5673),
    "Calgary / Canada": (51.0447, -114.0719),

    # Central African Republic
    "Bangui / Central African Republic": (4.3947, 18.5582),
    "Berberati / Central African Republic": (4.0333, 15.7833),
    "Birao / Central African Republic": (11.7167, 19.3833),
    "Carnot / Central African Republic": (4.6167, 15.8333),
    "Kaga Bandoro / Central African Republic": (5.7667, 19.3833),

    # Chad
    "N'Djamena / Chad": (12.1348, 15.0550),
    "Moundou / Chad": (8.5794, 15.7511),
    "Sarh / Chad": (9.1550, 15.4233),
    "Abéché / Chad": (13.8333, 20.8333),
    "Kelo / Chad": (9.2033, 15.7556),

    # Chile
    "Santiago / Chile": (-33.4489, -70.6693),
    "Valparaíso / Chile": (-33.0464, -71.6197),
    "Concepción / Chile": (-36.8278, -73.0500),
    "La Serena / Chile": (-29.9023, -71.2500),
    "Antofagasta / Chile": (-23.6500, -70.4000),

    # China
    "Beijing / China": (39.9042, 116.4074),
    "Shanghai / China": (31.2304, 121.4737),
    "Hong Kong / China": (22.3193, 114.1694),
    "Guangzhou / China": (23.1291, 113.2644),
    "Shenzhen / China": (22.5431, 114.0579),

    # Colombia
    "Bogotá / Colombia": (4.7110, -74.0721),
    "Medellín / Colombia": (6.2442, -75.5812),
    "Cali / Colombia": (3.4516, -76.5320),
    "Barranquilla / Colombia": (10.9639, -74.7964),
    "Cartagena / Colombia": (10.3910, -75.4794),

    # Comoros
    "Moroni / Comoros": (-11.7017, 43.2547),
    "Mutsamudu / Comoros": (-12.0650, 44.4036),
    "Fomboni / Comoros": (-12.2825, 43.7467),
    "Domoni / Comoros": (-12.3514, 44.5236),
    "Oichili / Comoros": (-11.6697, 43.3172),

    # Congo (Congo-Brazzaville)
    "Brazzaville / Congo (Congo-Brazzaville)": (-4.2634, 15.2429),
    "Pointe-Noire / Congo (Congo-Brazzaville)": (-4.7867, 11.8694),
    "Dolisie / Congo (Congo-Brazzaville)": (-4.1483, 12.2389),
    "Oyo / Congo (Congo-Brazzaville)": (-3.7917, 11.9167),
    "Nkayi / Congo (Congo-Brazzaville)": (-4.6000, 13.0000),

    # Costa Rica
    "San José / Costa Rica": (9.9281, -84.0907),
    "Alajuela / Costa Rica": (10.0161, -84.2126),
    "Cartago / Costa Rica": (9.8667, -83.9192),
    "Liberia / Costa Rica": (10.5881, -85.4411),
    "Puntarenas / Costa Rica": (9.9750, -84.8389),

    # Croatia
    "Zagreb / Croatia": (45.8131, 15.978),
    "Split / Croatia": (43.5081, 16.4402),
    "Dubrovnik / Croatia": (42.6507, 18.0944),
    "Rijeka / Croatia": (45.3275, 14.4422),
    "Osijek / Croatia": (45.5511, 18.6928),

    # Cuba
    "Havana / Cuba": (23.1136, -82.3666),
    "Santiago de Cuba / Cuba": (20.0245, -75.8219),
    "Camagüey / Cuba": (21.3800, -77.9167),
    "Holguín / Cuba": (20.8800, -76.2672),
    "Cienfuegos / Cuba": (22.1511, -80.4342),

    # Cyprus
    "Nicosia / Cyprus": (35.1856, 33.3823),
    "Limassol / Cyprus": (34.6739, 33.0447),
    "Larnaca / Cyprus": (34.9160, 33.6358),
    "Famagusta / Cyprus": (35.1167, 33.9333),
    "Paphos / Cyprus": (34.7667, 32.4167),

    # Czech Republic (Czechia)
    "Prague / Czech Republic": (50.0755, 14.4378),
    "Brno / Czech Republic": (49.1951, 16.6070),
    "Ostrava / Czech Republic": (49.8341, 18.2926),
    "Plzeň / Czech Republic": (49.7475, 13.3777),
    "Liberec / Czech Republic": (50.7672, 15.0585),

    # Denmark
    "Copenhagen / Denmark": (55.6761, 12.5683),
    "Aarhus / Denmark": (56.1629, 10.2039),
    "Odense / Denmark": (55.4038, 10.4024),
    "Aalborg / Denmark": (57.0488, 9.9217),
    "Esbjerg / Denmark": (55.4762, 8.4594),

    # Djibouti
    "Djibouti / Djibouti": (11.8251, 42.5903),
    "Ali Sabieh / Djibouti": (11.1530, 42.7345),
    "Tadjoura / Djibouti": (11.7494, 42.9744),
    "Dikhil / Djibouti": (11.1000, 42.4000),
    "Obock / Djibouti": (11.0014, 43.2681),

    # Dominica
    "Roseau / Dominica": (15.3014, -61.3880),
    "Portsmouth / Dominica": (15.5500, -61.4678),
    "Marigot / Dominica": (15.6172, -61.2828),
    "Soufrière / Dominica": (15.2794, -61.3444),
    "La Plaine / Dominica": (15.4061, -61.3222),

    # Dominican Republic
    "Santo Domingo / Dominican Republic": (18.4761, -69.9312),
    "Santiago de los Caballeros / Dominican Republic": (19.4559, -70.6934),
    "La Romana / Dominican Republic": (18.4226, -68.9817),
    "Puerto Plata / Dominican Republic": (19.7901, -70.6876),
    "San Pedro de Macorís / Dominican Republic": (18.4514, -69.2992),

    # Ecuador
    "Quito / Ecuador": (-0.1807, -78.4678),
    "Guayaquil / Ecuador": (-2.1700, -79.9224),
    "Cuenca / Ecuador": (-2.9000, -79.0043),
    "Machala / Ecuador": (-3.2589, -79.9589),
    "Ambato / Ecuador": (-1.2500, -78.6167),

    # Egypt
    "Cairo / Egypt": (30.0444, 31.2357),
    "Alexandria / Egypt": (31.2156, 29.9553),
    "Giza / Egypt": (30.0131, 31.2089),
    "Sharm El Sheikh / Egypt": (27.9158, 34.3299),
    "Luxor / Egypt": (25.6872, 32.6396),

    # El Salvador
    "San Salvador / El Salvador": (13.6929, -89.2182),
    "Santa Ana / El Salvador": (13.9981, -89.5541),
    "San Miguel / El Salvador": (13.4833, -88.1833),
    "Sonsonate / El Salvador": (13.7167, -89.3670),
    "Ahuachapán / El Salvador": (13.9500, -89.7667),

    # Equatorial Guinea
    "Malabo / Equatorial Guinea": (3.7500, 8.7833),
    "Bata / Equatorial Guinea": (1.8667, 9.7833),
    "Ebebiyin / Equatorial Guinea": (1.5500, 11.1000),
    "Aconibe / Equatorial Guinea": (1.6167, 11.4667),
    "Luba / Equatorial Guinea": (3.2500, 9.4833),

    # Eritrea
    "Asmara / Eritrea": (15.3325, 38.9339),
    "Massawa / Eritrea": (15.6000, 39.6167),
    "Keren / Eritrea": (15.7811, 38.4567),
    "Assab / Eritrea": (13.0000, 42.7400),
    "Mendefera / Eritrea": (15.3350, 38.7494),

    # Estonia
    "Tallinn / Estonia": (59.4370, 24.7535),
    "Tartu / Estonia": (58.3800, 26.7250),
    "Narva / Estonia": (59.3772, 28.1894),
    "Pärnu / Estonia": (58.3850, 24.4950),
    "Kohtla-Järve / Estonia": (59.3772, 27.2733),

    # Eswatini
    "Mbabane / Eswatini": (-26.3225, 31.1414),
    "Manzini / Eswatini": (-26.5231, 31.3761),
    "Lobamba / Eswatini": (-26.4444, 31.3158),
    "Nhlangano / Eswatini": (-26.0417, 31.3139),
    "Big Bend / Eswatini": (-26.3667, 31.5667),

    # Ethiopia
    "Addis Ababa / Ethiopia": (9.1450, 40.4897),
    "Gondar / Ethiopia": (12.6320, 37.4706),
    "Mekelle / Ethiopia": (13.4917, 39.4750),
    "Dire Dawa / Ethiopia": (9.5900, 41.8667),
    "Bahir Dar / Ethiopia": (11.5982, 37.3976),

    # Fiji
    "Suva / Fiji": (-18.1416, 178.4419),
    "Nadi / Fiji": (-17.8000, 177.4500),
    "Lautoka / Fiji": (-17.6131, 177.4469),
    "Labasa / Fiji": (-16.4167, 179.4000),
    "Sigatoka / Fiji": (-18.1347, 177.4933),

    # Finland
    "Helsinki / Finland": (60.1695, 24.9354),
    "Espoo / Finland": (60.2055, 24.6559),
    "Tampere / Finland": (61.4978, 23.7610),
    "Vantaa / Finland": (60.2941, 25.0403),
    "Oulu / Finland": (65.0120, 25.4681),

    # France
    "Paris / France": (48.8566, 2.3522),
    "Marseille / France": (43.2965, 5.3698),
    "Lyon / France": (45.7640, 4.8357),
    "Toulouse / France": (43.6047, 1.4442),
    "Nice / France": (43.7102, 7.2620),

    # Gabon
    "Libreville / Gabon": (0.4167, 9.4670),
    "Port-Gentil / Gabon": (-0.7167, 8.7833),
    "Franceville / Gabon": (-1.6171, 13.5833),
    "Moanda / Gabon": (-1.6000, 13.5500),
    "Oyem / Gabon": (1.6167, 11.6167),

    # Gambia
    "Banjul / Gambia": (13.4549, -16.5782),
    "Serrekunda / Gambia": (13.4625, -16.6917),
    "Brikama / Gambia": (13.3000, -15.6333),
    "Mansakonko / Gambia": (13.7167, -15.5000),
    "Basse Santa Su / Gambia": (13.2833, -14.4167),

    # Georgia
    "Tbilisi / Georgia": (41.7151, 44.8271),
    "Batumi / Georgia": (41.6407, 41.6351),
    "Kutaisi / Georgia": (42.2604, 42.6980),
    "Zugdidi / Georgia": (42.5145, 41.8523),
    "Rustavi / Georgia": (41.5205, 45.0487),

    # Germany
    "Berlin / Germany": (52.5200, 13.4050),
    "Munich / Germany": (48.1351, 11.5820),
    "Hamburg / Germany": (53.5511, 9.9937),
    "Cologne / Germany": (50.9375, 6.9603),
    "Frankfurt / Germany": (50.1109, 8.6821),

    # Ghana
    "Accra / Ghana": (5.6037, -0.1870),
    "Kumasi / Ghana": (6.6883, -1.6247),
    "Tamale / Ghana": (9.4000, -0.8333),
    "Takoradi / Ghana": (4.8977, -1.7491),
    "Ashaiman / Ghana": (5.6500, -0.0333),

    # Greece
    "Athens / Greece": (37.9838, 23.7275),
    "Thessaloniki / Greece": (40.6401, 22.9444),
    "Patras / Greece": (38.2404, 21.7362),
    "Heraklion / Greece": (35.3400, 25.1442),
    "Larissa / Greece": (39.6400, 22.4167),

    # Grenada
    "St. George's / Grenada": (12.0564, -61.7480),
    "Grenville / Grenada": (12.0803, -61.5304),
    "Victoria / Grenada": (12.2278, -61.5339),
    "Gouyave / Grenada": (12.1850, -61.5614),
    "Carriacou / Grenada": (12.4700, -61.4681),

    # Guatemala
    "Guatemala City / Guatemala": (14.6349, -90.5069),
    "Quetzaltenango / Guatemala": (14.8322, -91.5169),
    "Escuintla / Guatemala": (13.0703, -90.7825),
    "Cobán / Guatemala": (15.4667, -90.3833),
    "Antigua Guatemala / Guatemala": (14.5500, -90.7333),

    # Guinea
    "Conakry / Guinea": (9.5095, -13.7122),
    "Nzérékoré / Guinea": (7.7667, -8.7167),
    "Kindia / Guinea": (10.0000, -12.5000),
    "Faranah / Guinea": (10.0167, -10.0167),
    "Labe / Guinea": (11.3000, -12.2833),

    # Guinea-Bissau
    "Bissau / Guinea-Bissau": (11.8817, -15.6173),
    "Bafatá / Guinea-Bissau": (12.2833, -14.6167),
    "Gabú / Guinea-Bissau": (12.2670, -14.2833),
    "Cacheu / Guinea-Bissau": (11.2833, -15.6167),
    "Bissora / Guinea-Bissau": (12.2333, -14.5667),

    # Guyana
    "Georgetown / Guyana": (6.8013, -58.1551),
    "Linden / Guyana": (6.0167, -58.2833),
    "New Amsterdam / Guyana": (6.2486, -57.5072),
    "Anna Regina / Guyana": (7.2667, -58.2167),
    "Bartica / Guyana": (6.1833, -58.6167),

    # Haiti
    "Port-au-Prince / Haiti": (18.5944, -72.3070),
    "Cap-Haïtien / Haiti": (19.7580, -72.2033),
    "Les Cayes / Haiti": (18.2200, -73.7525),
    "Jacmel / Haiti": (18.2395, -72.5333),
    "Gonaïves / Haiti": (19.4500, -72.6833),

    # Honduras
    "Tegucigalpa / Honduras": (13.9676, -66.9500),
    "San Pedro Sula / Honduras": (13.5000, -87.1900),
    "Choloma / Honduras": (13.1100, -87.9740),
    "La Ceiba / Honduras": (15.7778, -86.7850),
    "El Progreso / Honduras": (13.4436, -87.9667),

    # Hungary
    "Budapest / Hungary": (47.4979, 19.0402),
    "Debrecen / Hungary": (47.5316, 21.6277),
    "Szeged / Hungary": (46.2530, 20.1419),
    "Pécs / Hungary": (45.9991, 18.2295),
    "Miskolc / Hungary": (48.1030, 20.7770),

    # Iceland
    "Reykjavik / Iceland": (64.1355, -21.8954),
    "Akureyri / Iceland": (65.6885, -18.1262),
    "Reykjanesbær / Iceland": (63.9333, -22.6900),
    "Kopavogur / Iceland": (64.1355, -21.8954),
    "Hafnarfjordur / Iceland": (64.0607, -21.9372),

    # India
    "New Delhi / India": (28.6139, 77.2090),
    "Mumbai / India": (19.0760, 72.8777),
    "Bangalore / India": (12.9716, 77.5946),
    "Chennai / India": (13.0827, 80.2707),
    "Kolkata / India": (22.5726, 88.3639),

    # Indonesia
    "Jakarta / Indonesia": (-6.2088, 106.8456),
    "Surabaya / Indonesia": (-7.2504, 112.7688),
    "Medan / Indonesia": (3.5952, 98.6722),
    "Bandung / Indonesia": (-6.9175, 107.6191),
    "Yogyakarta / Indonesia": (-7.7956, 110.3695),

    # Iran
    "Tehran / Iran": (35.6892, 51.3890),
    "Isfahan / Iran": (32.6546, 51.6670),
    "Shiraz / Iran": (29.6299, 52.5311),
    "Tabriz / Iran": (38.0800, 46.2900),
    "Ahvaz / Iran": (31.3200, 48.6900),

    # Iraq
    "Baghdad / Iraq": (33.3152, 44.3661),
    "Mosul / Iraq": (36.3350, 43.1189),
    "Basra / Iraq": (30.5085, 47.7835),
    "Kirkuk / Iraq": (35.4694, 44.3964),
    "Erbil / Iraq": (36.1911, 44.0097),

    # Ireland
    "Dublin / Ireland": (53.3498, -6.2603),
    "Cork / Ireland": (51.8979, -8.4756),
    "Limerick / Ireland": (52.6680, -8.6233),
    "Galway / Ireland": (53.2707, -9.0568),
    "Waterford / Ireland": (52.2580, -7.1101),

    # Israel
    "Jerusalem / Israel": (31.7683, 35.2137),
    "Tel Aviv / Israel": (32.0853, 34.7818),
    "Haifa / Israel": (32.7940, 34.9896),
    "Eilat / Israel": (29.5581, 34.9482),
    "Beer Sheva / Israel": (31.2518, 34.7913),

    # Italy
    "Rome / Italy": (41.9028, 12.4964),
    "Milan / Italy": (45.4642, 9.1900),
    "Naples / Italy": (40.8522, 14.2681),
    "Turin / Italy": (45.0703, 7.6869),
    "Florence / Italy": (43.7696, 11.2558),

    # Ivory Coast (Côte d'Ivoire)
    "Abidjan / Ivory Coast": (5.3097, -4.0126),
    "Bouaké / Ivory Coast": (7.6935, -5.0713),
    "Yamoussoukro / Ivory Coast": (6.8276, -5.2893),
    "San Pedro / Ivory Coast": (4.7500, -6.6378),
    "Daloa / Ivory Coast": (6.9000, -7.5000),

    # Jamaica
    "Kingston / Jamaica": (17.9714, -76.7936),
    "Montego Bay / Jamaica": (18.4769, -77.9150),
    "Mandeville / Jamaica": (17.9792, -77.6494),
    "Spanish Town / Jamaica": (17.9810, -76.9690),
    "Ocho Rios / Jamaica": (18.4043, -77.0995),

    # Japan
    "Tokyo / Japan": (35.6895, 139.6917),
    "Osaka / Japan": (34.6937, 135.5023),
    "Kyoto / Japan": (35.0116, 135.7681),
    "Hokkaido / Japan": (43.0642, 141.3469),
    "Fukuoka / Japan": (33.5902, 130.4017),

    # Jordan
    "Amman / Jordan": (31.9454, 35.9284),
    "Zarqa / Jordan": (32.0686, 36.0930),
    "Irbid / Jordan": (32.5554, 35.8531),
    "Aqaba / Jordan": (29.5333, 35.0000),
    "Mafraq / Jordan": (32.3397, 36.1964),

    # Kazakhstan
    "Almaty / Kazakhstan": (43.2220, 76.8512),
    "Astana / Kazakhstan": (51.1694, 71.4491),
    "Shymkent / Kazakhstan": (42.3417, 69.5892),
    "Karaganda / Kazakhstan": (49.8000, 73.0833),
    "Aktobe / Kazakhstan": (50.2833, 57.1667),

    # Kenya
    "Nairobi / Kenya": (-1.2864, 36.8172),
    "Mombasa / Kenya": (-4.0435, 39.6682),
    "Kisumu / Kenya": (-0.0917, 34.7617),
    "Nakuru / Kenya": (-0.3031, 36.0800),
    "Eldoret / Kenya": (0.5150, 35.2719),

    # Kiribati
    "South Tarawa / Kiribati": (-1.4514, 173.0333),
    "Bairiki / Kiribati": (-1.3500, 173.0167),
    "Betio / Kiribati": (-1.4500, 172.9790),
    "Buota / Kiribati": (-0.8528, 173.4069),
    "Tabiteuea / Kiribati": (-0.3972, 173.5092),

    # Kosovo
    "Pristina / Kosovo": (42.6722, 21.2285),
    "Pec / Kosovo": (42.6722, 20.3044),
    "Nis / Kosovo": (43.3206, 21.8954),
    "Mitrovica / Kosovo": (42.8833, 20.8667),
    "Gjakova / Kosovo": (42.3800, 20.4300),

    # Kuwait
    "Kuwait City / Kuwait": (29.3759, 47.9774),
    "Al Ahmadi / Kuwait": (28.9544, 48.0569),
    "Hawalli / Kuwait": (29.3400, 48.0122),
    "Salmiya / Kuwait": (29.5775, 48.1395),
    "Farwaniya / Kuwait": (29.2711, 47.9442),

    # Kyrgyzstan
    "Bishkek / Kyrgyzstan": (42.8746, 74.6121),
    "Osh / Kyrgyzstan": (40.5284, 72.7922),
    "Jalal-Abad / Kyrgyzstan": (40.9383, 72.8294),
    "Tokmok / Kyrgyzstan": (42.8400, 75.2786),
    "Karakol / Kyrgyzstan": (42.4892, 78.3900),

    # Laos
    "Vientiane / Laos": (17.9757, 102.6331),
    "Luang Prabang / Laos": (19.8833, 102.1417),
    "Savannakhet / Laos": (16.5667, 104.7500),
    "Pakse / Laos": (15.1167, 105.7833),
    "Xieng Khouang / Laos": (19.4281, 103.3581),

    # Latvia
    "Riga / Latvia": (56.9460, 24.1059),
    "Jurmala / Latvia": (56.9631, 23.8056),
    "Liepaja / Latvia": (56.5090, 21.0134),
    "Jelgava / Latvia": (56.6511, 23.7019),
    "Daugavpils / Latvia": (55.8826, 26.5465),

    # Lebanon
    "Beirut / Lebanon": (33.8938, 35.5018),
    "Sidon / Lebanon": (33.5633, 35.3790),
    "Tyre / Lebanon": (33.2704, 35.2056),
    "Zahle / Lebanon": (33.8533, 36.2197),

    # Lesotho
    "Maseru / Lesotho": (-29.3176, 27.4897),
    "Teyateyaneng / Lesotho": (-28.8983, 27.5536),
    "Mohale's Hoek / Lesotho": (-30.2319, 27.2269),
    "Quthing / Lesotho": (-30.3833, 27.3569),
    "Maputsoe / Lesotho": (-28.9792, 27.8833),

    # Liberia
    "Monrovia / Liberia": (6.4281, -9.4295),
    "Gbarnga / Liberia": (7.7167, -9.4500),
    "Buchanan / Liberia": (5.8722, -9.4292),
    "Harper / Liberia": (4.7453, -7.7192),
    "Zwedru / Liberia": (6.0794, -8.1414),

    # Libya
    "Tripoli / Libya": (32.8872, 13.1919),
    "Benghazi / Libya": (32.1186, 20.0691),
    "Misrata / Libya": (32.3772, 15.0933),
    "Sebha / Libya": (27.0446, 14.4290),
    "Zuwara / Libya": (32.9233, 12.0833),

    # Liechtenstein
    "Vaduz / Liechtenstein": (47.1415, 9.5215),
    "Schaan / Liechtenstein": (47.1667, 9.5167),
    "Balzers / Liechtenstein": (47.0430, 9.5107),
    "Eschen / Liechtenstein": (47.2053, 9.5536),

    # Lithuania
    "Vilnius / Lithuania": (54.6892, 25.2798),
    "Kaunas / Lithuania": (54.8980, 23.9036),
    "Klaipeda / Lithuania": (55.7030, 21.1447),
    "Šiauliai / Lithuania": (55.9333, 23.3167),
    "Panevėžys / Lithuania": (55.7333, 24.3667),

    # Luxembourg
    "Luxembourg City / Luxembourg": (49.6117, 6.13),
    "Esch-sur-Alzette / Luxembourg": (49.4937, 5.9790),
    "Differdange / Luxembourg": (49.5140, 5.9624),
    "Ettelbruck / Luxembourg": (49.8692, 6.1292),
    "Remich / Luxembourg": (49.5931, 6.3372),

    # Madagascar
    "Antananarivo / Madagascar": (-18.8792, 47.5079),
    "Toamasina / Madagascar": (-18.1653, 49.4028),
    "Antsiranana / Madagascar": (-12.2917, 49.2925),
    "Fianarantsoa / Madagascar": (-21.4522, 47.0856),
    "Mahajanga / Madagascar": (-15.7167, 46.3100),

    # Malawi
    "Lilongwe / Malawi": (-13.9833, 33.7833),
    "Blantyre / Malawi": (-15.7850, 35.0050),
    "Mzuzu / Malawi": (-11.4522, 34.0044),
    "Zomba / Malawi": (-15.3797, 35.3083),
    "Kasungu / Malawi": (-13.0103, 33.4833),

    # Malaysia
    "Kuala Lumpur / Malaysia": (3.1390, 101.6869),
    "Penang / Malaysia": (5.4167, 100.3333),
    "Johor Bahru / Malaysia": (1.4927, 103.7417),
    "Melaka / Malaysia": (2.1897, 102.2504),
    "Kota Kinabalu / Malaysia": (5.9804, 116.0735),

    # Maldives
    "Malé / Maldives": (4.1755, 73.5093),
    "Addu City / Maldives": (-0.6012, 73.1558),
    "Hithadhoo / Maldives": (-0.6000, 73.0833),
    "Fuvahmulah / Maldives": (-0.2810, 73.3978),
    "Kulhudhuffushi / Maldives": (6.6178, 73.4183),

    # Mali
    "Bamako / Mali": (12.6392, -8.0029),
    "Segou / Mali": (13.4300, -6.2700),
    "Mopti / Mali": (14.4742, -5.8592),
    "Sikasso / Mali": (11.2992, -5.6669),
    "Kayes / Mali": (14.4425, -11.4487),

    # Malta
    "Valletta / Malta": (35.8997, 14.5147),
    "Mosta / Malta": (35.8833, 14.4167),
    "Birkirkara / Malta": (35.8936, 14.4744),
    "Mellieha / Malta": (35.9656, 14.3586),
    "Sliema / Malta": (35.9069, 14.5106),

    # Marshall Islands
    "Majuro / Marshall Islands": (7.0606, 171.1901),
    "Ebeye / Marshall Islands": (8.7167, 167.7667),
    "Wotje / Marshall Islands": (8.5016, 169.8725),
    "Aur / Marshall Islands": (7.0955, 169.2696),
    "Kwajalein / Marshall Islands": (9.3958, 167.7350),

    # Mauritania
    "Nouakchott / Mauritania": (18.0761, -15.9807),
    "Nouadhibou / Mauritania": (20.9311, -17.0333),
    "Atar / Mauritania": (20.5200, -13.0333),
    "Kiffa / Mauritania": (16.6236, -11.3833),
    "Rosso / Mauritania": (16.4900, -15.7517),

    # Mauritius
    "Port Louis / Mauritius": (-20.1609, 57.5012),
    "Curepipe / Mauritius": (-20.3143, 57.5100),
    "Vacoas / Mauritius": (-20.3072, 57.4717),
    "Quatre Bornes / Mauritius": (-20.2592, 57.3800),
    "Beau Bassin / Mauritius": (-20.2700, 57.4460),

    # Mexico
    "Mexico City / Mexico": (19.4326, -99.1332),
    "Guadalajara / Mexico": (20.6597, -103.3496),
    "Monterrey / Mexico": (25.6761, -100.3180),
    "Cancún / Mexico": (21.1743, -86.8466),
    "Tijuana / Mexico": (32.5149, -117.0382),

    # Micronesia
    "Palikir / Micronesia": (6.9167, 158.1492),
    "Kolonia / Micronesia": (6.9833, 158.0233),
    "Weno / Micronesia": (7.4317, 151.8490),
    "Tofol / Micronesia": (6.7422, 158.1572),
    "Lelu / Micronesia": (6.9064, 158.2069),

    # Moldova
    "Chișinău / Moldova": (47.0105, 28.8638),
    "Tiraspol / Moldova": (46.8431, 29.6175),
    "Bălți / Moldova": (47.7469, 27.9227),
    "Bender / Moldova": (45.8481, 29.2130),
    "Briceni / Moldova": (48.2944, 26.5350),

    # Monaco
    "Monaco / Monaco": (43.7333, 7.4167),
    "Monte Carlo / Monaco": (43.7333, 7.4167),
    "Moneghetti / Monaco": (43.7273, 7.4194),
    "La Condamine / Monaco": (43.7333, 7.4167),
    "Fontvieille / Monaco": (43.7320, 7.4297),

    # Mongolia
    "Ulaanbaatar / Mongolia": (47.8864, 106.9057),
    "Erdenet / Mongolia": (49.0000, 104.2500),
    "Darkhan / Mongolia": (49.4878, 105.9000),
    "Mörön / Mongolia": (49.6000, 100.1670),
    "Choibalsan / Mongolia": (48.0350, 114.4914),

    # Montenegro
    "Podgorica / Montenegro": (42.4411, 19.2636),
    "Nikšić / Montenegro": (42.7794, 18.9617),
    "Herceg Novi / Montenegro": (42.4572, 18.5361),
    "Bijelo Polje / Montenegro": (43.0333, 19.1333),
    "Pljevlja / Montenegro": (43.3708, 19.3722),

    # Morocco
    "Rabat / Morocco": (34.0209, -6.8416),
    "Casablanca / Morocco": (33.5736, -7.5898),
    "Marrakech / Morocco": (31.6295, -7.9811),
    "Fes / Morocco": (34.0333, -5.0000),
    "Tangier / Morocco": (35.7595, -5.8339),

    # Mozambique
    "Maputo / Mozambique": (-25.9655, 32.5894),
    "Matola / Mozambique": (-25.9636, 32.4583),
    "Beira / Mozambique": (-19.8438, 34.8380),
    "Nampula / Mozambique": (-15.1167, 39.2667),
    "Chimoio / Mozambique": (-19.1641, 33.4908),

    # Myanmar (Burma)
    "Yangon / Myanmar": (16.8661, 96.1953),
    "Mandalay / Myanmar": (21.9747, 96.0836),
    "Naypyidaw / Myanmar": (19.7633, 96.0785),
    "Mawlamyine / Myanmar": (16.4900, 97.6200),
    "Taunggyi / Myanmar": (20.7800, 97.0350),

    # Namibia
    "Windhoek / Namibia": (-22.5597, 17.0836),
    "Swakopmund / Namibia": (-22.6800, 14.5322),
    "Walvis Bay / Namibia": (-22.9576, 14.5051),
    "Oshakati / Namibia": (-17.7833, 15.6406),
    "Rundu / Namibia": (-17.9333, 19.7833),

    # Nauru
    "Yaren / Nauru": (-0.5477, 166.9190),
    "Aiwo / Nauru": (-0.5275, 166.9275),
    "Anabar / Nauru": (-0.4881, 166.9267),
    "Boe / Nauru": (-0.4793, 166.9274),
    "Ewa / Nauru": (-0.5011, 166.9319),

    # Nepal
    "Kathmandu / Nepal": (27.7000, 85.3333),
    "Pokhara / Nepal": (28.2090, 83.9855),
    "Lalitpur / Nepal": (27.6667, 85.3333),
    "Bhaktapur / Nepal": (27.6719, 85.4294),
     "Biratnagar / Nepal": (26.4473, 87.2803),

    # Netherlands
    "Amsterdam / Netherlands": (52.3676, 4.9041),
    "Rotterdam / Netherlands": (51.9225, 4.4792),
    "The Hague / Netherlands": (52.0705, 4.3007),
    "Utrecht / Netherlands": (52.0907, 5.1214),
    "Eindhoven / Netherlands": (51.4416, 5.4697),

    # New Zealand
    "Wellington / New Zealand": (-41.2867, 174.7762),
    "Auckland / New Zealand": (-36.8485, 174.7633),
    "Christchurch / New Zealand": (-43.5321, 172.6362),
    "Hamilton / New Zealand": (-37.7833, 175.2833),
    "Dunedin / New Zealand": (-45.8742, 170.5036),

    # Nicaragua
    "Managua / Nicaragua": (12.1364, -86.2514),
    "Leon / Nicaragua": (12.4300, -86.8786),
    "Granada / Nicaragua": (11.9333, -85.9667),
    "Masaya / Nicaragua": (11.9706, -86.1014),
    "Bluefields / Nicaragua": (12.0000, -83.7500),

    # Niger
    "Niamey / Niger": (13.5123, 2.1128),
    "Maradi / Niger": (13.4611, 7.1000),
    "Zinder / Niger": (13.7833, 8.0000),
    "Agadez / Niger": (16.9700, 7.9833),
    "Tahoua / Niger": (14.9783, 5.2675),

    # Nigeria
    "Abuja / Nigeria": (9.0575, 7.4951),
    "Lagos / Nigeria": (6.5244, 3.3792),
    "Kano / Nigeria": (12.0022, 8.5911),
    "Port Harcourt / Nigeria": (4.7778, 7.0111),
    "Ibadan / Nigeria": (7.3775, 3.8954),

    # North Korea
    "Pyongyang / North Korea": (39.0194, 125.7381),
    "Hamhung / North Korea": (39.9181, 127.5350),
    "Chongjin / North Korea": (41.7744, 129.1917),
    "Wonsan / North Korea": (39.1494, 127.4481),
    "Nampo / North Korea": (38.7367, 125.3569),

    # North Macedonia (Macedonia)
    "Skopje / North Macedonia": (41.9981, 21.4254),
    "Bitola / North Macedonia": (41.0292, 21.3297),
    "Prilep / North Macedonia": (41.3417, 21.5461),
    "Kumanovo / North Macedonia": (42.1333, 21.7167),
    "Ohrid / North Macedonia": (41.1183, 20.8019),

    # Norway
    "Oslo / Norway": (59.9127, 10.7461),
    "Bergen / Norway": (60.3929, 5.3240),
    "Stavanger / Norway": (58.9690, 5.7331),
    "Drammen / Norway": (59.7430, 10.2045),
    "Trondheim / Norway": (63.4305, 10.3951),

    # Oman
    "Muscat / Oman": (23.5880, 58.3829),
    "Salalah / Oman": (17.0061, 54.0922),
    "Sohar / Oman": (24.3667, 56.7000),
    "Nizwa / Oman": (22.9333, 57.5333),
    "Bahla / Oman": (22.9639, 57.3281),

    # Pakistan
    "Islamabad / Pakistan": (33.6844, 73.0479),
    "Karachi / Pakistan": (24.8607, 67.0011),
    "Lahore / Pakistan": (31.5497, 74.3436),
    "Rawalpindi / Pakistan": (33.6844, 73.0479),
    "Faisalabad / Pakistan": (31.4167, 73.0833),

    # Palau
    "Ngerulmud / Palau": (7.5000, 134.6349),
    "Koror / Palau": (7.3286, 134.4750),
    "Melekeok / Palau": (7.4175, 134.6319),
    "Aimeliik / Palau": (7.5486, 134.5936),
    "Angaur / Palau": (6.9931, 134.6339),

    # Panama
    "Panama City / Panama": (8.9824, -79.5199),
    "David / Panama": (8.4281, -82.4326),
    "Colón / Panama": (9.3586, -79.9006),
    "Chitre / Panama": (7.9822, -80.4306),
    "La Chorrera / Panama": (8.8536, -79.7539),

    # Papua New Guinea
    "Port Moresby / Papua New Guinea": (-9.4438, 147.1803),
    "Lae / Papua New Guinea": (-6.7253, 146.9911),
    "Mount Hagen / Papua New Guinea": (-5.8611, 144.2928),
    "Madang / Papua New Guinea": (-5.2072, 145.7881),
    "Rabaul / Papua New Guinea": (-4.1933, 152.2292),

    # Paraguay
    "Asunción / Paraguay": (-25.2637, -57.5759),
    "Ciudad del Este / Paraguay": (-25.5083, -54.6156),
    "Encarnación / Paraguay": (-27.3378, -55.8844),
    "Pedro Juan Caballero / Paraguay": (-22.5486, -55.7497),
    "San Lorenzo / Paraguay": (-25.2892, -57.4814),

    # Peru
    "Lima / Peru": (-12.0464, -77.0428),
    "Arequipa / Peru": (-16.4091, -71.5375),
    "Cusco / Peru": (-13.5310, -71.9782),
    "Trujillo / Peru": (-8.1117, -79.0283),
    "Chiclayo / Peru": (-6.7744, -79.8467),

    # Philippines
    "Manila / Philippines": (14.5995, 120.9842),
    "Quezon City / Philippines": (14.6760, 121.0437),
    "Cebu City / Philippines": (10.3157, 123.8854),
    "Davao City / Philippines": (7.1907, 125.4553),
    "Taguig / Philippines": (14.5354, 121.0509),

    # Poland
    "Warsaw / Poland": (52.2298, 21.0118),
    "Kraków / Poland": (50.0647, 19.9450),
    "Łódź / Poland": (51.7592, 19.4560),
    "Wrocław / Poland": (51.1079, 17.0385),
    "Poznań / Poland": (52.4084, 16.9342),

    # Portugal
    "Lisbon / Portugal": (38.7169, -9.1395),
    "Porto / Portugal": (41.1496, -8.6109),
    "Amadora / Portugal": (38.7453, -9.2322),
    "Braga / Portugal": (41.5503, -8.4242),
    "Coimbra / Portugal": (40.2033, -8.4103),

    # Qatar
    "Doha / Qatar": (25.276987, 55.296249),
    "Al Rayyan / Qatar": (25.2867, 51.5310),
    "Al Khor / Qatar": (25.6850, 51.5278),
    "Umm Salal / Qatar": (25.4094, 51.2406),
    "Mesaieed / Qatar": (24.9781, 51.5561),

    # Romania
    "Bucharest / Romania": (44.4268, 26.1025),
    "Cluj-Napoca / Romania": (46.7709, 23.5897),
    "Timișoara / Romania": (45.7489, 21.2087),
    "Iași / Romania": (47.1585, 27.6014),
    "Constanța / Romania": (44.1598, 28.6348),

    # Russia
    "Moscow / Russia": (55.7558, 37.6176),
    "Saint Petersburg / Russia": (59.9343, 30.3351),
    "Novosibirsk / Russia": (55.0084, 82.9357),
    "Yekaterinburg / Russia": (56.8389, 60.6057),
    "Nizhny Novgorod / Russia": (56.2965, 43.9361),

    # Rwanda
    "Kigali / Rwanda": (-1.9441, 30.0619),
    "Butare / Rwanda": (-2.6000, 29.7500),
    "Gisenyi / Rwanda": (-1.6928, 29.2500),
    "Musanze / Rwanda": (-1.5047, 29.5972),
    "Rubavu / Rwanda": (-1.6864, 29.2386),

    # Saint Kitts and Nevis
    "Basseterre / Saint Kitts and Nevis": (17.2962, -62.7177),
    "Charlestown / Saint Kitts and Nevis": (17.1333, -62.5833),
    "Nevis / Saint Kitts and Nevis": (17.3333, -62.5833),
    "Tabernacle / Saint Kitts and Nevis": (17.2667, -62.7667),

    # Saint Lucia
    "Castries / Saint Lucia": (13.9976, -61.0022),
    "Gros Islet / Saint Lucia": (13.2019, -61.0081),
    "Vieux Fort / Saint Lucia": (13.7450, -61.1457),
    "Soufrière / Saint Lucia": (13.8606, -61.0636),
    "Rodney Bay / Saint Lucia": (13.0533, -61.1994),

    # Saint Vincent and the Grenadines
    "Kingstown / Saint Vincent and the Grenadines": (13.0931, -61.2207),
    "Bequia / Saint Vincent and the Grenadines": (13.2550, -61.2323),
    "Glen / Saint Vincent and the Grenadines": (13.1333, -61.2167),
    "Barrouallie / Saint Vincent and the Grenadines": (13.1833, -61.2733),
    "Calliaqua / Saint Vincent and the Grenadines": (13.1324, -61.1735),

    # Samoa
    "Apia / Samoa": (-13.8310, -172.0600),
    "Faleasiu / Samoa": (-13.9240, -172.1233),
    "Savai'i / Samoa": (-13.5833, -172.4167),
    "Lalomanu / Samoa": (-13.7675, -172.2075),
    "Mulifanua / Samoa": (-13.8347, -172.0669),

    # San Marino
    "City of San Marino / San Marino": (43.9333, 12.4500),
    "Serravalle / San Marino": (43.9333, 12.4833),
    "Acquaviva / San Marino": (43.9333, 12.4833),
    "Borgo Maggiore / San Marino": (43.9333, 12.4667),
    "Domagnano / San Marino": (43.9167, 12.4667),

    # São Tomé and Príncipe
    "São Tomé / São Tomé and Príncipe": (0.3365, 6.7272),
    "Principe / São Tomé and Príncipe": (1.5999, 7.4408),
    "Santana / São Tomé and Príncipe": (0.5833, 6.3500),
    "Trindade / São Tomé and Príncipe": (0.3333, 6.7500),
    "Neves / São Tomé and Príncipe": (0.1833, 6.3667),

    # Saudi Arabia
    "Riyadh / Saudi Arabia": (24.7136, 46.6753),
    "Jeddah / Saudi Arabia": (21.4858, 39.1925),
    "Mecca / Saudi Arabia": (21.4225, 39.8262),
    "Medina / Saudi Arabia": (24.4686, 39.6142),
    "Dammam / Saudi Arabia": (26.4207, 49.9777),

    # Senegal
    "Dakar / Senegal": (14.6928, -17.4467),
    "Touba / Senegal": (14.7675, -15.9908),
    "Thiès / Senegal": (14.7843, -16.9500),
    "Saint-Louis / Senegal": (16.0167, -16.5000),
    "Ziguinchor / Senegal": (12.5833, -16.2833),

    # Serbia
    "Belgrade / Serbia": (44.8176, 20.4633),
    "Novi Sad / Serbia": (45.2671, 19.8335),
    "Niš / Serbia": (43.3209, 21.8954),
    "Kragujevac / Serbia": (44.0167, 20.9167),
    "Subotica / Serbia": (46.1000, 19.6667),

    # Seychelles
    "Victoria / Seychelles": (-4.6167, 55.4500),
    "Praslin / Seychelles": (-4.3333, 55.6667),
    "La Digue / Seychelles": (-4.3333, 55.8333),
    "Bel Ombre / Seychelles": (-4.6172, 55.4047),
    "Anse Royale / Seychelles": (-4.7437, 55.4878),

    # Sierra Leone
    "Freetown / Sierra Leone": (8.4657, -13.2317),
    "Bo / Sierra Leone": (7.9667, -11.7111),
    "Kenema / Sierra Leone": (7.8833, -11.1897),
    "Makeni / Sierra Leone": (8.7167, -12.0500),
    "Kailahun / Sierra Leone": (7.7500, -10.8333),

    # Singapore
    "Singapore / Singapore": (1.2903, 103.8516),
    "Sentosa / Singapore": (1.2494, 103.8300),
    "Jurong / Singapore": (1.3076, 103.7054),
    "Bukit Timah / Singapore": (1.3333, 103.8000),
    "Changi / Singapore": (1.3644, 103.9916),

    # Slovakia
    "Bratislava / Slovakia": (48.1482, 17.1067),
    "Košice / Slovakia": (48.7164, 21.2611),
    "Prešov / Slovakia": (48.9981, 21.2614),
    "Nitra / Slovakia": (48.3083, 18.0875),
    "Trnava / Slovakia": (48.3750, 17.5922),

    # Slovenia
    "Ljubljana / Slovenia": (46.0511, 14.5051),
    "Maribor / Slovenia": (46.5547, 15.6450),
    "Celje / Slovenia": (46.2342, 15.2670),
    "Kranj / Slovenia": (46.2386, 14.3547),
    "Koper / Slovenia": (45.5463, 13.7306),

    # Solomon Islands
    "Honiara / Solomon Islands": (-9.4333, 159.9500),
    "Gizo / Solomon Islands": (-8.1000, 156.8000),
    "Auki / Solomon Islands": (-9.3147, 160.0717),
    "Kira Kira / Solomon Islands": (-10.0500, 161.5500),
    "Kirakira / Solomon Islands": (-10.0500, 161.5500),

    # Somalia
    "Mogadishu / Somalia": (2.0587, 45.3182),
    "Hargeisa / Somalia": (9.5525, 44.0739),
    "Merca / Somalia": (1.8000, 44.1833),
    "Bosaso / Somalia": (11.2897, 49.1817),
    "Kismayo / Somalia": (0.3586, 42.5457),

    # South Africa
    "Pretoria / South Africa": (-25.7460, 28.1881),
    "Cape Town / South Africa": (-33.9249, 18.4241),
    "Durban / South Africa": (-29.8587, 31.0218),
    "Johannesburg / South Africa": (-26.2041, 28.0473),
    "Port Elizabeth / South Africa": (-33.9186, 25.5700),

    # South Korea
    "Seoul / South Korea": (37.5665, 126.9780),
    "Busan / South Korea": (35.1796, 129.0756),
    "Incheon / South Korea": (37.4563, 126.7052),
    "Daegu / South Korea": (35.8714, 128.6014),
    "Daejeon / South Korea": (36.3504, 127.3845),

    # South Sudan
    "Juba / South Sudan": (4.8594, 31.5710),
    "Malakal / South Sudan": (9.5333, 31.6500),
    "Wau / South Sudan": (7.6167, 27.9833),
    "Aweil / South Sudan": (8.7806, 27.3972),
    "Bor / South Sudan": (6.2056, 31.5628),

    # Spain
    "Madrid / Spain": (40.4168, -3.7038),
    "Barcelona / Spain": (41.3884, 2.1914),
    "Seville / Spain": (37.3886, -5.9823),
    "Valencia / Spain": (39.4699, -0.3763),
    "Malaga / Spain": (36.7213, -4.4214),

    # Sri Lanka
    "Colombo / Sri Lanka": (6.9271, 79.8612),
    "Kandy / Sri Lanka": (7.2906, 80.6337),
    "Galle / Sri Lanka": (6.0320, 80.2195),
    "Negombo / Sri Lanka": (7.2082, 79.9753),
    "Jaffna / Sri Lanka": (9.6618, 80.0220),

    # Sudan
    "Khartoum / Sudan": (15.5007, 32.5599),
    "Omdurman / Sudan": (15.6789, 32.5034),
    "Port Sudan / Sudan": (19.6100, 37.2167),
    "Nyala / Sudan": (12.0467, 24.8750),
    "Wad Madani / Sudan": (14.4011, 33.1842),

    # Suriname
    "Paramaribo / Suriname": (5.8660, -55.1761),
    "Nieuw Nickerie / Suriname": (5.9286, -56.0032),
    "Lelydorp / Suriname": (5.6792, -55.2082),
    "Albina / Suriname": (5.7833, -54.1000),
    "Moengo / Suriname": (5.5114, -54.4167),

    # Sweden
    "Stockholm / Sweden": (59.3293, 18.0686),
    "Gothenburg / Sweden": (57.7089, 11.9746),
    "Malmö / Sweden": (55.6049, 13.0038),
    "Uppsala / Sweden": (59.8586, 17.6389),
    "Västerås / Sweden": (59.6091, 16.5440),

    # Switzerland
    "Zurich / Switzerland": (47.3769, 8.5417),
    "Geneva / Switzerland": (46.2044, 6.1432),
    "Basel / Switzerland": (47.5596, 7.5886),
    "Bern / Switzerland": (46.9481, 7.4474),
    "Lucerne / Switzerland": (47.0502, 8.3093),

    # Syria
    "Damascus / Syria": (33.5138, 36.2765),
    "Aleppo / Syria": (36.2028, 37.1343),
    "Homs / Syria": (34.7322, 36.7182),
    "Latakia / Syria": (35.5311, 35.7870),
    "Tartus / Syria": (34.8833, 35.8833),

    # Taiwan
    "Taipei / Taiwan": (25.0330, 121.5654),
    "Kaohsiung / Taiwan": (22.6163, 120.3133),
    "Taichung / Taiwan": (24.1477, 120.6736),
    "Tainan / Taiwan": (22.9999, 120.2270),
    "Keelung / Taiwan": (25.1275, 121.7411),

    # Tajikistan
    "Dushanbe / Tajikistan": (38.5598, 68.7784),
    "Khujand / Tajikistan": (40.2833, 69.6000),
    "Kulob / Tajikistan": (37.8833, 69.7833),
    "Kurgan-Tyube / Tajikistan": (37.8778, 68.7883),
    "Isfara / Tajikistan": (40.0174, 69.6580),

    # Tanzania
    "Dodoma / Tanzania": (-6.1659, 35.7516),
    "Dar es Salaam / Tanzania": (-6.7924, 39.2083),
    "Arusha / Tanzania": (-3.3869, 36.6878),
    "Moshi / Tanzania": (-3.3427, 37.3439),
    "Mbeya / Tanzania": (-8.8999, 33.4611),

    # Thailand
    "Bangkok / Thailand": (13.7563, 100.5018),
    "Chiang Mai / Thailand": (18.7953, 98.9981),
    "Phuket / Thailand": (7.8804, 98.3923),
    "Pattaya / Thailand": (12.9236, 100.8827),
    "Hua Hin / Thailand": (12.5711, 99.9575),

    # Timor-Leste (East Timor)
    "Dili / Timor-Leste": (-8.5569, 125.5603),
    "Baucau / Timor-Leste": (-8.4740, 126.4796),
    "Same / Timor-Leste": (-9.2150, 125.5167),
    "Maliana / Timor-Leste": (-8.5472, 125.4806),
    "Oe-cusse / Timor-Leste": (-9.2000, 124.3000),

    # Togo
    "Lomé / Togo": (6.1375, 1.2125),
    "Sokodé / Togo": (10.3500, 0.6333),
    "Kara / Togo": (9.5500, 1.1833),
    "Atakpamé / Togo": (7.4167, 1.1167),
    "Tsevie / Togo": (6.6667, 1.4000),

    # Tonga
    "Nuku'alofa / Tonga": (-21.1375, -175.2044),
    "Vava'u / Tonga": (-18.6000, -173.9833),
    "Ha'apai / Tonga": (-19.5200, -174.3700),
    "Eua / Tonga": (-21.2500, -175.1500),
    "Neiafu / Tonga": (-18.6333, -173.9833),

    # Trinidad and Tobago
    "Port of Spain / Trinidad and Tobago": (10.6515, -61.2225),
    "San Fernando / Trinidad and Tobago": (10.2833, -61.4611),
    "Scarborough / Trinidad and Tobago": (11.1833, -60.7333),
    "Chaguanas / Trinidad and Tobago": (10.5139, -61.4136),
    "Arima / Trinidad and Tobago": (10.6333, -61.2833),

    # Tunisia
    "Tunis / Tunisia": (36.8065, 10.1815),
    "Sfax / Tunisia": (34.7407, 10.7603),
    "Sousse / Tunisia": (35.8267, 10.6367),
    "Kairouan / Tunisia": (35.6772, 10.0961),
    "Bizerte / Tunisia": (37.2769, 9.8739),

    # Turkey
    "Ankara / Turkey": (39.9334, 32.8597),
    "Istanbul / Turkey": (41.0082, 28.9784),
    "Izmir / Turkey": (38.4192, 27.1287),
    "Antalya / Turkey": (36.8841, 30.7056),
    "Bursa / Turkey": (40.1950, 29.0600),

    # Turkmenistan
    "Ashgabat / Turkmenistan": (37.9601, 58.3790),
    "Mary / Turkmenistan": (37.6000, 61.8350),
    "Turkmenabat / Turkmenistan": (39.0803, 63.5997),
    "Dashoguz / Turkmenistan": (41.8383, 59.9797),
    "Balkanabat / Turkmenistan": (39.5297, 54.3667),

    # Tuvalu
    "Funafuti / Tuvalu": (-7.4800, 179.1944),
    "Fongafale / Tuvalu": (-7.4811, 179.1944),
    "Vaiaku / Tuvalu": (-7.4790, 179.1942),
    "Nanumea / Tuvalu": (-7.2842, 179.1211),
    "Nukufetau / Tuvalu": (-7.4739, 179.1019),

    # Uganda
    "Kampala / Uganda": (0.3136, 32.5812),
    "Entebbe / Uganda": (0.0500, 32.4467),
    "Mbarara / Uganda": (-0.5967, 30.6500),
    "Gulu / Uganda": (2.7747, 32.2993),
    "Mbale / Uganda": (1.0833, 34.1833),

    # Ukraine
    "Kyiv / Ukraine": (50.4501, 30.5236),
    "Lviv / Ukraine": (49.8397, 24.0297),
    "Kharkiv / Ukraine": (49.9935, 36.2304),
    "Odessa / Ukraine": (46.4825, 30.7326),
    "Dnipro / Ukraine": (48.4647, 35.0462),

    # United Arab Emirates
    "Abu Dhabi / United Arab Emirates": (24.4539, 54.3773),
    "Dubai / United Arab Emirates": (25.276987, 55.296249),
    "Sharjah / United Arab Emirates": (25.3372, 55.4128),
    "Ajman / United Arab Emirates": (25.4052, 55.5136),
    "Fujairah / United Arab Emirates": (25.1304, 56.3265),

    # United Kingdom
    "London / United Kingdom": (51.5074, -0.1278),
    "Manchester / United Kingdom": (53.4808, -2.2426),
    "Birmingham / United Kingdom": (52.4862, -1.8904),
    "Liverpool / United Kingdom": (53.4084, -2.9916),
    "Edinburgh / United Kingdom": (55.9533, -3.1883),

    # United States
    "Washington, D.C. / United States": (38.9072, -77.0369),
    "New York / United States": (40.7128, -74.0060),
    "Los Angeles / United States": (34.0522, -118.2437),
    "Chicago / United States": (41.8781, -87.6298),
    "Houston / United States": (29.7604, -95.3698),

    # Uruguay
    "Montevideo / Uruguay": (-34.9011, -56.1645),
    "Salto / Uruguay": (-31.3904, -57.9696),
    "Paysandú / Uruguay": (-32.3200, -58.0797),
    "Maldonado / Uruguay": (-34.9011, -54.9787),
    "Punta del Este / Uruguay": (-34.9587, -54.9602),

    # Uzbekistan
    "Tashkent / Uzbekistan": (41.2995, 69.2401),
    "Samarkand / Uzbekistan": (39.6542, 66.9597),
    "Bukhara / Uzbekistan": (39.7746, 64.4237),
    "Namangan / Uzbekistan": (41.0000, 71.6750),
    "Andijan / Uzbekistan": (40.7833, 72.3333),

    # Vanuatu
    "Port Vila / Vanuatu": (-17.7333, 168.3192),
    "Luganville / Vanuatu": (-15.5000, 167.2000),
    "Tanna / Vanuatu": (-19.5000, 169.3000),
    "Espiritu Santo / Vanuatu": (-15.4250, 167.2000),
    "Malekula / Vanuatu": (-15.7500, 167.8833),

    # Vatican City
    "Vatican City / Vatican City": (41.9029, 12.4534),

    # Venezuela
    "Caracas / Venezuela": (10.4880, -66.8792),
    "Maracaibo / Venezuela": (10.6543, -71.6406),
    "Valencia / Venezuela": (10.1620, -68.0133),
    "Barquisimeto / Venezuela": (10.0730, -69.3028),
    "Margarita Island / Venezuela": (10.9531, -63.8633),

    # Vietnam
    "Hanoi / Vietnam": (21.0285, 105.8542),
    "Ho Chi Minh City / Vietnam": (10.8231, 106.6297),
    "Da Nang / Vietnam": (16.0471, 108.2068),
    "Hai Phong / Vietnam": (20.8449, 106.6889),
    "Can Tho / Vietnam": (10.0303, 105.7835),

    # Yemen
    "Sana'a / Yemen": (15.3694, 44.1910),
    "Aden / Yemen": (12.7797, 45.0066),
    "Taiz / Yemen": (13.5793, 44.0200),
    "Hodeidah / Yemen": (13.0000, 42.9833),
    "Ibb / Yemen": (13.2500, 44.0800),

    # Zambia
    "Lusaka / Zambia": (-15.3875, 28.3228),
    "Ndola / Zambia": (-12.9667, 28.6333),
    "Kitwe / Zambia": (-12.8067, 28.2272),
    "Livingstone / Zambia": (-17.8583, 25.8500),
    "Chingola / Zambia": (-12.5464, 27.8467),

    # Zimbabwe
    "Harare / Zimbabwe": (-17.8292, 31.0522),
    "Bulawayo / Zimbabwe": (-20.1536, 28.5833),
    "Mutare / Zimbabwe": (-18.9714, 32.6500),
    "Gweru / Zimbabwe": (-19.4581, 29.8233),
    "Kwekwe / Zimbabwe": (-18.9667, 29.8197),

}
