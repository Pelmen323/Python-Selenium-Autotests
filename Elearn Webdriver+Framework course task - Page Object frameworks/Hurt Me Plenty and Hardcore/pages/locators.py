from selenium.webdriver.common.by import By


class PriceCalcPageLocators:
    SEARCH_BOX = (By.CSS_SELECTOR, "input[role='searchbox']")
    COMPUTE_ENGINE_FORM_MACHINE_QUANTITY = (By.CSS_SELECTOR, "input[ng-model*='computeServer.quantity']")
    COMPUTE_ENGINE_FORM_OS = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.os']")
    COMPUTE_ENGINE_FORM_MACHINE_CLASS = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.class']")
    COMPUTE_ENGINE_FORM_MACHINE_SERIES = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.series']")
    COMPUTE_ENGINE_FORM_MACHINE_TYPE = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.instance']")
    COMPUTE_ENGINE_FORM_SSD = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.ssd']")
    COMPUTE_ENGINE_FORM_DATACENTER_LOCATION = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.location']")
    COMPUTE_ENGINE_FORM_COMMITTED_USAGE = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.cud']")
    COMPUTE_ENGINE_FORM_GPU_CHECKBOX = (By.CSS_SELECTOR, "md-checkbox[ng-model*='computeServer.addGPUs']")
    COMPUTE_ENGINE_FORM_GPU_QUANTITY = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.gpuCount']")
    COMPUTE_ENGINE_FORM_GPU_MODEL = (By.CSS_SELECTOR, "md-select[ng-model*='computeServer.gpuType']")
    COMPUTE_ENGINE_FORM_SUBMIT_ESTIMATE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Add to Estimate']:not([disabled])")
    ESTIMATE_SECTION_DATACENTER_LOCATION = (By.XPATH, "//md-content[@id='compute']//div[contains(text(), 'Region:')]")
    ESTIMATE_SECTION_SSD = (By.XPATH, "//md-content[@id='compute']//div[contains(text(), 'Local SSD:')]")
    ESTIMATE_SECTION_MACHINE_CLASS = (By.XPATH, "//md-content[@id='compute']//div[contains(text(), 'VM class:')]")
    ESTIMATE_SECTION_MACHINE_TYPE = (By.XPATH, "//md-content[@id='compute']//div[contains(text(), 'Instance type:')]")
    ESTIMATE_SECTION_COMMITTED_USAGE = (By.XPATH, "//md-content[@id='compute']//div[contains(text(), 'Commitment term:')]")
    ESTIMATE_SECTION_TOTAL_COST = (By.XPATH, "//md-content[@id='compute']//*[contains(text(), 'Estimated Component Cost:')]")
    ESTIMATE_BUTTON_EMAIL = (By.CSS_SELECTOR, "button#email_quote")
    EMAIL_FORM_SEND_EMAIL = (By.CSS_SELECTOR, "button[aria-label='Send Email']")
    EMAIL_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    EMAIL_FORM_SEND_EMAIL = (By.CSS_SELECTOR, "button[aria-label='Send Email']")


class EmailPageLocators:
    EMAIL_PAGE_BODY_IFRAME = (By.CSS_SELECTOR, "iframe#ifmail")
    GET_RANDOM_EMAIL_LINK = (By.CSS_SELECTOR, "a[href='email-generator']:first-of-type")
    CHECK_INBOX_BUTTON = (By.XPATH, "//span[normalize-space()='Check Inbox']")
    CURRENT_EMAIL_LABEL = (By.CSS_SELECTOR, ".bname")
    REFRESH_EMAIL_INBOX_BUTTON = (By.CSS_SELECTOR, "#refresh")
    EMAIL_INBOX_IFRAME = (By.XPATH, "//iframe[@id='ifinbox']")
    EMAIL_ELEMENT_TO_INDICATE_NEW_EMAIL = (By.XPATH, "//div[text()='Google Cloud Price Estimate']")
    EMAIL_ESTIMATED_MONTHLY_COST_LABEL = (By.XPATH, "//*[contains(text(),'Estimated Monthly Cost:')]")
