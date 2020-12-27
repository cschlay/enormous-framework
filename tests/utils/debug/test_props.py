from unittest import TestCase

import pytest

from utils.debug.props import duration


class PropertiesTest(TestCase):
    """A property to measure and log execution duration."""

    def test_duration_synchronous(self):
        @duration
        def function():
            print("called")

        function()

