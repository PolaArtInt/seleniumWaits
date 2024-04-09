class URLS:
    main_url = 'https://victoretc.github.io/selenium_waits/'


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
