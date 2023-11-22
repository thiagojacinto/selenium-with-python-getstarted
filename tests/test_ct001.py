
def test_login_with_empty_credentials(start_by_login_page):
    login_page = start_by_login_page
    login_page.access_page()
    login_page.click_on_login()

    assert login_page.has_error_on_username_field(), "Error missing on empty username field"
    assert login_page.has_error_on_password_field(), "Error missing on empty password field"


def test_login_attempt_with_locked_out_user(start_by_login_page):
    login_page = start_by_login_page
    login_page.access_page()
    login_page.type_username("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_on_login()

    assert login_page.has_error_on_username_field(), "Error missing on empty username field"
    assert login_page.has_error_on_password_field(), "Error missing on empty password field"
    assert login_page.has_error_alert(error_text = "this user has been locked out")

