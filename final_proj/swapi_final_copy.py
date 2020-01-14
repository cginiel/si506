import json, requests, copy

ENDPOINT = 'https://swapi.co/api'

PEOPLE_KEYS = ("url", "name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year", "gender", "homeworld", "species",)
PLANETS_KEYS = ("url", "name", "system_position", "natural_satellites", "rotation_period", "orbital_period", "diameter", "climate", "gravity", "terrain", "surface_water", "population", "indigenous_life_forms",)
STARSHIP_KEYS = ("url", "starship_class", "name", "model", "manufacturer", "length", "width", "max_atmosphering_speed", "hyperdrive_rating", "MGLT", "crew", "passengers", "cargo_capacity", "consumables", "armament",)
SPECIES_KEYS = ("url", "name", "classification", "designation", "average_height", "skin_colors", "hair_colors", "eye_colors", "average_lifespan", "language",)
VEHICLES_KEYS = ("url", "vehicle_class", "name", "model", "manufacturer", "length", "max_atmosphering_speed", "crew", "passengers", "cargo_capacity", "consumables", "armament",)


def read_json(filepath):
    """Given a valid filepath, reads a JSON document and returns a dictionary.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: decoded JSON document expressed as a dictionary.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data

def get_swapi_resource(url, params=None):
    """Issues an HTTP GET request to return a representation of a resource. If no category is
    provided, the root resource will be returned. An optional query string of key:value pairs
    may be provided as search terms (e.g., {'search': 'yoda'}). If a match is achieved the
    JSON object that is returned will include a list property named 'results' that contains the
    resource(s) matched by the search query.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.

    Returns:
        dict: decoded JSON document expressed as dictionary.
    """

    if params:
        response = requests.get(url, params=params).json()
    else:
        response = requests.get(url).json()

    return response

def combine_data(default_data, override_data):
    """Creates a shallow copy of the default dictionary and then updates the new
    copy with override data. Override values will replace default values when if
    the keys match.

    For shallow vs deep copying of mutable objects like dictionaries and lists see:
    https://docs.python.org/3/library/copy.html

    For another approach see unpacking, see: https://www.python.org/dev/peps/pep-0448/

    Parameters:
        default_data (dict): entity data that provides the default representation of the object.
        override_data (dict): entity data intended to override matching default values.

    Returns:
        dict: updated dictionary that contains override values.

    """

    combined_data = default_data.copy()  # shallow
    # combined_data = copy.copy(default_data) # shallow
    # combined_data = copy.deepcopy(default_data) # deep
    combined_data.update(override_data)  # in place

    # Dictionary unpacking
    # combined_data = {**default_data, **override_data}

    return combined_data

def filter_data(data, filter_keys):
    """Returns a new dictionary based containing a filtered subset of key-value pairs
    sourced from a dictionary provided by the caller.

    Parameters:
        data (dict): source entity.
        filter_keys (tuple): sequence of keys used to select a subset of key-value pairs.

    Returns:
        dict: a new entity containing a subset of the source entity's key-value pairs.

    """

    # Alternative: dictionary comprehension (post-Thanksgiving discussion)
    # return {key: data[key] for key in filter_keys if key in data.keys()}

    record = {}
    for key in filter_keys:
        if key in data.keys():
            record[key] = data[key]

    return record

def is_unknown(value):
    """
    Determines whether the value is unknown or n/a using a Truth test.

    Parameters:
        Value (str): a string that is evaluated for being unknown or n/a.

    Returns:
        Boolean: returns True is the string is unknown or n/a. Otherwise returns the value entered.
    """
    if type(value) == str:
        value = value.lower().strip()
        if value == "unknown":
            return True
        elif value == "n/a":
            return True
        else:
            return False

def convert_string_to_float(value):
    """
    Converts a string to a float.

    Parameters:
        A string.

    Returns:
        Returns the converted string as a float, if the function works.
        Otherwise spits whatever was entered back out.
    """
    try:
        if type(value) == str:
            value = value.strip('standard')
            value = value.strip()
            return float(value)
        else:
            return value
    except ValueError:
        return value

def convert_string_to_int(value):
    """
    Converts a string into an integer.

    Parameters:
        A string.

    Returns:
        Returns the converted string as an integer, if the function works.
        Otherwise spits whatever was entered back atcha.

    """
    try:
        return int(value)
    except ValueError:
        return value

def convert_string_to_list(value, delimiter=', '):
    """
    Converts a string to a list.

    Parameters:
        Value (str): a string.
        Delimiter: default assignment of the delimiter as a comma, ",".

    Returns:
        List: a string converted into a list.
    """
    new_list = value.split(delimiter)
    return new_list

def clean_data(entity):
    """
    Converts string values to appropriate types (float, int, list, None). Manages property
    checks with tuples of named keys.

    Parameters:
        planet (dict): dictionary with values to be cleaned.

    Returns:
        dict: dictionary with cleaned values.
    """
    i = (
        "height", 
        "mass", 
        "rotation_period", 
        "orbital_period", 
        "diameter",
        "surface_water", 
        "population",
        "average_height",
        "average_lifespan",
        "max_atmosphering_speed",
        "MGLT",
        "crew",
        "passengers",
        "cargo_capacity",
    )
    f = (
        "gravity",
        "length",
        "hyperdrive_rating",
    )
    l = (
        "hair_color",
        "skin_color",
        "climate",
        "terrain",
        "skin_colors",
        "hair_colors",
        "eye_colors",
    )
    d = ("homeworld", "species",)

    new_dict = {}

    for key, value in entity.items(): # loops through keys and values of given dictionary
        if is_unknown(value): # checks if the value is unknown or n/a
            new_dict[key] = None # converts value to None if true

        elif key in i: # if the entity key is in our i tuple
            new_dict[key] = convert_string_to_int(value) # we convert the string to an int and add it to our new dictionary

        elif key in f: # if the entity key is in our f tuple
            new_dict[key] = convert_string_to_float(value) # we convert the value to a float and take the first item from the list and add it to our new dict

        elif key in l: # if the entity key is in our l tuple
            value = value.strip()
            new_dict[key] = convert_string_to_list(value) # we convert the string into a list and add it to our new dictionary

        elif key in d: # if the entity key is in our d tuple

            if key == "homeworld": # if the key is homeworld
                entity = get_swapi_resource(value) # assign the entity entered to what get_swapi produces (which I don't really know)
                filtered_dict = filter_data(entity, PLANETS_KEYS) # create a new dictionary with just the key values of the tuple we use
                done = clean_data(filtered_dict) # clean the data (i.e. convert items) from that dict using clean_data, assign it to a temp variable
                new_dict[key] = done # assign our new dictionary to the temp variable

            elif key == "species": # if the key is species
                entity = get_swapi_resource(value[0]) # assign the entity entered to what get_swapi produces (which I don't really know)
                filtered_dict = filter_data(entity, SPECIES_KEYS) # create a new dictionary with just the key values of the tuple we use
                done = clean_data(filtered_dict) # clean the data (i.e. convert items) from that dict using clean_data, assign it to a temp variable
                new_dict[key] = [done] # assign our new dictionary to the temp variable
        else:
            new_dict[key] = value # if none of the above applies, just maintain the format of the entity

    return new_dict # return the new dicionary

def assign_crew(starship, crew):
    """
    Takes the crew, a representation of a person, and assigns them to a starship. Both are dicts.

    Parameters:
        Starship (dict). Crew member (dict).

    Returns:
        Starship (dict) with crew assignments.

    """
    for key,value in crew.items():
        starship[key] = value
    return starship

def write_json(filepath, data):
    """Given a valid filepath, write data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)

# copy and paste from lecture25.py into main
def main():
    """
    Our crucial function. Creates the two JSONs to help out the Rebel Alliance. Squad Goals.

    Parameters:
        None.

    Returns:
        None.

    """
    
    planets_data = read_json("swapi_planets-v1p0.json")
    
    uninhabited_planets = []

    for planet in planets_data:
        if is_unknown(planet['population']) == True:
            dictionary = filter_data(planet, PLANETS_KEYS)
            uninhabited_planets.append(clean_data(dictionary))
    
    write_json("swapi_planets_uninhabited-v1p1.json", uninhabited_planets)


    # begin echo base main

    # set up echo base dictionary
    echo_base = read_json("swapi_echo_base-v1p0.json")

    # find hoth in the API
    swapi_hoth = get_swapi_resource('https://swapi.co/api/planets/4/')

    # add hoth to echo base
    echo_base_hoth = echo_base['location']['planet']
    hoth = combine_data(echo_base_hoth, swapi_hoth)
    hoth = filter_data(hoth, PLANETS_KEYS)
    hoth = clean_data(hoth)
    echo_base['location']['planet'] = hoth

    #echo base commander 
    echo_base_commander = echo_base['garrison']['commander']
    echo_base_commander = clean_data(echo_base_commander)
    echo_base['garrison']['commander'] = echo_base_commander

    #echo base smuggler
    echo_base_rendar = echo_base['visiting_starships']['freighters'][0]
    echo_base_rendar = clean_data(echo_base_rendar)
    echo_base_rendar = echo_base['visiting_starships']['freighters'][0]

    # echo base vehicles
    swapi_vehicles_url = f"{ENDPOINT}/vehicles/"
    swapi_snowspeeder = get_swapi_resource(swapi_vehicles_url, {'search': 'snowspeeder'})['results'][0]

    # echo base snowspeeder
    echo_base_snowspeeder = echo_base['vehicle_assets']['snowspeeders'][0]['type']
    snowspeeder = combine_data(echo_base_snowspeeder, swapi_snowspeeder)
    snowspeeder = filter_data(snowspeeder, VEHICLES_KEYS)
    snowspeeder = clean_data(snowspeeder)
    echo_base['vehicle_assets']['snowspeeders'][0]['type'] = snowspeeder

    # starships
    swapi_starships_url = f"{ENDPOINT}/starships/"

    # x-wing
    x_wing = get_swapi_resource(swapi_starships_url, {'search': 'T-65 X-wing'})['results'][0]
    echo_base_x_wing = echo_base['starship_assets']['starfighters'][0]['type']
    combine_x_wing = combine_data(x_wing, echo_base_x_wing)
    combine_x_wing = filter_data(combine_x_wing, STARSHIP_KEYS)
    combine_x_wing = clean_data(combine_x_wing)
    echo_base['starship_assets']['starfighters'][0]['type'] = combine_x_wing

    # gr-75
    gr_75 = get_swapi_resource(swapi_starships_url, {'search': 'GR-75 medium transport'})['results'][0]
    echo_base_gr_75 = echo_base['starship_assets']['transports'][0]['type']
    combine_gr_75 = combine_data(gr_75, echo_base_gr_75)
    combine_gr_75 = filter_data(combine_gr_75, STARSHIP_KEYS)
    combine_gr_75 = clean_data(combine_gr_75)
    echo_base['starship_assets']['transports'][0]['type'] = combine_gr_75

    # millennium falcon
    millennium_falcon = get_swapi_resource(swapi_starships_url, {'search': 'YT-1300 light freighter'})['results'][0]
    echo_base_millennium_falcon = echo_base['visiting_starships']['freighters'][0]
    falcon = combine_data(millennium_falcon, echo_base_millennium_falcon)
    falcon = filter_data(falcon, STARSHIP_KEYS)
    falcon = clean_data(falcon)

    echo_base['visiting_starships']['freighters'][0]['type'] = falcon

    # echo base light
    echo_base_light = echo_base['visiting_starships']['freighters'][1]
    echo_base_light = filter_data(echo_base_light, STARSHIP_KEYS)
    echo_base_light = clean_data(echo_base_light)

    # swapi people
    swapi_people_url = f"{ENDPOINT}/people/"

    # han solo
    han = get_swapi_resource(swapi_people_url, {'search': 'han solo'})['results'][0]
    han = filter_data(han, PEOPLE_KEYS)
    han = clean_data(han)

    # chewbacca
    chewbacca = get_swapi_resource(swapi_people_url, {'search': 'Chewbacca'})['results'][0] 
    chewbacca = filter_data(chewbacca, PEOPLE_KEYS)
    chewbacca = clean_data(chewbacca)

    # add our crew to millennium falcon
    combine_falcon = assign_crew(falcon, {'pilot': han, 'copilot': chewbacca}) 

    # add dash rendar???
    rendar = filter_data(echo_base['visiting_starships']['freighters'][1]['pilot'], PEOPLE_KEYS)
    rendar = clean_data(rendar)
    echo_base_light = assign_crew(echo_base_light, {'pilot': rendar})
    
    # empty list for our pilots
    echo_base['visiting_starships']['freighters'] = []

    # add our pilots
    echo_base['visiting_starships']['freighters'].append(combine_falcon)
    echo_base['visiting_starships']['freighters'].append(echo_base_light)

    # evacuation plan
    evac_plan = echo_base['evacuation_plan']
    i = 0 

    # loop over personnel and add to max_base_personnel propoerty
    for x in echo_base['garrison']['personnel']:
        #print(item)
        i += echo_base['garrison']['personnel'][x] 
    echo_base['evacuation_plan']['max_base_personnel'] = i
    echo_base['evacuation_plan']['max_available_transports'] = echo_base['starship_assets']['transports'][0]['num_available']    # max_available_transports = echo_base['starship_assets']['transports'][0]['num_available']
    echo_base['evacuation_plan']['max_passenger_overload_capacity'] = echo_base['evacuation_plan']['max_available_transports'] * echo_base['evacuation_plan']['passenger_overload_multiplier'] * echo_base['evacuation_plan']['max_available_transports'] * echo_base['evacuation_plan']['passenger_overload_multiplier'] 

    evac_transport = copy.deepcopy(echo_base['starship_assets']['transports'])

    # fix our rogue int...
    echo_base['visiting_starships']['freighters'][1]['cargo_capacity'] = str(echo_base['visiting_starships']['freighters'][1]['cargo_capacity'])
    

    # create our bright hope transport assignment
    evac_transport[0]['type']['name'] = 'Bright Hope'
    evac_plan['transport_assignments'] = evac_transport
    evac_data = evac_transport[0]['type']

    for key, value in evac_data.items():
        evac_plan['transport_assignments'][0][key] = value

    # remove some unwanted data
    evac_plan['transport_assignments'][0].pop('type')
    evac_plan['transport_assignments'][0].pop('num_available')

    # empty list for our homies
    evac_transport[0]['passenger_manifest'] = []

    # get leia
    leia = get_swapi_resource(swapi_people_url, {'search': 'Leia Organa'})['results'][0]
    leia = filter_data(leia, PEOPLE_KEYS)
    leia = clean_data(leia)

    # get c3_p0
    c3_p0 = get_swapi_resource(swapi_people_url, {'search': 'C-3PO'})['results'][0]
    c3_p0 = filter_data(c3_p0, PEOPLE_KEYS)
    c3_p0 = clean_data(c3_p0)

    # append the homies to passenger manifest
    evac_transport[0]['passenger_manifest'].append(leia)
    evac_transport[0]['passenger_manifest'].append(c3_p0) 

    # escorts list
    evac_transport[0]['escorts'] = [] 

    # make our echo base copy with luke and wedge
    luke_x_wing = echo_base['starship_assets']['starfighters'][0]['type'].copy()
    wedge_x_wing = echo_base['starship_assets']['starfighters'][0]['type'].copy()

    # get luke skywalker
    luke = get_swapi_resource(swapi_people_url, {'search': 'Luke Skywalker'})['results'][0]
    luke = filter_data(luke, PEOPLE_KEYS)
    luke = clean_data(luke)

    # get r2d2
    r2_d2 = get_swapi_resource(swapi_people_url, {'search': 'R2-D2'})['results'][0]
    r2_d2 = filter_data(r2_d2, PEOPLE_KEYS)
    r2_d2 = clean_data(r2_d2)

    # put luke in x_wing
    luke_x_wing = assign_crew(luke_x_wing, {'pilot' : luke, 'astromech_droid' : r2_d2})
    evac_transport[0]['escorts'].append(luke_x_wing)
    
    # get wedge
    wedge = get_swapi_resource(swapi_people_url, {'search': 'Wedge Antilles'})['results'][0]
    wedge = filter_data(wedge, PEOPLE_KEYS)
    wedge = clean_data(wedge)
    
    # get r5d4
    r5_d4 = get_swapi_resource(swapi_people_url, {'search': 'R5-D4'})['results'][0]
    r5_d4 = filter_data(r5_d4, PEOPLE_KEYS)
    r5_d4 = clean_data(r5_d4)

    # put wedge in x_wing
    wedge_x_wing = assign_crew(wedge_x_wing, {'pilot' : wedge, 'astromech_droid' : r5_d4})

    # assign wedge to escorts
    evac_transport[0]['escorts'].append(wedge_x_wing)

    # peace out 506
    write_json("swapi_echo_base-v1p1.json", echo_base)

    return uninhabited_planets


if __name__ == '__main__':
    main()
