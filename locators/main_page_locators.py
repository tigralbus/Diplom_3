from selenium.webdriver.common.by import By


class MainPageLocators:
    MAKE_BURGER_HEADER = [By.XPATH, "//div/main/section[@class = 'BurgerIngredients_ingredients__1N8v2']/h1"] #[By.XPATH, "//div/main//h1[@class='text text_type_main-large mb-5 mt-10'][text()='Соберите бургер']"]
    INGREDIENT_BUN = [By.XPATH, "//div/main//img[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'][@alt='Флюоресцентная булка R2-D3']"]
    INGREDIENT_DETAILS_MODAL_HEADER = [By.XPATH, "//div//div/h2[text()='Детали ингредиента']"]
    INGREDIENT_DETAILS_MODAL_CLOSE_ICON = [By.XPATH, "//div/section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type = 'button'][@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    BURGER_CONSTRUCTOR_TOP = [By.XPATH, "//div/main//ul//div[@class = 'constructor-element constructor-element_pos_top']/span/span[@class='constructor-element__action pr-2']"] #"//div//div[@class = 'constructor-element constructor-element_pos_top']/span[@class = 'constructor-element__row']"]#"//div//div[@class = 'constructor-element constructor-element_pos_top']"]
    BUNS_IN_ORDER_FOR_COUNT = [By.XPATH, "//div/main//ul/li[@class = 'BurgerConstructor_basket__listItem__aWMu1 mr-4']"]
    MAKE_ORDER_BUTTON = [By.XPATH, "//div/main//div/button[text()='Оформить заказ']"]
    ORDER_CREATED_MODAL_HEADER =  [By.XPATH, "//div/section//div/p[@class = 'undefined text text_type_main-medium mb-15'][text()='идентификатор заказа']"]


