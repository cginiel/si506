import json, requests, copy

ENDPOINT = 'https://swapi.co/api'

#Create an additional set of tuple constants that comprise ordered collection of key names 
#based on the key names described in the Entity tables listed below:

#DONE
PERSON_KEYS = ('url', 'name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'species')
PLANET_KEYS = ('url', 'name', 'system_position', 'natural_satellites', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population', 'indigenous_life_forms')
STARSHIP_KEYS =  ('url', 'starship_class', 'name', 'model', 'manufacturer', 'length', 'width', 'max_atmosphering_speed', 'hyperdrive_rating', 'MGLT','crew', 'passengers', 'cargo_capacity', 'consumables', 'armament')
SPECIES_KEYS = ('url', 'name', 'classification', 'designation', 'average_height', 'skin_colors', 'hair_colors', 'eye_colors', 'average_lifespan', 'language')
VEHICLE_KEYS = ('url', 'vehicle_class', 'name', 'model', 'manufacturer', 'length', 'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity', 'consumables', 'armament')

#You will use these constants as named key filters throughout your program.


def assign_crew(starship, crew):
   '''
   Decription: This function assigns crew members to a starship. 
   
   Parameters: 
        starship (dict)
        crew (dict): Each crew key defines a role (e.g., pilot, copilot, astromech_droid) that must be used as the new starship key (e.g., starship['pilot']). 
                    The crew value (dict) represents the crew member (e.g., Han Solo, Chewbacca). 
                    
    Returns: The function returns an updated starship with one or more new crew member key-value pairs added to the caller.
   '''
   #crew key: role
   #starship key: role
   #crew value: crew member

   #DONE

   for key,value in crew.items():
       starship[key] = value
   return starship

#n_dict = {'name': 'Lol', 'mass' : '56', 'gravity' : '45 lols','terrain' : 'i, love, food            ', 'population':'unknown', 'thing':66}

def clean_data(entity):
    '''
    Description: This function converts dictionary string values to more appropriate types such as float, int, list, or, in certain cases, None. 
        The function evaluates each key-value pair encountered with if-elif-else conditional statements, membership operators, 
        and calls to other functions that perform the actual type conversions to accomplish this task. 
    
    Parameters: entity (dict)
    
    Returns: After checking all values and performing type conversions on strings capable of conversion the function will return a dictionary with 'cleaned' values to the caller.

    #consider managing value checks with tuples of ordered named keys (e.g., int_props = (<key_name_01>, <key_name_02>, . . .) that serve as filters.
    '''

    i = ('height','mass','rotation_period','orbital_period','diameter','population', 'average_lifespan', 'max_atmosphering_speed','MGLT','crew','passengers','cargo_capacity','surface_water', 'average_height',)
    f = ('hyperdrive_rating','gravity','length',)
    l = ('hair_color','skin_color','climate','terrain','skin_colors','hair_colors','eye_colors',)
    d = ('homeworld','species',)
    

    cleaned = {}
    for key, value in entity.items():
        #thing = get_swapi_resource('https://swapi.co/api/', 'homeworld')
        #thing = get_swapi_resource('https://swapi.co/api/, 'species')[0]

        if type(value) == str and is_unknown(value):
            cleaned[key] = None

        elif key in i:
            cleaned[key] = convert_string_to_int(value)
        
        elif key in f:
            cleaned[key] = convert_string_to_float(value)

        elif key in l:
            cleaned[key] = convert_string_to_list(value)

        elif key in d:
            if key == 'homeworld':
                entity = get_swapi_resource(value)
                new = filter_data(entity, PLANET_KEYS)
                final = clean_data(new)
                cleaned[key] = final
            
            if key == 'species':
                entity = get_swapi_resource(value[0])
                new = filter_data(entity, SPECIES_KEYS)
                final = clean_data(new)
                cleaned[key] = [final]

        else:
            cleaned[key] = value

    return cleaned
        


def combine_data(default_data, override_data):
    '''
    Description: This function creates a shallow copy of the default dictionary and then updates the copy with key-value pairs from the 'override' dictionary. 
    
    Parameters: 
        default_data (dict)
        override_data (dict)
    
    Returns: The function returns a dictionary that combines the key-value pairs of both the default dictionary and the override dictionary, 
        with override values replacing default values on matching keys.
    '''
    #DONE
    combined_data = default_data.copy()  # shallow
    # combined_data = copy.copy(default_data) # shallow
    # combined_data = copy.deepcopy(default_data) # deep
    combined_data.update(override_data)  # in place

    # Dictionary unpacking
    # combined_data = {**default_data, **override_data}

    return combined_data


def convert_string_to_float(value):
    '''
    Description: This function attempts to convert a string to a floating point value. 
    
    Parameters: value (str)
    
    Returns: If unsuccessful the function returns the value unchanged. 
    
    #Use try / except blocks to accomplish the task.
    '''
    #DONE
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
    '''
    Description: This function attempts to convert a string to an int. 
    
    Parameters: value (str)
    
    Returns: If unsuccessful the function must return the value unchanged.

    #implement try / except blocks that catch the expected exception to accomplish the task
    '''

    #DONE
    try:
       return int(value)

    except ValueError:
        return value


def convert_string_to_list(value, delimiter = ', '):
    '''
    Description: This function converts a string of delimited text values to a list. 
    
    Parameters: 
        value(str)
        optional delimiter (str) 
    
    Returns: The function will split the passed in string using the provided delimiter and return the resulting list to the caller.
    '''
    #DONE
    #final = []
    new_list = value.split(delimiter)
    # for thing in new_list:
    #     done = thing.strip()
    #     final.append(done)
    return new_list



def filter_data(data, filter_keys):
    '''
    Description: This function applies a key name filter to a dictionary in order to return an ordered subset of key-values. 
    
    Parameters: 
        data (dict)
        filter_keys (tuple): The insertion order of the filtered key-value pairs is determined by the filter_key sequence. 
        
    Returns: (Dict) The function returns a filtered collection of key-value pairs to the caller. '''
    #im not sure what im suppsed to do here - maybe follow up on piazza
    #filtered = {}

    '''
    #if you want to replace the keys and standardize them
    for key,value in data.items():
        for item in filter_keys:
            filtered[item] = value
            '''

    record = {}
    for key in filter_keys:
        if key in data.keys():
            record[key] = data[key]
    
    return record

    #DONE


def get_swapi_resource(url, params=None):
    '''
    Description: This function initiates an HTTP GET request to the SWAPI service in order to return a representation of a resource. 
    
    Parameters: 
        url (str): resource url 
        params (dict): optional query string of key:value pairs may be provided as search terms (e.g., {'search': 'yoda'}). 
            If no category (e.g., people) is provided, the root resource will be returned. 
            
    Returns: 
    If a match is obtained the JSON object that is returned will include a list property named 'results' that contains the resource(s) matched by the search query term(s).

    SWAPI data is serialized as JSON. The get_swapi_resource() function must decode the response using the .json() method so that the data is returned as a dictionary.
    '''
    #DONE
    if params:
        response = requests.get(url, params=params).json()
    else:
        response = requests.get(url).json()

    return response

#print(get_swapi_resource('https://swapi.co/api/planets/', {'search': 'hoth'})['results'][0]['climate'] == 'frozen')


def is_unknown(value):
    '''
    Description: This function applies a case-insensitive truth value test for string values that equal unknown or n/a. 
    
    Parameters: 
        value(str)
        
    Returns: True if a match is obtained.
    '''
    #DONE
    
    try:
        value.lower()
        if 'unknown' in value.lower():
            yes = True
        
        else:
            if 'n/a' in value.lower():
                yes = True
            else:
                yes = False
        
        return yes

    except ValueError:
        return False


def read_json(filepath):
    '''
    Description: This function reads a JSON document and returns a dictionary if provided with a valid filepath. Basically just encodes it and spits out a dictionary.

    Parameters: filepath (str): json document

    Returns: A dictionary that will be encoded using the parameter utf-8
    When calling the built-in open() function set the optional encoding parameter to utf-8.
    '''
    #DONE
    with open(filepath, 'r', encoding = 'UTF-8') as f:
        encoded = json.load(f)
    
    return encoded


def write_json(filepath, data):
    '''
    Description: Write a general-purpose function named write_json() capable of writing SWAPI data to a target JSON document file. 
        The function must be capable of processing any arbitrary combination of SWAPI data and filepath provided to it as arguments.
        Call this function and pass it the appropriate arguments whenever you need to generate a JSON document file required to complete the assignment.
    
    Parameters: 
        filepath (str)
        data (?): that is to be written to the file 

    Returns: a json file with data that was inputted
    
    #When calling the built-in open() function set the optional encoding parameter to utf-8. When calling json.dump() set the optional ensure_ascii parameter value to False and the optional indent parameter value to 2.
    '''
    #DONE
    with open(filepath, 'w') as f:
        json.dump(data, f, ensure_ascii = False ,indent = 2)


def main():

    """
    Entry point. This program will interact with local file assets and the Star Wars
    API to create two data files required by Rebel Alliance Intelligence.

    - A JSON file comprising a list of likely uninhabited planets where a new rebel base could be
      situated if Imperial forces discover the location of Echo Base.

    - A JSON file of Echo Base information including an evacuation plan of base personnel
      along with passenger assignments for Princess Leia, the communications droid C-3PO aboard
      the transport Bright Hope escorted by two X-wing starfighters piloted by Luke Skywalker
      (with astromech droid R2-D2) and Wedge Antilles (with astromech droid R5-D4).

    Parameters:
        None

    Returns:
        None
    """
    #6.2 FILTER PLANET DATA
    #once combine data is made then filter_data should be able to pass which will help this one?

    list_planet_dict = read_json('swapi_planets-v1p0.json')
    uninhabited_list = []

    #iterate over a list of planet dictionaries
    for item in list_planet_dict:
        value = item['population']
        if is_unknown(value) == True:
            filtered = filter_data(item, PLANET_KEYS)
            new_clean = clean_data(filtered)
            uninhabited_list.append(new_clean)
        else:
            pass
    
    #write list of dictionaries to new file
    write_json('swapi_planets_uninhabited-v1p1.json', uninhabited_list)


    
    #Start of echo base main


    echo_base = read_json('swapi_echo_base-v1p0.json')
    swapi_hoth = get_swapi_resource('https://swapi.co/api/planets/4/')
    
    echo_base_hoth = echo_base['location']['planet']
    hoth = combine_data(echo_base_hoth, swapi_hoth)
    hoth = filter_data(hoth, PLANET_KEYS)
    hoth = clean_data(hoth)
    echo_base['location']['planet'] = hoth 


    echo_base_commander = echo_base['garrison']['commander']
    echo_base_commander = clean_data(echo_base_commander)
    echo_base['garrison']['commander'] = echo_base_commander

    echo_base_smuggler = echo_base['visiting_starships']['freighters'][0]
    echo_base_smuggler = clean_data(echo_base_smuggler)
    echo_base_smuggler = echo_base['visiting_starships']['freighters'][0]

    swapi_vehicles_url = f"{ENDPOINT}/vehicles/"
    swapi_snowspeeder = get_swapi_resource(swapi_vehicles_url, {'search': 'snowspeeder'})['results'][0]

    echo_base_snowspeeder = echo_base['vehicle_assets']['snowspeeders'][0]['type']
    snowspeeder = combine_data(echo_base_snowspeeder, swapi_snowspeeder)
    snowspeeder = filter_data(snowspeeder, VEHICLE_KEYS)
    snowspeeder = clean_data(snowspeeder)
    echo_base['vehicle_assets']['snowspeeders'][0]['type'] = snowspeeder

    swapi_starships_url = f"{ENDPOINT}/starships/"

    t_65 = get_swapi_resource(swapi_starships_url, {'search': 'T-65 X-wing'})['results'][0]
    echo_base_model = echo_base['starship_assets']['starfighters'][0]['type']
    combine_t65 = combine_data(t_65, echo_base_model)
    combine_t65 = filter_data(combine_t65, STARSHIP_KEYS)
    combine_t65 = clean_data(combine_t65)
    echo_base['starship_assets']['starfighters'][0]['type'] = combine_t65

    med = get_swapi_resource(swapi_starships_url, {'search': 'GR-75 medium transport'})['results'][0]
    echo_base_med = echo_base['starship_assets']['transports'][0]['type']
    combine_med = combine_data(med, echo_base_med)
    combine_med = filter_data(combine_med, STARSHIP_KEYS)
    combine_med = clean_data(combine_med)
    echo_base['starship_assets']['transports'][0]['type'] = combine_med

    falcon = get_swapi_resource(swapi_starships_url, {'search': 'YT-1300 light freighter'})['results'][0]
    echo_base_falcon = echo_base['visiting_starships']['freighters'][0]
    m_falcon = combine_data(falcon, echo_base_falcon)
    m_falcon = filter_data(m_falcon, STARSHIP_KEYS)
    m_falcon = clean_data(m_falcon)

    echo_base['visiting_starships']['freighters'][0]['type'] = m_falcon

    echo_base_light = echo_base['visiting_starships']['freighters'][1]
    echo_base_light = filter_data(echo_base_light, STARSHIP_KEYS)
    echo_base_light = clean_data(echo_base_light)
 

    swapi_people_url = f"{ENDPOINT}/people/"
    han = get_swapi_resource(swapi_people_url, {'search': 'han solo'})['results'][0]
    han = filter_data(han, PERSON_KEYS)
    han = clean_data(han)

    swapi_people_url = f"{ENDPOINT}/people/"
    chewie = get_swapi_resource(swapi_people_url, {'search': 'Chewbacca'})['results'][0] 
    chewie = filter_data(chewie, PERSON_KEYS)
    chewie = clean_data(chewie)
    
    combine_falcon = assign_crew(m_falcon, {'pilot': han, 'copilot': chewie}) 

    rendar = filter_data(echo_base['visiting_starships']['freighters'][1]['pilot'], PERSON_KEYS)
    rendar = clean_data(rendar)
    echo_base_light = assign_crew(echo_base_light, {'pilot': rendar})

    echo_base['visiting_starships']['freighters'] = []

    echo_base['visiting_starships']['freighters'].append(combine_falcon)
    echo_base['visiting_starships']['freighters'].append(echo_base_light)

    evac_plan = echo_base['evacuation_plan']
    i = 0 
    for item in echo_base['garrison']['personnel']:
        i += echo_base['garrison']['personnel'][item] 
    echo_base['evacuation_plan']['max_base_personnel'] = i
    echo_base['evacuation_plan']['max_available_transports'] = echo_base['starship_assets']['transports'][0]['num_available']    # max_available_transports = echo_base['starship_assets']['transports'][0]['num_available']
    echo_base['evacuation_plan']['max_passenger_overload_capacity'] = echo_base['evacuation_plan']['max_available_transports'] * echo_base['evacuation_plan']['passenger_overload_multiplier'] * echo_base['evacuation_plan']['max_available_transports'] * echo_base['evacuation_plan']['passenger_overload_multiplier']    
    
    evac_transport = copy.deepcopy(echo_base['starship_assets']['transports'])
    echo_base['visiting_starships']['freighters'][1]['cargo_capacity'] = str(echo_base['visiting_starships']['freighters'][1]['cargo_capacity'])
    # print(evac_transport[0]['type'])
    # evac_transport = evac_transport[0]['type']
    
    evac_transport[0]['type']['name'] = 'Bright Hope'
    evac_plan['transport_assignments'] = evac_transport
    data = evac_transport[0]['type']
    for key, value in data.items():
        evac_plan['transport_assignments'][0][key] = value

    evac_plan['transport_assignments'][0].pop('type')
    evac_plan['transport_assignments'][0].pop('num_available')

    evac_transport[0]['passenger_manifest'] = []

    leia = get_swapi_resource(swapi_people_url, {'search': 'Leia Organa'})['results'][0]
    leia = filter_data(leia, PERSON_KEYS)
    leia = clean_data(leia)

    c3_p0 = get_swapi_resource(swapi_people_url, {'search': 'C-3PO'})['results'][0]
    c3_p0 = filter_data(c3_p0, PERSON_KEYS)
    c3_p0 = clean_data(c3_p0)

    evac_transport[0]['passenger_manifest'].append(leia)

    evac_transport[0]['passenger_manifest'].append(c3_p0) 

    evac_transport[0]['escorts'] = [] 

    luke_x_wing = echo_base['starship_assets']['starfighters'][0]['type'].copy()
    wedge_x_wing = echo_base['starship_assets']['starfighters'][0]['type'].copy()

    luke = get_swapi_resource(swapi_people_url, {'search': 'Luke Skywalker'})['results'][0]
    luke = filter_data(luke, PERSON_KEYS)
    luke = clean_data(luke)

    r2_d2 = get_swapi_resource(swapi_people_url, {'search': 'R2-D2'})['results'][0]
    r2_d2 = filter_data(r2_d2, PERSON_KEYS)
    r2_d2 = clean_data(r2_d2)

    luke_x_wing = assign_crew(luke_x_wing, {'pilot' : luke, 'astromech_droid' : r2_d2})
    evac_transport[0]['escorts'].append(luke_x_wing)
    

    wedge = get_swapi_resource(swapi_people_url, {'search': 'Wedge Antilles'})['results'][0]
    wedge = filter_data(wedge, PERSON_KEYS)
    wedge = clean_data(wedge)

    
    r5_d4 = get_swapi_resource(swapi_people_url, {'search': 'R5-D4'})['results'][0]
    r5_d4 = filter_data(r5_d4, PERSON_KEYS)
    r5_d4 = clean_data(r5_d4)

    wedge_x_wing = assign_crew(wedge_x_wing, {'pilot' : wedge, 'astromech_droid' : r5_d4})

    evac_transport[0]['escorts'].append(wedge_x_wing)

    # echo_base['evacuation_plan']['transport_assignments'][0].pop('num_available')
    
    write_json('swapi_echo_base-v1p1.json', echo_base)
    
    return uninhabited_list









if __name__ == '__main__':
    main()


#TESTS
