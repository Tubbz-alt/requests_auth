import pytest

import requests_auth


def test_requests_negotiate_sspi_is_used_when_nothing_is_provided():
    with pytest.raises(Exception) as exception_info:
        requests_auth.NTLM()
    assert (
        str(exception_info.value)
        == "NTLM authentication requires requests_negotiate_sspi module."
    )


def test_requests_ntlm_is_used_when_user_and_pass_provided():
    with pytest.raises(Exception) as exception_info:
        requests_auth.NTLM("fake_user", "fake_pwd")
    assert (
        str(exception_info.value)
        == "NTLM authentication requires requests_ntlm module."
    )


def test_user_without_password_is_invalid():
    with pytest.raises(Exception) as exception_info:
        requests_auth.NTLM("fake_user")
    assert (
        str(exception_info.value)
        == 'NTLM authentication requires "password" to be provided in security_details.'
    )


def test_password_without_user_is_invalid():
    with pytest.raises(Exception) as exception_info:
        requests_auth.NTLM(password="fake_pwd")
    assert (
        str(exception_info.value)
        == 'NTLM authentication requires "username" to be provided in security_details.'
    )