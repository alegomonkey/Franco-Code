import re

CheckList = ['Abbeville LA', 'Acadia', 'Acadia Parish', 'Acadiana LA', 'Acadians', 'Acculturation and Assimilation', 'Acushnet MA', 'Adams MA', 'Addison County VT', 'Africa', 'African Americans', 'Alabama', 'Alaska', 'Albanian Americans', 'Albany NY', 'Albany VT', 'Albequerque NM', 'Alberta', 'Albion RI', 'Alburg Springs VT', 'Alburg VT', 'Alcohol and Drugs', 'Aldenville MA', 'Alfred ME', 'Algeria', 'Algonquin', 'Allagash ME', 'Allagash River Valley', 'Allen Parish', 'Allendale RI', 'Allenstown NH', 'Alna ME', 'Alpena MI', 'Alton ME', 'Alton NH', 'Amesbury MA', 'Amherst MA', 'Amherst NH', 'Andover MA', 'Androscoggin County ME', 'Androscoggin River Valley', 'Ann Arbor MI', 'Anoka MN', 'Anson ME', 'Ansonia CT', 'Antilles', 'Appleton ME', 'Arab Americans', 'Arctic Centre RI', 'Arctic RI', 'Argentina', 'Arizona', 'Arkansas', 'Arlington MA', 'Armenian Americans', 'Aroostook County ME', 'Art and Architecture', 'Ascension Parish LA', 'Ashland ME', 'Ashton RI', 'Ashuelot NH', 'Asia', 'Asian Americans', 'Assonet MA', 'Assumption Parish LA', 'Atchafalaya River Valley', 'Attawaugan CT', 'Attleboro MA', 'Auburn MA', 'Auburn ME', 'Auburn NH', 'Audio', 'Augusta ME', 'Aurora IL', 'Australia', 'Austria', 'Austrian Americans', 'Averill VT', 'Avon CT', 'Avon MA', 'Avoyelles Parish LA', 'Azoreans', 'Bailey Island ME', 'Baker Lake ME', 'Bakersfield VT', 'Bakersville VT', 'Bald Brook NH', 'Ballouville CT', 'Baltic CT', 'Baltimore MD', 'Bangor ME', 'Bar Harbor ME', 'Barbeau MI', 'Barnard VT', 'Barnet VT', 'Barre VT', 'Barrington NH', 'Bartlett NH', 'Barton VT', 'Basque', 'Bass River Valley', 'Bath ME', 'Baton Rouge LA', 'Bay City MI', 'Bayonne NJ', 'Beacon Falls CT', 'Bear Brook NH', 'Bedford MA', 'Bedford NH', 'Beebe Plain VT', 'Beebe VT', 'Beecher Falls NH', 'Beecher Falls VT', 'Belfast ME', 'Belgium', 'Belgrade Lakes ME', 'Bellechasse PQ', 'Belmont NH', 'Benedicta ME', 'Bennington County VT', 'Bennington VT', 'Benton ME', 'Berkeley CA', 'Berkeley RI', 'Berkshire County MA', 'Berkshire VT', 'Berlin NH', 'Berwick ME', 'Bethel CT', 'Bethel ME', 'Beverly MA', 'Bibliography', 'Biddeford ME', 'Big Sur CA', 'Billerica MA', 'Bingham ME', 'Biography', 'Black Brook NY', 'Blackstone MA', 'Blackstone RI', 'Blackstone River Valley', 'Blackstone Valley RI', 'Blaine ME', 'Blanchard ME', 'Bloomfield VT', 'Blooming Grove NY', 'Blue Hill ME', 'Bondsville MA', 'Boothbay ME', 'Boston MA', 'Bourbonnais IL', 'Bowenville MA', 'Bradford ME', 'Bradley IL', 'Bradley ME', 'Braintree MA', 'Brandon NY', 'Brandon VT', 'Branford CT', 'Brasher Falls NY', 'Brassua (Me?)', 'Brattleboro VT', 'Brazil', 'Breaux Bridge LA', 'Brentwood NH', 'Brewer ME', 'Brewster MA', 'Bridgeport CT', 'Brighton MA', 'Brighton VT', 'Bristol County MA', 'Bristol CT', 'Bristol VT', 'British Columbia', 'Brockton MA', 'Brookfield MA', 'Brookfield NH', 'Brooklyn CT', 'Brooklyn NY', 'Brookton ME', 'Brownington VT', 'Brownville ME', 'Brunswick ME', 'Bucks Harbor ME', 'Bucksport ME', 'Buffalo NY', 'Bulgaria', 'Burke NY', 'Burlington NC', 'Burlington VT', 'Burrillville RI', 'Business and Economics', 'Buxton ME', 'Cabot VT', 'Cabotville MA', 'Cadillac MI', 'Cajuns', 'Calais ME', 'Calcasieu Parish LA', 'Calcasieu River Valley', 'Caledonia County VT', 'California', 'Calumet MI', 'Cambodia', 'Cambridge MA', 'Canaan VT', 'Canada', 'Cane River LA', 'Canton CT', 'Canton MA', 'Canton ME', 'Canton NY', 'Cape Cod MA', 'Cape Elizabeth ME', 'Cape Porpoise ME', 'Cape Verdean Americans', 'Cape Vincent NY', 'Caratunk ME', 'Carencro LA', 'Caribbean', 'Caribou ME', 'Carolltown MI', 'Cascade NH', 'Casco ME', 'Castine ME', 'Castleton VT', 'Caswell ME', 'Centerville MA', 'Central Falls RI', 'Central Village CT', 'Centreville CT', 'Chackbay LA', 'Champlain NY', 'Charles River Valley', 'Charleston SC', 'Charleston VT', 'Charlestown MA', 'Charlestown NH', 'Charlotte VT', 'Chasm Falls NY', 'Chatham MA', 'Chaudiere River Valley', 'Chazy NY', 'Cheboygan MI', 'Chelmsford MA', 'Chelsea MA', 'Chelsea ME', 'Chelsea VT', 'Chesterville ME', 'Chesterville VT', 'Chesuncook ME', 'Chicago IL', 'Chichester NH', 'Chicopee Falls MA', 'Chicopee MA', "Children's Literature", 'China', 'Chinese Americans', 'Chisholm ME', 'Chittenden County VT', 'Churubusco NY', 'Cincinnatti OH', 'Claire ME', 'Claremont NH', 'Clarendon VT', 'Clarksville NH', 'Clayton Lake ME', 'Clayton NY', 'Clayville RI', 'Cleghorn MA', 'Cleveland OH', 'Clinton MA', 'Clintonville NY', 'Cloquet MN', 'Clubs and Societies', 'Clyde RI', 'Cobbosseecontee Lake ME', 'Coburn Gore ME', 'Cochituate MA', 'Cohoes NY', 'Colchester VT', 'Colebrook NH', 'Coles Grove NH', 'Colombia', 'Colorado', 'Columbia NH', 'Columbia SC', 'Community: Customs and Social Life', 'Concord MA', 'Concord ME', 'Concord NH', 'Concord River Valley', 'Conference Proceedings', 'Conifer NY', 'Connecticut', 'Connecticut River Valley', 'Constable NY', 'Conway NH', 'Cooks Mills MI', 'Cooperville NY', 'Coos County NH', 'Cornville ME', 'Coventry CT', 'Coventry RI', 'Coventry VT', 'Creoles', 'Criticism and Review', 'Croatian Americans', 'Crompton RI', 'Cromwell CT', 'Crown Point IN', 'Crown Point NY', 'Cuba', 'Cultural Studies: Ethnicity and Collective Identity', 'Cumberland County ME', 'Cumberland ME', 'Cumberland Mills ME', 'Cumberland RI', 'Cushing ME', 'Cut Off LA', 'Cyr ME', 'Dafoe MI', 'Daigle ME', 'Damariscotta ME', 'Damariscotta Mills ME', 'Danbury CT', 'Danforth ME', 'Danielson CT', 'Danielsonville CT', 'Danish Americans', 'Dannemora NY', 'Dartmouth NH', 'Dayville CT', 'Dead River Valley ME', 'Death and Disaster', 'Dedham MA', 'Deerfield MA', 'Delaware', 'Demography', 'Dennisport MA', 'Dennistown ME', 'Denver CO', 'Derby CT', 'Derby Line VT', 'Derby VT', 'Derry NH', 'Detroit ME', 'Detroit MI', 'Dexter ME', 'Dickey ME', 'Dighton MA', 'Dixfield ME', 'Dixville NH', 'Dodgeville MA', 'Dorchester MA', 'Douglas MA', 'Dover NH', 'Dracut MA', 'Dresden ME', 'Dubuque IA', 'Duchess County NY', 'Dudley MA', 'Duluth MN', 'Dummer NH', 'Dunbarton NH', 'Duralde LA', 'Durham NC', 'Durham NH', 'Duson LA', 'Eagle Island ME', 'Eagle Lake ME', 'Eagleville CT', 'East Chelmsford MA', 'East Concord NH', 'East Dorset VT', 'East Douglas MA', 'East Greenbush NY', 'East Greenwich RI', 'East Hartford CT', 'East Killingly CT', 'East Lansing MI', 'East Rutland VT', 'East Taunton MA', 'Easthampton MA', 'Easton MA', 'Easton NH', 'Eastport ME', 'Eden VT', 'Education', 'Ellenburg NY', 'Ellsworth ME', 'Elmville CT', 'Emigration and Immigration', 'Enfield NH', 'England', 'English Americans', 'Enosburg Falls VT', 'Enosburg VT', 'Epping NH', 'Erath LA', 'Erie NY', 'Errol NH', 'Escanaba IL', 'Esmond RI', 'Essay', 'Essex County MA', 'Essex County VT', 'Essex Junction VT', 'Essex VT', 'Estonia', 'Ethiopia', 'Ethnicity and Collective Identity', 'Europe', 'Eustis ME', 'Evangeline Parish LA', 'Eveleth MN', 'Everett MA', 'Excelville CT', 'Exeter ME', 'Exeter NH', 'Exeter RI', 'Exploration and Colonization', 'Fair Haven VT', 'Fairfax VT', 'Fairfield ME', 'Fairfield VT', 'Fairhaven MA', 'Fall River MA', 'Falmouth MA', 'Falmouth ME', 'False River LA', 'Family', 'Faribault MN', 'Farming and Agriculture', 'Farmingdale ME', 'Farmington ME', 'Farmington NH', 'Federal Hill RI', 'Ferrisburgh VT', 'Fiction and Literature', 'Filipino Americans', 'Film and Television', 'Finland', 'Finnish Americans', 'Fisherville MA', 'Fishing', 'Fishkill NY', 'Fiskdale MA', 'Fiskeville RI', 'Fitchburg MA', 'Fitzwilliam NH', 'Five Islands ME', 'Flagstaff ME', 'Flint Village MA', 'Florida', 'Folklore', 'Food', 'Forestdale RI', 'Forestry', 'Fort Covington NY', 'Fort Fairfield ME', 'Fort Kent ME', 'Fort Ticonderoga NY', 'Framingham MA', 'France', 'Franklin County ME', 'Franklin County VT', 'Franklin NH', 'Franklin VT', 'Freeport ME', 'Freetown MA', 'French Hill MA', 'French Hill NY', 'French Island ME', 'Frenchtown ME', 'Frenchtown RI', 'Frenchville ME', 'Friendship ME', 'Fryeburg ME', 'Fur-trading', 'Galliano LA', 'Gardiner ME', 'Gardiner NY', 'Gardner MA', 'Gardner MI', 'Gender and Sexuality', 'Genealogy', 'Geography', 'Georgetown ME', 'Georgia', 'Georgia VT', 'Georgiaville RI', 'German Americans', 'Germany', 'Gheens LA', 'Gilbertville MA', 'Gilead ME', 'Gilmanton NH', 'Glasgo CT', 'Glencliff NH', 'Glens Falls NY', 'Glenwood Springs CO', 'Globe Village MA', 'Gloucester MA', 'Glover VT', 'Goffstown NH', 'Golden Meadow LA', 'Gonic NH', 'Gorham ME', 'Gorham NH', 'Goshen NH', 'Gouldsboro ME', 'Government and Politics', 'Grafton MA', 'Grand Bois LA', 'Grand Falls ME', 'Grand Haven MI', 'Grand Isle County VT', 'Grand Isle LA', 'Grand Isle ME', 'Grand Isle VT', 'Grand Rapids MI', 'Graniteville VT', 'Great Britain', 'Great Falls NH', 'Great Lakes Region', 'Greece', 'Greek Americans', 'Green Bay WI', 'Greenbush ME', 'Greendale MA', 'Greene ME', 'Greeneville CT', 'Greenland MI', 'Greenland NH', 'Greenville ME', 'Greenville NH', 'Greenville SC', 'Greenwich CT', 'Griswold CT', 'Grosvenordale CT', 'Groton CT', 'Groton MA', 'Groveton NH', 'Guadeloupe', 'Haddam CT', 'Hadley Falls MA', 'Haiti', 'Hallowell ME', 'Hamlet RI', 'Hamlin ME', 'Hampden County MA', 'Hampden ME', 'Hampshire County MA', 'Hancock County ME', 'Hanover NH', 'Harborside ME', 'Hardwick MA', 'Hardwick VT', 'Harris RI', 'Harrison ME', 'Harrisville NH', 'Hartford CT', 'Hastings ME', 'Haverhill MA', 'Haverhill NH', 'Hawaii', 'Hazardville CT', 'Health and Wellness', 'Hebron ME', 'Henniker NH', 'Highgate VT', 'Hillsboro NH', 'Hillsborough County NH', 'Hillsborough NH', 'Hingham MA', 'Hispanic Americans', 'Hockanum River Valley', 'Hogansville GA', 'Holden MA', 'Holeb ME', 'Holland', 'Holland VT', 'Hollis ME', 'Hollywood FL', 'Holyoke MA', 'Hooksett NH', 'Hopeville MA', 'Houghton County MI', 'Houlton ME', 'Houma LA', 'Hubbard NH', 'Hudson Bay', 'Hudson Falls NY', 'Hudson MA', 'Hudson NH', 'Hudson River Valley', 'Huguenots', 'Hull QC', 'Hungarian Americans', 'Hungary', 'Hunting', 'Huntington CT', 'Hyannis MA', 'Hyde Park VT', 'Iberia Parish LA', 'Idaho', 'Illinois', 'Illness', 'Immigration', 'India', 'Indian Island ME', 'Indian Orchard MA', 'Indiana', 'Indianapolis IN', 'Interview', 'Iowa', 'Ipswich MA', 'Iran', 'Irasburg VT', 'Ireland', 'Irish Americans', 'Iron Mountain MI', 'Iroquois', 'Ishpeming MI', 'Island Falls ME', 'Island Pond VT', 'Isle au Haut ME', 'Isle LaMotte VT', 'Israel', 'Italian Americans', 'Italy', 'Jackman ME', 'Jackson NH', 'Jaffrey NH', 'Jamaica', 'Jamesville MA', 'Japan', 'Japanese Americans', 'Jay ME', 'Jay VT', 'Jefferson Davis Parish LA', 'Jericho VT', 'Jersey City NJ', 'Jerusalem', 'Jewett City CT', 'Jewish Americans', 'Johnson VT', 'Journalism', 'Kankakee County IL', 'Kankakee IL', 'Kansas', 'Kansas City MO', 'Keegan ME', 'Keene NH', 'Keeseville NY', 'Kennebago ME', 'Kennebec County ME', 'Kennebec River Valley', 'Kennebunk ME', 'Kennebunkport ME', 'Kensington NH', 'Kent County RI', 'Kentucky', 'Kenyon RI', 'Keweenaw Peninsula MI', 'Kezar Lake ME', 'Killingly CT', 'Killington VT', 'Kingfield ME', 'Kingston NH', 'Kittery ME', 'Knox County ME', 'Korea', 'Korean Americans', 'Kraemer LA', "L'Arable IL", 'La Beauce QC', 'Labadieville LA', 'Labor History', 'Labrador', 'Laconia NH', 'Lafayette IN', 'Lafayette LA', 'Lafayette Parish LA', 'Lafourche Parish LA', 'Lake Champlain VT', 'Lake Charles LA', 'Lake Clear NY', 'Lake Linden MI', 'Lake Winepesaukee NH', 'Lake Winnipesaukee NH', 'Lakeside VT', 'Lamoille County VT', 'Landaff NH', 'Language and Linguistics', 'Laos', 'Larchmont NY', 'Larose LA', 'Latin America', 'Latvian Americans', 'Lawrence MA', 'Lawrenceville NY', 'Lebanese Americans', 'Lebanon', 'Lebanon NH', 'Lectures', 'Ledyard CT', 'Leeds ME', 'Leeville LA', 'Leicester VT', 'Leominster MA', 'Lewiston ME', 'Lexington MA', 'Lille ME', 'Limerick ME', 'Limerock RI', 'Limestone ME', 'Limington ME', 'Lincoln County ME', 'Lincoln ME', 'Lincoln NE', 'Lincoln NH', 'Lincoln RI', 'Linwood MI', 'Lippit RI', 'Lippitsville RI', 'Lisbon Falls ME', 'Lisbon ME', 'Litchfield ME', 'Litchfield NH', 'Literary Works', 'Literary Works -- Anthology', "Literary Works -- Children's Literature", 'Literary Works -- Criticism and History', 'Literary Works -- Drama', 'Literary Works -- Fiction', 'Literary Works -- Other', 'Literary Works -- Poetry', 'Literary Works -- Short fiction', 'Literary Works -- Travel writing', 'Lithuania', 'Lithuanian Americans', 'Littleton MA', 'Littleton NH', 'Livermore Falls ME', 'Livermore ME', 'London ENG', 'Londonderry NH', 'Long Lake ME', 'Long Lake NY', 'Long Pond ME', 'Lonsdale RI', 'Los Angeles CA', 'Lothrop ME', 'Louisiana', 'Louisville KY', 'Lovell ME', 'Lowell MA', 'Lowell VT', 'Lowelltown ME', 'Lower Vacherie LA', 'Ludington MI', 'Ludlow MA', 'Lynchburg VA', 'Lyndeborough NH', 'Lyndon VT', 'Lyndonville VT', 'Lynn MA', 'Machias ME', 'Mackinac Island', 'Madawaska ME', 'Madison ME', 'Madison NH', 'Maidstone VT', 'Maine', 'Malden MA', 'Mali', 'Maliseets', 'Malone NY', 'Mamou LA', 'Manana Island ME', 'Manchang MA', 'Manchester CT', 'Manchester ME', 'Manchester NH', 'Manchester VT', 'Manistee MI', 'Manitoba', 'Mansfield MA', 'Manteno IL', 'Manville RI', 'Mapleton ME', 'Mapleville RI', 'Marblehead MA', 'Marieville RI', 'Marinette WI', 'Marion IL', 'Marion MA', 'Marksville LA', 'Marlboro MA', 'Marlborough NH', 'Marquette MI', 'Mars Hill ME', 'Martinique', 'Martinsburg NY', 'Maryland', 'Mashpee MA', 'Massachusetts', 'Massena NY', 'Mattapoisett MA', 'Mattawamkeag River Valley', 'Mauchburg MA', 'Mechanic Falls ME', 'Mechanicsville CT', 'Mechanicsville MA', 'Mechanicville NY', 'Medfield MA', 'Medford MA', 'Medway ME', 'Melrose MA', 'Memphis TN', 'Mendota MN', 'Menomenee MI', 'Mercer ME', 'Meriden CT', 'Merrimac MA', 'Merrimack County NH', 'Merrimack River Valley', 'Methuen MA', 'Mexican Americans', 'Mexico', 'Mexico ME', "Mi'kmaq", 'Miami FL', 'Michigan', 'Midcoast Region ME', 'Middlebury VT', 'Middlefield NY', 'Middlesex County MA', 'Middlesex VT', 'Middletown CT', 'Midland MI', 'Milan NH', 'Milford CT', 'Milford ME', 'Millbury MA', 'Millinocket ME', 'Mills and Mill Work', 'Millville MA', 'Milton MA', 'Milton VT', 'Milwaukee WI', 'Mining', 'Minneapolis MN', 'Minnesota', 'Minot ME', 'Mississippi', 'Mississippi River Valley', 'Missouri', 'Mobile AL', 'Moers Forks NY', 'Mohawk', 'Mohawk River Valley', 'Momence IL', 'Monkton VT', 'Monroe County MI', 'Monroe NH', 'Monson MA', 'Montague MA', 'Montague ME', 'Montana', 'Montgomery VT', 'Montpelier VT', 'Montréal QC', 'Montville CT', 'Moontville ME', 'Moose River Valley', 'Moosehead Lake Region', 'Moosup CT', 'Moretown VT', 'Morocco', 'Morrisonville NY', 'Morristown VT', 'Morses Line VT', 'Moscow RUS', 'Mossasuck River Valley', 'Moultonborough NH', 'Moxie ME', 'Mt. Desert Island ME', 'Music', 'Muskegon MI', 'Narragansett RI', 'Nash Stream NH', 'Nashoba Valley MA', 'Nashua NH', 'Nashville TN', 'Natick RI', 'Native Americans', 'Naugatuck CT', 'Nebraska', 'Nevada', 'New Auburn ME', 'New Bedford MA', 'New Boston CT', 'New Braintree MA', 'New Britain CT', 'New Brunswick', 'New Canada ME', 'New England', 'New Gloucester ME', 'New Hampshire', 'New Harbor ME', 'New Hartford CT', 'New Haven County CT', 'New Haven CT', 'New Haven VT', 'New Jersey', 'New London County CT', 'New London CT', 'New Mexico', 'New Orleans LA', 'New Paltz NY', 'New Rochelle NY', 'New Sweden ME', 'New Worcester MA', 'New York', 'New York NY', 'New Zealand', 'Newark NJ', 'Newbury VT', 'Newburyport MA', 'Newcastle ME', 'Newcomb NY', 'Newfoundland', 'Newman GA', 'Newport NH', 'Newport RI', 'Newport VT', 'Newton MA', 'Niagara Falls NY', 'Niles Mich', 'NMDC', 'Nobleboro ME', 'Nonfiction', 'Nonfiction -- Anthology', 'Nonfiction -- Anthropology', 'Nonfiction -- Art and Architecture', 'Nonfiction -- Demography', 'Nonfiction -- Education', 'Nonfiction -- Essay', 'Nonfiction -- Ethnic Studies', 'Nonfiction -- Folklore', 'Nonfiction -- French in North America', 'Nonfiction -- Geography', 'Nonfiction -- Government and Politics', 'Nonfiction -- Historiography', 'Nonfiction -- History', "Nonfiction -- History -- Children's Literature", 'Nonfiction -- History -- Clubs and Societies', 'Nonfiction -- History -- Documentary', 'Nonfiction -- History -- Economic and Industrial', 'Nonfiction -- History -- French in North America', 'Nonfiction -- History -- General', 'Nonfiction -- History -- Intellectual', 'Nonfiction -- History -- Labor and Social', 'Nonfiction -- History -- Local', 'Nonfiction -- History -- Pictorial', 'Nonfiction -- History -- Religion', 'Nonfiction -- Immigration', 'Nonfiction -- Journalism', 'Nonfiction -- Journals and Letters', 'Nonfiction -- Language and Linguistics', 'Nonfiction -- Music', 'Nonfiction -- Performance Studies', 'Nonfiction -- Psychology', 'Nonfiction -- Science and Medicine', 'Nonfiction -- Social Science: Anthropology and Sociology', 'Nonfiction -- Social Sciences', 'Nonfiction -- Sociology', 'Nonfiction -- Sports', 'Nonfiction -- Travel and Tourism', 'Norfolk County MA', 'Norfolk NY', 'Norridgewock ME', 'North Adams MA', 'North America', 'North Anson ME', 'North Attleborough MA', 'North Bangor NY', 'North Billerica MA', 'North Brookfield MA', 'North Carolina', 'North Concord VT', 'North Dakota', 'North Dartmouth MA', 'North Easton CT', 'North Grosvenordale CT', 'North Haven CT', 'North Hero VT', 'North Monmouth ME', 'North Shore MA', 'North Troy VT', 'North Uxbridge MA', 'North Whitefield ME', 'North Windham CT', 'North Yarmouth ME', 'Northampton MA', 'Northbridge MA', 'Northeast Kingdom VT', 'Northern Ireland', 'Northport NY', 'Northumberland NH', 'Norton MA', 'Norton VT', 'Norwalk CT', 'Norway', 'Norwegian Americans', 'Norwich CT', 'Norwich Falls CT', 'Notre Dame IN', 'Notre Dame ME', 'Nova Scotia', 'Oak Bluffs MA', 'Oakdale LA', 'Oakland ME', 'Occum CT', 'Ogdensburg NY', 'Ogunquit ME', 'Ohio', 'Oklahoma', 'Old Orchard Beach ME', 'Old Town ME', 'Olneyville RI', 'Onaway MI', 'Oneco CT', 'Oneida NY', 'Onendaga NY', 'Onset MA', 'Ontario', 'Opelousas LA', 'Oquossoc ME', 'Orange County VT', 'Orange VT', 'Oregon', 'Orford NH', 'Orland ME', 'Orlando FL', 'Orleans County VT', 'Orleans MA', 'Orono ME', "Orr's Island ME", 'Osterville MA', 'Oswego NY', 'Ottawa ON', "Owl's Head ME", 'Oxbow ME', 'Oxford County ME', 'Oxford MA', 'Oxford NH', 'Ozone Park NY', 'Palmer CT', 'Palmer MA', 'Papineau IL', 'Paraguay', 'Paris FR', 'Parks LA', 'Parlin Pond ME', 'Parmacheenee ME', 'Pascoag RI', 'Passamaquoddy', 'Passamaquoddy Township ME', 'Paterson NJ', 'Pawtucket RI', 'Pawtucketville MA', 'Pawtuxet River Valley', 'Pembroke NH', 'Pennsylvania', 'Penobscot', 'Penobscot County ME', 'Penobscot River Valley', 'Pepperell MA', 'Performing Arts', 'Perkins MI', 'Personal History: Biography and Oral History', 'Peru', 'Peru NY', 'Peterborough NH', 'Petersham MA', 'Petroleum', 'Phenix RI', 'Philadelphia PA', 'Phillipstown ME', 'Phippsburg ME', 'Phoenix RI', 'Photography', 'Piercefield NY', 'Piermont NH', 'Pierre SD', 'Pinconning MI', 'Pineville CT', 'Piscataquis County ME', 'Piscataquis River Valley', 'Pittsburg NH', 'Pittsburgh PA', 'Pittsfield MA', 'Pittsfield ME', 'Pittston ME', 'Plainfield CT', 'Plainfield NH', 'Plainville CT', 'Plaisted ME', 'Plattsburgh NY', 'Pleasant Point ME', 'Plymouth County MA', 'Plymouth MA', 'Pocasset MA', 'Poetry', 'Pointe Coupée Parish LA', 'Poland', 'Polish Americans', 'Polk Countyy MI', 'Pomfret CT', 'Pontook Reservoir NH', 'Popham ME', 'Portage Lake ME', 'Portland ME', 'Portsmouth NH', 'Portugal', 'Portuguese Americans', 'Pownal ME', 'Pownal VT', 'Prairie du Rocher IL', 'Presque Isle ME', 'Presumpscot River Valley', 'Prince Edward Island', 'Proctor VT', 'Providence RI', 'Provincetown MA', 'Puerto Rico', 'Putnam CT', 'Putney VT', 'Quarry Island ME', 'Québec', 'Québec City QC', 'Quequechan River Valley', 'Quincy MA', 'Quinebaug CT', 'Quinebaug River Valley', 'Quinnville RI', 'Radio', 'Rangeley ME', 'Rapid City SD', 'Raymond ME', 'Raynham MA', 'Readfield ME', 'Reading MA', 'Readsboro VT', 'Red River Valley', 'Rehoboth MA', 'Religion', 'Rhode Island', 'Richford VT', 'Richmond Hill NY', 'Richmond ME', 'Richmond NH', 'Richmond VT', 'Riley ME', 'River Raisin', 'Riverpoint RI', 'Riviere Verte ME', 'Robinhood ME', 'Rochester NH', 'Rochester NY', 'Rockingham County NH', 'Rockingham VT', 'Rockland ME', 'Rockport ME', 'Rockville CT', 'Rockwood ME', 'Rogers MA', 'Rollinsford NH', 'Rome IT', "Rouse's Point NY", "Rouse's Point VT", 'Rowley MA', 'Roxbury MA', 'Roxbury NH', 'Rumford Falls ME', 'Rumford ME', 'Rumney NH', 'Russia', 'Russian Americans', 'Rutland County VT', 'Rutland MA', 'Rutland VT', 'Rwanda', 'Rye NH', 'Rye NY', 'Sabattus ME', 'Saco ME', 'Saco River Valley', 'Sacramento CA', 'Sagadahoc County ME', 'Saginaw MI', 'Saginaw River Valley', 'Saint John River Valley', 'Salem MA', 'Salem NH', 'Salisbury MA', 'Salmon Falls NH', 'San Francisco CA', 'Sanbornville NH', 'Sand Hill ME', 'Sandwich MA', 'Sanford MA', 'Sanford ME', 'Saranac River Valley', 'Saratoga Springs NY', 'Saratoga WY', 'Saskatchewan', 'Saugus (Mass.)', 'Sault Sainte Marie MI', 'Sawyerville NH', 'Saylesville RI', 'Scandinavian Americans', 'Scarborough ME', 'Schenectady NY', 'Scituate RI', 'Scofield ME', 'Scotland', 'Scott LA', 'Scottish Americans', 'Seabrook NH', 'Searsport ME', 'Seattle WA', 'Sebasticook River Valley', 'Seekonk MA', 'Seguin Island ME', 'Senegal', 'Seymour CT', 'Sharon Heights MA', 'Sharpsburg PA', 'Shelburne NH', 'Shelburne VT', 'Sheldon Springs VT', 'Sheldon VT', 'Shelton CT', 'Sheridan ME', 'Shetland Islands', 'Shetucket River Valley', 'Shirley MA', 'Shirley ME', 'Shoreham VT', 'Sicilian Americans', 'Sicily', 'Sidney ME', 'Sinclair ME', 'Skinner ME', 'Skowhegan ME', 'Slatersville RI', 'Slavic Americans', 'Slovak Americans', 'Smithfield RI', 'Social History', 'Sociology', 'Soldier Pond ME', 'Solon ME', 'Somers CT', 'Somerset County ME', 'Somerset MA', 'Somersworth NH', 'Somerville MA', 'Somerville NH', 'South Addison ME', 'South Africa', 'South Asia', 'South Bellingham MA', 'South Berwick ME', 'South Billingham MA', 'South Boston MA', 'South Brewer ME', 'South Bristol ME', 'South Burlington VT', 'South Carolina', 'South China ME', 'South Coventry CT', 'South Dakota', 'South Fitchburg MA', 'South Freeport ME', 'South Hadley MA', 'South Hero VT', 'South Portland ME', 'South Waldoboro ME', 'South Waterford ME', 'South Worcester MA', 'Southbridge MA', 'Southington CT', 'Spain', 'Spalding MI', 'Spanish Americans', 'Speculator Lake NY', 'Spencer MA', 'Spicket River', 'Sports and Leisure', 'Sprague CT', 'Springfield MA', 'Springfield VT', 'Springvale ME', 'Sri Lanka', 'St. Agatha ME', 'St. Albans NY', 'St. Albans VT', 'St. Croix River Valley', 'St. David ME', 'St. Francis ME', 'St. Genevieve MO', 'St. George IL', 'St. George VT', 'St. Ignace MI', 'St. James Parish LA', 'St. John ME', 'St. John River Valley', 'St. Johnsbury VT', 'St. Joseph MI', 'St. Landry Parish LA', 'St. Lawrence River Valley', 'St. Louis MO', 'St. Luce ME', 'St. Martin Parish LA', 'St. Martinville LA', "St. Mary's Parish LA", 'St. Paul MN', 'St. Petersburg FL', 'St. Regis Falls NY', 'St. Regis NY', 'St. Zacharie ME', 'Stafford CT', 'Stafford Springs CT', 'Stamford CT', 'Standish ME', 'Starks ME', 'Staten Island NY', 'Ste. Anne IL', 'Ste. Marie IL', 'Steep Falls ME', 'Sterling CT', 'Stewartstown NH', 'Stockholm ME', 'Stonecutting', 'Stoneham MA', 'Stonington CT', 'Stonington ME', 'Stoughton MA', 'Stow MA', 'Stowe VT', 'Stratford County NH', 'Stratford NH', 'Stratham NH', 'Stratton ME', 'Stroudwater ME', 'Sturbridge MA', 'Sudan', 'Sulphur LA', 'Suncook NH', 'Susquehanna River Valley', 'Sutton MA', 'Sutton NH', 'Sutton VT', 'Swansea MA', 'Swanton VT', 'Sweden', 'Swedish Americans', 'Swiss Americans', 'Switzerland', 'Syracuse NY', 'Syria', 'Syrian Americans', 'Taftville CT', 'Tamworth NH', 'Tarrytown NY', 'Taunton MA', 'Taunton River Valley', 'Teche Parish LA', 'Tennessee', 'Terre Haute IN', 'Terrebonne Parish LA', 'Texas', 'The Weirs NH', 'Thomaston ME', 'Thompson CT', 'Thompsonville CT', 'Thorndike MA', 'Thorndike ME', 'Thornton NH', 'Three Rivers MA', 'Ticonderoga NY', 'Tilton NH', 'Tiverton RI', 'Tivoli NY', 'Topsfield ME', 'Topsham ME', 'Toronto ON', 'Torrington CT', 'Townsend MA', 'Trapping', 'Travel and Movement', 'Trois-Rivières QC', 'Trout River NY', 'Trowbridgeville MA', 'Troy NH', 'Troy NY', 'Troy VT', 'Trumbull CT', 'Tunisia', 'Tupper Lake NY', 'Turner ME', 'Turners Falls MA', 'Twin Mountain NH', 'Tyngsboro MA', 'Underhill VT', 'Union ME', 'Unionville CT', 'United States', 'Upper Frenchville ME', 'Upper Peninsula MI', 'Upper Saranac Lake NY', 'Uruguay', 'US Midwest', 'US Northwest', 'US South', 'US Southwest', 'Utah', 'Valley Falls MA', 'Valley Falls RI', 'Van Buren ME', 'Vanceboro ME', 'Vancouver BC', 'Vassalboro ME', 'Veazie ME', 'Vergennes VT', 'Vermilion Parish LA', 'Vermont', 'Versailles CT', 'Viennese Americans', 'Vietnam', 'Vietnamese Americans', 'Ville Platte LA', 'Vincennes IN', 'Violence', 'Virginia', 'Voluntown CT', 'Wabanaki', 'Wakefield MA', 'Walden VT', 'Waldo County ME', 'Waldoboro ME', 'Wales ME', 'Wallagrass ME', 'Wallingford CT', 'Waltham MA', 'Wanton VT', 'Wappingers Falls NY', 'War', 'Ware MA', 'Wareham MA', 'Warren MA', 'Warren NH', 'Warren RI', 'Warwick RI', 'Washburn ME', 'Washington', 'Washington County ME', 'Washington County VT', 'Washington DC', 'Waterboro ME', 'Waterbury CT', 'Waterbury VT', 'Waterford NY', 'Watertown CT', 'Watertown MA', 'Watertown NY', 'Waterville CT', 'Waterville ME', 'Waterville Valley NH', 'Wauregan CT', 'Wayne County MI', 'Wayne ME', 'Weaverton RI', 'Webster MA', 'Webster ME', 'Wellesley MA', 'Wellfleet MA', 'Wells ME', 'West Baton Rouge Parish LA', 'West Burke VT', 'West Derby VT', 'West Forks ME', 'West Groton MA', 'West Hartford CT', 'West Haven CT', 'West Indies', 'West Lafayette IN', 'West Milan NH', 'West Point ME', 'West Rutland VT', 'West Springfield MA', 'West Virginia', 'West Warwick RI', 'Westborough MA', 'Westbrook ME', 'Westerly RI', 'Westfield MA', 'Westfield ME', 'Westfield VT', 'Westford VT', 'Westmanland ME', 'Westminster MA', 'Westminster VT', 'Westmore VT', 'Weston MA', 'Westport MA', 'Westwego LA', 'Wethersfield CT', 'Weymouth MA', 'White River Junction VT', 'Whitefield ME', 'Whitehall NY', 'Whiting VT', 'Whitinsville MA', 'Whitney Park NY', 'Wickford RI', 'Wierville RI', 'Wildwood NJ', 'Wilkinsonville CT', 'Williamstown MA', 'Williamstown VT', 'Williamsville CT', 'Willimantic CT', 'Willimantic River Valley', 'Wilmington MA', 'Wilmington VT', 'Wilton NH', 'Winchendon MA', 'Winchester NH', 'Windham County CT', 'Windham County VT', 'Windsor County VT', 'Windsor Locks CT', 'Windsor ME', 'Windsor Mills CT', 'Windsor VT', 'Winn ME', 'Winnegance ME', 'Winnipeg MAN', 'Winooski Falls VT', 'Winooski VT', 'Winslow ME', 'Winsted CT', 'Winter Harbor ME', 'Winterville ME', 'Winthrop ME', 'Winthrop NY', 'Wisconsin', 'Woburn MA', 'Wolcott VT', 'Woodbury NH', 'Woodland ME', 'Woodstock NH', 'Woodville RI', 'Woolwich ME', 'Woonasquatucket River Valley', 'Woonsocket RI', 'Worcester County MA', 'Worcester MA', 'Wyoming', 'Wyoming RI', 'Yantic CT', 'Yarmouth ME', 'York County ME', 'York ME', 'Young Adult Literature', 'Youth', 'Yugoslavia']

# Python script to process strings and write to a file
def process_and_write(strings, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for string in strings:
            # Replace spaces with "+"
            modified_string = string.replace(" ", "+")
            # Write to file in the required format
            f.write(f'<a href="https://francolibrary.org/items/browse?tags={modified_string}>{string}<a>\n')

# Output to 'tagLinks.txt'
process_and_write(CheckList, "tagLinks.txt")


