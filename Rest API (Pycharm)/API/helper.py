import numpy as np
import pandas as pd

def preprocess():
    data = {'Name': ['Burger', 'Chocolate Cake', 'Pizza'],

            'Nutrient Info': [' Calories(749 kcal)\n Carbs(85 gm)\n Sugar(12 gm)\n Protein(12 gm)\n Fat(40 gm)\n Fiber(5.4 gm)\n',
                              ' Calories(311 kcal)\n Carbs(38 gm)\n Sugar(20 gm)\n Protein(3.3 gm)\n Fat(16 gm)\n Fiber(1.9 gm)\n',
                              ' Calories(546 kcal)\n Carbs(92 gm)\n Sugar(9 gm)\n Protein(15 gm)\n Fat(13 gm)\n Fiber(4.4 gm)\n'],

            'Preparation Time': ['50 mins', '60 mins', '70 mins'],

            'Ingredients': [
                'Potato (2 no)\nButter (4 tbsp)\nGreen Peas (0.5 Cup)\nRed Chili Powder (0.5 tsp)\nCumin Powder (0.5 tsp)\nCoriander Powder (0.5 tsp)\nChaat Masala Powder (0.5 tsp)\nDry Mango Powder (0.25 tsp)\nSalt (1 tsp)\nLemon Juice (2 tsp)\nCoriander Leaves (1 tbsp)\nFlattened Rice (0.5 cup)\nMaida (0.5 Cup)\nCorn Flour (0.25 cup)\nBlack Pepper Powder (0.25 tsp)\nWater (0.5 cup)\nBreadcrumbs (1 cup)\nSunflower Oil (For Deep Frying)\nBurger Buns (5 no)\nMayonnaise (0.25 Cup)\nTomato Sauce (2 tbsp)\nRed Chilli Sauce (1 tbsp)\nOnion (1 no)\nTomato (2 no)\nCheese Slice (5 no)',
                'Maida (1.5 cup)\nBaking Soda (1 tsp)\nCocoa Powder (0.25 cup)\nPowdered Sugar (1 cup)\nSalt (0.25 tsp)\nSunflower Oil(0.6 Cup)\nVinegar (1 tbsp)\nVanilla Essence(0.5 tsp)\nWater (1 cup)\nDark Chocolate (100 grams)\nFresh Cream(0.25 cup)\n',
                ' Water (1 cup)\n Sugar (2 tbsp)\n Instant Dry Yeast (2 tsp)\n Maida (3 cup)\n Salt (2 tsp)\n Olive Oil (2 tbsp)\n Pizza Sauce (3 tbsp)\n Mozzarella Cheese(0.5 cup)\n',
                ],

            'Instructions': ["1. Peel and grate the whole-boiled potatoes.\n" +
                             "2. In a pan, heat butter and add the green peas along with the masala powders. Add the ginger garlic paste and saute on a low flame.\n" +
                             "3. Add the grated potatoes and mix well. Use a potato masher if required to smoothen the mixture.\n" +
                             "4. Add lemon juice and coriander leaves and turn off the flame. Allow the mixture to cool.\n" +
                             "5. Wash the poha with water and strain it. Add this to the mixture to absorb the excess moisture.\n" +
                             "6. Make equal sized portions of the mixture. Flatten them into patties.\n" +
                             "7. Whisk together the maida, cornstarch, salt, pepper and water to form a thick batter.\n" +
                             "8. Coat the patties with breadcrumbs, then the batter and again in the breadcrumbs.\n" +
                             "9. Fry the patties in oil until golden brown.\n" +
                             "10. Apply butter on the burger buns and toast them.\n" +
                             "11. To make the sauce, mix the mayonnaise, ketchup and chilli sauce together.\n" +
                             "12. Assemble the burger by placing a patty, cheese slice, onion slices, tomatoes and the sauce on top.\n ",

                             "1. Sieve the maida, cocoa powder and baking soda together. Add the powdered sugar and salt.\n" +
                             "2. Make a hole in the center and add oil, vinegar, vanilla essence and warm water. Mix until there are no lumps.\n" +
                             "3. Transfer it to a greased pan. Bake in a preheated oven at 180 c for 20 minutes.\n" +
                             "4. For the frosting, add the chocolate and cream to a bowl. Place the bowl over a pot of boiling water and mix it until it melts.\n" +
                             "5. Take off the heat and allow it to refrigerate for 1 hour or until it thickens.\n" +
                             "6. Apply it over the cake.\n" +
                             "7. Additionally, you can also decorate it with strawberries or chocolate decorations.\n",

                             "1.  In a bowl, add the water, yeast and sugar. Allow it to rest for 10 minutes. This allows the yeast to bloom. If it doesnot rise, the yeast might be old or expired.\n" +
                             "2.  Add salt to the maida and mix, to make sure that the salt is distributed evenly.\n" +
                             "3.  Make a well in the centre of the maida, using your fingers or a wooden spoon. Add the wet mixture in the middle. Start adding a little bit of flour into the wet mixture. Continue doing this until all the flour is mixed in, and a shaggy dough is formed.\n" +
                             "4.  Add oil to the dough. Knead well again until the oil is completely mixed in and the dough becomes smooth.\n" +
                             "5.  Cover with a damp cloth and allow it to rise until doubled in size for at least 45 minutes, up to 1 ½ hours.\n" +
                             "6.  After the dough rises, divide it in two. One portion is for one pizza.\n" +
                             "7.  Cut the dough into a quarter and three-fourths.\n" +
                             "8.  Roll out the small portion into a flat disc. Heat on a tawa for 1 minute. Flip over and cook for a few seconds.\n" +
                             "9.  Roll out the larger portion. Apply the cheese spread and place the cooked dough on top.\n" +
                             "10. Spread the pizza sauce, followed by the grated cheese and all the toppings.\n" +
                             "11. Drizzle olive oil over the top.\n" +
                             "12. Cook in a preheated oven at the highest temperature until the cheese is completely melted, around 8-12 minutes. Apply olive oil around the edges. Cut and serve\n"
                             ]
            }

    df = pd.DataFrame(data)
    return df

def fun(food):
    df=preprocess()
    newDf=df[df['Name']==food].values.flatten().tolist()
    return newDf