# Starbucks Nutrition Analysis
This repo contains a web scraper and an analysis report of Starbucks drink nutrition data.

[Medium Post](https://medium.com/@yazihejazi/how-unhealthy-is-your-starbucks-drink-55b23ae371d6)
[Notebook](https://yhejazi.github.io/starbucks-nutrition/)


## About the Data
Starbucks provides a nutrition analysis of its menu items on its website to help you balance your Starbucks order with other foods you eat. Their goal is to provide you with the information you need to make sensible decisions about balance, variety, and moderation in your diet.

I first scraped JSON data from the online Starbucks drinks menu and saved it as a CSV on *September 2, 2020*. The data file contains the following variables: 

* drink_name: Name of the drink
* type: Type of drink, categories defined by Starbucks
* size: Size of the drink
* calories: Number of calories
* fat: Total fat (g)
* cholesterol: Cholesterol (mg)
* sodium: Sodium (mg)
* carb: Total carbohydrates (g)
* sugar: Sugars (g)
* protein: Protein (g)
* caffeine: Caffeine (g)

All drinks from the Starbucks online main menu (collected in Fall 2020) are included, with the exception of Clover® Brewed Coffees, Coffee Travelers, Iced Clover® Brewed Coffees, Bottled Teas, Milk, Sparkling Water, and Water. There are 11 columns and 525 rows.

For the purpose of this analysis, I filtered the dataset to only include drinks in grande (16oz) size in my notebook. Therefore, each line is a unique drink with a unique drink name. I also omitted drinks in which grande size nutrition data was not provided on the Starbucks online menu. After data cleaning, we are left analyzing a total of 139 rows (unique drinks).

## Focus: Calories, Sugar, & Caffeine
Why are we looking mostly at calories and sugar?

According to [NPD’s Health Aspirations and Behavioral Tracking Service](https://www.npd.com/wps/portal/npd/us/news/press-releases/2020/new-year-new-nutrition-facts-label-on-food-most-us-consumers-read-the-nutrition-facts-label-and-the-top-items-they-look-for-are-sugars-and-calories/), the top two items consumers look for on nutrition labels are sugars and calories. I also want to discuss caffeine as it is in **over 85%** of items on the drinks menu, and it is a [hot topic](https://www.health.harvard.edu/staying-healthy/the-buzz-about-caffeine-and-health) in today’s nutrition and health discussions.
