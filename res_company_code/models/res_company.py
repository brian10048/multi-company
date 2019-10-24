# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'
    _order = 'code, name'

    code = fields.Char(string='Code')

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The company code must be unique !')
    ]
