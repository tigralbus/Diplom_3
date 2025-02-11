from selenium.webdriver.common.by import By


class MainPageLocators:
    MAKE_BURGER_HEADER = [By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/h1"]
    INGREDIENT_BUN = [By.XPATH,
                      "//img[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'][@alt='Флюоресцентная булка R2-D3']"]
    INGREDIENT_DETAILS_MODAL_HEADER = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    INGREDIENT_DETAILS_MODAL_CLOSE_ICON = [By.XPATH,
                                           "//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type = 'button'][@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    BURGER_CONSTRUCTOR_TOP = [By.XPATH,
                              "//div[@class = 'constructor-element constructor-element_pos_top']//span[@class='constructor-element__action pr-2']"]
    BUNS_IN_ORDER_FOR_COUNT = [By.XPATH, "//li[@class = 'BurgerConstructor_basket__listItem__aWMu1 mr-4']"]
    MAKE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    ORDER_CREATED_MODAL_HEADER = [By.XPATH,
                                  "//p[text()='идентификатор заказа']"]
    CLOSE_BUTTON_CREATED_MODAL_POP_UP = [By.XPATH,
                                         "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    PREORDER_ID = [By.XPATH,
                   "//h2[text() = '9999'][@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]

    ORDER_ID_MODAL_POP_UP = [By.XPATH,
                             "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]

    MODAL_WINDOW_NEW_ORDER = [By.XPATH,
                             "//div[@class = 'Modal_modal__contentBox__sCy8X pt-30 pb-30']"]
