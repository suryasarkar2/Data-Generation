from mimesis import Food
import random

def food_list(nor):
    food = Food()

    categories = ['Mexican', 'Indian', 'Italian', 'Cajun', 'Soul', 'Thai', 'Greek', 'Chinese', 'Lebanese',
                  'Japanese', 'American', 'Moroccan', 'Mediterranean', 'French', 'Spanish', 'German', 'Korean',
                  'Turkish', 'Caribbean', 'Vietnamese']

    menu_list_all = []

    for i in range(nor):
        menu_list_ind = []

        item = food.dish()
        item_category = categories[random.randrange(0, len(categories))]

        # Pricing Determining
        p_sm = random.randrange(190, 900)
        p_md = p_sm + (0.10 * p_sm)
        p_lg = p_sm + (0.25 * p_sm)
        # PERCENTAGES FOR SMALL
        fcs_percent = random.randrange(25, 35)
        lcs_percent = random.randrange(10, 25)
        ocs_percent = 5
        # PERCENTAGES FOR MEDIUM
        fcm_percent = fcs_percent + random.randrange(1, 3)
        lcm_percent = lcs_percent + random.randrange(1, 3)
        ocm_percent = 5
        # PERCENTAGES FOR LARGE
        fcl_percent = fcs_percent + random.randrange(3, 6)
        lcl_percent = lcs_percent + random.randrange(3, 6)
        ocl_percent = 5
        # COSTING FOR SMALL
        fcs = (fcs_percent / 100) * p_sm
        lcs = (lcs_percent / 100) * p_sm
        ocs = (ocs_percent / 100) * p_sm
        profit_small = p_sm - (fcs + lcs + ocs)
        # COSTING FOR MEDIUM
        fcm = (fcm_percent / 100) * p_md
        lcm = (lcm_percent / 100) * p_md
        ocm = (ocm_percent / 100) * p_md
        profit_medium = p_md - (fcm + lcm + ocm)
        # COSTING FOR LARGE
        fcl = (fcl_percent / 100) * p_lg
        lcl = (lcl_percent / 100) * p_lg
        ocl = (ocl_percent / 100) * p_lg
        profit_large = p_lg - (fcl + lcl + ocl)

        # DishId DishName Category PriceSmall FoodCostSmall LabourCostSmall OverheadCostSmall       ---cont
        # PriceMedium FoodCostMedium LabourCostMedium OverheadCostMedium                            ---cont
        # PriceLarge FoodCostLarge LabourCostLarge OverheadCostLarge

        menu_list_ind.append(str(i + 1))
        menu_list_ind.append(item)
        menu_list_ind.append(item_category)
        menu_list_ind.append(str(round(p_sm, 2)))
        menu_list_ind.append(str(round(fcs, 2)))
        menu_list_ind.append(str(round(lcs, 2)))
        menu_list_ind.append(str(round(ocs, 2)))
        menu_list_ind.append(str(round(p_md, 2)))
        menu_list_ind.append(str(round(fcm, 2)))
        menu_list_ind.append(str(round(lcm, 2)))
        menu_list_ind.append(str(round(ocm, 2)))
        menu_list_ind.append(str(round(p_lg, 2)))
        menu_list_ind.append(str(round(fcl, 2)))
        menu_list_ind.append(str(round(lcl, 2)))
        menu_list_ind.append(str(round(ocl, 2)))

        menu_list_all.append(menu_list_ind)

    return menu_list_all


'''SAYANTAN CHATTERJEE'''


