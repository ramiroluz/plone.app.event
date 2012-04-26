import unittest2 as unittest

from plone.app.event.testing import PAEvent_INTEGRATION_TESTING


class TextBaseModule(unittest.TestCase):
    layer = PAEvent_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def assertEqualDatetime(self, date1, date2, msg=None):
        """ Compare two datetime instances to a resolution of minutes.
        """
        compare_str = '%Y-%m-%d %H:%M %Z'
        self.assertTrue(date1.strftime(compare_str) ==\
                        date2.strftime(compare_str), msg)

    def test_default_end_dt(self):
        from datetime import timedelta
        from plone.app.event.base import default_end_dt
        from plone.app.event.base import localized_now
        from plone.app.event.base import DEFAULT_END_DELTA

        self.assertEqualDatetime(
            default_end_dt() - timedelta(hours=DEFAULT_END_DELTA),
            localized_now())

    def test_default_start_dt(self):
        from plone.app.event.base import default_start_dt
        from plone.app.event.base import localized_now

        self.assertEqualDatetime(default_start_dt(), localized_now())

    def test_default_end_DT(self):
        from datetime import timedelta
        from plone.app.event.base import localized_now
        from plone.app.event.base import DT
        from plone.app.event.base import default_end_DT
        from plone.app.event.base import DEFAULT_END_DELTA
        DTE = default_end_DT()
        DTN = DT(localized_now() + timedelta(hours=DEFAULT_END_DELTA))

        self.assertTrue(DTE.year() == DTN.year() and
                        DTE.month() == DTN.month() and
                        DTE.day() == DTN.day() and
                        DTE.hour() == DTN.hour() and
                        DTE.minute() == DTN.minute())

    def test_default_start_DT(self):
        from plone.app.event.base import localized_now
        from plone.app.event.base import DT
        from plone.app.event.base import default_start_DT
        DTS = default_start_DT()
        DTN = DT(localized_now())

        self.assertTrue(DTS.year() == DTN.year() and
                        DTS.month() == DTN.month() and
                        DTS.day() == DTN.day() and
                        DTS.hour() == DTN.hour() and
                        DTS.minute() == DTN.minute())

    def test_DT(self):
        from plone.app.event.base import DT
        from datetime import datetime
        from DateTime import DateTime

        pdt = datetime(2011, 11, 23)
        zDT = DateTime(2011, 11, 23)
        self.assertTrue(zDT == DT(pdt))