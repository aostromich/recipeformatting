## What is the point of tags?
A tag must supply information not obtained by easily searching a word, in that way `t_sandwich` is not helpful, because you could just search “sandwich” (same for `t_sushi`). `t_wrap` is not helpful, because if you want a wrap, it’s because you have a kind of wrapper in mind (tortilla, etc), which is simpler to search by. There also weren’t enough recipes to justify the categories.

`t_soup` is helpful as it differentiates between `t_stock` and allows for searching by recipes for soup rather than those that suggest serving with soup. `t_stock` is helpful for stock recipes instead of recipes including stock as an ingredient.

## Questions to ask in tagging
1.  Where is it from? (Location/Ethnicity)
2.  What ingredients does it have? (Ingredients) (this is mostly automated)
3.  What kind of food is it? (Categories of Food)
4.  What are the macronutrients? (Meal Meta-Categories)
5.  Are there seasonal ingredients? (Seasonality)
6.  Misc. (Meal Identifiers)

## Tags

### Categories of Food
Barbequed `t_barbeque` - food made with a barbecue (no alternative preparation methods)

Dip `t_dip`

Drink `t_drink` - Drinks excluding smoothies

Deep Fried `t_deep_fry` - deep fried food (no alternative preparation methods)

Fake bread `t_fake_bread` - Not a bread, but bread-like (banana bread, cornbread, etc…)

Salad `t_salad`

Sauce `t_sauce` - Includes vinaigrettes and dressings

Smoothies and shakes `t_smoothie_shake` - Smoothies and milkshakes, not filed under drinks

Soup `t_soup`

Spread `t_spread`

Stock `t_stock` - soup stock and broth

Topping `t_topping` - can be a sauce or not, is a recipe for something which is meant to be served as a 
topping for another recipe (e.g. spiced maple syrup, candied pistachios)

### Ingredients
Recipes which contain a significant amount of the tagged ingredient

Fish `t_fish`

Fruit `t_fruit`

Meat `t_meat`

Pasta `t_pasta`

Pulses `t_pulses` - Beans, chickpeas, dried peas, lentils and (non-wheat) grains

Rice `t_rice`

Seafood `t_seafood` - Fish not included (filed under ‘Fish’)

Vegetable `t_vegetable` - Potatoes not included (filed under ‘Starch’). Dish has vegetables.

### Homemade
For example, to finding a recipe to make cheese, not mac 'n' cheese

Bread `t_bread` - Leavened bread, includes pizza

Sourdough `t_sourdough` - Uses sourdough starter

Cheese `t_cheese` - Homemade

Perogie `t_perogie` - includes dumplings, gyoza, mandu, steamed buns and empanadas

Spice `t_spice` - Powder spice mixes or pastes

Tortilla `t_tortilla` - Homemade wraps, tortillas, flatbreads…

Yogurt `t_yogurt` - Homemade yogurt

Jam `t_jam` - Homemade jam or jelly

Coffee `t_coffee` - Drink that has coffee

### Meal Meta-Categories
Meals `t_meal` - A meal, must include veggies and a protein (optionally also a starch)

Protein `t_protein` - May have small amounts of veggies/starch. Add to Vegetable + starch to create a meal

Protein and Starch `t_protein_starch` - Recipe could be made into a meal with the addition of vegetables/fruit

Side dish `t_side_dish` - includes appetizers. Is there a distinction between mashed potato and hors d'oeuvres? Yeah. Do I care to make it? Nah.

Starch `t_starch` - Dish only has bread, rice, potato, etc… (very little or no veg/protein). Add to protein + vegetable to make meal

Vegetable dish `t_vegetable_dish` - Dish consists almost exclusively of vegetables. Add on to protein + starch to create a meal.

Vegetable and Starch `t_vegetable_starch` - Recipe could be made into a meal with the addition of protein

### Meal Identifiers
Breakfast `t_breakfast`

Cool down `t_cool_down` - dishes served very cold (eg. ice cream, iced coffee, etc…)

Dairy free `t_dairy_free` - strictly dairy-free, assumes no access to dairy-free milk, dairy-free butter etc.

Dessert `t_dessert` - can stand on its own as a dessert

Snack `t_snack`

Sweet `t_sweet` - Recipes that straddle the line between meals and desserts (e.g pancakes) OR are otherwise sweet but don't constitute a dessert on their own (e.g. dulce de leche, popsicles -- eg search for ice-cream toppings with "t_sweet" "t_topping")

Gluten-free `t_gluten_free` - Recipe that is either naturally gluten-free or has a gluten-free modification

Meta `t_meta` - Not recipes. Includes information on ingredients and equipment, how to prep foods, etc.

### Advance prep
Make sure to include a note at the top of the recipe in the form "*Note: Start making the night before or the morning of*" or "*Note: Start making 1 week in advance*", etc.

Advance prep `t_advance_prep` - Recipe that requires advanced prep, such as the night before or morning of

Freezer-friendly `t_freeze` - Can be frozen in part or in whole, before or after cooking (doesn’t include ice cream). 

### Seasonality
Recipe requires ingredients which are in-season (e.g heirloom tomatoes)

Winter `t_winter`

Spring `t_spring`

Summer `t_summer`

Fall `t_fall`

### By Country / Ethnicity
Not exhaustive, simply based on my existing recipes

Argentina `t_argentinian`

Bangladesh `t_bengalis`

Bulgaria `t_bulgarian`

Cajun and Creole `t_cajun_creole`

Chile `t_chilean`

China `t_chinese`

Cuba `t_cuban`

Cyprus `t_cypriot`

Eritrea `t_eritrean`

Ethiopia `t_ethiopian`

Philippines `t_filipino`

France `t_french`

Georgia `t_georgian`

Germany `t_german`

Greece `t_greek`

Hawai’i `t_hawaiian`

Hong Kong `t_hong_kongese`

India `t_indian`

Indonesia `t_indonesian`

Iran (persia) `t_iran`

Ireland `t_irish`

Israel `t_israeli`

Italy `t_italian`

Jamaica `t_jamaican`

Japan `t_japanese`

Jews `t_jewish`

Kenya `t_kenyan`

South Korea `t_korean`

Lebanon `t_lebanese`

Madagascar `t_malagasy`

Malaysia `t_malaysian`

Mexico `t_mexican`

Morocco `t_moroccan`

Mozambique `t_mozambican`

Myanmar `t_burmese`

Nigeria `t_nigerian`

Peru `t_peruvian`

Portugal `t_portuguese`

Russia `t_russian`

São Tomé and Príncipe `t_santomean`

Senegal `t_senegalese`

Somalia `t_somali`

South Africa `t_south_african`

Sri Lanka `t_sri_lankan`

Spain `t_spanish`

Syria `t_syrian`

Taiwan `t_taiwanese`

Tanzania `t_tanzanian`

Turkey `t_turkish`

Thailand `t_thai`

Ukraine `t_ukrainian`

United Arab Emirates `t_emirati`

United States `t_american`

Vietnam `t_vietnamese`

Yemen `t_yemeni`

#### By Region
For making food from a greater region rather than a specific country

*East Africa*: Eritrea, Ethiopia, Kenya, Mozambique, Somalia, Tanzania
*North Africa*: North Africa
*Central Africa*: São Tomé and Príncipe
*South Africa*: South Africa (country)
*West Africa*: Nigeria, Senegal

*North America*: Cajun and Creole, Hawai’i, Mexico, United States
*South America*: Argentina, Chile, Peru, Brazil
*Latin America*: Latin America, Argentina, Chile, Mexico, Peru

*Arab World*: Arab world, Lebanon, Morocco, Syria, United Arab Emirates, Yemen
*Middle East*: Middle East, Cyprus, Iran, Israel, Lebanon, Turkey, United Arab Emirates, Yemen

*East Asia*: China, Hong Kong, Japan, South Korea, Taiwan
*South Asia*: Bangladesh, India, Sri Lanka
*Southeast Asia*: Southeast Asia, Myanmar, Indonesia, Malaysia, Philippines, Thailand, Vietnam

*The Caribbean*: The Caribbean, Cuba, Jamaica

*Eastern Europe*: Russia, Ukraine
*Northern Europe*: England, Ireland
*Southern Europe*: Bulgaria, Greece, Italy, Portugal, Spain
*Western Europe*: France, Germany
