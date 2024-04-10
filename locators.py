class URLS:
    main_url = 'https://victoretc.github.io/selenium_waits/'

    url_1 = 'https://www.selenium.dev/selenium/web/dynamic.html'
    url_2 = 'https://demoqa.com/dynamic-properties'
    url_3 = 'https://the-internet.herokuapp.com/dynamic_loading'


class MainLocks:
    main_header = ('xpath', '//h1')
    start_btn = ('xpath', '//button[@id="startTest"]')

    login_field = ('xpath', '//input[@id="login"]')
    pass_field = ('xpath', '//input[@id="password"]')
    checkbox = ('xpath', '//input[@id="agree"]')
    reg_btn = ('xpath', '//button[@id="register"]')

    loader = ('xpath', '//div[@id="loader"]')
    success_box = ('xpath', '//p[@id="successMessage"]')


class Messages:
    header_text = 'Практика с ожиданиями в Selenium'
    success_msg = 'Вы успешно зарегистрированы!'


class Data:
    login_text = 'login'
    pass_text = 'password'


class URL1Locks:
    add_box_btn = ('xpath', '//input[@id="adder"]')
    red_box = ('xpath', '//div[@class="redbox"]')

    add_input_btn = ('xpath', '//input[@id="reveal"]')
    new_input = ('xpath', '//input[@id="revealed"]')


class URL2Locks:
    random_id_text = ('xpath', '//p[contains(text(),"This text has random Id")]')
    enable_after_5_sec_btn = ('xpath', '//button[@id="enableAfter"]')
    change_color_btn = ('xpath', '//button[@id="colorChange"]')
    visible_after_5_sec_btn = ('xpath', '//button[@id="visibleAfter"]')


class URL3Locks:
    link_1 = ('xpath', '(//a)[2]')
    link_2 = ('xpath', '(//a)[3]')
    start_btn = ('xpath', '//div[@id="start"]/button')
    page_header_h4 = ('xpath', '//h4')
    loader = ('xpath', '//div[@id="loading"]')
    final_msg = ('xpath', '//div[@id="finish"]')

