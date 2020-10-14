import sys
import csv
from datetime import datetime

elo_teams = ['Aachen', 'Aalen', 'Aberdeen', 'Academica', 'Adanaspor', 'Ahlen', 'Ajaccio', 'Ajax', 'Akhisar',
             'Alanyaspor', 'Alaves', 'Albinoleffe', 'Alkmaar', 'Almeria', 'Amiens', 'Ancona', 'Anderlecht', 'Angers',
             'Ankaraguecue', 'Antalyaspor', 'Antwerp', 'Arles-Avignon', 'Arouca', 'Arsenal', 'Ascoli', 'Aston Villa',
             'Atalanta', 'Atletico', 'Aue', 'Augsburg', 'Auxerre', 'Avellino', 'Aves', 'Barcelona', 'Bari', 'Barnsley',
             'Bastia', 'Bayern', 'Beerschot AC', 'Beira Mar', 'Belenenses', 'Benevento', 'Benfica', 'Bergen',
             'Besiktas', 'Betis', 'Beveren', 'Bielefeld', 'Bilbao', 'Birmingham', 'Blackburn', 'Blackpool', 'Boavista',
             'Bochum', 'Bologna', 'Bolton', 'Bordeaux', 'Boulogne', 'Bournemouth', 'Braga', 'Braunschweig', 'Breda',
             'Brentford', 'Brescia', 'Brest', 'Brighton', 'Bristol City', 'Brugge', 'Bucaspor', 'Bueyueksehir',
             'Burnley', 'Bursaspor', 'Burton', 'CA Bastia', 'Caen', 'Cagliari', 'Cambuur', 'Cardiff', 'Carpi',
             'Catania', 'Celta', 'Celtic', 'Cercle Brugge', 'Cesena', 'Charleroi', 'Charlton', 'Chateauroux', 'Chaves',
             'Chelsea', 'Chievo', 'Cittadella', 'Clermont', 'Como', 'Cordoba', 'Cottbus', 'Coventry', 'Cremonese',
             'Creteil', 'Crotone', 'Crystal Palace', 'Darmstadt', 'De Graafschap', 'Den Haag', 'Denizlispor', 'Depor',
             'Derby', 'Dijon', 'Diyarbakirspor', 'Doncaster', 'Dordrecht', 'Dortmund', 'Dresden', 'Duesseldorf',
             'Duisburg', 'Dundee', 'Dundee United', 'Dunfermline', 'Eibar', 'Elche', 'Empoli', 'Eskisehirspor',
             'Espanyol', 'Estoril', 'Eupen', 'Everton', 'Evian TG', 'Excelsior', 'FSV Frankfurt', 'Falkirk', 'Feirense',
             'Fenerbahce', 'Feyenoord', 'Fiorentina', 'Foggia', 'Frankfurt', 'Freiburg', 'Frosinone', 'Fuerth',
             'Fulham', 'Galatasaray', 'Gallipoli', 'Gaziantepspor', 'Genclerbirligi', 'Genk', 'Genoa', 'Gent', 'Getafe',
             'Gijon', 'Gil Vicente', 'Go Ahead Eagles', 'Granada', 'Grenoble', 'Groningen', 'Grosseto', 'Gubbio',
             'Guimaraes', 'Guingamp', 'Hamburg', 'Hamilton', 'Hannover', 'Hearts', 'Heerenveen', 'Heidenheim',
             'Heracles', 'Hercules', 'Hertha', 'Hibernian', 'Hoffenheim', 'Huddersfield', 'Hull', 'Ingolstadt', 'Inter',
             'Inverness', 'Ipswich', 'Istres', 'Juve Stabia', 'Juventus', 'Karabuekspor', 'Karlsruhe', 'Kasimpasa',
             'Kayseri', 'Kilmarnock', 'Koblenz', 'Koeln', 'Konyaspor', 'Kortrijk', 'Las Palmas', 'Latina', 'Lautern',
             'Laval', 'Lazio', 'Le Havre', 'Le Mans', 'Lecce', 'Leeds', 'Leganes', 'Leicester', 'Leiria', 'Leixoes',
             'Lens', 'Leuven', 'Levante', 'Leverkusen', 'Lierse', 'Lille', 'Liverpool', 'Livorno', 'Lokeren', 'Lorient',
             'Lyon', 'Mainz', 'Malaga', 'Mallorca', 'Man City', 'Man United', 'Manisaspor', 'Mantova', 'Maritimo',
             'Marseille', 'Mechelen', 'Mersin Idman', 'Metz', 'Middlesbrough', 'Milan', 'Millwall', 'Modena', 'Monaco',
             'Montpellier', 'Moreirense', 'Motherwell', 'Mouscron', 'Muenchen 60', 'Nacional', 'Nancy', 'Nantes',
             'Napoli', 'Naval', 'Newcastle', 'Nice', 'Nijmegen', 'Nimes', 'Niort', 'Nocerina', 'Norwich', 'Novara',
             'Nuernberg', 'Oberhausen', 'Olhanense', 'Oostende', 'Orduspor', 'Orleans', 'Osasuna', 'Osnabrueck', 'PSV',
             'Pacos Ferreira', 'Paderborn', 'Padova', 'Palermo', 'Paris FC', 'Paris SG', 'Parma', 'Partick', 'Perugia',
             'Pescara', 'Peterboro', 'Piacenza', 'Pisa', 'Plymouth', 'Portimonense', 'Porto', 'Portogruaro',
             'Portsmouth', 'Preston', 'Pro Vercelli', 'QPR', 'RB Leipzig', 'Rangers', 'Rayo Vallecano', 'Reading',
             'Real Madrid', 'Red Star', 'Regensburg', 'Reggina', 'Reims', 'Rennes', 'Rio Ave', 'Rizespor', 'Roda',
             'Roeselare', 'Roma', 'Ross County', 'Rostock', 'Rotherham', 'Saint-Etienne', 'Salernitana', 'Sampdoria',
             'Samsunspor', 'Sandhausen', 'Santander', 'Sassuolo', 'Schalke', 'Scunthorpe', 'Sedan', 'Setubal',
             'Sevilla', 'Sheffield United', 'Sheffield Weds', 'Siena', 'Sivasspor', 'Sochaux', 'Sociedad',
             'Southampton', 'Spal', 'Sparta Rotterdam', 'Spezia', 'Sporting', 'St Johnstone', 'St Mirren', 'St Pauli',
             'St Truiden', 'Standard', 'Stoke', 'Strasbourg', 'Stuttgart', 'Sunderland', 'Swansea', 'Tenerife',
             'Ternana', 'Tondela', 'Torino', 'Tottenham', 'Toulouse', 'Tours', 'Trabzonspor', 'Trapani', 'Triestina',
             'Troyes', 'Twente', 'Udinese', 'Union Berlin', 'Utrecht', 'Valencia', 'Valenciennes', 'Valladolid',
             'Vannes', 'Varese', 'Venezia', 'Venlo', 'Verona', 'Vicenza', 'Villarreal', 'Virtus Lanciano', 'Vitesse',
             'Waalwijk', 'Watford', 'Werder', 'West Brom', 'West Ham', 'Westerlo', 'Wigan', 'Willem II', 'Wolfsburg',
             'Wolves', 'Xerez', 'Yeovil', 'Zaragoza', 'Zulte Waregem', 'Zwolle']
elo_teams = set(elo_teams)

elo_ratings = dict()
team_elo_map = {'Ajaccio GFCO': 'Ajaccio', 'Albacete': None,
                'Alcorcon': None,
                'Alcoyano': None,
                'Alicante': None,
                'Arezzo': None,
                'Arles': 'Arles-Avignon',
                'Ath Bilbao': 'Bilbao',
                'Ath Bilbao B': None,
                'Ath Madrid': 'Atletico'
    , 'Barcelona B': None,
                'Bayern Munich': 'Bayern',
                'Beziers': None,
                'Bourg Peronnas': None,
                'Burghausen': None,
                'CZ Jena': None,
                'Cadiz': None,
                'Cartagena': None,
                'Castellon': None,
                'Catanzaro': None,
                'Chambly': None,
                'Ciudad de Murcia': None,
                'Colchester': None,
                'Cosenza': None,
                'Crewe': None,
                'Ein Frankfurt': 'Frankfurt',
                'Erzgebirge Aue': 'Aue',
                'Espanol': 'Espanyol',
                'Essen': None,
                'Evian Thonon Gaillard': None,
                'Extremadura UD': None,
                'FC Koln': 'Koeln',
                'Ferrol': None,
                'Fortuna Dusseldorf': 'Duesseldorf',
                'Frankfurt FSV': 'FSV Frankfurt',
                'Fuenlabrada': None,
                'Gimnastic': None,
                'Girona': None,
                'Granada 74': None,
                'Greuther Furth': None,
                'Guadalajara': None,
                'Gueugnon': None,
                'Hansa Rostock': 'Rostock',
                'Holstein Kiel': None,
                'Huesca': None,
                'Jaen': None,
                'Kaiserslautern': 'Lautern',
                'Kaiserslautern ': 'Lautern',
                'La Coruna': 'Depor',
                'Leonesa': None,
                'Libourne': None,
                'Llagostera': None,
                'Lleida': None,
                'Lorca': None,
                'Lugo': None,
                'Luton': None,
                "M'gladbach": 'Gladbach',
                'Magdeburg': None,
                'Malaga B': None,
                'Messina': None,
                'Milton Keynes Dons': None,
                'Mirandes': None,
                'Munich 1860': 'Muenchen 60',
                'Murcia': None,
                "Nott'm Forest": None,
                'Numancia': None,
                'Nurnberg': 'Nuernberg',
                'Offenbach': None,
                'Osnabruck': 'Osnabrueck',
                'Oviedo': None,
                'Poli Ejido': None,
                'Ponferradina': None,
                'Pordenone': None,
                'Quevilly Rouen': None,
                'Ravenna': None,
                'Rayo Majadahonda': None,
                'Real Madrid B': None,
                'Real Union': None,
                'Recreativo': None,
                'Reus Deportiu': None,
                'Rimini': None,
                'Rodez': None,
                'Saarbrucken': None,
                'Sabadell': None,
                'Salamanca': None,
                'Schalke 04': 'Schalke',
                'Sete': None,
                'Sevilla B': None,
                'Siegen': None,
                'Southend': None,
                'Sp Gijon': 'Gijon',
                'St Etienne': 'Saint-Etienne',
                'Treviso': None,
                'UCAM Murcia': None,
                'Unterhaching': None,
                'Vallecano': 'Rayo Vallecano',
                'Vecindario': None,
                'Villarreal B': None,
                'Virtus Entella': None,
                'Wehen': None,
                'Werder Bremen': 'Werder',
                'Wurzburger Kickers': None}

team_fifa_map = {'Aachen': 'Alemannia Aachen',
                 'Aalen': 'VfR Aalen',
                 'Ahlen': 'Rot-Weiß Ahlen',
                 'Ajaccio': 'AC Ajaccio',
                 'Ajaccio GFCO': 'GFC Ajaccio',
                 'Alaves': 'Deportivo Alavés',
                 'Albacete': 'Albacete BP',
                 'Albinoleffe': 'UC AlbinoLeffe',
                 'Alcorcon': 'AD Alcorcón',
                 'Alcoyano': 'CD Alcoyano',
                 'Alicante': 'Alicante CF',
                 'Almeria': 'UD Almería',
                 'Amiens': 'Amiens SC',
                 'Ancona': 'Ancona',
                 'Angers': 'Angers SCO',
                 'Arezzo': 'Arezzo',
                 'Arles': 'AC Arles Avignon',
                 'Arsenal': 'Arsenal',
                 'Ascoli': 'Ascoli',
                 'Aston Villa': 'Aston Villa',
                 'Atalanta': 'Atalanta',
                 'Ath Bilbao': 'Athletic Club de Bilbao',
                 'Ath Bilbao B': 'Bilbao Athletic',
                 'Ath Madrid': 'Atlético Madrid',
                 'Augsburg': 'FC Augsburg',
                 'Auxerre': 'AJ Auxerre',
                 'Avellino': 'Avellino',
                 'Barcelona': 'FC Barcelona',
                 'Barcelona B': 'FC Barcelona B',
                 'Bari': 'Bari',
                 'Barnsley': 'Barnsley',
                 'Bastia': 'Sporting Club de Bastia',
                 'Bayern Munich': 'FC Bayern München',
                 'Benevento': 'Benevento',
                 'Betis': 'Real Betis',
                 'Beziers': 'AS Béziers',
                 'Bielefeld': 'DSC Arminia Bielefeld',
                 'Birmingham': 'Birmingham City',
                 'Blackburn': 'Blackburn Rovers',
                 'Blackpool': 'Blackpool',
                 'Bochum': 'VfL Bochum 1848',
                 'Bologna': 'Bologna',
                 'Bolton': 'Bolton Wanderers',
                 'Bordeaux': 'FC Girondins de Bordeaux',
                 'Boulogne': "US Boulogne Cote D'Opale",
                 'Bourg Peronnas': 'Football Bourg En Bresse Peronnas 01',
                 'Bournemouth': 'Bournemouth',
                 'Braunschweig': 'Eintracht Braunschweig',
                 'Brentford': 'Brentford',
                 'Brescia': 'Brescia',
                 'Brest': 'Stade Brestois 29',
                 'Brighton': 'Brighton & Hove Albion',
                 'Bristol City': 'Bristol City',
                 'Burghausen': 'Wacker Burghausen',
                 'Burnley': 'Burnley',
                 'Burton': 'Burton Albion',
                 'CA Bastia': 'Sporting Club de Bastia',
                 'CZ Jena': 'FC Carl Zeiss Jena',
                 'Cadiz': 'Cádiz CF',
                 'Caen': 'Stade Malherbe Caen',
                 'Cagliari': 'Cagliari',
                 'Cardiff': 'Cardiff City',
                 'Carpi': 'Carpi',
                 'Cartagena': 'FC Cartagena',
                 'Castellon': 'C.D. Castellón',
                 'Catania': 'Catania',
                 'Catanzaro': None,
                 'Celta': 'RC Celta',
                 'Cesena': 'Cesena',
                 'Chambly': 'FC Chambly Oise',
                 'Charlton': 'Charlton Athletic',
                 'Chateauroux': 'La Berrichonne de Châteauroux',
                 'Chelsea': 'Chelsea',
                 'Chievo': 'Chievo Verona',
                 'Cittadella': 'Cittadella',
                 'Ciudad de Murcia': 'CF Ciudad de Murcia',
                 'Clermont': 'Clermont Foot 63',
                 'Colchester': None,
                 'Como': 'Como',
                 'Cordoba': 'Córdoba CF',
                 'Cosenza': 'Cosenza',
                 'Cottbus': 'FC Energie Cottbus',
                 'Coventry': 'Coventry City',
                 'Cremonese': 'US Cremonese',
                 'Creteil': 'US Créteil-Lusitanos',
                 'Crewe': None,
                 'Crotone': 'Crotone',
                 'Crystal Palace': 'Crystal Palace',
                 'Darmstadt': 'SV Darmstadt 98',
                 'Derby': 'Derby County',
                 'Dijon': 'Dijon FCO',
                 'Doncaster': 'Doncaster Rovers',
                 'Dortmund': 'Borussia Dortmund',
                 'Dresden': 'SG Dynamo Dresden',
                 'Duisburg': 'MSV Duisburg',
                 'Eibar': 'SD Eibar',
                 'Ein Frankfurt': 'Eintracht Frankfurt',
                 'Elche': 'Elche CF',
                 'Empoli': 'Empoli',
                 'Erzgebirge Aue': 'FC Erzgebirge Aue',
                 'Espanol': 'RCD Espanyol',
                 'Essen': None,
                 'Everton': 'Everton',
                 'Evian Thonon Gaillard': 'Évian Thonon Gaillard FC',
                 'Extremadura UD': 'Extremadura UD',
                 'FC Koln': 'FC Köln',
                 'Ferrol': 'Racing de Ferrol',
                 'Fiorentina': 'Fiorentina',
                 'Foggia': 'Foggia',
                 'Fortuna Dusseldorf': 'Fortuna Düsseldorf',
                 'Frankfurt FSV': "FSV Frankfurt",
                 'Freiburg': "SC Freiburg",
                 'Frosinone': 'Frosinone',
                 'Fuenlabrada': 'CF Fuenlabrada',
                 'Fulham': 'Fulham',  # CF Fuenlabrada
                 'Gallipoli': 'Gallipoli',
                 'Genoa': 'Genoa',
                 'Getafe': 'Getafe CF',
                 'Gimnastic': 'Gimnàstic de Tarragona',
                 'Girona': 'Girona FC',
                 'Granada': 'Granada CF',
                 'Granada 74': None,
                 'Grenoble': 'Grenoble Foot 38',
                 'Greuther Furth': 'SpVgg Greuther Fürth',
                 'Grosseto': 'Grosseto',
                 'Guadalajara': 'CD Guadalajara',
                 'Gubbio': 'Gubbio',
                 'Gueugnon': 'FC Gueugnon',
                 'Guingamp': 'En Avant de Guingamp',
                 'Hamburg': 'Hamburger SV',
                 'Hannover': 'Hannover 96',
                 'Hansa Rostock': 'FC Hansa Rostock',
                 'Heidenheim': 'FC Heidenheim 1846',
                 'Hercules': 'Hércules CF',
                 'Hertha': 'Hertha BSC',
                 'Hoffenheim': 'TSG 1899 Hoffenheim',
                 'Holstein Kiel': 'Holstein Kiel',
                 'Huddersfield': 'Huddersfield Town',
                 'Huesca': 'SD Huesca',
                 'Hull': 'Hull City',
                 'Ingolstadt': 'FC Ingolstadt 04',
                 'Inter': 'Inter',
                 'Ipswich': 'Ipswich Town',
                 'Istres': 'FC Istres Ouest Provence',
                 'Jaen': 'Real Jaén CF',
                 'Juve Stabia': 'Castellammare di Stabia',
                 'Juventus': 'Juventus',
                 'Kaiserslautern': 'FC Kaiserslautern', 'Kaiserslautern ': 'FC Kaiserslautern',
                 'Karlsruhe': 'Karlsruher SC',
                 'Koblenz': 'TuS Koblenz',
                 'La Coruna': 'Deportivo de La Coruña',
                 'Las Palmas': 'UD Las Palmas',
                 'Latina': 'Latina',
                 'Laval': 'Stade Lavallois Mayenne FC',
                 'Lazio': 'Lazio',
                 'Le Havre': 'Le Havre AC',
                 'Le Mans': 'Le Mans FC',
                 'Lecce': 'Lecce',
                 'Leeds': 'Leeds United',
                 'Leganes': 'CD Leganés',
                 'Leicester': 'Leicester City',
                 'Lens': 'Racing Club de Lens',
                 'Leonesa': 'Cultural Leonesa',
                 'Levante': 'Levante UD',
                 'Leverkusen': 'Bayer 04 Leverkusen',
                 'Libourne': 'FC Libourne-Saint-Seurin',
                 'Lille': 'LOSC Lille',
                 'Liverpool': 'Liverpool',
                 'Livorno': 'Livorno',
                 'Llagostera': 'UE Llagostera',
                 'Lleida': None,
                 'Lorca': 'Lorca FC',
                 'Lorient': 'FC Lorient',
                 'Lugo': 'CD Lugo',
                 'Luton': 'Luton Town',
                 'Lyon': 'Olympique Lyonnais',
                 "M'gladbach": 'Borussia Mönchengladbach',
                 'Magdeburg': 'FC Magdeburg',
                 'Mainz': 'FSV Mainz 05',
                 'Malaga': 'Málaga CF',
                 'Malaga B': None,
                 'Mallorca': 'RCD Mallorca',
                 'Man City': 'Manchester City',
                 'Man United': 'Manchester United',
                 'Mantova': 'Mantova',
                 'Marseille': 'Olympique de Marseille',
                 'Messina': 'Messina',
                 'Metz': 'FC Metz',
                 'Middlesbrough': 'Middlesbrough',
                 'Milan': 'Milan',
                 'Millwall': 'Millwall',
                 'Milton Keynes Dons': 'Milton Keynes Dons',
                 'Mirandes': 'CD Mirandés',
                 'Modena': 'Modena',
                 'Monaco': 'AS Monaco',
                 'Montpellier': 'Montpellier HSC',
                 'Munich 1860': 'TSV 1860 München',
                 'Murcia': 'Real Murcia Club de Fútbol',
                 'Nancy': 'AS Nancy Lorraine',
                 'Nantes': 'FC Nantes',
                 'Napoli': 'Napoli',
                 'Newcastle': 'Newcastle United',
                 'Nice': 'OGC Nice',
                 'Nimes': 'Nîmes Olympique',
                 'Niort': 'Chamois Niortais Football Club',
                 'Nocerina': 'Nocera Inferiore',
                 'Norwich': 'Norwich City',
                 "Nott'm Forest": 'Nottingham Forest',
                 'Novara': 'Novara',
                 'Numancia': 'CD Numancia',
                 'Nurnberg': 'FC Nürnberg',
                 'Oberhausen': 'Rot-Weiß Oberhausen',
                 'Offenbach': 'Kickers Offenbach',
                 'Orleans': 'US Orléans Loiret Football',
                 'Osasuna': 'CA Osasuna',
                 'Osnabruck': 'VfL Osnabrück',
                 'Oviedo': 'Real Oviedo',
                 'Paderborn': 'SC Paderborn 07',
                 'Padova': 'Padova',
                 'Palermo': 'Palermo',
                 'Paris FC': 'Paris FC',
                 'Paris SG': 'Paris Saint-Germain',
                 'Parma': 'Parma',
                 'Perugia': 'Perugia',
                 'Pescara': 'Pescara',
                 'Peterboro': 'Peterborough United',
                 'Piacenza': 'Piacenza',
                 'Pisa': 'Pisa',
                 'Plymouth': ' Plymouth Argyle',
                 'Poli Ejido': 'C.P. Ejido',
                 'Ponferradina': 'SD Ponferradina',
                 'Pordenone': 'Pordenone',
                 'Portogruaro': 'Portogruaro Calcio ASD',
                 'Portsmouth': 'Portsmouth',
                 'Preston': 'Preston North End',
                 'Pro Vercelli': 'FC Pro Vercelli 1892',
                 'QPR': 'Queens Park Rangers',
                 'Quevilly Rouen': 'US Quevilly Rouen Métropole',
                 'RB Leipzig': 'RB Leipzig',
                 'Ravenna': 'Ravenna',
                 'Rayo Majadahonda': 'CF Rayo Majadahonda',
                 'Reading': 'Reading',
                 'Real Madrid': 'Real Madrid',
                 'Real Madrid B': 'Real Madrid Castilla',
                 'Real Union': 'Real Unión Club Irún',
                 'Recreativo': 'RC Recreativo de Huelva',
                 'Red Star': 'Red Star FC',
                 'Regensburg': 'SSV Jahn Regensburg',
                 'Reggina': 'Urbs Reggina 1914',
                 'Reims': 'Stade de Reims',
                 'Rennes': 'Stade Rennais FC',
                 'Reus Deportiu': 'CF Reus Deportiu',
                 'Rimini': 'Rimini',
                 'Rodez': 'Rodez Aveyron Football',
                 'Roma': 'Roma',
                 'Rotherham': 'Rotherham United',
                 'Saarbrucken': None,
                 'Sabadell': 'CE Sabadell FC',
                 'Salamanca': 'UD Salamanca',
                 'Salernitana': 'US Salernitana 1919',
                 'Sampdoria': 'Sampdoria',
                 'Sandhausen': 'SV Sandhausen',
                 'Santander': 'Racing Santander',
                 'Sassuolo': 'Sassuolo',
                 'Schalke 04': 'FC Schalke 04',
                 'Scunthorpe': 'Scunthorpe United',
                 'Sedan': 'CS Sedan Ardennes',
                 'Sete': None,
                 'Sevilla': 'Sevilla FC',
                 'Sevilla B': 'Sevilla Atlético',
                 'Sheffield United': 'Sheffield United',
                 'Sheffield Weds': 'Sheffield Wednesday',
                 'Siegen': None,
                 'Siena': 'Siena',
                 'Sochaux': 'FC Sochaux-Montbéliard',
                 'Sociedad': 'Real Sociedad',
                 'Southampton': 'Southampton',
                 'Southend': 'Southend United',
                 'Sp Gijon': 'Real Sporting de Gijón',
                 'Spal': 'SPAL',
                 'Spezia': 'Spezia',
                 'St Etienne': 'AS Saint-Étienne',
                 'St Pauli': 'FC St. Pauli',
                 'Stoke': 'Stoke City',
                 'Strasbourg': 'RC Strasbourg Alsace',
                 'Stuttgart': 'VfB Stuttgart',
                 'Sunderland': 'Sunderland',
                 'Swansea': 'Swansea City',
                 'Tenerife': 'CD Tenerife',
                 'Ternana': 'Ternana',
                 'Torino': 'Torino',
                 'Tottenham': 'Tottenham Hotspur',
                 'Toulouse': 'Toulouse Football Club',
                 'Tours': 'Tours FC',
                 'Trapani': 'Trapani',
                 'Treviso': 'Treviso',
                 'Triestina': 'Triestina',
                 'Troyes': 'ESTAC Troyes',
                 'UCAM Murcia': 'Real Murcia Club de Fútbol',
                 'Udinese': 'Udinese', 'Union Berlin': 'FC Union Berlin',
                 'Unterhaching': 'pVgg Unterhaching',
                 'Valencia': 'Valencia CF',
                 'Valenciennes': 'Valenciennes FC',
                 'Valladolid': 'Real Valladolid CF',
                 'Vallecano': 'Rayo Vallecano',
                 'Vannes': 'Vannes OC',
                 'Varese': 'Varese',
                 'Vecindario': 'UD Vecindario',
                 'Venezia': 'Venezia FC',
                 'Verona': 'Chievo Verona',
                 'Vicenza': 'Vicenza',
                 'Villarreal': 'Villarreal CF',
                 'Villarreal B': 'Villarreal CF B',
                 'Virtus Entella': 'Virtus Entella',
                 'Virtus Lanciano': 'SS Virtus Lanciano',
                 'Watford': 'Watford',
                 'Wehen': 'SV Wehen Wiesbaden',
                 'Werder Bremen': 'SV Werder Bremen',
                 'West Brom': 'West Bromwich Albion',
                 'West Ham': 'West Ham United',
                 'Wigan': 'Wigan Athletic',
                 'Wolfsburg': 'VfL Wolfsburg',
                 'Wolves': 'Wolverhampton Wanderers',
                 'Wurzburger Kickers': 'FC Würzburger Kickers',
                 'Xerez': 'Xerez Club Deportivo',
                 'Yeovil': 'Yeovil Town', 'Zaragoza': 'Real Zaragoza'}


def change_date_format(date):
    x = date.split('-')
    print(date)
    print(x)
    year = x[0][2:4]
    month = x[1]
    day = x[2]
    return day + '/' + month + '/' + year


with open(r'fifa_data/elo_scores.csv', encoding="utf8", errors='ignore') as elo_file:
    ratings = csv.DictReader(elo_file)
    a = []
    for rating in ratings:
        if rating:
            a.append(rating)
            club = rating['Club']
            data = (float(rating['Elo']), datetime.strptime(rating['From'], '%d/%m/%Y'),
                    datetime.strptime(rating['To'],
                                      '%d/%m/%Y'))
            if club not in elo_ratings:
                elo_ratings[club] = [data]
            else:
                elo_ratings[club].append(data)
    for club in elo_ratings.values():
        club.sort(key=lambda x: x[1])


def find_elo_date(date, elo_ratings):
    # helper function-returns the index of the right elo rating by the dates list
    for i in range(len(elo_ratings)):
        era = elo_ratings[i]
        if i == 0 and date < era[1]:
            return 0
        if era[1] <= date <= era[2]:
            return i


league_names_skip = {'English Premier League (1)', 'French Ligue 1 (1)', 'German 1. Bundesliga (1)',
                     'Italian Serie A (1)', 'Spain Primera Division (1)', 'English League Championship (2)',
                     'French Ligue 2 (2)', 'Italian Serie B (2)', 'German 2. Bundesliga (2)',
                     'Spanish Segunda División (2)'}

fifa_2006_aug_ratings = dict()
fifa_2007_feb_ratings = dict()
fifa_2007_aug_ratings = dict()
fifa_2008_feb_ratings = dict()
fifa_2008_aug_ratings = dict()
fifa_2009_feb_ratings = dict()
fifa_2009_aug_ratings = dict()
fifa_2010_feb_ratings = dict()
fifa_2010_aug_ratings = dict()
fifa_2011_feb_ratings = dict()
fifa_2011_aug_ratings = dict()
fifa_2012_feb_ratings = dict()
fifa_2012_aug_ratings = dict()
fifa_2013_feb_ratings = dict()
fifa_2013_aug_ratings = dict()
fifa_2014_feb_ratings = dict()
fifa_2014_aug_ratings = dict()
fifa_2015_feb_ratings = dict()
fifa_2015_aug_ratings = dict()
fifa_2016_feb_ratings = dict()
fifa_2016_aug_ratings = dict()
fifa_2017_feb_ratings = dict()
fifa_2017_aug_ratings = dict()
fifa_2018_feb_ratings = dict()
fifa_2018_aug_ratings = dict()
fifa_2019_feb_ratings = dict()
fifa_2019_aug_ratings = dict()


# league_names_skip_lst_test = list(league_names_skip)

def fifa_create_ratings(ratings, dates):
    rating_number = []
    names = []
    for rating in ratings:
        rating = rating.strip()
        if rating and rating not in league_names_skip:
            line = rating.split()
            if line[0].isdigit():  # this is a the rating
                rating_number.append(int(line[0]))
            else:
                names.append(rating)
    for i in range(len(rating_number)):
        dates[names[i]] = rating_number[i]


with open(r'fifa_data/fifa_rating_2006_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2006_aug_ratings)

with open(r'fifa_data/fifa_rating_2007_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2007_aug_ratings)

with open(r'fifa_data/fifa_rating_2008_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2008_aug_ratings)

with open(r'fifa_data/fifa_rating_2009_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2009_aug_ratings)

with open(r'fifa_data/fifa_rating_2010_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2010_aug_ratings)

with open(r'fifa_data/fifa_rating_2011_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2011_aug_ratings)

with open(r'fifa_data/fifa_rating_2012_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2012_aug_ratings)

with open(r'fifa_data/fifa_rating_2013_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2013_aug_ratings)

with open(r'fifa_data/fifa_rating_2014_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2014_aug_ratings)

with open(r'fifa_data/fifa_rating_2015_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2015_aug_ratings)

with open(r'fifa_data/fifa_rating_2016_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2016_aug_ratings)

with open(r'fifa_data/fifa_rating_2017_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2017_aug_ratings)

with open(r'fifa_data/fifa_rating_2018_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2018_aug_ratings)

with open(r'fifa_data/fifa_rating_2019_aug.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2019_aug_ratings)

with open(r'fifa_data/fifa_rating_2007_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2007_feb_ratings)

with open(r'fifa_data/fifa_rating_2008_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2008_feb_ratings)

with open(r'fifa_data/fifa_rating_2009_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2009_feb_ratings)

with open(r'fifa_data/fifa_rating_2010_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2010_feb_ratings)

with open(r'fifa_data/fifa_rating_2011_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2011_feb_ratings)

with open(r'fifa_data/fifa_rating_2012_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2012_feb_ratings)

with open(r'fifa_data/fifa_rating_2013_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2013_feb_ratings)

with open(r'fifa_data/fifa_rating_2014_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2014_feb_ratings)

with open(r'fifa_data/fifa_rating_2015_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2015_feb_ratings)

with open(r'fifa_data/fifa_rating_2016_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2016_feb_ratings)

with open(r'fifa_data/fifa_rating_2017_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2017_feb_ratings)

with open(r'fifa_data/fifa_rating_2018_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2018_feb_ratings)

with open(r'fifa_data/fifa_rating_2019_feb.txt', encoding="utf8", errors='ignore') as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2019_feb_ratings)

fifa_ratings_dates = [
    (fifa_2006_aug_ratings, datetime.strptime('01/08/06', '%d/%m/%y')),
    (fifa_2007_feb_ratings, datetime.strptime('01/02/07', '%d/%m/%y')),
    (fifa_2007_aug_ratings, datetime.strptime('01/08/07', '%d/%m/%y')),
    (fifa_2008_feb_ratings, datetime.strptime('01/02/08', '%d/%m/%y')),
    (fifa_2008_aug_ratings, datetime.strptime('01/08/08', '%d/%m/%y')),
    (fifa_2009_feb_ratings, datetime.strptime('01/02/09', '%d/%m/%y')),
    (fifa_2009_aug_ratings, datetime.strptime('01/08/09', '%d/%m/%y')),
    (fifa_2010_feb_ratings, datetime.strptime('01/02/10', '%d/%m/%y')),
    (fifa_2010_aug_ratings, datetime.strptime('01/08/10', '%d/%m/%y')),
    (fifa_2011_feb_ratings, datetime.strptime('01/02/11', '%d/%m/%y')),
    (fifa_2011_aug_ratings, datetime.strptime('01/08/11', '%d/%m/%y')),
    (fifa_2012_feb_ratings, datetime.strptime('01/02/12', '%d/%m/%y')),
    (fifa_2012_aug_ratings, datetime.strptime('01/08/12', '%d/%m/%y')),
    (fifa_2013_feb_ratings, datetime.strptime('01/02/13', '%d/%m/%y')),
    (fifa_2013_aug_ratings, datetime.strptime('01/08/13', '%d/%m/%y')),
    (fifa_2014_feb_ratings, datetime.strptime('01/02/14', '%d/%m/%y')),
    (fifa_2014_aug_ratings, datetime.strptime('01/08/14', '%d/%m/%y')),
    (fifa_2015_feb_ratings, datetime.strptime('01/02/15', '%d/%m/%y')),
    (fifa_2015_aug_ratings, datetime.strptime('01/08/15', '%d/%m/%y')),
    (fifa_2016_feb_ratings, datetime.strptime('01/02/16', '%d/%m/%y')),
    (fifa_2016_aug_ratings, datetime.strptime('01/08/16', '%d/%m/%y')),
    (fifa_2017_feb_ratings, datetime.strptime('01/02/17', '%d/%m/%y')),
    (fifa_2017_aug_ratings, datetime.strptime('01/08/17', '%d/%m/%y')),
    (fifa_2018_feb_ratings, datetime.strptime('01/02/18', '%d/%m/%y')),
    (fifa_2018_aug_ratings, datetime.strptime('01/08/18', '%d/%m/%y')),
    (fifa_2019_feb_ratings, datetime.strptime('01/02/19', '%d/%m/%y')),
    (fifa_2019_aug_ratings, datetime.strptime('01/08/19', '%d/%m/%y'))]


def find_fifa_date(date):
    # helper function-returns the index of the right elo rating by the dates list
    for i in range(len(fifa_ratings_dates)):
        era = fifa_ratings_dates[i]
        if date < era[1]:
            return i - 1
    return len(fifa_ratings_dates) - 1


for num in range(1):
    games = []
    # print(len(sys.argv))
    # print(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        output_file_name = sys.argv[2] + '.csv'
    else:
        file_name = sys.argv[1] + ' ' + sys.argv[2]
        output_file_name = sys.argv[3] + '.csv'
    # print(file_name)
    # print('BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
    # file_name = 'data/I1 (10).csv'
    # output_file_name = '43.csv'
    """print("BUg")
    for r in fifa_ratings_dates:
        print(r)
    print("BUg")
    print("BUg")"""
    with open(file_name, 'r', encoding="utf8", errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            games.append(row)

    games_states = []

    for i, game in enumerate(games):
        if game['Date'] == '':
            continue
        if len(game['Date']) > 8:
            game['Date'] = game['Date'][0:6] + game['Date'][8:]
        game_state = {'Date': datetime.strptime(game['Date'], '%d/%m/%y'), 'HomeTeam': game['HomeTeam'],
                      'AwayTeam': game['AwayTeam'], 'h_played': 0,
                      'h_played_h': 0, 'a_played': 0,
                      'a_played_a': 0, 'h_won': 0, 'h_won_h': 0, 'h_drawn': 0, 'h_drawn_h': 0, 'h_lost': 0,
                      'h_lost_h': 0,
                      'h_points': 0, 'h_points_h': 0, 'h_scored': 0, 'h_scored_h': 0, 'h_conced': 0, 'h_conced_h': 0,
                      'h_clean': 0, 'h_clean_h': 0, 'h_fail': 0, 'h_fail_h': 0,
                      # new from here, home
                      'h_goal_diff': 0, 'h_goal_diff_h': 0,
                      'h_shots': 0, 'h_shots_h': 0, 'h_shots_against': 0, 'h_shots_against_h': 0,
                      'h_shots_target': 0, 'h_shots_target_h': 0, 'h_shots_target_against': 0,
                      'h_shots_target_against_h': 0,
                      'h_shots_diff_h': 0, 'h_shots_diff': 0,
                      'h_shots_target_diff': 0,
                      'h_shots_target_diff_h': 0,
                      # 'h_hit_woodwork': 0, 'h_hit_woodwork_h': 0,
                      # 'h_hit_woodwork_against': 0, 'h_hit_woodwork_diff': 0,
                      'h_red_cards': 0, 'h_red_cards_h': 0,
                      'h_red_cards_against': 0, 'h_red_cards_diff': 0,
                      'h_red_cards_against_h': 0, 'h_red_cards_diff_h': 0,
                      'h_elo': 0, 'h_fifa_rating': 0,
                      'h_current_win_streak': 0, 'h_current_no_lose_streak': 0,
                      'h_current_lose_streak': 0, 'h_current_no_win_streak': 0,
                      'h_last_5_games_points': 0, 'h_last_5_games_wins': 0, 'h_last_5_games_loss': 0,
                      'h_last_5_games_draw': 0, 'h_last_5_games_scored': 0, 'h_last_5_games_conced': 0,
                      'h_last_5_games_goal_diff': 0, 'h_last_5_games_clean': 0, 'h_last_5_games_failed': 0,

                      'a_won': 0, 'a_won_a': 0, 'a_drawn': 0, 'a_drawn_a': 0, 'a_lost': 0, 'a_lost_a': 0,
                      'a_points': 0, 'a_points_a': 0, 'a_scored': 0, 'a_scored_a': 0, 'a_conced': 0, 'a_conced_a': 0,
                      'a_clean': 0, 'a_clean_a': 0, 'a_fail': 0, 'a_fail_a': 0,
                      # new from here: away
                      'a_goal_diff': 0, 'a_goal_diff_a': 0,
                      'a_shots': 0, 'a_shots_a': 0,
                      'a_shots_target': 0, 'a_shots_target_a': 0, 'a_shots_against': 0, 'a_shots_against_a': 0,
                      'a_shots_target_against': 0, 'a_shots_target_against_a': 0,
                      'a_shots_diff': 0,
                      'a_shots_diff_a': 0,
                      'a_shots_target_diff': 0,
                      'a_shots_target_diff_a': 0,
                      # 'a_hit_woodwork': 0, 'a_hit_woodwork_a': 0,
                      # 'a_hit_woodwork_against': 0, 'a_hit_woodwork_diff': 0,
                      # 'a_hit_woodwork_against_a': 0, 'a_hit_woodwork_diff_a': 0,
                      'a_red_cards': 0, 'a_red_cards_a': 0,
                      'a_red_cards_against': 0, 'a_red_cards_diff': 0,
                      'a_red_cards_against_a': 0, 'a_red_cards_diff_a': 0,
                      'a_elo': 0, 'a_fifa_rating': 0,
                      'a_current_win_streak': 0, 'a_current_no_lose_streak': 0,
                      'a_current_lose_streak': 0, 'a_current_no_win_streak': 0,
                      'a_last_5_games_points': 0, 'a_last_5_games_wins': 0, 'a_last_5_games_loss': 0,
                      'a_last_5_games_draw': 0, 'a_last_5_games_scored': 0, 'a_last_5_games_conced': 0,
                      'a_last_5_games_goal_diff': 0, 'a_last_5_games_clean': 0, 'a_last_5_games_failed': 0,

                      'home_goal': game['FTHG'], 'away_goal': game['FTAG'],
                      'home_odd': game['B365H'],
                      'draw_odd': game['B365D'], 'away_odd': game['B365A'],
                      #'home_odd_2': game['LBH'], 'draw_odd_2': game['LBD'], 'away_odd_2': game['LBA'],
                      'home_odd_3': game['WHH'], 'draw_odd_3': game['WHD'], 'away_odd_3': game['WHA'],
                      'RESULT': ''
                      }

        # elo ratings
        dates = ''
        if game['HomeTeam'] in elo_teams:
            dates = elo_ratings[game['HomeTeam']]
        else:
            if team_elo_map[game['HomeTeam']] is not None:
                dates = elo_ratings[team_elo_map[game['HomeTeam']]]
            else:
                dates = -1

        date = datetime.strptime(game['Date'], '%d/%m/%y')

        if dates != -1:
            index = find_elo_date(date, dates)
            game_state['h_elo'] = dates[index][0]
        else:
            game_state['h_elo'] = 1000

        if game['AwayTeam'] in elo_teams:
            dates = elo_ratings[game['AwayTeam']]
        else:
            if team_elo_map[game['AwayTeam']] is not None:
                dates = elo_ratings[team_elo_map[game['AwayTeam']]]
            else:
                dates = -1

        date = datetime.strptime(game['Date'], '%d/%m/%y')
        if dates != -1:
            index = find_elo_date(date, dates)
            game_state['a_elo'] = dates[index][0]
        else:
            game_state['a_elo'] = 1000

        # fifa ratings
        name = team_fifa_map[game['HomeTeam']]
        index = find_fifa_date(date)
        # print(fifa_ratings_dates[index], date, index)
        # print(fifa_ratings_dates[index][0][name])
        fifa_rating = fifa_ratings_dates[index][0][name]
        game_state['h_fifa_rating'] = fifa_rating
        name = team_fifa_map[game['AwayTeam']]
        index = find_fifa_date(date)
        fifa_rating = fifa_ratings_dates[index][0][name]
        game_state['a_fifa_rating'] = fifa_rating

        if game['FTR'] == 'H':
            game_state['RESULT'] = 'HOME'
        if game['FTR'] == 'D':
            game_state['RESULT'] = 'DRAW'
        if game['FTR'] == 'A':
            game_state['RESULT'] = 'AWAY'

        h_last_5_games = []
        a_last_5_games = []

        for j in range(i):
            pre_game = games[j]
            if pre_game['HS'] == '':
                continue
            if pre_game['Date'] == '':
                continue
            if pre_game['HomeTeam'] == game_state['HomeTeam']:
                game_state['h_played'] += 1
                game_state['h_played_h'] += 1

                game_state['h_scored'] += int(pre_game['FTHG'])
                game_state['h_scored_h'] += int(pre_game['FTHG'])
                game_state['h_conced'] += int(pre_game['FTAG'])
                game_state['h_conced_h'] += int(pre_game['FTAG'])
                ###
                game_state['h_shots'] += int(pre_game['HS'])
                game_state['h_shots_h'] += int(pre_game['HS'])
                game_state['h_shots_target'] += int(pre_game['HST'])
                game_state['h_shots_target_h'] += int(pre_game['HST'])
                game_state['h_shots_target_against'] += int(pre_game['AST'])
                game_state['h_shots_target_against_h'] += int(pre_game['AST'])
                ###
                """game_state['h_hit_woodwork'] += int(pre_game['HHW'])
                game_state['h_hit_woodwork_h'] += int(pre_game['HHW'])"""
                ###
                game_state['h_red_cards'] += int(pre_game['HR'])
                game_state['h_red_cards_h'] += int(pre_game['HR'])

                # against
                game_state['h_shots_against'] += int(pre_game['AST'])
                game_state['h_shots_against_h'] += int(pre_game['AST'])
                ###
                game_state['h_red_cards_against'] += int(pre_game['AR'])
                game_state['h_red_cards_against_h'] += int(pre_game['AR'])

                if pre_game['FTR'] == 'H':
                    game_state['h_current_win_streak'] += 1
                    game_state['h_current_no_lose_streak'] += 1
                    game_state['h_current_no_win_streak'] = 0
                    game_state['h_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'D':
                    game_state['h_current_no_win_streak'] += 1
                    game_state['h_current_no_lose_streak'] += 1
                    game_state['h_current_win_streak'] = 0
                    game_state['h_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'A':
                    game_state['h_current_lose_streak'] += 1
                    game_state['h_current_no_win_streak'] += 1
                    game_state['h_current_win_streak'] = 0
                    game_state['h_current_no_lose_streak'] = 0

                if pre_game['FTHG'] == '0':
                    game_state['h_fail'] += 1
                    game_state['h_fail_h'] += 1
                if pre_game['FTAG'] == '0':
                    game_state['h_clean'] += 1
                    game_state['h_clean_h'] += 1

                if pre_game['FTR'] == 'H':
                    game_state['h_won'] += 1
                    game_state['h_won_h'] += 1
                    game_state['h_points'] += 3
                    game_state['h_points_h'] += 3
                if pre_game['FTR'] == 'D':
                    game_state['h_drawn'] += 1
                    game_state['h_drawn_h'] += 1
                    game_state['h_points'] += 1
                    game_state['h_points_h'] += 1
                if pre_game['FTR'] == 'A':
                    game_state['h_lost'] += 1
                    game_state['h_lost_h'] += 1

                h_last_5_games.append(pre_game)
                if h_last_5_games.__len__() > 5:
                    h_last_5_games.pop(0)

            if pre_game['AwayTeam'] == game_state['AwayTeam']:
                game_state['a_played'] += 1
                game_state['a_played_a'] += 1
                game_state['a_scored'] += int(pre_game['FTAG'])
                game_state['a_scored_a'] += int(pre_game['FTAG'])
                game_state['a_conced'] += int(pre_game['FTHG'])
                game_state['a_conced_a'] += int(pre_game['FTHG'])
                ###
                game_state['a_shots'] += int(pre_game['AS'])
                game_state['a_shots_a'] += int(pre_game['AS'])
                game_state['a_shots_target'] += int(pre_game['AST'])
                game_state['a_shots_target_a'] += int(pre_game['AST'])
                game_state['a_shots_target_against'] += int(pre_game['HST'])
                game_state['a_shots_target_against_a'] += int(pre_game['HST'])
                ###
                """game_state['a_hit_woodwork'] += int(pre_game['AHW'])
                game_state['a_hit_woodwork_a'] += int(pre_game['AHW'])"""
                ###
                game_state['a_red_cards'] += int(pre_game['AR'])
                game_state['a_red_cards_a'] += int(pre_game['AR'])

                # against
                game_state['a_shots_against'] += int(pre_game['HST'])
                game_state['a_shots_against_a'] += int(pre_game['HST'])
                ###
                game_state['a_red_cards_against'] += int(pre_game['HR'])
                game_state['a_red_cards_against_a'] += int(pre_game['HR'])

                if pre_game['FTR'] == 'A':
                    game_state['a_current_win_streak'] += 1
                    game_state['a_current_no_lose_streak'] += 1
                    game_state['a_current_no_win_streak'] = 0
                    game_state['a_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'D':
                    game_state['a_current_no_win_streak'] += 1
                    game_state['a_current_no_lose_streak'] += 1
                    game_state['a_current_win_streak'] = 0
                    game_state['a_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'H':
                    game_state['a_current_lose_streak'] += 1
                    game_state['a_current_no_win_streak'] += 1
                    game_state['a_current_win_streak'] = 0
                    game_state['a_current_no_lose_streak'] = 0

                if pre_game['FTAG'] == '0':
                    game_state['a_fail'] += 1
                    game_state['a_fail_a'] += 1
                if pre_game['FTHG'] == '0':
                    game_state['a_clean'] += 1
                    game_state['a_clean_a'] += 1

                if pre_game['FTR'] == 'A':
                    game_state['a_won'] += 1
                    game_state['a_won_a'] += 1
                    game_state['a_points'] += 3
                    game_state['a_points_a'] += 3
                if pre_game['FTR'] == 'D':
                    game_state['a_drawn'] += 1
                    game_state['a_drawn_a'] += 1
                    game_state['a_points'] += 1
                    game_state['a_points_a'] += 1
                if pre_game['FTR'] == 'H':
                    game_state['a_lost'] += 1
                    game_state['a_lost_a'] += 1

                a_last_5_games.append(pre_game)
                if a_last_5_games.__len__() > 5:
                    a_last_5_games.pop(0)

            if pre_game['AwayTeam'] == game_state['HomeTeam']:
                game_state['h_played'] += 1
                game_state['h_scored'] += int(pre_game['FTAG'])
                game_state['h_conced'] += int(pre_game['FTHG'])
                ###
                game_state['h_shots'] += int(pre_game['AS'])
                game_state['h_shots_target'] += int(pre_game['AST'])
                game_state['h_shots_target_against'] += int(pre_game['HST'])
                ###
                """game_state['h_hit_woodwork'] += int(pre_game['AHW'])"""
                ###
                game_state['h_red_cards'] += int(pre_game['AR'])

                # against
                game_state['h_shots_against'] += int(pre_game['HST'])
                ###
                game_state['h_red_cards_against'] += int(pre_game['HR'])

                if pre_game['FTR'] == 'A':
                    game_state['h_current_win_streak'] += 1
                    game_state['h_current_no_lose_streak'] += 1
                    game_state['h_current_no_win_streak'] = 0
                    game_state['h_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'D':
                    game_state['h_current_no_win_streak'] += 1
                    game_state['h_current_no_lose_streak'] += 1
                    game_state['h_current_win_streak'] = 0
                    game_state['h_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'H':
                    game_state['h_current_lose_streak'] += 1
                    game_state['h_current_no_win_streak'] += 1
                    game_state['h_current_win_streak'] = 0
                    game_state['h_current_no_lose_streak'] = 0

                if pre_game['FTAG'] == '0':
                    game_state['h_fail'] += 1
                if pre_game['FTHG'] == '0':
                    game_state['h_clean'] += 1

                if pre_game['FTR'] == 'A':
                    game_state['h_won'] += 1
                    game_state['h_points'] += 3
                if pre_game['FTR'] == 'D':
                    game_state['h_drawn'] += 1
                    game_state['h_points'] += 1
                if pre_game['FTR'] == 'H':
                    game_state['h_lost'] += 1

                h_last_5_games.append(pre_game)
                if h_last_5_games.__len__() > 5:
                    h_last_5_games.pop(0)

            if pre_game['HomeTeam'] == game_state['AwayTeam']:
                game_state['a_played'] += 1
                game_state['a_scored'] += int(pre_game['FTHG'])
                game_state['a_conced'] += int(pre_game['FTAG'])
                ###
                game_state['a_shots'] += int(pre_game['HS'])
                game_state['a_shots_target'] += int(pre_game['HST'])
                game_state['a_shots_target_against'] += int(pre_game['AST'])
                ###
                """game_state['a_hit_woodwork'] += int(pre_game['HHW'])"""
                ###

                # against
                game_state['a_shots_against'] += int(pre_game['AST'])
                ###
                game_state['a_red_cards_against'] += int(pre_game['AR'])

                if pre_game['FTR'] == 'H':
                    game_state['a_current_win_streak'] += 1
                    game_state['a_current_no_lose_streak'] += 1
                    game_state['a_current_no_win_streak'] = 0
                    game_state['a_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'D':
                    game_state['a_current_no_win_streak'] += 1
                    game_state['a_current_no_lose_streak'] += 1
                    game_state['a_current_win_streak'] = 0
                    game_state['a_current_lose_streak'] = 0
                elif pre_game['FTR'] == 'A':
                    game_state['a_current_lose_streak'] += 1
                    game_state['a_current_no_win_streak'] += 1
                    game_state['a_current_win_streak'] = 0
                    game_state['a_current_no_lose_streak'] = 0

                if pre_game['FTHG'] == '0':
                    game_state['a_fail'] += 1
                if pre_game['FTAG'] == '0':
                    game_state['a_clean'] += 1

                if pre_game['FTR'] == 'H':
                    game_state['a_won'] += 1
                    game_state['a_points'] += 3
                if pre_game['FTR'] == 'D':
                    game_state['a_drawn'] += 1
                    game_state['a_points'] += 1
                if pre_game['FTR'] == 'A':
                    game_state['a_lost'] += 1

                a_last_5_games.append(pre_game)
                if a_last_5_games.__len__() > 5:
                    a_last_5_games.pop(0)
        # diff
        # HOME
        ### scored diff
        game_state['h_goal_diff'] = game_state['h_scored'] - game_state['h_conced']
        game_state['h_goal_diff_h'] = game_state['h_scored_h'] - game_state['h_conced_h']
        ### shots diff
        game_state['h_shots_diff'] = game_state['h_shots'] - game_state['h_shots_against']
        game_state['h_shots_diff_h'] = game_state['h_shots_h'] - game_state['h_shots_against_h']
        game_state['h_shots_target_diff'] = game_state['h_shots_target'] - game_state['h_shots_target_against']
        game_state['h_shots_target_diff_h'] = game_state['h_shots_target_h'] - game_state['h_shots_target_against_h']
        ### red cards diff
        game_state['h_red_cards_diff'] = game_state['h_red_cards'] - game_state['h_red_cards_against']
        game_state['h_red_cards_diff_h'] = game_state['h_red_cards_h'] - game_state['h_red_cards_against_h']

        # AWAY
        game_state['a_goal_diff'] += game_state['a_scored'] - game_state['a_conced']
        game_state['a_goal_diff_a'] += game_state['a_scored_a'] - game_state['a_conced_a']
        ###shots diff
        game_state['a_shots_diff'] += game_state['a_shots'] - game_state['a_shots_against']
        game_state['a_shots_diff_a'] += game_state['a_shots_a'] - game_state['a_shots_against_a']
        game_state['a_shots_target_diff'] = game_state['a_shots_target'] - game_state['a_shots_target_against']
        game_state['a_shots_target_diff_a'] = game_state['a_shots_target_a'] - game_state['a_shots_target_against_a']
        ### red cards diff
        game_state['a_red_cards_diff'] += game_state['a_red_cards'] - game_state['a_red_cards_against']
        game_state['a_red_cards_diff_a'] += game_state['a_red_cards_a'] - game_state['a_red_cards_against_a']

        for last_h, last_a in zip(h_last_5_games, a_last_5_games):
            # HOME
            if last_h['HomeTeam'] == game_state['HomeTeam']:
                # points
                if last_h['FTR'] == 'H':
                    game_state['h_last_5_games_points'] += 3
                    game_state['h_last_5_games_wins'] += 1
                elif last_h['FTR'] == 'D':
                    game_state['h_last_5_games_points'] += 1
                    game_state['h_last_5_games_draw'] += 1
                elif last_h['FTR'] == 'A':
                    game_state['h_last_5_games_loss'] += 1
                # goals
                game_state['h_last_5_games_scored'] += int(last_h['FTHG'])
                game_state['h_last_5_games_conced'] += int(last_h['FTAG'])
                if last_h['FTHG'] == '0':
                    game_state['h_last_5_games_failed'] += 1
                if last_h['FTAG'] == '0':
                    game_state['h_last_5_games_clean'] += 1
            else:
                # points
                if last_h['FTR'] == 'A':
                    game_state['h_last_5_games_points'] += 3
                    game_state['h_last_5_games_wins'] += 1
                elif last_h['FTR'] == 'D':
                    game_state['h_last_5_games_points'] += 1
                    game_state['h_last_5_games_draw'] += 1
                elif last_h['FTR'] == 'H':
                    game_state['h_last_5_games_loss'] += 1
                # goals
                game_state['h_last_5_games_scored'] += int(last_h['FTAG'])
                game_state['h_last_5_games_conced'] += int(last_h['FTHG'])
                if last_h['FTAG'] == '0':
                    game_state['h_last_5_games_failed'] += 1
                if last_h['FTHG'] == '0':
                    game_state['h_last_5_games_clean'] += 1
            # AWAY
            if last_a['AwayTeam'] == game_state['AwayTeam']:
                # points
                if last_a['FTR'] == 'A':
                    game_state['a_last_5_games_points'] += 3
                    game_state['a_last_5_games_wins'] += 1
                elif last_a['FTR'] == 'D':
                    game_state['a_last_5_games_points'] += 1
                    game_state['a_last_5_games_draw'] += 1
                elif last_a['FTR'] == 'H':
                    game_state['a_last_5_games_loss'] += 1
                # goals
                game_state['a_last_5_games_scored'] += int(last_h['FTAG'])
                game_state['a_last_5_games_conced'] += int(last_h['FTHG'])
                if last_a['FTAG'] == '0':
                    game_state['a_last_5_games_failed'] += 1
                if last_a['FTHG'] == '0':
                    game_state['a_last_5_games_clean'] += 1
            else:
                # points
                if last_a['FTR'] == 'H':
                    game_state['a_last_5_games_points'] += 3
                    game_state['a_last_5_games_wins'] += 1
                elif last_a['FTR'] == 'D':
                    game_state['a_last_5_games_points'] += 1
                    game_state['a_last_5_games_draw'] += 1
                elif last_a['FTR'] == 'A':
                    game_state['a_last_5_games_loss'] += 1
                # goals
                game_state['a_last_5_games_scored'] += int(last_h['FTHG'])
                game_state['a_last_5_games_conced'] += int(last_h['FTAG'])
                if last_a['FTHG'] == 0:
                    game_state['a_last_5_games_failed'] += 1
                if last_a['FTAG'] == 0:
                    game_state['a_last_5_games_clean'] += 1
        game_state['h_last_5_games_goal_diff'] += game_state['h_last_5_games_scored'] - game_state[
            'h_last_5_games_conced']
        game_state['a_last_5_games_goal_diff'] += game_state['a_last_5_games_scored'] - game_state[
            'a_last_5_games_conced']

        games_states.append(game_state)

    with open(output_file_name, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'HomeTeam', 'AwayTeam', 'h_played', 'h_played_h', 'a_played',
                      'a_played_a', 'h_won', 'h_won_h', 'h_drawn', 'h_drawn_h', 'h_lost', 'h_lost_h',
                      'h_points', 'h_points_h', 'h_scored', 'h_scored_h', 'h_conced', 'h_conced_h',
                      'h_clean', 'h_clean_h', 'h_fail', 'h_fail_h',

                      # new
                      'h_goal_diff', 'h_goal_diff_h',
                      'h_shots', 'h_shots_h', 'h_shots_against', 'h_shots_against_h',
                      'h_shots_target', 'h_shots_target_h', 'h_shots_target_against', 'h_shots_target_against_h',
                      'h_shots_diff_h', 'h_shots_diff',
                      'h_shots_target_diff',
                      'h_shots_target_diff_h',

                      # 'h_hit_woodwork', 'h_hit_woodwork_h',
                      # 'h_hit_woodwork_against', 'h_hit_woodwork_diff',
                      'h_red_cards', 'h_red_cards_h',
                      'h_red_cards_against', 'h_red_cards_diff',
                      'h_red_cards_against_h', 'h_red_cards_diff_h',
                      'h_elo', 'h_fifa_rating',
                      'h_current_win_streak', 'h_current_no_lose_streak',
                      'h_current_lose_streak', 'h_current_no_win_streak',
                      'h_last_5_games_points', 'h_last_5_games_wins', 'h_last_5_games_loss',
                      'h_last_5_games_draw', 'h_last_5_games_scored', 'h_last_5_games_conced',
                      'h_last_5_games_goal_diff', 'h_last_5_games_clean', 'h_last_5_games_failed',

                      'a_won', 'a_won_a', 'a_drawn', 'a_drawn_a', 'a_lost', 'a_lost_a',
                      'a_points', 'a_points_a', 'a_scored', 'a_scored_a', 'a_conced', 'a_conced_a',
                      'a_clean', 'a_clean_a', 'a_fail', 'a_fail_a',

                      # new
                      'a_goal_diff', 'a_goal_diff_a',
                      'a_shots', 'a_shots_a', 'a_shots_against', 'a_shots_against_a',
                      'a_shots_target', 'a_shots_target_a', 'a_shots_target_against', 'a_shots_target_against_a',
                      'a_shots_diff_a', 'a_shots_diff',
                      'a_shots_target_diff',
                      'a_shots_target_diff_a',
                      # 'a_hit_woodwork', 'a_hit_woodwork_a',
                      # 'a_hit_woodwork_against', 'a_hit_woodwork_diff',
                      'a_red_cards', 'a_red_cards_a',
                      'a_red_cards_against', 'a_red_cards_diff',
                      'a_red_cards_against_a', 'a_red_cards_diff_a',
                      'a_elo', 'a_fifa_rating',
                      'a_current_win_streak', 'a_current_no_lose_streak',
                      'a_current_lose_streak', 'a_current_no_win_streak',
                      'a_last_5_games_points', 'a_last_5_games_wins', 'a_last_5_games_loss',
                      'a_last_5_games_draw', 'a_last_5_games_scored', 'a_last_5_games_conced',
                      'a_last_5_games_goal_diff', 'a_last_5_games_clean', 'a_last_5_games_failed',

                      'home_goal', 'away_goal',
                      'home_odd',
                      'draw_odd', 'away_odd',
                      #'home_odd_2', 'draw_odd_2', 'away_odd_2',
                      'home_odd_3', 'draw_odd_3', 'away_odd_3',
                      'RESULT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for game_state in games_states:
            writer.writerow(
                {'Date': game_state['Date'], 'HomeTeam': game_state['HomeTeam'], 'AwayTeam': game_state['AwayTeam'],
                 'h_played': game_state['h_played'], 'h_played_h': game_state['h_played_h'],
                 'a_played': game_state['a_played'],
                 'a_played_a': game_state['a_played_a'], 'h_won': game_state['h_won'], 'h_won_h': game_state['h_won_h'],
                 'h_drawn': game_state['h_drawn'], 'h_drawn_h': game_state['h_drawn_h'], 'h_lost': game_state['h_lost'],
                 'h_lost_h': game_state['h_lost_h'], 'h_points': game_state['h_points'],
                 'h_points_h': game_state['h_points_h'],
                 'h_scored': game_state['h_scored'], 'h_scored_h': game_state['h_scored_h'],
                 'h_conced': game_state['h_conced'],
                 'h_conced_h': game_state['h_conced_h'], 'h_clean': game_state['h_clean'],
                 'h_clean_h': game_state['h_clean_h'],
                 'h_fail': game_state['h_fail'], 'h_fail_h': game_state['h_fail_h'],
                 # new away
                 # goals
                 'h_goal_diff': game_state['h_goal_diff'],
                 'h_goal_diff_h': game_state['h_goal_diff_h'],

                 'h_shots': game_state['h_shots'], 'h_shots_h': game_state['h_scored_h'],
                 'h_shots_against': game_state['h_shots_against'], 'h_shots_against_h': game_state['h_shots_against_h'],
                 'h_shots_target': game_state['h_shots_target'], 'h_shots_target_h': game_state['h_shots_target_h'],
                 'h_shots_diff_h': game_state['h_shots_diff_h'], 'h_shots_diff': game_state['h_shots_diff'],
                 'h_shots_target_against': game_state['h_shots_target_against'],
                 'h_shots_target_against_h': game_state['h_shots_target_against_h'],
                 'h_shots_target_diff': game_state['h_shots_target_diff'],
                 'h_shots_target_diff_h': game_state['h_shots_target_diff_h'],
                 # hit woodwork
                 # 'h_hit_woodwork': game_state['h_hit_woodwork'],
                 # 'h_hit_woodwork_h': game_state['h_hit_woodwork_h'],
                 # 'h_hit_woodwork_against': game_state['h_hit_woodwork_against'],
                 # 'h_hit_woodwork_diff': game_state['h_hit_woodwork_diff'],
                 # cards
                 'h_red_cards': game_state['h_red_cards'], 'h_red_cards_h': game_state['h_red_cards_h'],
                 'h_red_cards_against': game_state['h_red_cards_against'],
                 'h_red_cards_diff': game_state['h_red_cards_diff'],
                 'h_red_cards_against_h': game_state['h_red_cards_against_h'],
                 'h_red_cards_diff_h': game_state['h_red_cards_diff_h'],
                 # ranking
                 'h_elo': game_state['h_elo'], 'h_fifa_rating': game_state['h_fifa_rating'],
                 # streaks
                 'h_current_win_streak': game_state['h_current_win_streak'],
                 'h_current_no_lose_streak': game_state['h_current_no_lose_streak'],
                 'h_current_lose_streak': game_state['h_current_lose_streak'],
                 'h_current_no_win_streak': game_state['h_current_no_win_streak'],
                 # last status
                 'h_last_5_games_points': game_state['h_last_5_games_points'],
                 'h_last_5_games_wins': game_state['h_last_5_games_wins'],
                 'h_last_5_games_loss': game_state['h_last_5_games_loss'],
                 'h_last_5_games_draw': game_state['h_last_5_games_draw'],
                 'h_last_5_games_scored': game_state['h_last_5_games_scored'],
                 'h_last_5_games_conced': game_state['h_last_5_games_conced'],
                 'h_last_5_games_goal_diff': game_state['h_last_5_games_goal_diff'],
                 'h_last_5_games_clean': game_state['h_last_5_games_clean'],
                 'h_last_5_games_failed': game_state['h_last_5_games_failed'],

                 'a_won': game_state['a_won'],
                 'a_won_a': game_state['a_won_a'], 'a_drawn': game_state['a_drawn'],
                 'a_drawn_a': game_state['a_drawn_a'],
                 'a_lost': game_state['a_lost'], 'a_lost_a': game_state['a_lost_a'], 'a_points': game_state['a_points'],
                 'a_points_a': game_state['a_points_a'], 'a_scored': game_state['a_scored'],
                 'a_scored_a': game_state['a_scored_a'],
                 'a_conced': game_state['a_conced'], 'a_conced_a': game_state['a_conced_a'],
                 'a_clean': game_state['a_clean'],
                 'a_clean_a': game_state['a_clean_a'], 'a_fail': game_state['a_fail'],
                 'a_fail_a': game_state['a_fail_a'],
                 # new away
                 # goals
                 'a_goal_diff': game_state['a_goal_diff'], 'a_goal_diff_a': game_state['a_goal_diff_a'],
                 # shots
                 'a_shots': game_state['a_shots'], 'a_shots_a': game_state['a_shots_a'],
                 'a_shots_against': game_state['a_shots_against'],
                 'a_shots_against_a': game_state['a_shots_against_a'],
                 'a_shots_target': game_state['a_shots_target'], 'a_shots_target_a': game_state['a_shots_target_a'],
                 'a_shots_diff_a': game_state['a_shots_diff_a'], 'a_shots_diff': game_state['a_shots_diff'],
                 'a_shots_target_against': game_state['a_shots_target_against'],
                 'a_shots_target_against_a': game_state['a_shots_target_against_a'],
                 'a_shots_target_diff': game_state['a_shots_target_diff'],
                 'a_shots_target_diff_a': game_state['a_shots_target_diff_a'],
                 # hit woodwork
                 # 'a_hit_woodwork': game_state['a_hit_woodwork'],
                 # 'a_hit_woodwork_a': game_state['a_hit_woodwork_a'],
                 # 'a_hit_woodwork_against': game_state['a_hit_woodwork_against'],
                 # 'a_hit_woodwork_diff': game_state['a_hit_woodwork_diff'],
                 # cards
                 'a_red_cards': game_state['a_red_cards'], 'a_red_cards_a': game_state['a_red_cards_a'],
                 'a_red_cards_against': game_state['a_red_cards_against'],
                 'a_red_cards_diff': game_state['a_red_cards_diff'],
                 'a_red_cards_against_a': game_state['a_red_cards_against_a'],
                 'a_red_cards_diff_a': game_state['a_red_cards_diff_a'],
                 # ranking
                 'a_elo': game_state['a_elo'], 'a_fifa_rating': game_state['a_fifa_rating'],
                 # streaks
                 'a_current_win_streak': game_state['a_current_win_streak'],
                 'a_current_no_lose_streak': game_state['a_current_no_lose_streak'],
                 'a_current_lose_streak': game_state['a_current_lose_streak'],
                 'a_current_no_win_streak': game_state['a_current_no_win_streak'],
                 # last status
                 'a_last_5_games_points': game_state['a_last_5_games_points'],
                 'a_last_5_games_wins': game_state['a_last_5_games_wins'],
                 'a_last_5_games_loss': game_state['a_last_5_games_loss'],
                 'a_last_5_games_draw': game_state['a_last_5_games_draw'],
                 'a_last_5_games_scored': game_state['a_last_5_games_scored'],
                 'a_last_5_games_conced': game_state['a_last_5_games_conced'],
                 'a_last_5_games_goal_diff': game_state['a_last_5_games_goal_diff'],
                 'a_last_5_games_clean': game_state['a_last_5_games_clean'],
                 'a_last_5_games_failed': game_state['a_last_5_games_failed'],
                 # odds
                 'home_goal': game_state['home_goal'], 'away_goal': game_state['away_goal'],
                 'home_odd': game_state['home_odd'], 'draw_odd': game_state['draw_odd'],
                 'away_odd': game_state['away_odd'],
                 # 'home_odd_2': game_state['home_odd_2'], 'draw_odd_2': game_state['draw_odd_2'],
                 # 'away_odd_2': game_state['away_odd_2'],
                 'home_odd_3': game_state['home_odd_3'], 'draw_odd_3': game_state['draw_odd_3'],
                 'away_odd_3': game_state['away_odd_3'],
                 'RESULT': game_state['RESULT']})
