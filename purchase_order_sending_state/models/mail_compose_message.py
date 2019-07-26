# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, api


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def send_mail(self, auto_commit=False):
        """Mark purchase orders as sent in the case of mass mailing or sending a single order."""
        context = self._context
        if context.get('mark_rfq_as_sent') and self.model == 'purchase.order' and context.get('active_ids'):
            self.env['purchase.order'].browse(context.get('active_ids')).write({'po_sent': True})
        return super(MailComposeMessage, self).send_mail(auto_commit=auto_commit)
