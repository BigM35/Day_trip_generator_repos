import random
from datetime import datetime   
import sys 



#Lists of cities and Descriptions
cities = [
"San Francisco? - San Francisco, a beautiful city built on massive hills and surrounded by water, is a place that marches to the beat of its own drum. Novices are always shocked at how chilly it is here, so pack a heavy sweater at any time of year, and use it while riding a cable car, taking a day-tour to Alcatraz Island, walking across the Golden Gate Bridge or laughing at the chubby sea lions at Fisherman's Wharf. ",
"Boston? - History and modernity are joined at the hip in Boston, one of America's first big cities and still one of its best. It's the place where federal architecture harkens back to the 1600s, juxtaposed with ultra-modern buildings by Frank Gehry, Walter Gropius and I.M. Pei. Speaking of architecture: be sure to see the Back Bay row houses, usual Instagram fodder that is actually an eye-catching must-see. From chowder to lobster rolls, Boston also loves its seafood, so be sure to visit the city's best raw bars and lobster shacks while you're in town.",
"Charleston? - Charleston is truly one of America's great metropolises, steeped in the history of the nation while boasting a thoroughly modern attitude toward the arts, culture and cuisine—you just need one quick glance at our list of the best Charleston restaurants to see that. Since around 1670, the architecture—and particularly the churches on every corner—has been enough of a reason to head to South Carolina's jewel, but recently the city has become a food and drink haven as well. Water views and hipsters abound at the Pavilion Bar; City Market sells the city's signature sweetgrass baskets; and dinner at chef Sean Brock's Husk is a transcendental experience.",
"Seattle? - From its emerald parks to the endless views of Puget Sound, Seattle is the crowning jewel of the Pacific Northwest. You'll see it all from the top of the iconic Space Needle—a 360 degree rotating atrium with a glass floor—but don't stop there. Seattle is full of incredible restaurants and world-class museums like the Seattle Art Museum and the Museum of Pop Culture. It's also the home of famed glass artist Dale Chihuly's Garden and Glass. And while the grunge era that put the city on the map is long gone, there are still plenty of excellent music venues to check out including Neumos and the Showbox.",
"Milwaukee? - You probably didn't know that Milwaukee holds the world's largest music festival, Summerfest, over three consecutive weekends in June and July. When the massive festival goes down, the pretty city by Lake Michigan goes more than a little crazy. With 11 stages, over 800 bands and close to a million fans rolling through, they're taking advantage of the warm weather in a big way. During the rest of the year, think cheese curds, beer breweries, cornhole tournaments and Packers fanatics, juxtaposed with a gorgeous art museum and the annual Sculpture Milwaukee outdoor showcase all over town (summer/fall). It's a vibrant, friendly city that Harley-Davidson calls home—don't miss their massive museum here.", 
"New Orleans? - After 300 years of existence, New Orleans is in the midst of a renaissance—except for the streets, which are the bumpiest you've ever encountered in a major metropolis. They love to dress up and party here, so put on a wig and mask, and hit the French Quarter and the Marigny for fabulous food at the best New Orleans restaurants. Grab a to-go cup filled with craft cocktails from one of the city's best bars, and indulge in the live music for which New Orleans is famous. Then dig deeper by visiting the Bywater neighborhood, home to an intoxicating mix of art and funk with incredible murals on every block, and stop at Bacchanal Wine for a munch, a sip, and a song (or two). One thing to remember while here: always keep an eye on the iconic architecture that defines this one-in-a-million, music-loving city.", 
"Chicago? - Frank Lloyd Wright buildings, deep-dish pizza, and the Cubbies: just three of the wonderful things that put Chicago on the world's radar. It's a big city with a friendly vibe that's got a whole street, Rush Street, devoted to drinking and dancing. You can party there until 4am, but save some strength for the festivals this city loves to put on, from July's Taste of Chicago and September's Pitchfork Music Fest to the big daddy of them all, Lollapalooza. This oh-so-cold city hunkers down in the winter, unless the Bears are playing football, in which case shirtless guys will brave subzero temps to cheer on their boys at Soldier Field.", 
"Salt Lake City? - No matter where you are in Salt Lake City, the snowcapped Rocky Mountains are never out of sight. They tower over the uber-clean city, a stunning landscape fit for a painting. And while Salt Lake is well-known for its Mormon heritage, there's more to the scene here than meets the eye. Restaurants range from the fine-dining favorite Log Haven to a healthy variety of ethnic and international restaurants. And while alcohol isn't as readily available here as in some cities, it's much easier to find than you think, including at the White Horse and Bourbon House downtown. While there, don't forget to take in a little of the outdoors: hiking, swimming, and picnicking at the Great Salt Lake is a good place to start.",
]

#List of each city's restaurants
san_francisco_restaurant = [
"Empress by Boon - Empress by Boon—from Malaysia-born Michelin-starred Chef Ho Chee Boon—is one of the most exciting restaurants to open in San Francisco recently. The restaurant opened its doors in June 2021, debuting a fully restored interior (inside the former space of Empress of China, an iconic Cantonese banquet hall in the heart of Chinatown that operated for roughly 50 years) that modernizes the space while keeping some of its original woodwork. Chef Ho, a Michelin-starred chef with experience at restaurants around the world (including Hakkasan), presents a prix fixe menu at a startingly reasonable rate of $78, as well as a separate small bites menu that's served in a trendy bar area. The menu focuses on modern takes on traditional Cantonese fare prepared with local ingredients, many from the restaurant's own organic farm in Gilroy, California.", 
"Nari - Nari is the most recent restaurant from chef Pim Techamuanvivit. A bit more sophisticated in both decor and cuisine than her previous spot, Kin Khao, the restaurant is led by mostly women including chef de cuisine Meghan Clark and bar director Megan Daniel Hoang. A contemporary Thai restaurant, chefs swap out some traditional Thai ingredients for locally grown seasonal ones, all the while preserving classic flavor profiles. The menu features large format dishes appropriate for sharing including rich curries with lamb, eggplant, pork belly and Cornish game hen.", 
"Liholiho - Liholiho brings a sunny dose of Hawaii to fog-shrouded San Francisco, from the bright yellow open kitchen to the “Aloha” spelled out in blue tile underfoot. The menu is divided into small, medium, and large plates, all designed for sharing. Dishes might include tuna poke on nori crackers, scallops with misoyaki pork belly, pecans, squash and grapes, or kimchi fried rice with smoked egg yolk, house-made spam and clamshell mushrooms. Save room for the Baked Hawaii, a fluffy, modern twist on the retro Baked Alaska made with caramelized pineapple ice cream and vanilla chiffon.",
"Taj Campton Place - Chef Srijith Gopinathan creates Cal-Indian cuisine by imbuing farmer's market ingredients with traditional Indian spices. The result is an exotic, high-end spin on Southern Indian food—one that has earned him at least one Michelin star every year since 2011. The Spice Route prix fixe menu ($167) features dishes like Maine lobster in a curry broth, duck breast with rhubarb and basil, and slow-cooked lamb served over basmati rice, snap peas, and cumin-lime yogurt. (The lamb and game bird dishes are cooked in an authentic tandoori oven.) For a more affordable but still luxurious experience, check out the weekend brunch service.",
"Acquerello - Acquerello may be one of the oldest restaurants on this list but it's far from stuck in its ways. The Italian favorite keeps things innovative by showcasing talented young chefs alongside the expertise of master chef-partner Suzette Gresham. In one of the most Old World refined dining rooms in town, diners revel in a prix fixe ($115 for three courses, $135 for four, $150 for five) or seasonal tasting menu ($225) showcasing dishes like the decadent Dungeness crab risotto with asparagus, cured egg yolk and oxalis. A two-star Michelin restaurant, Acquarello is not just a place to celebrate, its food is a celebration in-and-of itself.", 
"Angler - Appropriately located on the Embarcadero, this waterfront restaurant from chef Joshua Skenes, of Saison fame, relishes the taste of the sea with a raw bar and delicacies like Monterey abalone, giant octopus and scorpion fish roasted over an open wood fireplace. With walls hung in taxidermied game, it should be no surprise that Angler's earthly delights, too, are delightful—dishes like smoky, succulent cordycep mushrooms, the signature radicchio salad with vegetarian XO sauce and hot fried quail.", 
"Aziza - It's back! After a long absence, Aziza is open again, and this time it's a more neighborhood focused contemporary California restaurant with Moroccan influences. There are still some of the classic Moroccan dishes that diners loved, such as basteeya, beef tagine and hand rolled couscous with aged butter but also fresh new dishes like cured ocean trout with citrus, avocado and marash chile. A glowing new bar is beautiful with blue-green tiles. The airy main dining room can get loud on busy nights, so ask to be seated in the cozy back room if you want a quieter experience.", 
"Ben - Dried fruit, flowers, and herbs hang overhead and the kitchen is visible through spotless glass at this three-Michelin-starred restaurant. The French-meets-Asian food is the vision of James Beard Award-winner Corey Lee, formerly the head chef at French Laundry. The nightly tasting menu skews primarily toward seafood and vegetables and Asian influences emerge in dishes like a thousand-year-old quail egg, lobster coral soup dumplings, and abalone-stuffed chicken wings. The wine list includes more than 300 bottles. ", 
"El Buen Comer - This Bernal Heights cafe is serving up authentic Chilango cuisine from Mexico-born chef Isabel Caudillo in a bright, casual space. Housemade tortillas, beans and rice complement a variety of guisados which change on a daily basis, ranging from slow-cooked stews like tinga (pulled chicken simmered in tomato, onion and chipotle) and albondigas to a variety of mole dishes. Tacos, sopes and tostadas are topped with chicharron in salsa verde, rajas con crema and papas con chorizo. Saturday and Sunday brunch feature irresistible chilaquiles smothered in red or green sauce.", 
"Californios - This Michelin-starred Mexican spot is a design-lover's dream, from the mirrored, unmarked facade to the neon art in the restroom. With its black walls, low lighting, and vibrant art, the decor matches the food: splurgy and surprising. Slip into the leather banquette or snag a spot at the bar for a view of the open kitchen. Chef Val Cantu's decadent, 16-course tasting menu changes seasonally—expect heart-stoppingly rich dishes like lobster tacos, wagyu steak, and foie gras-garnished churros. The beverage pairing typically includes wine, beer, and cider."
]

boston_restaurants = [
"Sarma - As the casual sibling of Ana Sortun's celebrated Oleana, Sarma is one of the area's best spots to find big, bold Mediterranean and Middle Eastern flavors crammed into small bites. All items from chef-owner Cassie Piuma's prix-fixe culinary experience—from the sesame fried chicken to the merguez pinwheels—are served in a traditional family-style format. Vegetarians can rejoice, as the eatery offers an entire menu of meatless meze. The bar also deserves an applause for its aromatic cocktails featuring ingredients like cardamom, orange blossom and fenugreek.",
"Nightshade Noodle Bar - Just north of the city, you'll find this intimate, plant-packed and rattan-accented oasis serving up refreshing, Vietnamese-inspired cuisine. Chef-owner Rachel Miller is at the helm of this female-forward kitchen in Lynn, which first started as a pop-up venture before becoming a brick-and-mortar establishment in 2019. The menu dazzles with delicate yet decadent dishes that offer playfully unexpected flavor combinations, such as the frothy, vanilla-laced lobster glacé, foie gras with grilled coconut sticky rice and sour cherries, and warm Mediterranean olives tossed in sesame and Asian aromatics. More substantial plates include a rotation of hand-pulled noodles (normally served in some sort of bliss-inducing broth) and fried rice (go with the bone marrow variety for an extra dose of umami). Be on the lookout for indulgent seafood specialties like the Viet Cajun shellfish boil or live sea urchins crammed with glass noodles, tomato water nuoc cham, pickled peppers and charred tomato hollandaise—the latter of which is hidden under a smoke-filled cloche and theatrically revealed tableside. Ask the extremely friendly staff to guide you through their highly curated selection of wines, customize a spritz to your liking or go with an Southeast Asian-influenced cocktail (i.e. its signature saigon cigar club, a blend of bourbon, thai banana and black cardamom).",
"Spoke Wine Bar - New American cuisine and Old World wines intermingle at this intimate Somerville eatery and bar. Located in the center of Davis Square, this cozy little sanctuary is all about thoughtful curation, both in terms of its diverse wine list and the ingredients its kitchen procures from local purveyors. Spoke keeps its short list of modern New England small plates dynamic, regularly swapping out dishes for new ones to reflect the seasons—but no matter what time of year you stop into this spot, you'll find effortlessly elegant bites to accompany whatever pour you prefer. If our descriptors haven't tipped you off yet, this place is super small, so reservations are highly recommended.  ",
"O Ya - Clear out your bank account and clear your weekend, because o ya's singular dining experience is one to be savored. Owners Tim and Nancy Cushman set a new bar for special-event dining with o ya's opening in 2007, but even today, the restaurant regularly wins accolades as one of the best restaurants in all of New England. The sushi and omakase menu is a marvel of both flavor and presentation, with every morsel—from the foie gras nigiri to the bluefin tuna and smoked salmon sashimi—proving to be a delectable work of art. ",
"Urban Hearth - What started as a supper club is now a charmingly tiny restaurant located just a short stroll from Somerville's Davis Square. As chef-owner Erin Miller puts it, this place strives to be “whimsy and unpretentious”—a feat that it easily accomplishes with its elevated New American fare and casually chic space. Enter this intimate eatery—which immediately feels more like someone's apartment rather than a restaurant—and you'll find a weekly menu of hyper-local food prepared with purpose and a keen eye for balance. With a slightly European approach, the kitchen here (which is literally in the dining room) takes its time and places an emphasis on savoring the experience, so don't expect a mad dash of a meal.",
"Barra - Paola Ibarra and Yhadira Guzmán bring the brightness of their beloved Mexico City to Somerville's Union Square with Barra. This eatery may be small on space, but it's big on acid and is sure to leave patrons' taste buds tingling -- whether it's with its guacamole piled onto freshly fried chicharrón, its cactus salad or its aguachile. Alongside a selection of top-notch tacos and seasonal tamales, diners can sip on flights of the finest mezcal, refreshing pints of michelada and margaritas rimmed with chapulines for a truly Mexican touch.",
"Celeste - What started as Juanma Calderón and Maria Rondeau's home-based pop-up has now become the city's top-rated Peruvian restaurant. Located a short stroll from Union Square, Celeste attracts Somerville and Cambridge residents, who get a front-row seat to all of the open kitchen action as they eat. Diners fill the small space to nosh on Peruvian standards—ceviche, causa, lomo saltado—done in style. When you go, don't miss out on the bar program, which focuses on pisco-based cocktails.",
"Mahaniyom - Nestled in Brookline Village, Mahaniyom serves Thai tapas and cocktails with finesse. The team behind this neighborhood hangout strives to share a piece of Thailand with guests through flavors that feel like home. The menu here is filled with street food favorites—think Chicken Ka-Prow—as well as spectacular small plates, like Muk Yang Ka-Min (grilled spiced squid) and Yum Ngoh (a rambutan salad studded with fried shrimp, toasted coconut, cashews, fried shallots and garlic, and chili jam). And as far as the bar goes, this place knows how to punch up classic Western libations with serious Southeast Asian touches, such as a Sazerac made with Thai tea-infused rye and a chrysanthemum-flavored gin and tonic.",
"Pammy's - Situated between Central and Harvard Squares, this hip trattoria has a slightly retro feel thanks to the amber glow of its globe lights and double-sided fireplace. The globally minded menu heavily relies on Asian ingredients, often applying them to Italian preparations and creating fantastically flavored fusion food. Nosh on handmade pastas, like its renowned lumache with bolognese and gojuchang, and strike up a conversation with your dining neighbors at the vintage communal table. Sexy cocktails, including its draft aperitivi, are not to be missed.",
"Giulia - Chef-owner Michael Pagliarini and his staff pamper their guests with friendly, professional service and killer pastas, which are prepared daily on a custom-made table that accommodates large groups at night. Brick walls and candlelight keep the vibe romantic and rustic. The all-Italian wine list pairs well with the menu, some of which is inspired by the chef's travels throughout Italy. Be sure to save room for dessert—particularly the pistachio gelato with sour cherries and anise pizelle—because this eatery does dolci right. "
]

charleston_restaurants = [
"Zero Restaurant + Bar -An upscale cafe helmed by chef Vinson Petrillo that's one of the most romantic and under-the-radar restaurants in Charleston. On offer is a luxurious prix-fixe, six-course menu that's creative and plated like a work of art. The restaurant's setting, within a boutique hotel, affords it a one-of-a-kind ambiance that has diners feel like they're consuming a meal right in the chef's home.  ", 
"Wild Olive Restaurant - This cozy Italian eatery has a homey, rustic feel, making it the perfect place for a weeknight get-together with friends, a casual date night or dinner with the whole family. The wine list is extensive and the food menu is so large that you could return here regularly and never eat the same thing twice.", 
"Stella's - A lively, homestyle Greek kitchen serving meze and Mediterranean fare. The restaurant is a neighborhood favorite and is always crowded, so you'll definitely want to make a reservation ahead of time. The menu is a great combination of classic and modern Greek food, which pairs perfectly with the specialty cocktails and Greek wine list.", 
"Cuban Gypsy Pantry -  From humble beginnings in a food truck, Cuban Gypsy Pantry now has its own permanent residence on Calhoun Street. Alright, so it's fairly intimate, but that only adds to the experience.", 
"Halls Chophouse -  An upscale steakhouse in downtown Charleston offering some seriously good cuts of meat. When it comes to steak, you'd be hard pressed to find a better one than the one served at Halls. The food, coupled with the restaurant's dark wood features, muted lighting and emphasis on hospitality, make it the perfect place to celebrate a special occasion.", 
"Rodney Scott's - Proper South Carolina barbecue that goes the whole hog - literally, over a wood-stoked fire pit. Expect a fun and relaxed vibe, with high quality cooking.", 
"Balao - Charleston's newest rooftop bar opened just in time to usher in summer weather. The space is quaint and cozy, with lots of natural browns, blues and wood elements to complement the restauran's ocean theme. The menu itself changes daily based on what's available, although the tuna nachos seem to be a set standard—and for good reason, too. The combination of poblano queso, blackened tuna and guacamole with their house-made tortilla chips is a real winner.", 
"Millers All Day - Millers All Day is the perfect place for those who think that brunch should not be limited to just the weekends. Millers serves a great menu full of favorites—think waffles, biscuits and gravy, and a rotating grits bowl—every day of the week. And since it's not really brunch without a proper drink, the venue's specialty cocktails (like the super popular brunch punch, a frozen concoction that's deceivingly delicious and easy to drink) make the perfect pairing with any menu item.", 
"Workshop -  Charleston's first (and, as of now, only) food hall is in Wagener Terrace downtown and features a rotating residence of innovative (and sometimes experimental) restaurants and pop-ups. It's infusing some much needed variety into Charleston's culinary scene, with flavors and cuisines that had previously been missing from the city's dining options.", 
"R Kitchen - Fancy a seat at the chef's table? You got it! At R Kitchen (the R stands for Rutledge), every table belongs to the chef as the intimate room - which is basically the kitchen - seats just 16."
]

seattle_restaurants = [
"Canlis - It can be hard to find a unique menu of American fare these days, but the Original lives up to its name with local freshwater fish dishes and Wisconsin produce-inspired plates. The dimly-lit wooden bar becomes the perfect environment to enjoy a cocktail or glass of wine, especially since each menu item offers a suggested pairing.", 
"Archipelago - This intimate, inventive restaurant in Hillman City melds Pacific Northwest cuisine with Filipino-American flavors. Offering a seasonal 9-12 course tasting menu, the meal weaves flavors with the story of the chef-owners' journeys as immigrants to the region. The focus is on local produce, enhanced with a bit of history.", 
"Meesha - Taste Indian cuisine in a whole new way at Meesha. The contemporary dishes are bursting with flavor, a simple celebration. Familiar dishes like pakoras and butter chicken are on the menu, but don't miss Amritsari fish (panfried rockfish with cardamom and fenugreek), paneer in a spiced tomato sauce or bukhara dal. ", 
"Sushi Kashiba - Believe it or not, Pike Place Market is home to a James Beard Outstanding Chef nominee. Seats at the bar here are the most coveted, as you can watch said master sushi chef at work. The omakase option will feature seasonal offerings, but every item on the menu will be fresh and delicious.", 
"Bar del Corso - For spot-on Neapolitan pizzas, head to Beacon Hill. Though slightly hidden, Bar del Corso is frequently packed, but the wait is worth it for the pizzas with bubbly, crispy crust. The rest of the menu is equally tasty, with items like meatballs, salt cod fritters or grilled octopus with corona beans." 
"Super six - From the owners of the Marination group of tasty restaurants comes a Korean-Hawaiian joint set up in a vintage garage. The all-day menu includes hearty dishes like loco moco, sichuan pork noodles, spam musubi and addictively sweet malasadas.",
"Xi'ian Noodles - At this unassuming spot in the University District, you'll find some of the best noodles in town. Chewy, tender, hand-pulled noodles are best when served simply with hot chili oil, but toppings like spicy cumin lamb and stewed pork.", 
"Un Bien - Chew on what many consider to be Seattle's most delicious sandwich offerings at Un Bien. Hours-long cooked meats drenched in the best Caribbean juices make waiting on the side of the street for your order worth it. Trust us on this one.", 
"Kau Kau - At this unassuming spot in the University District, you'll find some of the best noodles in town. Chewy, tender, hand-pulled noodles are best when served simply with hot chili oil, but toppings like spicy cumin lamb and stewed pork.", 
"Bruciato - Taking a ferry to visit a restaurant may sound a bit excessive but, in this case, it's exactly what you should be doing. With a wood-burning stove on site, Bruciato serves one of the best slices you'll ever nosh on. Offering pies bursting with the likes of chorizo, honey and morel mushrooms (only when they are in season, of course), the eatery promises to deliver one of the most transcendent pizza-eating experiences of your life."
]

milwaukee_restaurants = [
'Goodkind -  It can be hard to find a unique menu of American fare these days, but the Original lives up to its name with local freshwater fish dishes and Wisconsin produce-inspired plates. The dimly-lit wooden bar becomes the perfect environment to enjoy a cocktail or glass of wine, especially since each menu item offers a suggested pairing.', 
"Kipp's Frozen custard -  America's Dairyland is famously known for its frozen custard and butter burgers, and Kopp's tops the list for both. While you'll have to venture out to the suburbs to find a Kopp's location, it's totally worth the trek. Come with an appetite for flat burgers the size of your head, and be sure to check the Flavor Forecast beforehand so you can have your order planned out in advance.", 
"Blue Egg - If you ask anyone in Milwaukee where the best brunch food is, they''ll point you towards Blue's Egg. Its original west side location was so popular that they opened a north side location to meet the demand, though both still can have lengthy waits. From traditional breakfasts to unique brunch items, everything on the menu is delicious and affordable. They've got a flawless Bloody Mary if you're in need of a little “hair of the dog.", 
"Lakefront Brewery - There is no shortage of breweries in Milwaukee, but Lakefront tops them all for a full boozy experience. The brewery tour is a must, providing tokens for free beer tastings at the end. Even if you aren't interested in how their beer is made, their Wisconsin-centric menu will win you over. The Friday Fish Fry is consistently rated one of the city's best, often paired with live polka music. Keep the oil-dunked fare going with a dish of their popular fried cheese curds.", 
"Harbor House - There is no better view of downtown Milwaukee and Lake Michigan than from the Harbor House. Posted between the Milwaukee Art Museum and the Summerfest grounds on a long pier, it's the perfect locale for a fancy dinner or special occasion. Part of the city's famous Bartolotta restaurant group, this gem shines with a focus on fresh seafood fare alongside an extensive wine list.", 
"sobelman's on St. Paul -  Milwaukee is a major drinking town, which mean proper hangover cures are a necessity. Sobelman's on St. Paul is down in the up-and-coming Menominee Valley area and is globally known for its comically extravagant Bloody Mary garnishes. These can include anything from a cheeseburger slider, a slice of pizza, or a whole fried chicken...or all three! If you're still hungry (doubtful), then you can take a stab at the actual food menu.", 
"Vanguard Bar - You can't go to Milwaukee without eating some stellar sausages.They offer a variety of choices ranging from classic Milwaukee brats to Asian-inspired links, and everything in between (read: Vegan sausage). In true Wisconsin form, there are plenty of local beers and draft cocktails to wash down your delicious sausages before heading out in hip Bay View for the night.", 
"Bodegon - Fine dining that isn't American fare can be hard to come by in Milwaukee; that was until Bodegón broke into the scene. Located in the historical Hotel Madrid building in Walker's Point, the restaurant sports a menu featuring rustic Spanish specialities paired with an impressive wine cellar and full bar. While it's called Hotel Madrid, it's mainly just the restaurant with two AirBnB apartments upstairs.", 
"La Merenda - If you're ever indecisive about what you want to eat for dinner, La Merenda is the answer (especially if you like to share). One of the initial restaurants to open in the trendy Walker's Point neighborhood, it was a key source of attraction for hungry suburbanites. With small plates from around the world, its tapas is as varied as its guests and furnishings: No two items are the same.  ", 
"The Original - It can be hard to find a unique menu of American fare these days, but the Original lives up to its name with local freshwater fish dishes and Wisconsin produce-inspired plates. The dimly-lit wooden bar becomes the perfect environment to enjoy a cocktail or glass of wine, especially since each menu item offers a suggested pairing."
]

new_orleans_restaurants = [
"Commander's Palace - The crown jewel of the Brennan food empire, this landmark Garden District restaurant has been a beacon of fine dining since 1880. There's no resting on laurels here, though: Chefs Paul Prudhomme, Emeril Lagasse, Jaime Shannon, Tory McPhail and now Meg Bickford have nurtured the Creole menu while making their own marks. The iconic Victorian mansion is the perfect setting for an intimate meal, large celebration or relaxed 25-cent martini lunch. Turtle soup is a must, the bread pudding soufflé provides an excellent finish and everything in between will impress.",
"Herbsaint - Chef Donald Link's restaurant group is heavy on the James Beard awards, bestowed upon loads of chefs that have passed through his flagship restaurant. This Central Business District favorite is consistently packed with a mix of the after-work business crowd, local families and tourists. Local farmers and fishermen are well represented on the seasonal menu that combines French, Southern and rustic Italian influences. Daily lunch and dinner specials always impress alongside standards like house-made spaghetti with a poached farm egg or duck confit with dirty rice, all enhanced by an eclectic wine list.",
"Brigtsen's - This century-old Victorian cottage tucked away in the Riverbend is home to some of the best modern Creole fare in the city. Chef Frank Brigtsen updates classic dishes in a straightforward way with delicious results. Perfect after enjoying a stroll through the surrounding neighborhood, it's an excellent option for sampling New Orleans cooking in an intimate, friendly setting that feels like a friend's home. Each dish—from the rabbit gumbo and maque choux to shrimp rémoulade and trout meuniere—is made with care and full of flavor.",
"Coquette - This Garden District gem has the vibe of a neighborhood bistro but the menu of a forward-thinking, adventurous kitchen. The small list changes regularly to reflect what's fresh and local, as well as what creative twists chefs Kristen Essig and Michael Stoltzfus have come up with. Entrées have included black drum in vegetable sauce with fennel sausage and Mexican street corn-style okra and red snapper with butter beans. Can't decide? The five-course blind tasting option is always full of surprises.",
"Cochon - This bright, welcoming spot from Donald Link and Stephen Stryjewski elevates the boucherie and the flavors of Cajun country with refined takes on boudin, andouille and head cheese. Pork, seafood and produce are locally sourced and prepared in-house. The cocktail list includes flights of moonshine to get you prepped for rabbit and dumplings, cochon with cracklings, “fisherman's style” whole Gulf fish or smoked short rib with chanterelles. The setting—anchored by heavy wood tables—is rustic yet contemporary, reflective of its Warehouse District location. Stop next door at Cochon Butcher to take home a few meaty treats.",
"Gris-Gris - New Orleans has plenty of restaurants serving the classics, but Gris-Gris takes them to new heights, with updates that are more than just trendy twists on the original. An oyster BLT comes with smoked pork belly, tomato jam, arugula and sugar cane vinegar, while the standout duck breast—topped with local molasses and a sugarcane demi-glace—is served with a roasted sweet potato and pecan casserole. Chef Eric Cook's mom's recipe for chicken and dumplings is a hit as well. The setting—downstairs has an open kitchen and counter seating, upstairs has a dining room and bar as well as outdoor balcony seating with views of lower Magazine Street—has helped establish Gris-Gris as a go-to spot for neighborhood regulars as well as special occasion diners.",
"Saba - Chef Alon Shaya serves contemporary Israeli cuisine with a dedication to ingredients, technique and staff wellbeing. The bright, airy Uptown restaurant provides a warm setting in which to enjoy shareable dishes like Shaya's grandmother's lutenitsa, local tomato ezme, harissa roasted chicken and hummus topped with blue crab. The pita, served fresh from the wood-burning oven, is simply heavenly. Creative cocktails and a wine list that includes Slovenian and Israeli selections are perfect complements.",
"La Petite Grocery - Chef Justin Devillier has been creatively enhancing New Orleans classics on Magazine Street for more than a decade. Refined but lively, La Petite Grocery is where to go for a bit of edge alongside the familiar: Beignets are stuffed with blue crab and finished with malt vinegar; the gumbo features tasso and chicken confit; and turtle Bolognese is served with bucatini and a fried soft boiled egg. The LPG Cheeseburger, with house-made pickles, onion marmalade, aioli and gruyere on a brioche bun, is another crowd favorite. Chef Devillier has expanded his talents, most recently with Justine, but this Uptown spot remains his signature offering.",
"GW Fins - Fresh fish is the star at this French Quarter fine dining establishment. As an avid fisherman, chef Tenney Flynn is meticulous when it comes to choosing the freshest product from his sources, and his entrées change daily to reflect the best catch. Whatever the preparation—wood-grilled, parmesan crusted, blackened—the flavors of the fish shine through. Appetizers like lobster dumplings and New Orleans-style barbecue shrimp are constants. Try not to fill up on the delectable biscuits and cross your fingers that the “Scalibut”—a deliciously unique halibut/scallop combo—is on the menu.",
"Compere Lapin - Chef Nina Compton has made her mark on New Orleans since opening Compere Lapin in the Old 77 Hotel & Chandlery in 2015. Mixing the flavors of her Caribbean homeland of Saint Lucia with classic New Orleans cuisine, her menu has received consistent raves. The setting—with its exposed brick and wooden beams—is both intimate and buzzy. The excellent cocktail program kicks things off, followed by must-try conversation starters like spiced pig ears and conch croquettes. The goat curry, set atop sweet potato gnocchi, is a star entrée, and seasonal updates bring exciting new flavors to palates. Following the success of Compere Lapin, chef Compton opened Bywater American Bistro, which has also proven to be a hit."
]

chicago_restaurants = [
"Lula Cafe -  A unanimously beloved neighborhood darling that's been doing the whole farm-to-table thing long before it was a thing.",
"Dear Margaret - An unpretentious, warm and inviting destination for hearty French-Canadian fare.",
"Alla Vita - A hearty Italian eatery helmed by longtime Boka exectutive chef Lee Wolen, where you can indulge in a carb-heavy meal of fresh pasta and wood-fired pizza.",
"Tzuco - ? Chef Carlos Gaytán's splashy Chicago comeback: a breathtakingly beautiful River North restaurant that pays homage to his hometown of Huitzuco, Mexico.",
"Galit - New Orleans chef Zachary Engel's (Shaya) raved-about entry to Chicago's dining scene: a Middle Eastern eatery in the heart of Lincoln Park",
"The Hot Dog Box - A year-round outpost of small but mighty hot dog stand that originally opened in Bronzeville's Boxville Marketplace, founded by local musician Bobby Morelli and his daughter Brooklyn.",
"Esme - Chef Jenner Tomaska (Next) and his wife/business partner Katrina Bravo bring pricey tasting menus to a well-to-do corner near the Lincoln Park Zoo",
"Hinoki Sushiko - A bi-level izakaya and omakase restaurant from chef Otto Phan, who also runs the acclaimed 14-seat omakase restaurant Kyōten in Logan Square.",
"The Bristol -  With seasonal tasting menus and great à la carte options, Bucktown stalwart The Bristol toes the line between fine dining and an upscale neighborhood restaurant.",
"Lardon -  A meat- and cheese-centric cafe just off the California Blue Line stop that serves Metropolis coffee and sandwiches during the day as well as cheese boards and entrees in the evening."
]

salt_lake_restaurants = [
"Ruth's Diner - The grandmother of SLC eateries, Ruth's has been flipping burgers since 1930—though it's changed locations and hands over the years. Tucked away in Emigration Canyon, this local institution has a sprawling, verdant patio that feels like a well-kept secret. What's not a secret are Ruth's mile-high biscuits, which make excellent fluffy vehicles for everything from bacon to maple syrup.",
"Bagels and Greens - Legit bagels west of the Mississippi are hard to come by. That's why Bagels and Greens—and its older sister restaurant the Bagel Project—are precious commodities in Utah. The new downtown outpost for chewy dough slings irresistible bagel sandwiches like the local favorite Lox and Loaded. Don't leave this essential lunch spot without a baker's dozen and house-made cream cheese to-go, too.",
"Pig & a Jelly Jar - When you need an epic breakfast at two in the afternoon, head to this bright and funky Southern diner. The important choice: white meat (fried chicken and Belgian waffles) or the other white meat (smoked ham and green chile hollandaise eggs with biscuits)? The menu here doesn't just pay lip service to the South. Pig & a Jelly also serves regional favorites like pork cracklings and beignets with a blueberry lavender jam."
"Red Iguana - Utahns may not see eye-to-eye on some things, but we can all put politics aside and agree that Red Iguana is king of Mexican in the city. A local favorite since the mid-'80s, this colorful restaurant has not one but seven varieties of mole on the menu, including a must-try Mole Colaradito with Mexican chocolate, pine nuts and fresh poblano over carnitas. The Cardenas family behind Red Iguana also serves killer Mexican cocktails from a Paloma to a sour-sweet Tamarindo marg.",
"Mom's Kitchen - Nestled amidst car dealerships on State Street in South Salt Lake, this Taiwanese restaurant is the definition of hole-in-the-wall. An order of Mom's Dumplings here is the ultimate comfort food come winter. And don't put on a brave face when it comes to spice; even a 2 or 3 out of 10 on Mom's heat scale will make you sweat. The menu's no pushover either; you'll find everything from pig intestines boiled in blood to bamboo fungus soup—but you can always play it safe with fried rice.",
"Lucky 13 Bar and Grill - Part sports bar, part happening patio, part biker destination, this award-winning burger joint just blocks from Smith's Ballpark defies categorization. A foot-tall burger is just one of the many culinary trials that await. If you don't feel like consuming 28 ounces of fresh ground chuck in one sitting, there are many more reasonably sized options, from the Fungus Amoungus to the Pigpen, topped with bacon smoked in-house, ham, cheddar, Swiss and Lucky 13 sauce.",
"The Dodo - There are a lot of reasons to visit this Sugarhouse mainstay, but the most important one is named Ramon. This talented pastry chef has been baking up pies and other desserts at the Dodo since it opened over three decades ago. If you insist on going savory before digging into the signature Toll House pie or a slice of banana cream cheesecake, the Dodo's known for its stacked turkey sandwiches.",
"Bombay House - Aromas of cumin, turmeric, and cardamom hit before you even set foot inside Bombay House, which prepares many of its items in a tandoor—a clay coal-fired oven—imparting a delicate smoky flavor to meats and flatbreads alike. The latter go far beyond garlic naan, with options ranging from a gluten-free chickpea Channa Roti to the bold Peshawari Naan, stuffed with coconut, raisins, and cashews.",
"Laid Back Poke Shack - Aromas of cumin, turmeric, and cardamom hit before you even set foot inside Bombay House, which prepares many of its items in a tandoor—a clay coal-fired oven—imparting a delicate smoky flavor to meats and flatbreads alike. The latter go far beyond garlic naan, with options ranging from a gluten-free chickpea Channa Roti to the bold Peshawari Naan, stuffed with coconut, raisins, and cashews.",
"Settebello - If your pizza motto is “Naples or bust,” this is your place for pies in SLC. Vera Pizza Napoletana (a non-profit cultivating the culinary art of Neapolitan pizza) Member no. 245 bakes its pizzas in a wood-fired oven made of bricks literally bound together by volcanic sand from Mt. Vesuvius. The Pizza Carbonara topped with pancetta and egg is what Neapolitan dreams are made of."
]

#List of activities to do
things_to_do = [" going on a free walking tour ", "taking an audio tour ", "exploreing the Markets ", "visiting Free Museums and Galleries ", "hanging out with the locals ", "going on a Carnival, then to a festival and enjoying some free live performances ", "Strolling around a Park ", "going to the library ", "visiting the Churches and Cathedrals and asking for forgivness "]

#List of transportation methoid
mode_of_transportation = ["driving ","Taxiing ", " taking the train ", "flying ", "taking a boat ", "taking the flying ferry ", "walking? ", "jumping ", "crawling ", "skipping "]

#Get the hr(int) for current time
curr_hour = datetime.now()
hour = curr_hour.hour

#Prompt user to enter their name
user_name = input("Please Enter your name: ")

#Using the hour of the current local time, generate a greeting message to match the current time of day
def determine_part_of_day(time,name):
    if 5 < time < 12:
        return f"Good morning {name}, "
    elif 12 <= time < 17:
        return f"Good afternoon {name}, "
    elif 17 <= time < 22:
        return f"Good evening {name}, "
    else:
       return f"Its late {name}, but reguardless, "

#Determine if input is yes/no
def determine_user_input(pass_input):
    while "no" != pass_input.lower() != 'yes':
        print("\n")
        pass_input = input("Invalid Entry! Please answer with [Yes/No]. So does the last entry sound good? [Yes/No]: ").lower()
        if pass_input == 'yes' or 'no':
            return pass_input
    if pass_input.lower() == 'yes' or 'no':
        return pass_input

#Greeting and introduction
def introduction():
    print("\n")
    user_answer_from_intro = input(f"{determine_part_of_day(hour, user_name)} I am here to help you determine the location of your next trip, recommend some great restaurants, some fun activities, and the transportation choices. Are you ready to get started? [Yes/No]: ").lower()
    checked_answer = determine_user_input(user_answer_from_intro)
    if "no" == checked_answer:
        print("\n")
        print(f"Okay {user_name}, I will be here whenever you need help with your trip, goodbye for now.") 
        exit()
    else: 
        print("\n")
        print(f"Excellent! So {user_name}, lets start off with the destination...")
        
#Given a list of items, return a random element
def generate_new_choice(current_list):
    user_choice = random.choice(current_list)
    print("\n")
    user_answer = input(f"How about {user_choice}. Sounds good? [Yes/No]: ").lower()
    checked_user_answer = determine_user_input(user_answer)
    while checked_user_answer == "no":
        print("\n")
        user_choice = random.choice(current_list)
        user_answer = input(f"How about {user_choice}. Sounds good? [Yes/No]: ").lower()
        checked_user_answer = determine_user_input(user_answer)
    if checked_user_answer.lower() == "yes":
        return user_choice
    
#Base on the element in the list, determine the city name
def get_city_name(info):
    if "San Francisco?" in info:
        return "San Francisco"
    elif ("Boston?") in info:
       return "Boston"
    elif ("Charleston?") in info:
        return "Charleston"
    elif "Seattle?" in info:
        return "Seattle"
    elif ("Milwaukee?") in info:
        return "Milwaukee"
    elif ("New Orleans?") in info:
        return "New Orleans"
    elif ("Chicago?") in info:
        return "Chicago"
    elif ("Salt Lake City?") in info:
       return "Salt Lake City"

#Determine what the restaurants
def get_restaurant(city):
    if "San Francisco" == city:
        print("\n")
        print("Great, now on to restaurants in San Francisco!")
        return generate_new_choice(salt_lake_restaurants)
    elif "Boston" == city:
        print("\n")
        print("Great, now on to restaurants in Boston!")
        return generate_new_choice(boston_restaurants)
    elif "Charleston" == city:
        print("\n")
        print("Great, now on to restaurants in Charleston!")
        return generate_new_choice(charleston_restaurants)
    elif "Seattle" == city:
        print("\n")
        print("Great, now on to restaurants in Seattle!")
        return generate_new_choice(seattle_restaurants)
    elif "Milwaukee" == city:
        print("\n")
        print("Great, now on to restaurants in Milwaukee!")
        return generate_new_choice(milwaukee_restaurants)
    elif "New Orleans" == city:
        print("\n")
        print("Great, now on to restaurants in New Orleans!")
        return generate_new_choice(new_orleans_restaurants)
    elif "Chicago" == city:
        print("\n")
        print("Great, now on to restaurants in Chicago!")
        return generate_new_choice(chicago_restaurants)
    elif "Salt Lake City?" == city:
        print("\n")
        print("Great, now on to restaurants in Salt Lake City!")
        return generate_new_choice(salt_lake_restaurants)

#Generate random actitive
def generate_activity(city_name, act_list):
    print("\n")
    print(f"Sounds wonderful! But a trip to {city_name} is not completed without finding something to do! With that being said...")
    return generate_new_choice(act_list)

#Generate transportation
def generate_transportation(city_name,transport_list):
    print("\n")
    print(f"Sounds fun! Finally, lets decide on how we will be getting to {city_name}!")
    return generate_new_choice(transport_list)

def verfied_restaurant(first_des, final_des):
    if first_des != final_des:
        return get_restaurant(final_des)
    else:
        return first_des

#calling function
print(introduction())
destination_details = generate_new_choice(cities)
destination_name = get_city_name(destination_details)
chosen_restaurant = get_restaurant(destination_name)
chosen_thing_to_do = generate_activity(destination_name, things_to_do)
chosen_transport = generate_transportation(destination_name, mode_of_transportation)

 
#Final confirmation
print("\n")
print("You are almost done, let just confirm a few things. ")

def user_confirmation(whats_chosen_so_far,listt):
    print("\n")
    user_confirmation = input(f"Are you satified with {whats_chosen_so_far}? [Yes/No]: ")
    checked_confirmation_input = determine_user_input(user_confirmation)
    if checked_confirmation_input == ("no"):
        re_chosen_option = generate_new_choice(listt)
        return re_chosen_option
    else:
        return whats_chosen_so_far


new_destination = user_confirmation(destination_name, cities)
new_destination_name = get_city_name(new_destination)
new_restaurant = verfied_restaurant(destination_name, new_destination_name)
new_thing_to_do = user_confirmation(chosen_thing_to_do, things_to_do)
new_transport = user_confirmation(chosen_transport, mode_of_transportation)
verfy_new_restaurant = user_confirmation(new_restaurant, new_destination)


print("\n") 
final_confirmation = input(f"Congratulations {user_name}! You have completed all choices for the Day Trip Generator. You will be {new_transport} to you newly generated day trip to {new_destination_name}, which you will be {new_thing_to_do}. After a long day of {new_thing_to_do}, you will be dining at the fabulous restaurant called {verfy_new_restaurant}. That should conclude your trip to {new_destination_name}, at which point, you will be {new_transport} back home. Does this sound acceptable for you? [Yes/No]: ")

if determine_user_input(final_confirmation) == ("yes"):
    print("\n")
    print (f"Sounds fun {user_name}! Hope you have a great time in {new_destination_name}, I will be here when you are in need of my assistance again.")