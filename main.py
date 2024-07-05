import re
import locale

locale.setlocale(locale.LC_ALL, 'en_CA')


def format_recipe_text(ingredients, recipe):
    """Format the recipe"""
    ingredients = ingredients_replace(ingredients)
    ingredients = universal_replace(ingredients)
    recipe = universal_replace(recipe)
    recipe = body_replace(recipe)

    if recipe[-1] == '.':
        recipe = recipe[:-1]

    return ingredients, recipe


# Which terms trigger a tag for the recipe
match_tags = {
    't_vegetable': ["artichoke(s)?", "arugula", "asparagus", "avocado(s)?", "bamboo shoot(s)?", "beet(s)?",
         "beetroot", "endive(s)?", "escarole", "pepper(s)?", "bok choy", "broccoli", "rapini", "choy sum",
        "cabbage(s)?", "cauliflower", "broccolini", "parsnip(s)?", "celeriac", "celery", "chard", "chicory",
        "napa", "collard(s)?", "corn", "courgette(s)?", "cucumber(s)?", "edamame", "perilla", "cremini",
        "eggplant(s)?", "fennel", "fiddlehead(s)?", "portobello(s)?", "okra", "pickle(s)?", "shiso",
        "daikon", "shallot(s)?", "jicama", "kale", "leek(s)?", "shiitake(s)?", "zucchini(s)?", "pea(s)?",
        "mushroom(s)?", "romaine", "lettuce", "onion(s)?", "rabe", "radicchio(s)?", "radish(es)?",
        "rutabaga", "spinach", "butternut", "squash", "tomatillo(s|es)?", "tomato(es)?", "turnip(s)?",
        "lotus", "burdock", "pumpkin", "watercress", "wakame", "hijiki", "tenkusa", "funori", "kimchi",
        "sweetcorn", "snaps", "shimeji", "kabocha", "microgreens", "pesto", "carrot(s)?", "salsa",
        "cassava", "yuca", "green(s)?", "ancho", "guajillo", "serrano", "pimiento", "(-)?leaf",
        "sprout(s)?"],
    't_fruit': ["(granny smith )?apple(s)?", "apricot(s)?", "banana(s)?", "(medjool )?date(s)?( syrup)?",
        "(straw|blue|black|cran|mul|rasp)?berr(y|ies)", "cantaloupe(s)?", "cherries", "clementine(s)?",
        "coconut(s)?", "currant(s)?", "fig(s)?", "grape(s)?", "guava", "honeydew(s)?", "jackfruit(s)?",
        "lychee(s)?", "watermelon", "mandarin(s)?", "mango(es)?", "nectarine(s)?", "melon(s)?", "orange(s)?",
        "papaya(s)?", "peach(es)?", "pear(s)?", "persimmon(s)?", "plantain(s)?", "plum(s)?", "pomegranate(s)?",
        "raisin(s)?", "prune(s)?", "quince(s)?", "rhubarb(s)?", "starfruit(s)?", "tangerine(s)?", "jam",
        "pineapple(s)?", "cactus", "passion fruit", "grapefruit(s)?", "whitecurrant(s)?", "cornichon(s)?",
        "kiwi(s)?",],
    't_barbecue': ["barbecue"],
    't_salad': ["salad"],
    't_smoothie': ["smoothie", "milkshake"],
    't_soup': ["soup"],
    't_fish': ["basa", "fish", "flounder", "sole", "trout", "bass", "haddock", "pollock", "salmon", "snapper",
        "tilapia", "carp", "catfish", "grouper", "halibut", "cod", "monkfish", "sturgeon", "anchov(y|ies)",
        "tuna", "mackerel", "escolar", "roe", "sardine(s)?", "whitefish", "smelt", "mullet"],
    't_seafood': ["shrimp", "crawfish", "crayfish", "lobster", "prawn", "cuttlefish", "clam", "prawn(s)?",
        "oyster(?! sauce)", "mussel(s)?", "octopus", "scallop(s)?", "squid", "crab"],
    't_cool_down': ["ice cream", "popsicle"],
    't_pasta': ["pasta", "noodles", "macaroni", "spaghetti", "fettuccine", "penne", "linguine", "lasagne",
        "fusilli", "rotini", "orzo", "tortellini", "ravioli", "rigatoni", "ramen"],
    't_rice': ["rice(?! vinegar)", "risotto"],
    't_meat': ["meat", "beef", "chuck", "flap", "flank", "steak(s)?", "turkey", "venison", "hot dog(s)?",
        "rabbit", "goose", "liver(s)?", "prosciutto", "salami", "sausage(s)?", "chicken", "breast(s)?",
        "thigh(s)?", "ham", "bacon", "lamb", "goat", "pork", "boneless", "bone-in", "(-)?eye", "rib(s)?",
        "duck(ling)?", "tenderloin", "drumstick(s)?", "brisket", "sirloin", "shank", "shoulder", "belly",
        "skirt", "quail", "bison", "mutton"],
    't_pulses': ["black (turtle )?beans", "Great Northern beans",
        "(broad|fava|butter|baby|large|lima|cannellini|kidney|mung|navy|pinto|romano|borlotti|cranberry) beans",
        "dal", "black gram", "chickpeas", "garbanzo", "(black-eyed|split)? peas",
        "(beluga|brown|green|Puy|red)? lentils", "quinoa", "barley", "buckwheat", "millet"],
    # Plain sugar is often used in savory recipes, exclude it from this tag
    't_dessert': ["chocolate", "semi-sweet", "brownie", "pie", "cake", "tart", "maple syrup", "honey",
        "ice cream", "popsicle", "pudding", "dulce de leche", "vanilla( extract)?", "cocoa", "matcha",
        "(raw )?(confectioners(')?|icing|demerara|coconut|muscovado|superfine)", "cookie", "bittersweet",
        "marshmallow(s)?", "honeycomb", "cookie(s)?"],
    't_sweet':["(simple )?syrup"],
    't_japanese':["wasabi", "katsuobushi", "bonito"],
    't_korean':["kimchi"],
    't_bread':["yeast"]
}
neg_match_tags = {
    "t_gluten_free": ["flour", "bread", "tortilla(s)?", "pita", "brioche", "sourdough", "pita(s)?", "semolina",
        "instant", "active dry", "yeast", "wheat bran", "starter", "wheat", "cracker(s)?", "baguette",
        "ciabatta", "loaf", "pearl", "barley", "cereal", "naan", "wonton", "dough", "panko",
        "ramen", "rye"] + match_tags["t_pasta"],
    "t_dairy_free": ["butter", "(sweetened condensed )?milk", "(heavy )?(whipping )?cream( of tartar)?",
        "(greek )?yogurt", "feta", "buttermilk", "half-and-half", "mozzarella", "parmesan", "labneh",
        "mascarpone", "creme fraiche", "queso fresco", "cheddar", "halloumi", "grana padano", "ricotta",
        "Monterey Jack", "queso blanco", "crema", "tzatziki", "brie", "kefir", "gouda", "Emmental", "whey",
        "cheese",]
}
starches = ["potato", "crumb(s)?", "tapioca", "flour", "starch", "quinoa", "buckwheat", "grain", "cornmeal",
        "Basmati", "potato(es)?", "bran", "millet", "amaranth", "fonio", "sorghum", "teff"] \
        + match_tags["t_pasta"] + match_tags["t_rice"]
proteins = ["egg(s)?", "yolk(s)?", "fava", "lima", "bean(s)?", "chickpea(s)?", "lentil(s)?", "tofu"] + \
        match_tags["t_meat"] + match_tags["t_fish"] + match_tags["t_seafood"]

# Grab a list of ingredients to be bolded in output
possible_ingredients = [
    # spices, herbs and aromatics
    # clove (the spice) is not included as garlic cloves are much more likely to show up in a recipe
    "cayenne", "powder", "peppercorn(s)?", "flakes", "((italian)? )?parsley", "lovage", "cumin", "salt", "paprika",
    "sumac", "bay", "thyme", "pimento", "allspice", "cilantro", "za'atar", "sage", "coriander", "turmeric",
    "pod(s)?", "cinnamon", "dill", "ginger", "rosemary", "basil", "oregano", "caraway", "chili(s|es)?", "chilli(es)?",
    "chile(s)?", "saffron", "nigella", "curry", "chive(s)?", "fenugreek", "baharat",  "tarragon", "mint", "nutmeg",
    "herb(s)?", "savory", "gochugaru", "garlic", "lavender", "jasmine", "besobela", "ajowan", "berbere", "garam",
    "cardamom(s)?", "masala", "marjoram", "fleur de sel", "balm", "chervil", "epazote",
    # fats
    "margarine", "fat", "vegetable", "extra(-| )virgin", "canola", "rapeseed", "olive(s)?", "sunflower", "oil", "ghee",
    "grapeseed", "shortening", "lard", "nonstick cooking spray", "safflower",
    # descriptors
    "hard-boiled", "toasted", "ground", "baby", "snow", "fine", "coarse", "sea", "kosher", "bell", "sherry", "balsamic",
    "sauce", "paste", "(un)?salted", "stick(s)?", "whole", "roasted", "frozen", "dried", "fresh", "blanched",
    "flat", "preserve(s|d)", "split", "king", "raw", "superfine", "fillet(s)?", "rolled", "steel-cut", "heirloom",
    "smoke(d)?", "double", "single", "new", "mini", "broad", "evaporated", "sheet(s)?", "powdered", "old-fashioned",
    "sour", "natural", "skin-on", "(short|long)(-)?", "puffed", "crushed", "wrappers", "clarified", "flaky", "hulled",
    "sweet", "button", "enoki", "iceberg", "shelled", "grainy", "snap", "salata", "tendrils", "cannellini", "haricot",
    "skinless", "pickled", "whipped", "cold", "mashed", "fried", "delicious", "cooked", "roaster", "boiling",
    "stale", "delicata", "acorn", "carnaroli", "wild", "chai", "cracked", "fingerling", "wood", "unsweetened", "virgin",
    "neutral", "puree", "packed", "style",
    # place, nationality or ethnicity
    "mexican", "french", "spanish", "yukon", "worcestershire", "shaoxing", "dijon", "kalamata", "korean", "asian",
    "turkish", "espelette", "aleppo", "fresno", "holland", "japanese", "thai", "amarillo", "idaho", "korean", "venus",
    "szechuan", "kashmiri", "swiss", "english", "persian", "brussels", "castelvetrano", "hungarian", "cotija",
    "chinese", "calabrian", "arborio", "sichuan", "guizhou", "european",
    # colour
    "dark", "light", "brown", "yellow", "orange", "black", "navy", "white", "pink", "gold(en)?", "purple", "red",
    "blue", "russet",
    # condiments
    "tamari", "soy", "ketchup", "mustard", "harissa", "yukari", "mayonnaise", "miso", "tahini", "tehina", "gochujang",
    "doenjang", "marmalade", "hoisin", "hummus", "dressing", "malt",
    # nuts and seeds
    "sesame", "nut(s)?", "seed(s)?", "pecan(s)?", "chestnut(s)?", "pine", "flaxseed(s)?", "peanut(s)?", "walnut(s)?",
    "chia", "poppy", "hazelnut(s)?", "almond(s)?", "pepita(s)?", "pistachio(s)?", "flax", "cashew(s)?", "hemp",
    "psyllium husk",
    # produce
    "lemon(s)?", "lime(s)?", "kombu", "konbu", "seaweed", "gim", "nori", "yuzu", "bergamot",
    # Cherry is here as it's unlikely for a recipe to call for 1 cherry and otherwise, cherry tomatoes trigger the
    # fruit categorization
    "cherry", "scallion(s)?", "kernel(s)?", "(edible )?flower(s)?", "wildflower", "borage", "marigold", "root",
        # blood orange or blood-blood
    "blood", "caper(s)?", "tamarind", "scotch bonnet", "umeboshi", "chipotle", "arbol", "jalapeno", "stalks",
    # liquids
    "cider", "rum", "brandy", "wine", "whiskey", "stock", "broth", "dashi", "sake", "mirin", "coffee", "espresso",
    "tea", "seltzer", "liqueur", "(rice )?vinegar", "amaretto", "champagne", "brew", "vermouth", "bouillon",
    # misc
    "cornstarch", "xanthan gum", "baking", "soda", "meal", "sugar", "romero", "romano", "poblano", "wax", "germ",
    # buffalo is more likely the cheese than the meat
    "buffalo", "molasses", "oat(s)?", "cottage", "tabasco", "gelatin", "pectin", "palm", "pulp", "popcorn",
    # sour cream doesn't bold in the dairy category and the cream ensures the DF tag isnt added
    "sour cream", "muscovado", "chips", "multi(-)?", "fr(y|ies)", "can", "fire", "tree", "cloud", "ear(s)?"]
for value_list in match_tags.values(), neg_match_tags.values():
    for value in value_list:
        possible_ingredients.extend(value)

# Because starches and proteins contain substrings of items in other categories, it must be added last so the longest
# possible matching string is always found first and bolded in full (e.g. 'sweet potato' rather from t_vegetable rather
# than only 'potato' in t_starch
# This solution is fragile and ugly and for that I apologize
possible_ingredients += starches + proteins


def write_file(recipe_ingredients, raw_ingredients, recipe_body, recipe):
    """Write out the formatted recipe with additional elements (e.g. time estimates)"""
    with open('recipe.html', 'wb') as file:
        if recipe.title == "":
            recipe.title = "Title"
        file_contents = f"<br>{recipe.title}<br>"

        multiple_times = False
        if recipe.yield_str != "":
            file_contents += f"<b>Yield</b>: {recipe.yield_str.lower()}"
            multiple_times = True
        if recipe.prep_time != "":
            if multiple_times:
                file_contents += " | "
            file_contents += f"<b>Prep Time</b>: {recipe.prep_time}"
            multiple_times = True
        if recipe.total_time != "":
            if multiple_times:
                file_contents += " | "
            file_contents += f"<b>Total Time</b>: {recipe.total_time}"
        if multiple_times:
            file_contents += "<br>"

        file_contents += f"<ul>{recipe_ingredients}</ul> {recipe_body}<br>"

        if recipe.make_ahead != "" or recipe.storage != "" or recipe.to_serve != "":
            file_contents += "<br>"
            if recipe.to_serve != "":
                file_contents += f"<b>To serve</b>: {recipe.to_serve}<br>"
            if recipe.make_ahead != "":
                file_contents += f"<b>Make ahead</b>: {recipe.make_ahead}<br>"
            if recipe.storage != "":
                file_contents += f"<b>Storage</b>: {recipe.storage}<br>"
        if recipe.note != "":
            file_contents += f"<br><b>Note</b>: {recipe.note}<br>"

        file_contents += "<br>Source: "
        if recipe.link != "":
            if recipe.source == "":
                from urllib.parse import urlparse
                recipe.source = urlparse(recipe.link).hostname.split('.', 1)[1]
            file_contents += f'<a href="{recipe.link}">{recipe.source}</a>'
        else:
            file_contents += recipe.source

        file_contents += "<br><br>Tags: "
        # A set to prevent auto-generated tags from duplicating hard-coded ones
        tags_list = set()
        if recipe.default_tags:
            temp_tags = recipe.default_tags.split(sep=", ")
            for x in temp_tags:
                tags_list.add(x)

        # Guess at possibly applicable tags
        # This is a rudimentary system and must be corrected manually
        raw_ingredients = ''.join(raw_ingredients)
        for key, value in match_tags.items():
            # Search for whole-word matches only
            if any(re.search(r"\b" + match + r"\b", raw_ingredients.lower()) for match in value):
                tags_list.add(key)
        for key, value in neg_match_tags.items():
            if not any(re.search(r"\b" + match + r"\b", raw_ingredients.lower()) for match in value):
                tags_list.add(key)

        # Add meal tags to savory dishes
        if "t_dessert" not in tags_list:
            starch_tag = False
            protein_tag = False
            veg_tag = False

            if any(re.search(r"\b" + match + r"\b", raw_ingredients.lower()) for match in starches):
                starch_tag = True
            if any(re.search(r"\b" + match + r"\b", raw_ingredients.lower()) for match in proteins):
                protein_tag = True
            if "t_vegetable" in tags_list:
                veg_tag = True

            if protein_tag and veg_tag:
                # with or without starch
                tags_list.add("t_meal")
            elif starch_tag and protein_tag:
                tags_list.add("t_protein_starch")
            elif starch_tag and veg_tag:
                tags_list.add("t_vegetable_starch")
            elif protein_tag:
                tags_list.add("t_protein")
            elif veg_tag:
                tags_list.add("t_vegetable_dish")

        file_contents += ", ".join(str(e) for e in tags_list)
        file.write(file_contents.encode("utf-8"))


def universal_replace(words):
    """Perform recipe formatting (convert units to metric, etc)"""
    case_insensitive_subs = {
        "(?<![0-9])1 (tbsp|tbs)(\.)?": "1 tablespoon",
        "(?<![0-9])1 tsp(\.)?": "1 teaspoon",
        "([0-9]+ [0-9]/[0-9]) (tbsp|tbs)(\.)?": r"\1 tablespoons",
        "([0-9]/[0-9]) (tbsp|tbs)(\.)?": r"\1 tablespoon",
        "([0-9]+ [0-9]/[0-9]) tsp(\.)?": r"\1 teaspoons",
        "([0-9]/[0-9]) tsp(\.)?": r"\1 teaspoon",
        "([0-9]+) (tbsp|tbs)(\.)?": r"\1 tablespoons",
        "([0-9]+) tsp(\.)?": r"\1 teaspoons",
        # capturing formatted fractions like ½
        "([0-9]+( )?.) (tbsp|tbs)(\.)?": r"\1 tablespoons",
        "(.) (tbsp|tbs)(\.)?": r"\1 tablespoon",
        "([0-9]+( )?.) tsp(\.)?": r"\1 teaspoons",
        "(.) tsp(\.)?": r"\1 teaspoon"
    }

    units = {
        "1/16(-| )(inch|\")": "2 mm",
        "1/8(-| )(inch|\")": "3 mm",
        "1/4(-| )(inch|\")": "6 mm",
        "1/2(-| )(inch|\")": "1.2 cm",
        "3/4(-| )(inch|\")": "2 cm",
        "1(-| )(inch|\")": "2.5 cm",
        "2(-inch| inches|\")": "5 cm",
        "3(-inch| inches|\")": "8 cm",
        "4(-inch| inches|\")": "10 cm",
        "5(-inch| inches|\")": "13 cm",
        "6(-inch| inches|\")": "15 cm",
        "8(-inch| inches|\")": "20 cm",
        "10(-inch| inches|\")": "25 cm",
        "11(-inch| inches|\")": "28 cm",
        "12(-inch| inches|\")": "30 cm",
        "13(-inch| inches|\")": "33 cm",
        "14(-inch| inches|\")": "36 cm",
        "15(-inch| inches|\")": "38 cm",
        "16(-inch| inches|\")": "41 cm",
        " 1/2 (lb|pound|lb\.)": " 113 g",
        " 3/4 (lb|pound|lb\.)": " 340 g",
        " 1 (lb|pound|lb\.)": " 454 g",
        " 1 1/2 (lbs|lbs\.|pounds)": " 680 g",
        " 2 (lbs|lbs\.|pounds)": " 907 g",
        " 2 1/2 (lbs|lbs\.|pounds)": " 1.13 kg",
        " 3 (lbs|lbs\.|pounds)": " 1.4 kg",
        "1/2 ounce": "14 g",
        "1 ounce": "28 g",
        "1 1/2 ounces": "43 g",
        "2 ounces": "57 g",
        "3 ounces": "85 g",
        "4 ounces": "113 g",
        "5 ounces": "142 g",
        "6 ounces": "170 g",
        "7 ounces": "198 g",
        "8 ounces": "227 g",
        "10 ounces": "283 g",
        "12 ounces": "340 g",
        "6 fl oz": "180 ml"
    }

    ingredient_renames = {
        "scallions": "green onions",
        "Scallions": "Green onions",
        "scallion": "green onion",
        "Scallion": "Green onion",
        "rice wine vinegar": "rice vinegar",
        "Rice wine vinegar": "Rice vinegar",
        "cannellini": "cannellini (white kidney)"
    }

    words = perform_case_insensitive_replace(case_insensitive_subs, words)
    # Frankly more trouble than it's worth
    # words = perform_case_insensitive_replace(units, words)
    words = perform_replace(ingredient_renames, words)
    words = words.replace('<br><br>', '<br>')

    return words


def ingredients_replace(lines):
    """Format ingredients as a bulleted list"""
    # strip newlines
    lines = [bullet.replace('\n', '') for bullet in lines]
    lines = list(filter(None, lines))

    # Clean up, bold and capitalize the ingredients
    for index, ingredient in enumerate(lines):
        # strip prefixing special characters
        lines[index] = re.sub("▢( )?", "", lines[index])
        if "optional" in ingredient:
            lines[index] = lines[index][0].lower() + lines[index][1:]
            lines[index] = re.sub('(, )?(\()?optional(ly)?(\))?', "", lines[index], flags=re.IGNORECASE)
            lines[index] = "Optional: " + lines[index]
        else:
            # bold non-optional ingredients
            lines[index] = lines[index].capitalize()
            for tag_val in possible_ingredients:
                lines[index] = re.sub('\\b' + tag_val + '\\b', r'<b>\g<0></b>', lines[index], flags=re.IGNORECASE)

    # Convert to bullet points
    bulleted_ingredients = ""
    for ingredient in lines:
        bulleted_ingredients = f"{bulleted_ingredients}<li>{ingredient}</li>"

    return bulleted_ingredients


def body_replace(words):
    """Split paragraphs into one sentence per line"""
    substitutions = {
        "!": "!<br>",
        ".\n": "<br>",
        ". ": "<br>",
        ".)": ")<br>",
        " \n": "<br>",
        "\n\n": "<br>",
        "\n ": "<br>",
        "\n": "<br>"
    }

    words = perform_replace(substitutions, words)

    return words


def perform_replace(substitutions, words):
    """Perform find and replace given a dictionary"""
    for key, value in substitutions.items():
        words = words.replace(key, value)

    return words


def perform_case_insensitive_replace(substitutions, words):
    """Perform case-insensitive find and replace given a dictionary"""
    for key, value in substitutions.items():
        words = re.sub(key, value, words, flags=re.IGNORECASE)

    return words


class Recipe:
    import xml.etree.ElementTree as ET
    import sys

    xml_file = 'recipe.xml'
    if sys.argv[1:]:
        xml_file = sys.argv[1]

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find the entry node
    entry = root.find('entry')

    # Extract the values and strip leading/trailing whitespace
    title = entry.find('title').text.strip().title()
    yield_str = entry.find('yield').text.strip()
    prep_time = entry.find('prep_time').text.strip()
    total_time = entry.find('total_time').text.strip()
    to_serve = entry.find('to_serve').text.strip()
    make_ahead = entry.find('make_ahead').text.strip()
    storage = entry.find('storage').text.strip()
    note = entry.find('note').text.strip()

    ingredients = entry.find('ingredients').text.strip().splitlines()
    instructions = entry.find('instructions').text.strip()
    
    source = entry.find('source').text.strip()
    link = entry.find('link').text.strip()
    default_tags = entry.find('default_tags').text.strip()


if __name__ == '__main__':
    ingredients_txt, recipe_body_txt = format_recipe_text(Recipe.ingredients, Recipe.instructions)

    write_file(ingredients_txt, Recipe.ingredients, recipe_body_txt, Recipe())
