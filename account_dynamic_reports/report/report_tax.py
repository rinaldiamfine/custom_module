# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError


class InsTaxReport(models.AbstractModel):
    _name = 'report.account_dynamic_reports.tax_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # If it is a call from Js window
        if self.env.context.get('from_js'):
            if data.get('js_data'):
                data.update({'data': data.get('js_data')})
        return [{}]