import os

import pytest as pytest

from motivtelecom.model.data.data_for_tests import unregistered_phone_number, \
    wrong_password, \
    valid_password, \
    error_password_text, \
    error_phone_text, \
    smartphones, \
    laptops, valid_phone_number

authorization_with_params = \
    pytest.mark.parametrize('phone_number, password, error_text',
                            [(valid_phone_number,
                              wrong_password,
                              error_password_text),
                             (unregistered_phone_number,
                              valid_password,
                              error_phone_text)],
                            ids=['wrong_password',
                                 'unregistered_phone_number'])

categorys_params = pytest.mark.parametrize('category',
                                           [smartphones, laptops],
                                           ids=['smartphones',
                                                'laptops'])


