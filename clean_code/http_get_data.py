#code for creating the elo ratings files
import urllib
import urllib.request
clubs = ['Aston Villa', 'Bastia', 'Bayern', 'Beerschot AC', 'Beira Mar', 'Belenenses', 'Benevento', 'Benfica', 'Bergen', 'Besiktas', 'Betis', 'Beveren', 'Bielefeld', 'Bilbao', 'Birmingham', 'Blackburn', 'Blackpool', 'Boavista', 'Bochum', 'Bologna', 'Bolton', 'Bordeaux', 'Boulogne', 'Bournemouth', 'Braga', 'Braunschweig', 'Breda', 'Brentford', 'Brescia', 'Brest', 'Brighton', 'Bristol City', 'Brugge', 'Bucaspor', 'Bueyueksehir', 'Burnley', 'Bursaspor', 'Burton', 'CA Bastia', 'Caen', 'Cagliari', 'Cambuur', 'Cardiff', 'Carpi', 'Catania', 'Celta', 'Celtic', 'Cercle Brugge', 'Cesena', 'Charleroi', 'Charlton', 'Chateauroux', 'Chaves', 'Chelsea', 'Chievo', 'Cittadella', 'Clermont', 'Como', 'Cordoba', 'Cottbus', 'Coventry', 'Cremonese', 'Creteil', 'Crotone', 'Crystal Palace', 'Darmstadt', 'De Graafschap', 'Den Haag', 'Denizlispor', 'Depor', 'Derby', 'Dijon', 'Diyarbakirspor', 'Doncaster', 'Dordrecht', 'Dortmund', 'Dresden', 'Duesseldorf', 'Duisburg', 'Dundee', 'Dundee United', 'Dunfermline', 'Eibar', 'Elche', 'Empoli', 'Eskisehirspor', 'Espanyol', 'Estoril', 'Eupen', 'Everton', 'Evian TG', 'Excelsior', 'FSV Frankfurt', 'Falkirk', 'Feirense', 'Fenerbahce', 'Feyenoord', 'Fiorentina', 'Foggia', 'Frankfurt', 'Freiburg', 'Frosinone', 'Fuerth', 'Fulham', 'Galatasaray', 'Gallipoli', 'Gaziantepspor', 'Genclerbirligi', 'Genk', 'Genoa', 'Gent', 'Getafe', 'Gijon', 'Gil Vicente', 'Go Ahead Eagles', 'Granada', 'Grenoble', 'Groningen', 'Grosseto', 'Gubbio', 'Guimaraes', 'Guingamp', 'Hamburg', 'Hamilton', 'Hannover', 'Hearts', 'Heerenveen', 'Heidenheim', 'Heracles', 'Hercules', 'Hertha', 'Hibernian', 'Hoffenheim', 'Huddersfield', 'Hull', 'Ingolstadt', 'Inter', 'Inverness', 'Ipswich', 'Istres', 'Juve Stabia', 'Juventus', 'Karabuekspor', 'Karlsruhe', 'Kasimpasa', 'Kayseri', 'Kilmarnock', 'Koblenz', 'Koeln', 'Konyaspor', 'Kortrijk', 'Las Palmas', 'Latina', 'Lautern', 'Laval', 'Lazio', 'Le Havre', 'Le Mans', 'Lecce', 'Leeds', 'Leganes', 'Leicester', 'Leiria', 'Leixoes', 'Lens', 'Leuven', 'Levante', 'Leverkusen', 'Lierse', 'Lille', 'Liverpool', 'Livorno', 'Lokeren', 'Lorient', 'Lyon', 'Mainz', 'Malaga', 'Mallorca', 'Man City', 'Man United', 'Manisaspor', 'Mantova', 'Maritimo', 'Marseille', 'Mechelen', 'Mersin Idman', 'Metz', 'Middlesbrough', 'Milan', 'Millwall', 'Modena', 'Monaco', 'Montpellier', 'Moreirense', 'Motherwell', 'Mouscron', 'Muenchen 60', 'Nacional', 'Nancy', 'Nantes', 'Napoli', 'Naval', 'Newcastle', 'Nice', 'Nijmegen', 'Nimes', 'Niort', 'Nocerina', 'Norwich', 'Novara', 'Nuernberg', 'Oberhausen', 'Olhanense', 'Oostende', 'Orduspor', 'Orleans', 'Osasuna', 'Osnabrueck', 'PSV', 'Pacos Ferreira', 'Paderborn', 'Padova', 'Palermo', 'Paris FC', 'Paris SG', 'Parma', 'Partick', 'Perugia', 'Pescara', 'Peterboro', 'Piacenza', 'Pisa', 'Plymouth', 'Portimonense', 'Porto', 'Portogruaro', 'Portsmouth', 'Preston', 'Pro Vercelli', 'QPR', 'RB Leipzig', 'Rangers', 'Rayo Vallecano', 'Reading', 'Real Madrid', 'Red Star', 'Regensburg', 'Reggina', 'Reims', 'Rennes', 'Rio Ave', 'Rizespor', 'Roda', 'Roeselare', 'Roma', 'Ross County', 'Rostock', 'Rotherham', 'Saint-Etienne', 'Salernitana', 'Sampdoria', 'Samsunspor', 'Sandhausen', 'Santander', 'Sassuolo', 'Schalke', 'Scunthorpe', 'Sedan', 'Setubal', 'Sevilla', 'Sheffield United', 'Sheffield Weds', 'Siena', 'Sivasspor', 'Sochaux', 'Sociedad', 'Southampton', 'Spal', 'Sparta Rotterdam', 'Spezia', 'Sporting', 'St Johnstone', 'St Mirren', 'St Pauli', 'St Truiden', 'Standard', 'Stoke', 'Strasbourg', 'Stuttgart', 'Sunderland', 'Swansea', 'Tenerife', 'Ternana', 'Tondela', 'Torino', 'Tottenham', 'Toulouse', 'Tours', 'Trabzonspor', 'Trapani', 'Triestina', 'Troyes', 'Twente', 'Udinese', 'Union Berlin', 'Utrecht', 'Valencia', 'Valenciennes', 'Valladolid', 'Vannes', 'Varese', 'Venezia', 'Venlo', 'Verona', 'Vicenza', 'Villarreal', 'Virtus Lanciano', 'Vitesse', 'Waalwijk', 'Watford', 'Werder', 'West Brom', 'West Ham', 'Westerlo', 'Wigan', 'Willem II', 'Wolfsburg', 'Wolves', 'Xerez', 'Yeovil', 'Zaragoza', 'Zulte Waregem', 'Zwolle']
#clubs = ['Udinese', 'Union Berlin', 'Utrecht', 'Valencia', 'Valenciennes', 'Valladolid', 'Vannes', 'Varese', 'Venezia', 'Venlo', 'Verona', 'Vicenza', 'Villarreal', 'Virtus Lanciano', 'Vitesse', 'Waalwijk', 'Watford', 'Werder', 'West Brom', 'West Ham', 'Westerlo', 'Wigan', 'Willem II', 'Wolfsburg', 'Wolves', 'Xerez', 'Yeovil', 'Zaragoza', 'Zulte Waregem', 'Zwolle']

skipped_club = []
for club in clubs:
	print(club)
	if ' ' in club:
		skipped_club.append(club)
		continue
	response = urllib.request.urlopen(f"http://api.clubelo.com/{club}")
	open(fr"C:\Users\Idan\PycharmProjects\project_ai\{club}.csv", "wb").write(response.read())
print(skipped_club)