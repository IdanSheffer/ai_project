import csv
elo_teams = ['Aachen', 'Aalen', 'Aberdeen', 'Academica', 'Adanaspor', 'Ahlen', 'Ajaccio', 'Ajax', 'Akhisar', 'Alanyaspor', 'Alaves', 'Albinoleffe', 'Alkmaar', 'Almeria', 'Amiens', 'Ancona', 'Anderlecht', 'Angers', 'Ankaraguecue', 'Antalyaspor', 'Antwerp', 'Arles-Avignon', 'Arouca', 'Arsenal', 'Ascoli', 'Aston Villa', 'Atalanta', 'Atletico', 'Aue', 'Augsburg', 'Auxerre', 'Avellino', 'Aves', 'Barcelona', 'Bari', 'Barnsley', 'Bastia', 'Bayern', 'Beerschot AC', 'Belenenses', 'Benevento', 'Benfica', 'Bergen', 'Besiktas', 'Betis', 'Beveren', 'Bielefeld', 'Bilbao', 'Birmingham', 'Blackburn', 'Blackpool', 'Boavista', 'Bochum', 'Bologna', 'Bolton', 'Bordeaux', 'Boulogne', 'Bournemouth', 'Braga', 'Braunschweig', 'Breda', 'Brentford', 'Brescia', 'Brest', 'Brighton', 'Bristol City', 'Brugge', 'Bucaspor', 'Bueyueksehir', 'Burnley', 'Bursaspor', 'Burton', 'Caen', 'Cagliari', 'Cambuur', 'Cardiff', 'Carpi', 'Catania', 'Celta', 'Celtic', 'Cercle Brugge', 'Cesena', 'Charleroi', 'Charlton', 'Chateauroux', 'Chaves', 'Chelsea', 'Chievo', 'Cittadella', 'Clermont', 'Como', 'Cordoba', 'Cottbus', 'Coventry', 'Cremonese', 'Creteil', 'Crotone', 'Crystal Palace', 'Darmstadt', 'Den Haag', 'Denizlispor', 'Depor', 'Derby', 'Dijon', 'Diyarbakirspor', 'Doncaster', 'Dordrecht', 'Dortmund', 'Dresden', 'Duesseldorf', 'Duisburg', 'Dundee', 'Dundee United', 'Dunfermline', 'Eibar', 'Elche', 'Empoli', 'Eskisehirspor', 'Espanyol', 'Estoril', 'Eupen', 'Everton', 'Excelsior', 'Falkirk', 'Feirense', 'Fenerbahce', 'Feyenoord', 'Fiorentina', 'Foggia', 'Frankfurt', 'Freiburg', 'Frosinone', 'Fuerth', 'Fulham', 'Galatasaray', 'Gallipoli', 'Gaziantepspor', 'Genclerbirligi', 'Genk', 'Genoa', 'Gent', 'Getafe', 'Gijon', 'Gil Vicente', 'Granada', 'Grenoble', 'Groningen', 'Grosseto', 'Gubbio', 'Guimaraes', 'Guingamp', 'Hamburg', 'Hamilton', 'Hannover', 'Hearts', 'Heerenveen', 'Heidenheim', 'Heracles', 'Hercules', 'Hertha', 'Hibernian', 'Hoffenheim', 'Huddersfield', 'Hull', 'Ingolstadt', 'Inter', 'Inverness', 'Ipswich', 'Istres', 'Juve Stabia', 'Juventus', 'Karabuekspor', 'Karlsruhe', 'Kasimpasa', 'Kayseri', 'Kilmarnock', 'Koblenz', 'Koeln', 'Konyaspor', 'Kortrijk', 'Las Palmas', 'Latina', 'Lautern', 'Laval', 'Lazio', 'Le Havre', 'Lecce', 'Leeds', 'Leganes', 'Leicester', 'Leiria', 'Leixoes', 'Lens', 'Leuven', 'Levante', 'Leverkusen', 'Lierse', 'Lille', 'Liverpool', 'Livorno', 'Lokeren', 'Lorient', 'Lyon', 'Mainz', 'Malaga', 'Mallorca', 'Man City', 'Man United', 'Manisaspor', 'Mantova', 'Maritimo', 'Marseille', 'Mechelen', 'Metz', 'Middlesbrough', 'Milan', 'Millwall', 'Modena', 'Monaco', 'Montpellier', 'Moreirense', 'Motherwell', 'Mouscron', 'Nacional', 'Nancy', 'Nantes', 'Napoli', 'Naval', 'Newcastle', 'Nice', 'Nijmegen', 'Nimes', 'Niort', 'Nocerina', 'Norwich', 'Novara', 'Nuernberg', 'Oberhausen', 'Olhanense', 'Oostende', 'Orduspor', 'Orleans', 'Osasuna', 'Osnabrueck', 'PSV','Paderborn', 'Padova', 'Palermo', 'Paris FC', 'Paris SG', 'Parma', 'Partick', 'Perugia', 'Pescara', 'Peterboro', 'Piacenza', 'Pisa', 'Plymouth', 'Portimonense', 'Porto', 'Portogruaro', 'Portsmouth', 'Preston', 'QPR', 'RB Leipzig', 'Rangers', 'Rayo Vallecano', 'Reading', 'Real Madrid', 'Regensburg', 'Reggina', 'Reims', 'Rennes', 'Rio Ave', 'Rizespor', 'Roda', 'Roeselare', 'Roma', 'Ross County', 'Rostock', 'Rotherham', 'Saint-Etienne', 'Salernitana', 'Sampdoria', 'Samsunspor', 'Sandhausen', 'Santander', 'Sassuolo', 'Schalke', 'Scunthorpe', 'Sedan', 'Setubal', 'Sevilla', 'Sheffield United', 'Sheffield Weds', 'Siena', 'Sivasspor', 'Sochaux', 'Sociedad', 'Southampton', 'Spal', 'Sparta Rotterdam', 'Spezia', 'Sporting', 'St Johnstone', 'St Mirren', 'St Pauli', 'St Truiden', 'Standard', 'Stoke', 'Strasbourg', 'Stuttgart', 'Sunderland', 'Swansea', 'Tenerife', 'Ternana', 'Tondela', 'Torino', 'Tottenham', 'Toulouse', 'Tours', 'Trabzonspor', 'Trapani', 'Triestina', 'Troyes', 'Twente', 'Udinese', 'Union Berlin', 'Utrecht', 'Valencia', 'Valenciennes', 'Valladolid', 'Vannes', 'Varese', 'Venezia', 'Venlo', 'Verona', 'Vicenza', 'Villarreal', 'Vitesse', 'Waalwijk', 'Watford', 'Werder', 'West Brom', 'West Ham', 'Westerlo', 'Wigan', 'Willem II', 'Wolfsburg', 'Wolves', 'Xerez', 'Yeovil', 'Zaragoza', 'Zulte Waregem', 'Zwolle']
elo_first_date= dict()
elo_team_id = dict()
elo_last_date = dict()

with open(r'C:\Users\Idan\PycharmProjects\project_ai\elo_scores.csv', encoding="utf8") as elo_file:
    ratings =csv.DictReader(elo_file)
    for rating in ratings:
        if rating:
            club = rating['Club']
            data = (float(rating['Elo']), rating['From'], rating['To'])
            elo_team_id[club] = rating['team_id']
            #elo_last_date[club] = rating['From']
            if club not in elo_first_date:
                elo_first_date[club] = rating['From']


field_names = ['team_id', 'Club', 'Elo', 'From', 'To']
output_file_name = 'elo_scores.csv'
#input_file_name = 'Aachen.csv'
#team = 'Aachen'
with open(output_file_name, 'a', encoding="utf8", newline='') as elo_file:
    writer = csv.DictWriter(elo_file, fieldnames=field_names)
    for team in elo_teams:
        #input_file_name = team + '.csv'
        with open(fr"{team}.csv", 'r', encoding="utf8") as team_elo:
            #print(team_elo.read())
            reader = csv.DictReader(team_elo)
            data = dict()
            data['Club'] = team
            data['team_id'] = elo_team_id[team]
            written_something = False
            for row in reader:
            # if row['Club'] != team:
            #     continue
                written_something = True
                data['From'] = row['From']
                data['To'] = row['To']
                data['Elo'] = row['Elo']
                if ('2006-08-01' <= data['From']) and (data['From'] <= elo_first_date[team]):
                #if (elo_last_date[team] <= data['From']):
                    writer.writerow(data)
            if written_something == False:
                print(team)
print("finished")
