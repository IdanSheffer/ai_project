import sys
import csv


elo_teams = ['Aachen', 'Aalen', 'Aberdeen', 'Academica', 'Adanaspor', 'Ahlen', 'Ajaccio', 'Ajax', 'Akhisar', 'Alanyaspor', 'Alaves', 'Albinoleffe', 'Alkmaar', 'Almeria', 'Amiens', 'Ancona', 'Anderlecht', 'Angers', 'Ankaraguecue', 'Antalyaspor', 'Antwerp', 'Arles-Avignon', 'Arouca', 'Arsenal', 'Ascoli', 'Aston Villa', 'Atalanta', 'Atletico', 'Aue', 'Augsburg', 'Auxerre', 'Avellino', 'Aves', 'Barcelona', 'Bari', 'Barnsley', 'Bastia', 'Bayern', 'Beerschot AC', 'Beira Mar', 'Belenenses', 'Benevento', 'Benfica', 'Bergen', 'Besiktas', 'Betis', 'Beveren', 'Bielefeld', 'Bilbao', 'Birmingham', 'Blackburn', 'Blackpool', 'Boavista', 'Bochum', 'Bologna', 'Bolton', 'Bordeaux', 'Boulogne', 'Bournemouth', 'Braga', 'Braunschweig', 'Breda', 'Brentford', 'Brescia', 'Brest', 'Brighton', 'Bristol City', 'Brugge', 'Bucaspor', 'Bueyueksehir', 'Burnley', 'Bursaspor', 'Burton', 'CA Bastia', 'Caen', 'Cagliari', 'Cambuur', 'Cardiff', 'Carpi', 'Catania', 'Celta', 'Celtic', 'Cercle Brugge', 'Cesena', 'Charleroi', 'Charlton', 'Chateauroux', 'Chaves', 'Chelsea', 'Chievo', 'Cittadella', 'Clermont', 'Como', 'Cordoba', 'Cottbus', 'Coventry', 'Cremonese', 'Creteil', 'Crotone', 'Crystal Palace', 'Darmstadt', 'De Graafschap', 'Den Haag', 'Denizlispor', 'Depor', 'Derby', 'Dijon', 'Diyarbakirspor', 'Doncaster', 'Dordrecht', 'Dortmund', 'Dresden', 'Duesseldorf', 'Duisburg', 'Dundee', 'Dundee United', 'Dunfermline', 'Eibar', 'Elche', 'Empoli', 'Eskisehirspor', 'Espanyol', 'Estoril', 'Eupen', 'Everton', 'Evian TG', 'Excelsior', 'FSV Frankfurt', 'Falkirk', 'Feirense', 'Fenerbahce', 'Feyenoord', 'Fiorentina', 'Foggia', 'Frankfurt', 'Freiburg', 'Frosinone', 'Fuerth', 'Fulham', 'Galatasaray', 'Gallipoli', 'Gaziantepspor', 'Genclerbirligi', 'Genk', 'Genoa', 'Gent', 'Getafe', 'Gijon', 'Gil Vicente', 'Go Ahead Eagles', 'Granada', 'Grenoble', 'Groningen', 'Grosseto', 'Gubbio', 'Guimaraes', 'Guingamp', 'Hamburg', 'Hamilton', 'Hannover', 'Hearts', 'Heerenveen', 'Heidenheim', 'Heracles', 'Hercules', 'Hertha', 'Hibernian', 'Hoffenheim', 'Huddersfield', 'Hull', 'Ingolstadt', 'Inter', 'Inverness', 'Ipswich', 'Istres', 'Juve Stabia', 'Juventus', 'Karabuekspor', 'Karlsruhe', 'Kasimpasa', 'Kayseri', 'Kilmarnock', 'Koblenz', 'Koeln', 'Konyaspor', 'Kortrijk', 'Las Palmas', 'Latina', 'Lautern', 'Laval', 'Lazio', 'Le Havre', 'Le Mans', 'Lecce', 'Leeds', 'Leganes', 'Leicester', 'Leiria', 'Leixoes', 'Lens', 'Leuven', 'Levante', 'Leverkusen', 'Lierse', 'Lille', 'Liverpool', 'Livorno', 'Lokeren', 'Lorient', 'Lyon', 'Mainz', 'Malaga', 'Mallorca', 'Man City', 'Man United', 'Manisaspor', 'Mantova', 'Maritimo', 'Marseille', 'Mechelen', 'Mersin Idman', 'Metz', 'Middlesbrough', 'Milan', 'Millwall', 'Modena', 'Monaco', 'Montpellier', 'Moreirense', 'Motherwell', 'Mouscron', 'Muenchen 60', 'Nacional', 'Nancy', 'Nantes', 'Napoli', 'Naval', 'Newcastle', 'Nice', 'Nijmegen', 'Nimes', 'Niort', 'Nocerina', 'Norwich', 'Novara', 'Nuernberg', 'Oberhausen', 'Olhanense', 'Oostende', 'Orduspor', 'Orleans', 'Osasuna', 'Osnabrueck', 'PSV', 'Pacos Ferreira', 'Paderborn', 'Padova', 'Palermo', 'Paris FC', 'Paris SG', 'Parma', 'Partick', 'Perugia', 'Pescara', 'Peterboro', 'Piacenza', 'Pisa', 'Plymouth', 'Portimonense', 'Porto', 'Portogruaro', 'Portsmouth', 'Preston', 'Pro Vercelli', 'QPR', 'RB Leipzig', 'Rangers', 'Rayo Vallecano', 'Reading', 'Real Madrid', 'Red Star', 'Regensburg', 'Reggina', 'Reims', 'Rennes', 'Rio Ave', 'Rizespor', 'Roda', 'Roeselare', 'Roma', 'Ross County', 'Rostock', 'Rotherham', 'Saint-Etienne', 'Salernitana', 'Sampdoria', 'Samsunspor', 'Sandhausen', 'Santander', 'Sassuolo', 'Schalke', 'Scunthorpe', 'Sedan', 'Setubal', 'Sevilla', 'Sheffield United', 'Sheffield Weds', 'Siena', 'Sivasspor', 'Sochaux', 'Sociedad', 'Southampton', 'Spal', 'Sparta Rotterdam', 'Spezia', 'Sporting', 'St Johnstone', 'St Mirren', 'St Pauli', 'St Truiden', 'Standard', 'Stoke', 'Strasbourg', 'Stuttgart', 'Sunderland', 'Swansea', 'Tenerife', 'Ternana', 'Tondela', 'Torino', 'Tottenham', 'Toulouse', 'Tours', 'Trabzonspor', 'Trapani', 'Triestina', 'Troyes', 'Twente', 'Udinese', 'Union Berlin', 'Utrecht', 'Valencia', 'Valenciennes', 'Valladolid', 'Vannes', 'Varese', 'Venezia', 'Venlo', 'Verona', 'Vicenza', 'Villarreal', 'Virtus Lanciano', 'Vitesse', 'Waalwijk', 'Watford', 'Werder', 'West Brom', 'West Ham', 'Westerlo', 'Wigan', 'Willem II', 'Wolfsburg', 'Wolves', 'Xerez', 'Yeovil', 'Zaragoza', 'Zulte Waregem', 'Zwolle']
elo_teams = set(elo_teams)

elo_ratings = dict()
team_elo_map = {'Ajaccio GFCO' : 'Ajaccio', 'Albacete': None,
 'Alcorcon' : None,
 'Alcoyano' : None,
 'Alicante' : None,
 'Arezzo' : None,
 'Arles': 'Arles-Avignon',
 'Ath Bilbao': 'Bilbao',
 'Ath Bilbao B' : None,
 'Ath Madrid' : 'Atletico'
 , 'Barcelona B' : None,
 'Bayern Munich' : 'Bayern',
 'Beziers' : None,
 'Bourg Peronnas' : None,
 'Burghausen' : None,
 'CZ Jena' : None,
 'Cadiz' : None,
 'Cartagena' : None,
 'Castellon' : None,
 'Catanzaro' : None,
 'Chambly' : None,
 'Ciudad de Murcia' : None,
 'Colchester' : None,
 'Cosenza' : None,
 'Crewe' : None,
 'Ein Frankfurt' : 'Frankfurt',
 'Erzgebirge Aue' : 'Aue',
 'Espanol' : 'Espanyol',
 'Essen' : None,
 'Evian Thonon Gaillard' : None,
 'Extremadura UD' : None,
 'FC Koln': 'Koeln',
 'Ferrol': None,
 'Fortuna Dusseldorf': 'Duesseldorf',
 'Frankfurt FSV' : 'FSV Frankfurt',
 'Fuenlabrada' : None,
 'Gimnastic' : None,
 'Girona' : None,
 'Granada 74' : None,
 'Greuther Furth' : None,
 'Guadalajara' : None,
 'Gueugnon' : None,
 'Hansa Rostock' : 'Rostock',
 'Holstein Kiel' : None,
 'Huesca' : None,
 'Jaen' : None,
 'Kaiserslautern' : 'Lautern',
 'Kaiserslautern ' : 'Lautern',
 'La Coruna' : 'Depor',
 'Leonesa' : None,
 'Libourne' : None,
 'Llagostera' : None,
 'Lleida' : None,
 'Lorca' : None,
 'Lugo' : None,
 'Luton' : None,
 "M'gladbach" : None,
 'Magdeburg' : None,
 'Malaga B': None,
 'Messina': None,
 'Milton Keynes Dons' : None,
 'Mirandes' : None,
 'Munich 1860' : 'Muenchen 60',
 'Murcia' : None,
 "Nott'm Forest" : None,
 'Numancia' : None,
 'Nurnberg' : 'Nuernberg',
 'Offenbach' : None,
 'Osnabruck': 'Osnabrueck',
 'Oviedo' : None,
 'Poli Ejido' : None,
 'Ponferradina' : None,
 'Pordenone' : None,
 'Quevilly Rouen' : None,
 'Ravenna' : None,
 'Rayo Majadahonda' : None,
 'Real Madrid B' : None,
 'Real Union' : None,
 'Recreativo' : None,
 'Reus Deportiu' : None,
 'Rimini' : None,
 'Rodez' : None,
 'Saarbrucken' : None,
 'Sabadell' : None,
 'Salamanca' : None,
 'Schalke 04' : 'Schalke',
 'Sete' : None,
 'Sevilla B' : None,
 'Siegen' : None,
 'Southend' : None,
 'Sp Gijon': 'Gijon',
 'St Etienne' : 'Saint-Etienne',
 'Treviso' : None,
 'UCAM Murcia' : None,
 'Unterhaching' : None,
 'Vallecano': 'Rayo Vallecano',
 'Vecindario' : None,
 'Villarreal B' : None,
 'Virtus Entella' : None,
 'Wehen' : None,
 'Werder Bremen' : 'Werder',
 'Wurzburger Kickers' : None}


team_fifa_map ={'Aachen' : 'Alemannia Aachen',
 'Aalen' : 'VfR Aalen',
 'Ahlen' : 'Rot-Weiß Ahlen',
 'Ajaccio' : 'AC Ajaccio',
 'Ajaccio GFCO' : 'GFC Ajaccioe',
 'Alaves' : 'Deportivo Alavés',
 'Albacete' : 'Albacete BP',
 'Albinoleffe' : 'UC AlbinoLeffe',
 'Alcorcon' : 'AD Alcorcón',
 'Alcoyano': 'CD Alcoyano',
 'Alicante' : None,
 'Almeria' : 'UD Almería',
 'Amiens' : 'Amiens SC',
 'Ancona' : 'Ancona',
 'Angers' : 'Angers SCO',
 'Arezzo' : None,
 'Arles' : 'AC Arles Avignon',
 'Arsenal' : 'Arsenal',
 'Ascoli' : 'Ascoli',
 'Aston Villa' : 'Aston Villa',
 'Atalanta' : 'Atalanta',
 'Ath Bilbao' : 'Athletic Club de Bilbao',
 'Ath Bilbao B' : None,
 'Ath Madrid' : 'Atlético Madrid',
 'Augsburg' : 'FC Augsburg',
 'Auxerre' : 'AJ Auxerre',
 'Avellino' : 'Avellino',
 'Barcelona' : 'FC Barcelona',
 'Barcelona B' : 'FC Barcelona B',
 'Bari' : 'Bary',
 'Barnsley' : 'Barnsley',
 'Bastia' : 'Sporting Club de Bastia',
 'Bayern Munich' : 'FC Bayern München',
 'Benevento' : 'Benevento',
 'Betis' : 'Real Betis',
 'Beziers' : 'AS Béziers',
 'Bielefeld' : 'DSC Arminia Bielefeld',
 'Birmingham' : 'Birmingham City',
 'Blackburn' : 'Blackburn Rovers',
 'Blackpool' : 'Blackpool',
 'Bochum' : 'VfL Bochum 1848',
 'Bologna' : 'Bologna',
 'Bolton' : 'Bolton Wanderers',
 'Bordeaux' : 'FC Girondins de Bordeaux',
 'Boulogne' : "US Boulogne Cote D'Opale",
 'Bourg Peronnas' : 'Football Bourg En Bresse Peronnas 01',
 'Bournemouth' : 'Bournemouth',
 'Braunschweig' : 'Eintracht Braunschweig',
 'Brentford' : 'Brentford',
 'Brescia' : 'Brescia',
 'Brest' : 'Stade Brestois 29 ',
 'Brighton' : 'Brighton & Hove Albion',
 'Bristol City' : 'Bristol City',
 'Burghausen' : None,
 'Burnley' : 'Burnley',
 'Burton' : 'Burton Albion',
 'CA Bastia' : 'Sporting Club de Bastia',
 'CZ Jena' : None,
 'Cadiz' : 'Cádiz CF',
 'Caen' : 'Stade Malherbe Caen',
 'Cagliari' : 'Cagliari',
 'Cardiff': 'Cardiff City',
 'Carpi' : 'Carpi',
 'Cartagena' : 'FC Cartagena',
 'Castellon' : 'C.D. Castellón',
 'Catania' : 'Catania',
 'Catanzaro' : None,
 'Celta' : 'RC Celta',
 'Cesena' : 'Cesena',
 'Chambly' : 'FC Chambly Oise',
 'Charlton' : 'Charlton Athletic',
 'Chateauroux' : 'La Berrichonne de Châteauroux',
 'Chelsea' : 'Chelsea',
 'Chievo' : 'Chievo Verona',
 'Cittadella' : 'Cittadella',
 'Ciudad de Murcia' : None,
 'Clermont' : 'Clermont Foot 63',
 'Colchester' : None,
 'Como' : 'Como',
 'Cordoba' : 'Córdoba CF',
 'Cosenza' : 'Cosenza',
 'Cottbus' : 'FC Energie Cottbus',
 'Coventry' : 'Coventry City',
 'Cremonese' : 'US Cremonese',
 'Creteil' : 'US Créteil-Lusitanos',
 'Crewe' : None,
 'Crotone' : 'Crotone',
 'Crystal Palace' : 'Crystal Palace',
 'Darmstadt' : 'SV Darmstadt 98',
 'Derby' : 'Derby County',
 'Dijon' : 'Dijon FCO',
 'Doncaster' : 'Doncaster Rovers',
 'Dortmund' : 'Borussia Dortmund',
 'Dresden' : 'SG Dynamo Dresden',
 'Duisburg' : 'MSV Duisburg',
 'Eibar' : 'SD Eibar',
 'Ein Frankfurt': 'Eintracht Frankfurt',
 'Elche' : 'Elche CF',
 'Empoli' : 'Empoli',
 'Erzgebirge Aue' : 'FC Erzgebirge Aue',
 'Espanol' : 'RCD Espanyol',
 'Essen' : None,
 'Everton': 'Everton',
 'Evian Thonon Gaillard' : 'Évian Thonon Gaillard FC',
 'Extremadura UD' : 'Extremadura UD',
 'FC Koln' : 'FC Köln',
 'Ferrol' : None,
 'Fiorentina' : 'Fiorentina',
 'Foggia' : 'Foggia',
 'Fortuna Dusseldorf' : 'Fortuna Düsseldorf',
 'Frankfurt FSV' : "FSV Frankfurt",
 'Freiburg' : "SC Freiburg",
 'Frosinone' : 'Frosinone',
 'Fuenlabrada' : 'CF Fuenlabrada',
 'Fulham' : 'CF Fuenlabrada',
 'Gallipoli' : 'Gallipoli',
 'Genoa' : 'Genoa',
 'Getafe' : 'Getafe CF',
 'Gimnastic' : 'Gimnàstic de Tarragona',
 'Girona' : 'Girona FC',
 'Granada' : 'Granada CF',
'Granada 74' : None,
 'Grenoble' : 'Grenoble Foot 38',
 'Greuther Furth': 'SpVgg Greuther Fürth',
 'Grosseto' : 'Grosseto',
 'Guadalajara' : 'CD Guadalajara',
 'Gubbio' : 'Gubbio',
 'Gueugnon' : None,
 'Guingamp' : 'En Avant de Guingamp',
 'Hamburg' : 'Hamburger SV',
 'Hannover' : 'Hannover 96',
 'Hansa Rostock' : 'FC Hansa Rostock',
 'Heidenheim' : 'FC Heidenheim 1846',
 'Hercules' : 'Hércules CF',
 'Hertha' : 'Hertha BSC',
 'Hoffenheim' : 'TSG 1899 Hoffenheim',
 'Holstein Kiel' : 'Holstein Kiel',
 'Huddersfield' : 'Huddersfield Town',
 'Huesca' : 'SD Huesca',
 'Hull' : 'Hull City',
 'Ingolstadt' : 'FC Ingolstadt 04',
 'Inter' : 'Inter',
 'Ipswich' : 'Ipswich Town',
 'Istres' : 'FC Istres Ouest Provence',
 'Jaen' : 'Real Jaén CF',
 'Juve Stabia' : 'Castellammare di Stabia',
'Juventus' : 'Juventus',
 'Kaiserslautern' : 'FC Kaiserslautern', 'Kaiserslautern ' : 'FC Kaiserslautern',
 'Karlsruhe' : 'Karlsruher SC',
 'Koblenz' : 'TuS Koblenz',
 'La Coruna' : 'Deportivo de La Coruña',
 'Las Palmas' : 'UD Las Palma',
 'Latina' : 'Latina',
 'Laval' : 'Stade Lavallois Mayenne FC',
 'Lazio' : 'Lazio',
 'Le Havre' : 'Le Havre AC',
 'Le Mans' : 'Le Mans FC',
 'Lecce': 'Lecce',
 'Leeds' : 'Leeds United',
 'Leganes' : 'CD Leganés',
 'Leicester' : 'Leicester City',
 'Lens' : 'Racing Club de Lens',
 'Leonesa' : 'Cultural Leonesa',
 'Levante' : 'Levante UD',
'Leverkusen' : 'Bayer 04 Leverkusen',
 'Libourne': None,
 'Lille' : 'LOSC Lille',
 'Liverpool' : 'Liverpool',
 'Livorno' : 'Livorno',
 'Llagostera' : 'UE Llagostera',
 'Lleida' : None,
 'Lorca' : 'Lorca FC',
 'Lorient' : 'FC Lorient',
 'Lugo' : 'CD Lugo',
 'Luton' : 'Luton Town',
 'Lyon' : 'Olympique Lyonnais',
 "M'gladbach" : 'Borussia Mönchengladbach',
 'Magdeburg' : 'FC Magdeburg',
 'Mainz' : 'FSV Mainz 05',
 'Malaga' : 'Málaga CF',
 'Malaga B' : None,
 'Mallorca' : 'RCD Mallorca',
 'Man City' : 'Manchester City',
'Man United': 'Manchester United',
 'Mantova' : 'Mantova',
 'Marseille' : 'Olympique de Marseille',
 'Messina' : None,
 'Metz' : 'FC Metz',
 'Middlesbrough' : 'Middlesbrough',
 'Milan' : 'Milan',
 'Millwall' : 'Millwall',
 'Milton Keynes Dons' : 'Milton Keynes Dons',
 'Mirandes' : 'CD Mirandés',
 'Modena' : 'Modena',
 'Monaco' : 'AS Monaco',
'Montpellier' : 'Montpellier HSC',
 'Munich 1860' : 'TSV 1860 München',
 'Murcia' : 'Real Murcia Club de Fútbol',
 'Nancy' : 'AS Nancy Lorraine',
 'Nantes' : 'FC Nantes',
 'Napoli' : 'Napoli',
 'Newcastle' : 'Newcastle United',
'Nice' : 'OGC Nice',
 'Nimes' : 'Nîmes Olympique',
 'Niort' : 'Chamois Niortais Football Club',
 'Nocerina' : 'Nocera Inferiore',
 'Norwich' : 'Norwich City',
 "Nott'm Forest" : 'Nottingham Forest',
 'Novara' : 'Novara',
 'Numancia' : 'CD Numancia',
 'Nurnberg' : 'FC Nürnberg',
 'Oberhausen' : 'Rot-Weiß Oberhausen',
 'Offenbach' : None,
 'Orleans' : 'US Orléans Loiret Football',
 'Osasuna' : 'CA Osasuna',
 'Osnabruck' : 'VfL Osnabrück',
 'Oviedo' : 'Real Oviedo',
 'Paderborn' : 'SC Paderborn 07',
 'Padova' : 'Padova',
 'Palermo' : 'Palermo',
 'Paris FC' : 'Paris FC',
 'Paris SG' : 'Paris Saint-Germain',
 'Parma' : 'Parma',
 'Perugia' : 'Perugia',
 'Pescara' : 'Pescara',
 'Peterboro' : 'Peterborough United',
 'Piacenza' : 'Piacenza',
 'Pisa' : 'Pisa',
 'Plymouth' : ' Plymouth Argyle',
 'Poli Ejido' : None,
 'Ponferradina' : 'SD Ponferradina',
 'Pordenone' : 'Pordenone',
 'Portogruaro' : 'Portogruaro Calcio ASD',
 'Portsmouth' : 'Portsmouth',
 'Preston' : 'Preston North End',
 'Pro Vercelli' : 'FC Pro Vercelli 1892',
 'QPR' : 'Queens Park Rangers',
 'Quevilly Rouen' : 'US Quevilly Rouen Métropole',
 'RB Leipzig' : 'RB Leipzig',
 'Ravenna' : None,
 'Rayo Majadahonda' : 'CF Rayo Majadahonda',
 'Reading' : 'Reading',
 'Real Madrid' : 'Real Madrid',
 'Real Madrid B': 'Real Madrid Castilla',
 'Real Union' : 'Real Unión Club Irún',
 'Recreativo' : 'RC Recreativo de Huelva',
 'Red Star' : 'Red Star FC',
 'Regensburg' : 'SSV Jahn Regensburg',
 'Reggina' : 'Urbs Reggina 1914',
 'Reims' : 'Stade de Reims',
 'Rennes' : 'Stade Rennais FC ',
 'Reus Deportiu' : 'CF Reus Deportiu',
 'Rimini' : None,
 'Rodez' : 'Rodez Aveyron Football',
 'Roma' : 'Roma',
 'Rotherham' : 'Rotherham United',
 'Saarbrucken' : None,
 'Sabadell' : 'CE Sabadell FC',
 'Salamanca' : 'UD Salamanca',
 'Salernitana' : 'US Salernitana 1919',
 'Sampdoria' : 'Sampdoria',
 'Sandhausen' : 'SV Sandhausen',
 'Santander' : 'Racing Santander',
 'Sassuolo' : 'Sassuolo',
 'Schalke 04' : 'FC Schalke 04',
 'Scunthorpe' : 'Scunthorpe United',
 'Sedan' : 'CS Sedan Ardennes',
'Sete' : None,
'Sevilla' : 'Sevilla FC',
 'Sevilla B' : 'Sevilla Atlético',
 'Sheffield United' : 'Sheffield United',
 'Sheffield Weds' : 'Sheffield Wednesday',
 'Siegen' : None,
 'Siena' : 'Siena',
 'Sochaux' : 'FC Sochaux-Montbéliard',
 'Sociedad' : 'Real Sociedad',
 'Southampton' : 'Southampton',
 'Southend' : None,
 'Sp Gijon' : 'Real Sporting de Gijón',
 'Spal' : 'SPAL',
 'Spezia' : 'Spezia',
 'St Etienne' : 'AS Saint-Étienne',
 'St Pauli' : 'FC St. Pauli',
 'Stoke' : 'Stoke City',
 'Strasbourg' : 'RC Strasbourg Alsace',
'Stuttgart' : 'VfB Stuttgart',
 'Sunderland' : 'Sunderland',
 'Swansea' : 'Swansea City',
 'Tenerife' : 'CD Tenerife',
 'Ternana' : 'Ternana',
'Torino' : 'Torino',
 'Tottenham' : 'Tottenham Hotspur',
 'Toulouse' : 'Toulouse Football Club',
 'Tours' : 'Tours FC',
 'Trapani' : 'Trapani',
'Treviso': None,
 'Triestina' : 'Triestina',
 'Troyes' : 'ESTAC Troyes',
 'UCAM Murcia' : 'Real Murcia Club de Fútbol',
 'Udinese' : 'Udinese', 'Union Berlin' : 'FC Union Berlin',
 'Unterhaching' : None,
 'Valencia' : 'Valencia CF',
 'Valenciennes' : 'Valenciennes FC',
 'Valladolid' : 'Real Valladolid CF',
 'Vallecano' : 'Rayo Vallecano',
 'Vannes' : 'Vannes OC',
'Varese' : 'Varese',
 'Vecindario' : None,
 'Venezia' : 'Venezia FC',
 'Verona' : 'Chievo Verona',
 'Vicenza' : 'Vicenza',
 'Villarreal' : 'Villarreal CF',
 'Villarreal B' : 'Villarreal CF B',
 'Virtus Entella' : 'Virtus Entella',
 'Virtus Lanciano' : 'SS Virtus Lanciano',
 'Watford' :'Watford',
 'Wehen' : 'SV Wehen Wiesbaden',
 'Werder Bremen' : 'SV Werder Bremen',
 'West Brom' : 'West Bromwich Albion',
 'West Ham' : 'West Ham United',
 'Wigan' : 'Wigan Athletic',
 'Wolfsburg' : 'VfL Wolfsburg',
 'Wolves' : 'Wolverhampton Wanderers',
 'Wurzburger Kickers' : 'FC Würzburger Kickers',
 'Xerez' : 'Xerez Club Deportivo',
 'Yeovil' : 'Yeovil Town', 'Zaragoza' : 'Real Zaragoza'}


with open(r'C:\Users\Idan\PycharmProjects\project_ai\elo_scores.csv', encoding="utf8") as elo_file:
    ratings =csv.DictReader(elo_file)
    for rating in ratings:
        if rating:
            club = rating['Club']
            data = (float(rating['Elo']), rating['From'], rating['To'])
            if club not in elo_ratings:
                elo_ratings[club] = [data]
            else:
                elo_ratings[club].append(data)


def find_elo_date(date, elo_ratings):
    #helper function-returns the index of the right elo rating by the dates list
    for i in range (len(elo_ratings)):
        era = elo_ratings[i]
        if not(date < era[1] or  era[2] < date):
            return i

league_names_skip = {'English Premier League (1)', 'French Ligue 1 (1)', 'German 1. Bundesliga (1)',
                     'Italian Serie A (1)', 'Spain Primera Division (1)', 'English League Championship (2)',
                     'French Ligue 2 (2)', 'Italian Serie B (2)', 'German 2. Bundesliga (2)',
                     'Spanish Segunda División (2)'}



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



#league_names_skip_lst_test = list(league_names_skip)

def fifa_create_ratings(ratings, dates):
    rating_number = []
    names = []
    for rating in ratings:
        rating = rating.strip()
        if rating and rating not in league_names_skip:
            line = rating.split()
            if line[0].isdigit():   #this is a the rating
                rating_number.append(int(line[0]))
            else:
                names.append(rating)
    for i in range(len(rating_number)):
        dates[names[i]] = rating_number[i]



with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2009_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2009_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2010_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2010_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2011_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2011_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2012_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2012_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2013_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2013_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2014_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2014_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2015_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2015_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2016_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2016_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2017_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2017_aug_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2018_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2018_aug_ratings)


with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2019_aug.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2019_aug_ratings)


with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2010_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2010_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2011_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2011_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2012_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2012_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2013_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2013_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2014_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2014_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2015_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2015_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2016_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2016_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2017_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2017_feb_ratings)

with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2018_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2018_feb_ratings)


with open(r'C:\Users\Idan\PycharmProjects\project_ai\fifa_rating_2019_feb.txt', encoding="utf8") as fifa_file:
    ratings = fifa_file.read().splitlines()
    fifa_create_ratings(ratings, fifa_2019_feb_ratings)


fifa_ratings_dates = [
(fifa_2009_aug_ratings, '2009-08-01')
,(fifa_2010_feb_ratings, '2010-02-01')
,(fifa_2010_aug_ratings, '2010-08-01')
,(fifa_2011_feb_ratings, '2011-02-01')
,(fifa_2011_aug_ratings, '2011-08-01')
,(fifa_2012_feb_ratings, '2012-02-01')
,(fifa_2012_aug_ratings, '2012-08-01')
,(fifa_2013_feb_ratings, '2013-02-01')
,(fifa_2013_aug_ratings, '2013-08-01')
,(fifa_2014_feb_ratings, '2014-02-01')
,(fifa_2014_aug_ratings, '2014-08-01')
,(fifa_2015_feb_ratings, '2015-02-01')
,(fifa_2015_aug_ratings, '2015-08-01')
,(fifa_2016_feb_ratings, '2016-02-01')
,(fifa_2016_aug_ratings, '2016-08-01')
,(fifa_2017_feb_ratings, '2017-02-01')
,(fifa_2017_aug_ratings, '2017-08-01')
,(fifa_2018_feb_ratings, '2018-02-01')
,(fifa_2018_aug_ratings, '2018-08-01')
,(fifa_2019_feb_ratings, '2019-02-01')
,(fifa_2019_aug_ratings, '2019-08-01')]

def find_fifa_date(date):
    #helper function-returns the index of the right elo rating by the dates list
    for i in range (len(fifa_ratings_dates)) :
        era = fifa_ratings_dates[i]
        if date < era[1]:
            return i - 1
    return len(fifa_ratings_dates)

for num in range(1):
    games = []
    print(len(sys.argv))
    print(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        output_file_name = sys.argv[2] + '.csv'
    else:
        file_name = sys.argv[1]+' '+sys.argv[2]
        output_file_name = sys.argv[3] + '.csv'
    with open(file_name, 'r', encoding="utf8", errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            games.append(row)

    games_states = []

    for i, game in enumerate(games):
        game_state = {'Date': game['Date'], 'HomeTeam': game['HomeTeam'], 'AwayTeam': game['AwayTeam'], 'h_played': 0, 'h_played_h': 0, 'a_played': 0,
                      'a_played_a': 0, 'h_won': 0, 'h_won_h': 0, 'h_drawn': 0, 'h_drawn_h': 0, 'h_lost': 0, 'h_lost_h': 0,
                      'h_points': 0, 'h_points_h': 0, 'h_scored': 0, 'h_scored_h': 0, 'h_conced': 0, 'h_conced_h': 0,
                      'h_clean': 0, 'h_clean_h': 0, 'h_fail': 0, 'h_fail_h': 0,
                      #new from here, home
                      'h_goal_diff' : 0, 'h_goal_diff_h' : 0,
                      'h_shots': 0, 'h_shots_h': 0, 'h_shots_against': 0, 'h_shots_against_h': 0,
                      'h_shots_target': 0, 'h_shots_target_h': 0, 'h_shots_diff_h' : 0, 'h_shots_diff' : 0,
                      'h_shots_target_diff_h': 0, 'h_hit_woodwork' : 0, 'h_hit_woodwork_h' : 0,
                      'h_hit_woodwork_against' : 0,'h_hit_woodwork_diff' : 0,
                      'h_red_cards': 0, 'h_red_carss_h': 0,
                      'h_red_cards_against': 0, 'h_red_cards_diff': 0,
                      'h_red_cards_against_h': 0, 'h_red_cards_diff_h': 0,
                      'h_elo': 0, 'h_fifa_rating' : 0,
                      'h_current_win_streak' : 0, 'h_current_no_lose_streak' : 0,
                      'h_current_lose_streak': 0, 'h_current_no_win_streak': 0,
                      'h_last_5_games_points' : 0, 'h_last_5_games_wins' : 0, 'h_last_5_games_loss' : 0,
                      'h_last_5_games_draw': 0, 'h_last_5_games_scored': 0, 'h_last_5_games_conced': 0,
                      'h_last_5_games_goal_diff': 0, 'h_last_5_games_clean': 0, 'h_last_5_games_failed': 0,

                      'a_won': 0, 'a_won_a': 0, 'a_drawn': 0, 'a_drawn_a': 0, 'a_lost': 0, 'a_lost_a': 0,
                      'a_points': 0, 'a_points_a': 0, 'a_scored': 0, 'a_scored_a': 0, 'a_conced': 0, 'a_conced_a': 0,
                      'a_clean': 0, 'a_clean_a': 0, 'a_fail': 0, 'a_fail_a': 0,
                      #new from here: away
                      'a_goal_diff': 0, 'a_goal_diff_a': 0,
                      'a_shots': 0, 'a_shots_a': 0,
                      'a_shots_target': 0, 'a_shots_target_a': 0,  'a_shots_against': 0, 'a_shots_against_a': 0,
                      'a_shots_diff_a': 0, 'a_shots_target_diff_a': 0, 'a_hit_woodwork': 0, 'a_hit_woodwork_a': 0,
                      'a_hit_woodwork_against': 0, 'a_hit_woodwork_diff': 0,
                      'a_hit_woodwork_against_a': 0, 'a_hit_woodwork_diff_a': 0,
                      'a_red_cards': 0, 'a_red_cards_a': 0,
                      'a_red_cards_against': 0, 'a_red_cards_diff': 0,
                      'a_red_cards_against_a': 0, 'a_red_cards_diff_a': 0,
                      'a_elo': 0, 'a_fifa_rating' : 0,
                      'a_current_win_streak': 0, 'a_current_no_lose_streak': 0,
                      'a_current_lose_streak': 0, 'a_current_no_win_streak': 0,
                      'a_last_5_games_points': 0, 'a_last_5_games_wins': 0, 'a_last_5_games_loss': 0,
                      'a_last_5_games_draw': 0, 'a_last_5_games_scored': 0, 'a_last_5_games_conced': 0,
                      'a_last_5_games_goal_diff': 0, 'a_last_5_games_clean': 0, 'a_last_5_games_failed': 0,
                      'home_odd': game['B365H'],
                      'draw_odd': game['B365D'], 'away_odd': game['B365A'], 'RESULT': ''
                      }

        #elo ratings
        dates = ''
        if game['HomeTeam'] not in elo_teams:
            dates = team_elo_map[game['HomeTeam']]
        else:
            dates = team_elo_map[game['HomeTeam']]
        date = game['Date']
        index = find_elo_date(date, dates)
        game_state['h_elo'] = dates[index][0]
        dates = team_elo_map[game['AwayTeam']]
        date = game['Date']
        index = find_elo_date(date, dates)
        game_state['a_elo'] = dates[index][0]

        #fifa ratings
        name = team_fifa_map[game['HomeTeam']]
        index = find_fifa_date(date)
        fifa_rating = fifa_ratings_dates[index][1][name]
        game_state['h_fifa_rating'] = fifa_rating
        name = team_fifa_map[game['AwayTeam']]
        index = find_fifa_date(date)
        fifa_rating = fifa_ratings_dates[index][1][name]
        game_state['a_fifa_rating'] = fifa_rating

        if game['FTR'] == 'H':
            game_state['RESULT'] = 'HOME'
        if game['FTR'] == 'D':
            game_state['RESULT'] = 'DRAW'
        if game['FTR'] == 'A':
            game_state['RESULT'] = 'AWAY'

        for j in range(i):
            pre_game = games[j]
            if pre_game['Date'] == '':
                continue
            if pre_game['HomeTeam'] == game_state['HomeTeam']:
                game_state['h_played'] += 1
                game_state['h_played_h'] += 1

                game_state['h_scored'] += int(pre_game['FTHG'])
                game_state['h_scored_h'] += int(pre_game['FTHG'])
                game_state['h_conced'] += int(pre_game['FTAG'])
                game_state['h_conced_h'] += int(pre_game['FTAG'])
                game_state['h_shots'] += int(pre_game['HS'])
                game_state['h_shots_h'] += int(pre_game['HS'])
                game_state['h_shots_target'] += int(pre_game['HST'])
                game_state['h_shots_target_h'] += int(pre_game['HST'])

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


            if pre_game['AwayTeam'] == game_state['AwayTeam']:
                game_state['a_played'] += 1
                game_state['a_played_a'] += 1
                game_state['a_scored'] += int(pre_game['FTAG'])
                game_state['a_scored_a'] += int(pre_game['FTAG'])
                game_state['a_conced'] += int(pre_game['FTHG'])
                game_state['a_conced_a'] += int(pre_game['FTHG'])
                game_state['a_shots'] += int(pre_game['AS'])
                game_state['a_shots_a'] += int(pre_game['AS'])
                game_state['a_shots_target'] += int(pre_game['AST'])
                game_state['a_shots_target_a'] += int(pre_game['AST'])

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

            if pre_game['AwayTeam'] == game_state['HomeTeam']:
                game_state['h_played'] += 1
                game_state['h_scored'] += int(pre_game['FTAG'])
                game_state['h_conced'] += int(pre_game['FTHG'])
                game_state['h_shots'] += int(pre_game['AS'])
                game_state['h_shots_target'] += int(pre_game['AST'])

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

            if pre_game['HomeTeam'] == game_state['AwayTeam']:
                game_state['a_played'] += 1
                game_state['a_scored'] += int(pre_game['FTHG'])
                game_state['a_conced'] += int(pre_game['FTAG'])
                game_state['a_shots'] += int(pre_game['HS'])
                game_state['a_shots_target'] += int(pre_game['HST'])

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
        games_states.append(game_state)

    with open(output_file_name, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'HomeTeam', 'AwayTeam', 'h_played', 'h_played_h', 'a_played',
                      'a_played_a', 'h_won', 'h_won_h', 'h_drawn', 'h_drawn_h', 'h_lost', 'h_lost_h',
                      'h_points', 'h_points_h', 'h_scored', 'h_scored_h', 'h_conced', 'h_conced_h',
                      'h_clean', 'h_clean_h', 'h_fail', 'h_fail_h',
                      #'h_shots', 'h_shots_h',
                      #'h_shots_target', 'h_shots_target_h',
                      'a_won', 'a_won_a', 'a_drawn', 'a_drawn_a', 'a_lost', 'a_lost_a',
                      'a_points', 'a_points_a', 'a_scored', 'a_scored_a', 'a_conced', 'a_conced_a',
                      'a_clean', 'a_clean_a', 'a_fail', 'a_fail_a',
                      #'a_shots', 'a_shots_a',
                      #'a_shots_target', 'a_shots_target_a',
                      'home_odd',
                      'draw_odd', 'away_odd', 'RESULT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for game_state in games_states:
            writer.writerow({'Date': game_state['Date'], 'HomeTeam': game_state['HomeTeam'], 'AwayTeam': game_state['AwayTeam'],
                             'h_played': game_state['h_played'], 'h_played_h': game_state['h_played_h'], 'a_played': game_state['a_played'],
                             'a_played_a': game_state['a_played_a'], 'h_won': game_state['h_won'], 'h_won_h': game_state['h_won_h'],
                             'h_drawn': game_state['h_drawn'], 'h_drawn_h': game_state['h_drawn_h'], 'h_lost': game_state['h_lost'],
                             'h_lost_h': game_state['h_lost_h'], 'h_points': game_state['h_points'], 'h_points_h': game_state['h_points_h'],
                             'h_scored': game_state['h_scored'], 'h_scored_h': game_state['h_scored_h'], 'h_conced': game_state['h_conced'],
                             'h_conced_h': game_state['h_conced_h'], 'h_clean': game_state['h_clean'], 'h_clean_h': game_state['h_clean_h'],
                             'h_fail': game_state['h_fail'], 'h_fail_h': game_state['h_fail_h'],
                             #'h_shots': game_state['h_shots'], 'h_shots_h': game_state['h_shots_h'],
                             #'h_shots_target': game_state['h_shots_target'], 'h_shots_target_h': game_state['h_shots_target_h'],
                             'a_won': game_state['a_won'],
                             'a_won_a': game_state['a_won_a'], 'a_drawn': game_state['a_drawn'], 'a_drawn_a': game_state['a_drawn_a'],
                             'a_lost': game_state['a_lost'], 'a_lost_a': game_state['a_lost_a'], 'a_points': game_state['a_points'],
                             'a_points_a': game_state['a_points_a'], 'a_scored': game_state['a_scored'], 'a_scored_a': game_state['a_scored_a'],
                             'a_conced': game_state['a_conced'], 'a_conced_a': game_state['a_conced_a'], 'a_clean': game_state['a_clean'],
                             'a_clean_a': game_state['a_clean_a'], 'a_fail': game_state['a_fail'], 'a_fail_a': game_state['a_fail_a'],
                             #'a_shots': game_state['a_shots'], 'a_shots_a': game_state['a_scored_a'],
                             #'a_shots_target': game_state['a_shots_target'],
                             #'a_shots_target_a': game_state['a_shots_target_a'],
                             'home_odd': game_state['home_odd'], 'draw_odd': game_state['draw_odd'], 'away_odd': game_state['away_odd'],
                             'RESULT': game_state['RESULT']})