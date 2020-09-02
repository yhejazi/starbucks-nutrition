import requests as r
import pandas as pd

if __name__ == '__main__':
    page = r.get("https://www.starbucks.com/bff/ordering/menu")
    drinks = next((x for x in page.json()['menus'] if x['name'] == 'Drinks'), None)

    result = []
    test = drinks['children'][0]

    unwanted = ['Clover® Brewed Coffees', 'Coffee Travelers', 'Iced Clover® Brewed Coffees', 'Bottled Teas', 
        'Milk', 'Sparkling Water', 'Water'] # mostly packaged drinks

    for drink_type in drinks['children']: # i.e. Hot Coffees
        category = drink_type['name']
        print('---', category, '---')

        for drink_family in drink_type['children']: 
            if (drink_family['name'] not in unwanted):
                print(drink_family['name']) # i.e. Americanos
                for product in drink_family['products']:
                    # Get product's nutrition page
                    url = product['uri'].split("/")
                    prod_page = r.get("https://www.starbucks.com/bff/ordering/" + url[2] + '/' + url[3])
                    drink = prod_page.json()['products'][0]

                    drink_name = drink['name'] 

                    for drink_size in drink['sizes']:
                        size = drink_size['name']
                        nutrition = drink_size['nutrition']
                        if nutrition is not None:
                            calories = nutrition.get('calories').get('displayValue')
                            additionalFacts = nutrition['additionalFacts']
                            fat = additionalFacts[0]['value']
                            cholesterol = additionalFacts[1]['value']
                            sodium = additionalFacts[2]['value']
                            carb = additionalFacts[3]['value']
                            sugar = additionalFacts[3]['sugars']['value']
                            protein = additionalFacts[4]['value']
                            caffeine = additionalFacts[5]['value']
                        else:
                            calories = fat = cholesterol = sodium = carb = sugar = protein = caffeine = 'NA'

                        result.append([drink_name, category, size, calories, fat, cholesterol, sodium, carb, sugar, protein, caffeine])
                    
        
    columnNames = ['drink_name', 'type', 'size', 'calories', 'fat', 'cholesterol', 'sodium', 'carb', 'sugar', 'protein', 'caffeine']
    df = pd.DataFrame(result, columns=columnNames)

    df.to_csv(path_or_buf='sbux_nutrition.csv', index=False)
    print("----- Finished! -----")
            